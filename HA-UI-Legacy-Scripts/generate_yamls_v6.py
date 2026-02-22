import yaml
import json

def generate_yaml_v6():
    # Device Data
    rooms_data = {
        "餐厅": {
            "icon": "mdi:silverware-fork-knife",
            "switches": [
                {"id": "switch.can_ting_switch_1", "name": "灯具主1"},
                {"id": "switch.can_ting_switch_2", "name": "灯具主2"},
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
            "icon": "mdi:stove",
            "switches": [
                {"id": "switch.chu_fang_switch_1", "name": "厨房1"},
                {"id": "switch.chu_fang_switch_2", "name": "厨房2"},
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
            "icon": "mdi:bed-empty",
            "switches": [
                {"id": "switch.ci_wo_switch_1", "name": "次主灯"},
                {"id": "switch.ci_wo_switch_2", "name": "辅灯"},
                {"id": "switch.ci_wo_switch_3", "name": "筒灯"},
                {"id": "switch.xiaomi_m4_50e9_dryer", "name": "干燥"},
                {"id": "switch.xiaomi_m4_50e9_eco", "name": "ECO"},
                {"id": "switch.xiaomi_m4_50e9_heater_2", "name": "辅热"},
                {"id": "switch.xiaomi_m4_50e9_sleep_mode", "name": "睡眠"},
                {"id": "switch.xiaomi_m4_50e9_switch_status", "name": "状灯"},
                {"id": "switch.xiaomi_m4_50e9_unstraight_blowing", "name": "防吹"},
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
            "icon": "mdi:transit-connection-horizontal",
            "switches": [
                {"id": "switch.guo_dao_switch_1", "name": "前灯"},
                {"id": "switch.guo_dao_switch_2", "name": "中灯"},
                {"id": "switch.guo_dao_switch_3", "name": "后灯"},
            ],
            "devices": [
                "light.lemesh_wy0c15_318d_light",
                "light.lemesh_wy0c15_033d_light",
                "light.lemesh_wy0c15_16a4_light",
                "light.lemesh_wy0c15_2faf_light",
            ]
        },
        "客厅": {
            "icon": "mdi:sofa",
            "switches": [
                {"id": "switch.ke_ting_deng_dai_switch_1", "name": "东灯带"},
                {"id": "switch.ke_ting_deng_dai_switch_2", "name": "西灯带"},
                {"id": "switch.ke_ting_tong_deng_switch_1", "name": "内筒灯"},
                {"id": "switch.ke_ting_tong_deng_switch_2", "name": "外筒灯"},
                {"id": "switch.dooya_c1_f2db_mode_2", "name": "纱帘"},
                {"id": "switch.dooya_c1_cc3d_mode_2", "name": "主帘"},
                {"id": "switch.zjdh_xj001_0a74_motor_reverse", "name": "反转"},
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
            "icon": "mdi:washing-machine",
            "switches": [
                {"id": "switch.sheng_huo_yang_tai_switch_1", "name": "顶灯"},
                {"id": "switch.yszn01_ys2102_c8c6_dryer", "name": "烘干"},
                {"id": "switch.yszn01_ys2102_c8c6_uv", "name": "杀菌"},
            ],
            "devices": [
                "cover.yszn01_ys2102_c8c6_airer",
                "light.yszn01_ys2102_c8c6_light"
            ]
        },
        "书房": {
            "icon": "mdi:laptop",
            "switches": [
                {"id": "switch.shu_fang_switch_1", "name": "主灯"},
                {"id": "switch.shu_fang_switch_2", "name": "氛灯"},
                {"id": "switch.shu_fang_switch_3", "name": "射灯"},
                {"id": "switch.xiaomi_m4_549b_dryer", "name": "干燥"},
                {"id": "switch.xiaomi_m4_549b_eco", "name": "ECO"},
                {"id": "switch.xiaomi_m4_549b_heater_2", "name": "辅热"},
                {"id": "switch.xiaomi_m4_549b_sleep_mode", "name": "睡眠"},
                {"id": "switch.xiaomi_m4_549b_switch_status", "name": "状态灯"},
                {"id": "switch.xiaomi_m4_549b_unstraight_blowing", "name": "防吹"},
                {"id": "switch.xiaomi_m4_549b_alarm", "name": "音效"},
                {"id": "switch.xiaomi_lx06_843f_sleep_mode", "name": "静音"},
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
            "icon": "mdi:door-open",
            "switches": [
                {"id": "switch.xuan_guan_switch_1", "name": "入户"},
                {"id": "switch.xuan_guan_switch_2", "name": "鞋柜"},
            ],
            "sensors": [
                "binary_sensor.xuan_guan_men_ci_door"
            ]
        },
        "阳台": {
            "icon": "mdi:flower",
            "switches": [
                {"id": "switch.yang_tai_switch_1", "name": "南阳"},
                {"id": "switch.yang_tai_switch_2", "name": "氛围灯"},
                {"id": "switch.yang_tai_switch_3", "name": "植物灯"},
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
            "icon": "mdi:bed-double",
            "switches": [
                {"id": "switch.zhu_wo_switch_1", "name": "主灯"},
                {"id": "switch.zhu_wo_switch_2", "name": "灯带"},
                {"id": "switch.zhu_wo_switch_3", "name": "阅灯"},
                {"id": "switch.zhu_wo_switch_4", "name": "夜灯"},
                {"id": "switch.xiaomi_m4_1c38_dryer", "name": "干燥"},
                {"id": "switch.xiaomi_m4_1c38_eco", "name": "ECO"},
                {"id": "switch.xiaomi_m4_1c38_heater_2", "name": "辅热"},
                {"id": "switch.xiaomi_m4_1c38_sleep_mode", "name": "睡眠"},
                {"id": "switch.xiaomi_m4_1c38_switch_status", "name": "指示"},
                {"id": "switch.xiaomi_m4_1c38_unstraight_blowing", "name": "防吹"},
                {"id": "switch.xiaomi_m4_1c38_alarm", "name": "警报"},
                {"id": "switch.zhu_wo_men_deng_switch_1", "name": "门灯"},
                {"id": "switch.zhu_wo_she_deng_tai_deng_switch_1", "name": "左射"},
                {"id": "switch.zhu_wo_she_deng_tai_deng_switch_2", "name": "右射"},
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
             "icon": "mdi:shower",
             "switches": [
                {"id": "switch.zhu_wei_switch_1", "name": "镜灯"},
                {"id": "switch.zhu_wei_switch_2", "name": "顶灯"},
                {"id": "switch.zhu_wei_kai_guan_switch_1", "name": "换气"},
                {"id": "switch.zhu_wei_kai_guan_switch_2", "name": "送风"},
             ]
        }
    }

    yaml_out = """title: "RACING DASHBOARD V6"
theme: default
background: "no-repeat center center / cover url('https://w.wallhaven.cc/full/qd/wallhaven-qd9rm5.png')"

button_card_templates:
  # ==========================================
  # [RACING GEAR SHIFT] - The Room Nav Buttons
  # ==========================================
  racing_gear_nav:
    show_name: true
    show_icon: true
    styles:
      card:
        - height: "55px" 
        - background: "rgba(10, 10, 12, 0.7)"
        - border-left: "3px solid transparent"
        - clip-path: "polygon(5% 0, 100% 0%, 95% 100%, 0% 100%)"
        - margin-bottom: "8px"
        - border-bottom: "1px solid rgba(255,255,255,0.05)"
        - padding: "0"
        - transition: "all 0.2s cubic-bezier(0.25, 0.8, 0.25, 1)"
      grid:
        - grid-template-areas: '"i n"'
        - grid-template-columns: "45px auto"
      icon:
        - color: "#444"
        - width: "24px"
      name:
        - color: "#888"
        - font-size: "15px"
        - font-weight: "700"
        - font-style: "italic"
        - justify-self: "start"
    state:
      - operator: template
        value: >
          [[[ return states['input_select.room_select'].state === variables.room_name; ]]]
        styles:
          card:
            - background: "linear-gradient(90deg, rgba(0, 210, 255, 0.3) 0%, rgba(10,10,12,0.8) 100%)"
            - border-left: "4px solid #00d2ff"
          icon:
            - color: "#00d2ff"
            - filter: "drop-shadow(0 0 5px #00d2ff)"
          name:
            - color: "#fff"
            - text-shadow: "0 0 8px rgba(0, 210, 255, 0.8)"
    tap_action:
      action: call-service
      service: input_select.select_option
      service_data:
        entity_id: input_select.room_select
        option: "[[[ return variables.room_name; ]]]"

views:
  - path: default_view
    title: RACING COCKPIT
    panel: true # Enable panel mode for full width
    cards:
      - type: custom:layout-card
        layout_type: custom:grid-layout
        layout:
          grid-template-columns: 16vw 84vw
          grid-template-rows: 100vh
          grid-gap: 0px
        cards:
          
          # ====================================================
          # LEFT GEAR BOX: Nav Base
          # ====================================================
          - type: vertical-stack
            view_layout:
              grid-column: 1
              grid-row: 1
            card_mod:
              style: |
                ha-card, div { 
                  height: 100vh !important; 
                  background: rgba(10, 11, 14, 0.95) !important; 
                  border-right: 2px solid rgba(0, 210, 255, 0.1);
                  padding: 15px 5px !important;
                }
            cards:
              - type: custom:button-card
                name: "ENGINE O-N"
                icon: mdi:engine
                styles:
                  card: [background: "transparent", border: "none", box-shadow: "none", margin-bottom: "15px"]
                  name: [color: "#ff2a5f", font-weight: "900", font-style: "italic", letter-spacing: "2px", font-size: "16px"]
                  icon: [color: "#ff2a5f", width: "45px"]
"""
    # Create the left navigation buttons
    for room, data in rooms_data.items():
        yaml_out += f"""              - type: custom:button-card
                name: "{room}"
                template: racing_nav
                icon: "{data['icon']}"
                variables:
                  room_name: "{room}"
"""

    yaml_out += """
          # ====================================================
          # RIGHT HUD DASHBOARD: The Main Screen
          # ====================================================
          - type: vertical-stack
            view_layout:
              grid-column: 2
              grid-row: 1
            card_mod:
              style: |
                ha-card, div { 
                   padding: 20px 40px !important; 
                   max-width: 100% !important; /* 强制填满红框区域 */
                   height: 100%;
                   overflow: hidden; /* 严禁滚动条 */
                }
            cards:
"""
    neon_colors = ["#ff2a5f", "#00d2ff", "#00ffcc", "#ffaa00", "#b366ff"]

    for idx, (room, data) in enumerate(rooms_data.items()):
        current_neon = neon_colors[idx % len(neon_colors)]
        
        yaml_out += f"""              - type: conditional
                conditions:
                  - entity: input_select.room_select
                    state: "{room}"
                card:
                  type: vertical-stack
                  cards:
                    
                    # 顶部状态栏
                    - type: custom:button-card
                      name: ">>> {room} // SYS_STATUS: OPTIMAL ..."
                      styles:
                        card: 
                          - background: "linear-gradient(90deg, rgba(20,22,28,0.9) 0%, transparent 100%)"
                          - border-left: "8px solid {current_neon}"
                          - height: "50px"
                          - margin-bottom: "20px"
                          - justify-content: "start"
                          - padding-left: "20px"
                          - border-radius: "0"
                        name:
                          - color: "#fff"
                          - font-size: "16px"
                          - font-weight: "900"
                          - font-family: "monospace"
                          - letter-spacing: "2px"
"""
        # ==========================================
        # 1. SWITCHES (Using mushroom entity to restore visual state but high density)
        # ==========================================
        if data.get("switches"):
            yaml_out += f"""                    - type: custom:mushroom-title-card
                      title: "CIRCUITS"
                      card_mod:
                        style: |
                          h1 {{ color: #777 !important; font-size: 14px !important; letter-spacing: 2px; text-transform: uppercase; }}
                    - type: grid
                      columns: 7 # 7列布局，完美利用极度宽广的右侧横向空间！
                      card_mod:
                        style: |
                          div#root {{ gap: 10px !important; margin-bottom: 20px; }}
                      cards:
"""
            for sw in data.get("switches", []):
                yaml_out += f"""                        - type: custom:mushroom-entity-card
                          entity: {sw['id']}
                          name: "{sw['name']}"
                          layout: horizontal
                          primary_info: name
                          secondary_info: state
                          card_mod:
                            style: |
                              ha-card {{ 
                                background: rgba(22, 24, 29, 0.8); 
                                border: 1px solid rgba(255,255,255,0.05); 
                                border-radius: 8px;
                                --primary-text-color: #ffffff;
                                --secondary-text-color: #aaaaaa;
                              }}
"""

        # ==========================================
        # 2. MEDIA & CLIMATES
        # ==========================================
        climates = data.get("climates", [])
        media = data.get("media", [])
        if climates or media:
             yaml_out += f"""                    - type: custom:mushroom-title-card
                      title: "ENGINES"
                      card_mod:
                        style: |
                          h1 {{ color: #777 !important; font-size: 14px !important; letter-spacing: 2px; text-transform: uppercase; }}
                    - type: grid
                      columns: 3
                      card_mod:
                        style: |
                          div#root {{ gap: 20px !important; margin-bottom: 20px; }}
                      cards:
"""
             for clim in climates:
                 yaml_out += f"""                        - type: custom:mushroom-climate-card
                          entity: {clim}
                          show_temperature_control: true
                          collapsible_controls: false
                          layout: horizontal
                          card_mod:
                            style: |
                              ha-card {{ 
                                background: rgba(20, 22, 28, 0.8); 
                                border-top: 3px solid {current_neon}; 
                                border-radius: 12px;
                                clip-path: polygon(0 0, 100% 0, 97% 100%, 0% 100%);
                                --primary-text-color: #ffffff;
                                --secondary-text-color: #aaaaaa;
                              }}
"""
             for med in media:
                 yaml_out += f"""                        - type: custom:mushroom-media-player-card
                          entity: {med}
                          use_media_info: true
                          show_volume_level: true
                          layout: horizontal
                          card_mod:
                            style: |
                              ha-card {{ 
                                background: rgba(20, 22, 28, 0.8); 
                                border-top: 3px solid {current_neon}; 
                                border-radius: 12px;
                                clip-path: polygon(3% 0, 100% 0, 100% 100%, 0% 100%);
                                --primary-text-color: #ffffff;
                                --secondary-text-color: #aaaaaa;
                              }}
"""

        # ==========================================
        # 3. LIGHTS AND COVERS
        # ==========================================
        lights = [d for d in data.get("devices", []) if d.startswith("light.")]
        covers = [d for d in data.get("devices", []) if d.startswith("cover.")]
        if lights or covers:
             yaml_out += f"""                    - type: custom:mushroom-title-card
                      title: "ILLUMINATION / COVERS"
                      card_mod:
                        style: |
                          h1 {{ color: #777 !important; font-size: 14px !important; letter-spacing: 2px; text-transform: uppercase; }}
                    - type: grid
                      columns: 4 # 利用宽度排列4列灯光滑块
                      card_mod:
                        style: |
                          div#root {{ gap: 15px !important; margin-bottom: 20px; }}
                      cards:
"""
             for light in lights:
                 yaml_out += f"""                        - type: custom:mushroom-light-card
                          entity: {light}
                          show_brightness_control: true
                          layout: horizontal
                          card_mod:
                            style: |
                              ha-card {{ 
                                background: rgba(25, 27, 33, 0.7); 
                                border: 1px dashed rgba(255,255,255,0.08);
                                border-radius: 8px;
                                --primary-text-color: #ffffff;
                                --secondary-text-color: #aaaaaa;
                              }}
"""
             for cov in covers:
                 yaml_out += f"""                        - type: custom:mushroom-cover-card
                          entity: {cov}
                          show_position_control: true
                          show_buttons_control: true
                          layout: horizontal
                          card_mod:
                            style: |
                              ha-card {{ 
                                background: rgba(25, 27, 33, 0.7); 
                                border: 1px dashed rgba(255,255,255,0.08);
                                border-radius: 8px;
                                --primary-text-color: #ffffff;
                                --secondary-text-color: #aaaaaa;
                              }}
"""

        # ==========================================
        # 4. SENSORS (HUD Stats)
        # ==========================================
        sensors = data.get("sensors", [])
        if sensors:
             yaml_out += f"""                    - type: custom:mushroom-title-card
                      title: "TELEMETRY"
                      card_mod:
                        style: |
                          h1 {{ color: #777 !important; font-size: 14px !important; letter-spacing: 2px; text-transform: uppercase; }}
                    - type: grid
                      columns: 6 # 更高密度的传感器阵列
                      card_mod:
                        style: |
                          div#root {{ gap: 12px !important; }}
                      cards:
"""
             for sens in sensors:
                 yaml_out += f"""                        - type: custom:mushroom-entity-card
                          entity: {sens}
                          layout: vertical
                          primary_info: state
                          secondary_info: name
                          icon_color: "{current_neon.replace('#','')}"
                          card_mod:
                            style: |
                              ha-card {{ 
                                background: rgba(0,0,0,0.4); 
                                border: 1px solid rgba({current_neon}, 0.2); 
                                border-radius: 6px;
                                --primary-text-color: #ffffff;
                                --secondary-text-color: #aaaaaa;
                              }}
"""

    
    with open("c:/Users/zhong/Downloads/Compressed/files/HA-UI/ha_cyber_ui_v6.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_out)
        print("Generated ha_cyber_ui_v6.yaml (Full Width Racing Cockpit)!")

if __name__ == "__main__":
    generate_yaml_v6()
