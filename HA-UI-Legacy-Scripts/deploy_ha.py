import asyncio
import json
import websockets
import yaml
import sys

URI = "ws://192.168.50.2:8123/api/websocket"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmNDM3ZTI5YWY5NmQ0MWIzOTczMTEyNGY3OGNmNTliZSIsImlhdCI6MTc3MTAwNzgzNCwiZXhwIjoyMDg2MzY3ODM0fQ.2fVuAoLPVOjBdhqKUL3Kzne_ogW81AczlxWs7H4rS6c"

async def deploy():
    async with websockets.connect(URI) as websocket:
        # 1. Check auth required
        msg = await websocket.recv()
        auth_msg = json.loads(msg)
        if auth_msg.get("type") == "auth_required":
            print("Authenticating...")
            await websocket.send(json.dumps({"type": "auth", "access_token": TOKEN}))
            
            auth_ok_msg = await websocket.recv()
            auth_ok = json.loads(auth_ok_msg)
            if auth_ok.get("type") != "auth_ok":
                print("Auth failed:", auth_ok)
                return

        print("Authentication successful.")
        
        # 2. Backup current config
        print("Fetching current Lovelace config...")
        await websocket.send(json.dumps({
            "id": 1,
            "type": "lovelace/config"
        }))
        res_msg = await websocket.recv()
        res = json.loads(res_msg)
        if res.get("success"):
            old_config = res.get("result")
            with open("HA-UI/old_lovelace_backup.yaml", "w", encoding="utf-8") as f:
                yaml.dump(old_config, f, allow_unicode=True)
            print("Backup saved to HA-UI/old_lovelace_backup.yaml")
        else:
            print("Could not fetch current config (it might be the first time taking over UI). Error:", res.get("error"))

        # 3. Read new config
        try:
            with open("HA-UI/ha_cyber_ui_v12.yaml", "r", encoding="utf-8") as f:
                new_config = yaml.safe_load(f)
        except Exception as e:
            print("Error parsing new config HA-UI/ha_cyber_ui_v12.yaml:", e)
            return

        # 4. Save new config
        print("Pushing new Lovelace config...")
        await websocket.send(json.dumps({
            "id": 2,
            "type": "lovelace/config/save",
            "config": new_config
        }))
        save_msg = await websocket.recv()
        save_res = json.loads(save_msg)
        
        if save_res.get("success"):
            print("SUCCESS: New Lovelace UI deployed successfully!")
        else:
            print("FAILED to deploy UI:", save_res.get("error"))

if __name__ == "__main__":
    asyncio.run(deploy())
