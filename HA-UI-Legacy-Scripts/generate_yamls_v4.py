import yaml
import json

def generate_yaml_v4():
    # Device Data
    rooms_data = {
        "餐厅": {
            "path": "room_canting",
            "icon": "mdi:silverware-fork-knife",
            "switches": [
                {"id": "switch.can_ting_switch_1", "name": "灯具主控1"},
                {"id": "switch.can_ting_switch_2", "name": "灯具主控2"},
            ],
            "devices": [
                "light.lemesh_wy0c15_a4d3_light",
                "light.lemesh_wy0c15_be94_light",
                "light.lemesh_wy0c15_f24c_light",
                "light.lemesh_wy0c15_0ef1_light",
                "light.lemesh_wyra01_4639_ambient_light",
                "light.lemesh_wyra01_4639_light"
            ]
        },
        "厨房": {
            "path": "room_chufang",
            "icon": "mdi:stove",
            "switches": [
                {"id": "switch.chu_fang_switch_1", "name": "厨房开关1"},
                {"id": "switch.chu_fang_switch_2", "name": "厨房开关2"},
            ],
            "devices": [
                "light.lemesh_wy0c15_7a81_light",
                "light.lemesh_wy0c15_cb6a_light",
                "light.lemesh_wy0c15_9bf5_light",
                "light.lemesh_wy0c15_647f_light",
            ],
            "sensors": [
                "binary_sensor.chu_fang_gan_ying_motion",
                "binary_sensor.ran_qi_bao_jing_qi_gas",
                "binary_sensor.wu_xian_shui_jin_chuan_gan_qi_moisture",
                "binary_sensor.yan_wu_chuan_gan_qi_smoke"
            ]
        },
        "次卧": {
            "path": "room_ciwo",
            "icon": "mdi:bed-empty",
            "switches": [
                {"id": "switch.ci_wo_switch_1", "name": "次卧主灯"},
                {"id": "switch.ci_wo_switch_2", "name": "次卧辅灯"},
                {"id": "switch.ci_wo_switch_3", "name": "次卧筒灯"},
                {"id": "switch.xiaomi_m4_50e9_dryer", "name": "空调干燥"},
                {"id": "switch.xiaomi_m4_50e9_eco", "name": "空调ECO"},
                {"id": "switch.xiaomi_m4_50e9_heater_2", "name": "辅热"},
                {"id": "switch.xiaomi_m4_50e9_sleep_mode", "name": "睡眠模型"},
                {"id": "switch.xiaomi_m4_50e9_switch_status", "name": "状态灯"},
                {"id": "switch.xiaomi_m4_50e9_unstraight_blowing", "name": "防直吹"},
                {"id": "switch.xiaomi_m4_50e9_alarm", "name": "警音"},
            ],
            "devices": [
                "light.lemesh_wy0c15_318b_light",
                "light.xiaomi_m4_50e9_indicator_light",
                "light.lemesh_wy0c15_e178_light",
                "light.lemesh_wy0c15_9c89_light",
                "light.lemesh_wy0c15_06a2_light",
                "light.lemesh_wy0c15_831b_light",
            ],
            "sensors": [
                "sensor.xiaomi_m4_50e9_relative_humidity",
                "sensor.xiaomi_m4_50e9_temperature",
                "sensor.xiaomi_m4_50e9_filter_life_level"
            ],
            "climates": [
                 "climate.xiaomi_m4_50e9_air_conditioner"
            ]
        },
        "过道": {
            "path": "room_guodao",
            "icon": "mdi:transit-connection-horizontal",
            "switches": [
                {"id": "switch.guo_dao_switch_1", "name": "前段灯"},
                {"id": "switch.guo_dao_switch_2", "name": "中段灯"},
                {"id": "switch.guo_dao_switch_3", "name": "后段灯"},
            ],
            "devices": [
                "light.lemesh_wy0c15_318d_light",
                "light.lemesh_wy0c15_033d_light",
                "light.lemesh_wy0c15_16a4_light",
                "light.lemesh_wy0c15_2faf_light",
            ]
        },
        "客厅": {
            "path": "room_keting",
            "icon": "mdi:sofa",
            "switches": [
                {"id": "switch.ke_ting_deng_dai_switch_1", "name": "东墙灯带"},
                {"id": "switch.ke_ting_deng_dai_switch_2", "name": "西墙灯带"},
                {"id": "switch.ke_ting_tong_deng_switch_1", "name": "内圈筒灯"},
                {"id": "switch.ke_ting_tong_deng_switch_2", "name": "外圈筒灯"},
                {"id": "switch.dooya_c1_f2db_mode_2", "name": "阳台纱帘"},
                {"id": "switch.dooya_c1_cc3d_mode_2", "name": "阳台主帘"},
                {"id": "switch.zjdh_xj001_0a74_motor_reverse", "name": "电机反转"},
            ],
            "devices": [
                "light.lemesh_wy0c15_adb0_light",
                "light.lemesh_wy0c15_b016_light",
                "light.lemesh_wy0c15_bcd7_light",
                "light.lemesh_wy0c15_b455_light",
                "light.lemesh_wy0c15_f240_light",
                "light.lemesh_wy0c15_bcc2_light",
                "light.lemesh_wy0c15_dbff_light",
                "light.lemesh_wy0c15_0a31_light",
                "light.lemesh_wy0c15_ed5a_light",
                "cover.dooya_c1_f2db_curtain",
                "cover.dooya_c1_cc3d_curtain",
                "cover.zjdh_xj001_0a74_curtain",
            ],
            "media": [
                "media_player.ke_ting",
                "media_player.samsung_qx3ca_85_tv"
            ]
        },
        "生活阳台": {
            "path": "room_shenghuoyangtai",
            "icon": "mdi:washing-machine",
            "switches": [
                {"id": "switch.sheng_huo_yang_tai_switch_1", "name": "顶灯控制"},
                {"id": "switch.yszn01_ys2102_c8c6_dryer", "name": "晾衣机烘干"},
                {"id": "switch.yszn01_ys2102_c8c6_uv", "name": "晾衣机杀菌"},
            ],
            "devices": [
                "cover.yszn01_ys2102_c8c6_airer",
                "light.yszn01_ys2102_c8c6_light"
            ]
        },
        "书房": {
            "path": "room_shufang",
            "icon": "mdi:laptop",
            "switches": [
                {"id": "switch.shu_fang_switch_1", "name": "书房主灯"},
                {"id": "switch.shu_fang_switch_2", "name": "氛围灯"},
                {"id": "switch.shu_fang_switch_3", "name": "射灯"},
                {"id": "switch.xiaomi_m4_549b_dryer", "name": "空调干燥"},
                {"id": "switch.xiaomi_m4_549b_eco", "name": "空调ECO"},
                {"id": "switch.xiaomi_m4_549b_heater_2", "name": "空调辅热"},
                {"id": "switch.xiaomi_m4_549b_sleep_mode", "name": "睡眠模式"},
                {"id": "switch.xiaomi_m4_549b_switch_status", "name": "指示灯"},
                {"id": "switch.xiaomi_m4_549b_unstraight_blowing", "name": "防直吹"},
                {"id": "switch.xiaomi_m4_549b_alarm", "name": "空调提示音"},
                {"id": "switch.xiaomi_lx06_843f_sleep_mode", "name": "小爱静音"},
            ],
            "devices": [
                "light.lemesh_wy0c15_312c_light",
                "light.lemesh_wy0c15_3221_light",
                "light.xiaomi_m4_549b_indicator_light",
                "light.lemesh_wy0c15_00ca_light",
                "light.lemesh_wy0c15_6d30_light",
                "light.lemesh_wy0c15_e3ed_light",
            ],
            "sensors": [
                "sensor.xiaomi_m4_549b_relative_humidity",
                "sensor.xiaomi_m4_549b_temperature",
                "sensor.xiaomi_m4_549b_filter_life_level",
                "sensor.xiaomi_lx06_843f_conversation"
            ],
            "media": [
                "media_player.xiaomi_lx06_843f_play_control"
            ],
            "climates": [
                 "climate.xiaomi_m4_549b_air_conditioner"
            ]
        },
        "玄关": {
            "path": "room_xuanguan",
            "icon": "mdi:door-open",
            "switches": [
                {"id": "switch.xuan_guan_switch_1", "name": "入户顶灯"},
                {"id": "switch.xuan_guan_switch_2", "name": "鞋柜灯带"},
            ],
            "sensors": [
                "binary_sensor.xuan_guan_men_ci_door"
            ]
        },
        "阳台": {
            "path": "room_yangtai",
            "icon": "mdi:flower",
            "switches": [
                {"id": "switch.yang_tai_switch_1", "name": "南阳台灯"},
                {"id": "switch.yang_tai_switch_2", "name": "氛围灯"},
                {"id": "switch.yang_tai_switch_3", "name": "植物补光"},
            ],
            "devices": [
                "light.lemesh_wy0c15_a2d3_light",
                "light.lemesh_wy0c15_2ee4_light",
                "light.lemesh_wy0c15_2d1b_light",
                "light.lemesh_wy0c08_67f7_light",
                "light.lemesh_wy0c09_c969_light",
                "light.lemesh_wy0c08_a7fa_light"
            ]
        },
        "主卧": {
            "path": "room_zhuwo",
            "icon": "mdi:bed-double",
            "switches": [
                {"id": "switch.zhu_wo_switch_1", "name": "主灯"},
                {"id": "switch.zhu_wo_switch_2", "name": "灯带"},
                {"id": "switch.zhu_wo_switch_3", "name": "阅读灯"},
                {"id": "switch.zhu_wo_switch_4", "name": "夜灯"},
                {"id": "switch.xiaomi_m4_1c38_dryer", "name": "空调干燥"},
                {"id": "switch.xiaomi_m4_1c38_eco", "name": "空调ECO"},
                {"id": "switch.xiaomi_m4_1c38_heater_2", "name": "辅热"},
                {"id": "switch.xiaomi_m4_1c38_sleep_mode", "name": "睡眠"},
                {"id": "switch.xiaomi_m4_1c38_switch_status", "name": "指示灯"},
                {"id": "switch.xiaomi_m4_1c38_unstraight_blowing", "name": "防直吹"},
                {"id": "switch.xiaomi_m4_1c38_alarm", "name": "提示音"},
                {"id": "switch.zhu_wo_men_deng_switch_1", "name": "门灯"},
                {"id": "switch.zhu_wo_she_deng_tai_deng_switch_1", "name": "左射灯"},
                {"id": "switch.zhu_wo_she_deng_tai_deng_switch_2", "name": "右射灯"},
            ],
            "devices": [
                "light.lemesh_wy0c14_c615_light",
                "light.lemesh_wy0c15_ae79_light",
                "light.xiaomi_m4_1c38_indicator_light",
                "light.lemesh_wy0c15_f7b6_light",
                "light.lemesh_wy0c15_f712_light",
                "light.lemesh_wy0c15_2fda_light",
                "light.lemesh_wy0c15_7bc9_light",
                "light.lemesh_wy0c15_5d3b_light",
                "light.lemesh_wy0c15_25e7_light"
            ],
            "sensors": [
                "sensor.xiaomi_m4_1c38_relative_humidity",
                "sensor.xiaomi_m4_1c38_temperature",
                "sensor.xiaomi_m4_1c38_filter_life_level"
            ],
            "climates": [
                 "climate.xiaomi_m4_1c38_air_conditioner"
            ]
        },
        "主卫": {
             "path": "room_zhuwei",
             "icon": "mdi:shower",
             "switches": [
                {"id": "switch.zhu_wei_switch_1", "name": "镜前灯"},
                {"id": "switch.zhu_wei_switch_2", "name": "主顶灯"},
                {"id": "switch.zhu_wei_kai_guan_switch_1", "name": "换气"},
                {"id": "switch.zhu_wei_kai_guan_switch_2", "name": "送风"},
             ]
        }
    }

    yaml_out = """title: "NEON HOME v4"
theme: default
background: "#111114"

button_card_templates:
  # 房间入口大磁贴 (主导航用)
  room_portal:
    show_name: true
    show_icon: true
    show_state: false
    styles:
      card:
        - aspect-ratio: "2.5/1"
        - background: "rgba(25, 27, 33, 0.8)"
        - border-radius: "16px"
        - border: "1px solid rgba(255, 255, 255, 0.05)"
        - padding: "12px"
        - box-shadow: "0 4px 10px rgba(0,0,0,0.2)"
        - transition: "all 0.3s ease"
      grid:
        - grid-template-areas: '"i n"'
        - grid-template-columns: "45px auto"
      icon:
        - color: "#00d2ff"
        - width: "26px"
        - justify-self: "center"
      name:
        - color: "#e1e5f2"
        - font-size: "15px"
        - font-weight: "600"
        - justify-self: "start"
        - align-self: "center"

views:
  # =========================================================
  # 1. 首页看总览 (Home Dashboard)
  # =========================================================
  - path: default_view
    title: NEON HOME
    icon: mdi:home-automation
    cards:
      - type: custom:layout-card
        layout_type: masonry
        cards:
          
          # ===============================
          # 顶级状态栏：天气与人员
          # ===============================
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-title-card
                title: 欢迎回来，主人
                subtitle: 系统运行中...
                card_mod:
                  style: |
                    ha-card { --title-color: #00d2ff; --subtitle-color: #8a91a6; }
              - type: custom:mushroom-person-card
                entity: person.zuo_deng_zhen_xiang
                layout: vertical
                icon_type: entity-picture
                card_mod:
                  style: |
                    ha-card { background: rgba(25, 27, 33, 0.5); border: 1px solid rgba(255,255,255,0.05); }
              - type: custom:mushroom-person-card
                entity: person.jing_jing_jing
                layout: vertical
                icon_type: entity-picture
                card_mod:
                  style: |
                    ha-card { background: rgba(25, 27, 33, 0.5); border: 1px solid rgba(255,255,255,0.05); }
              - type: weather-forecast
                entity: weather.forecast_wo_de_jia
                show_forecast: false
                card_mod:
                  style: |
                    ha-card { background: rgba(25, 27, 33, 0.5); border: 1px solid rgba(255,255,255,0.05); }

          - type: custom:mushroom-title-card
            title: 🏠 区域空间节点
            subtitle: 点击进入对应房间查看专属设备控制台

          # ===============================
          # 房间导航网格阵列
          # 这里采用与您发来的参考图一样的网格卡片结构
          # ===============================
          - type: grid
            columns: 4
            cards:
"""
    # Build main dashboard buttons navigating to subviews
    for room, data in rooms_data.items():
        yaml_out += f"""              - type: custom:mushroom-template-card
                primary: "{room}"
                icon: "{data['icon']}"
                icon_color: "#00d2ff"
                layout: vertical
                card_mod:
                  style: |
                    ha-card {{
                      background: rgba(30, 32, 40, 0.7);
                      border: 1px solid rgba(255, 255, 255, 0.05);
                      border-radius: 16px;
                      transition: all 0.3s ease;
                      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                    }}
                    ha-card:hover {{
                      border: 1px solid #00d2ff;
                      box-shadow: 0 0 15px rgba(0, 210, 255, 0.3);
                      transform: scale(1.02);
                    }}
                tap_action:
                  action: navigate
                  navigation_path: /lovelace/{data['path']}
"""

    yaml_out += """
  # =========================================================
  # 2. 独立房间视图 (Subviews)
  # =========================================================
"""
    
    # Generate a dedicated subview for each room
    for room, data in rooms_data.items():
        yaml_out += f"""
  - path: {data['path']}
    title: {room}
    icon: "{data['icon']}"
    subview: true  # 这是关键，把它变成专门的子页面
    cards:
      - type: custom:layout-card
        layout_type: masonry
        cards:
"""
        # Section 1: Climates & Media (The big stuff)
        has_big = data.get("climates") or data.get("media")
        if has_big:
            yaml_out += f"""          - type: custom:mushroom-title-card
            title: ❄️ 空调与音视频
          - type: grid
            columns: 2
            cards:
"""
            for clim in data.get("climates", []):
                yaml_out += f"""              - type: custom:mushroom-climate-card
                entity: {clim}
                show_temperature_control: true
                collapsible_controls: false
                layout: horizontal
                card_mod:
                  style: |
                    ha-card {{ background: rgba(22, 24, 29, 0.6); border: 1px solid rgba(255,255,255,0.05); border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }}
"""
            for med in data.get("media", []):
                yaml_out += f"""              - type: custom:mushroom-media-player-card
                entity: {med}
                use_media_info: true
                show_volume_level: true
                layout: horizontal
                card_mod:
                  style: |
                    ha-card {{ background: rgba(22, 24, 29, 0.6); border: 1px solid rgba(255,255,255,0.05); border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }}
"""

        # Section 2: Lights & Covers
        lights = [d for d in data.get("devices", []) if d.startswith("light.")]
        covers = [d for d in data.get("devices", []) if d.startswith("cover.")]
        
        if lights or covers:
            yaml_out += f"""          - type: custom:mushroom-title-card
            title: 💡 照明与窗帘系统
          - type: grid
            columns: 4
            cards:
"""
            for light in lights:
                yaml_out += f"""              - type: custom:mushroom-light-card
                entity: {light}
                show_brightness_control: true
                layout: vertical
                card_mod:
                  style: |
                    ha-card {{ background: rgba(30, 32, 40, 0.8); border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; }}
"""
            for cov in covers:
                yaml_out += f"""              - type: custom:mushroom-cover-card
                entity: {cov}
                show_position_control: true
                show_buttons_control: true
                layout: vertical
                card_mod:
                  style: |
                    ha-card {{ background: rgba(30, 32, 40, 0.8); border: 1px solid rgba(255,255,255,0.03); border-radius: 12px; }}
"""

        # Section 3: Switches
        if data.get("switches"):
            yaml_out += f"""          - type: custom:mushroom-title-card
            title: ⚙️ 开关控制矩阵
          - type: grid
            columns: 4
            cards:
"""
            for sw in data.get("switches", []):
                yaml_out += f"""              - type: custom:mushroom-entity-card
                entity: {sw['id']}
                name: "{sw['name']}"
                layout: vertical
                secondary_info: state
                card_mod:
                  style: |
                    ha-card {{ background: rgba(24, 26, 31, 0.9); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; }}
"""

        # Section 4: Sensors
        if data.get("sensors"):
            yaml_out += f"""          - type: custom:mushroom-title-card
            title: 📡 环境节点侦测
          - type: grid
            columns: 5
            cards:
"""
            for sens in data.get("sensors", []):
                yaml_out += f"""              - type: custom:mushroom-entity-card
                entity: {sens}
                layout: vertical
                primary_info: state
                secondary_info: name
                icon_color: teal
                card_mod:
                  style: |
                    ha-card {{ background: transparent; border: 1px dashed rgba(0, 210, 255, 0.15); border-radius: 12px; box-shadow: none; }}
"""

    with open("c:/Users/zhong/Downloads/Compressed/files/HA-UI/ha_cyber_ui_v4.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_out)
        print("Generated ha_cyber_ui_v4.yaml using Home/Subview architecture!")

if __name__ == "__main__":
    generate_yaml_v4()
