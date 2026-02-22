import asyncio
import json
import websockets

URI = "ws://192.168.50.2:8123/api/websocket"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJmNDM3ZTI5YWY5NmQ0MWIzOTczMTEyNGY3OGNmNTliZSIsImlhdCI6MTc3MTAwNzgzNCwiZXhwIjoyMDg2MzY3ODM0fQ.2fVuAoLPVOjBdhqKUL3Kzne_ogW81AczlxWs7H4rS6c"

async def fetch_data():
    try:
        async with websockets.connect(URI) as ws:
            # Auth
            await ws.recv()
            await ws.send(json.dumps({"type": "auth", "access_token": TOKEN}))
            auth_res = await ws.recv()
            print("Auth:", auth_res[:100])
            
            # Get areas
            await ws.send(json.dumps({"id": 1, "type": "config/area_registry/list"}))
            areas_msg = await ws.recv()
            areas = json.loads(areas_msg).get("result", [])
            print(f"Fetched {len(areas)} areas.")
            
            # Get devices
            await ws.send(json.dumps({"id": 2, "type": "config/device_registry/list"}))
            devices_msg = await ws.recv()
            devices = json.loads(devices_msg).get("result", [])
            print(f"Fetched {len(devices)} devices.")
            
            # Get entities
            await ws.send(json.dumps({"id": 3, "type": "config/entity_registry/list"}))
            entities_msg = await ws.recv()
            entities = json.loads(entities_msg).get("result", [])
            print(f"Fetched {len(entities)} entities.")
            
            # Get live states
            await ws.send(json.dumps({"id": 4, "type": "get_states"}))
            states_msg = await ws.recv()
            states = json.loads(states_msg).get("result", [])
            print(f"Fetched {len(states)} live states.")
            
            data = {
                "areas": areas,
                "devices": devices,
                "entities": entities,
                "states": states
            }
            
            with open("HA-UI/ha_data_dump.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            print("Data saved to HA-UI/ha_data_dump.json")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(fetch_data())
