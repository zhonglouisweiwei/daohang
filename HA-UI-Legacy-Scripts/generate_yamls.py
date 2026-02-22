import yaml

def generate_yaml():
    rooms_data = {
        "餐厅": {
            "switches": [
                {"id": "switch.can_ting_switch_1", "name": "餐厅开关1"},
                {"id": "switch.can_ting_switch_2", "name": "餐厅开关2"},
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
            "switches": [
                {"id": "switch.ci_wo_switch_1", "name": "次卧开关1"},
                {"id": "switch.ci_wo_switch_2", "name": "次卧开关2"},
                {"id": "switch.ci_wo_switch_3", "name": "次卧开关3"},
                {"id": "switch.xiaomi_m4_50e9_dryer", "name": "空调干燥"},
                {"id": "switch.xiaomi_m4_50e9_eco", "name": "空调ECO"},
                {"id": "switch.xiaomi_m4_50e9_heater_2", "name": "空调加热"},
                {"id": "switch.xiaomi_m4_50e9_sleep_mode", "name": "睡眠模式"},
                {"id": "switch.xiaomi_m4_50e9_switch_status", "name": "状态显示"},
                {"id": "switch.xiaomi_m4_50e9_unstraight_blowing", "name": "防直吹"},
                {"id": "switch.xiaomi_m4_50e9_alarm", "name": "警报"},
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
            "switches": [
                {"id": "switch.guo_dao_switch_1", "name": "过道开关1"},
                {"id": "switch.guo_dao_switch_2", "name": "过道开关2"},
                {"id": "switch.guo_dao_switch_3", "name": "过道开关3"},
            ],
            "devices": [
                "light.lemesh_wy0c15_318d_light",
                "light.lemesh_wy0c15_033d_light",
                "light.lemesh_wy0c15_16a4_light",
                "light.lemesh_wy0c15_2faf_light",
            ]
        },
        "客厅": {
            "switches": [
                {"id": "switch.ke_ting_deng_dai_switch_1", "name": "灯带开关1"},
                {"id": "switch.ke_ting_deng_dai_switch_2", "name": "灯带开关2"},
                {"id": "switch.ke_ting_tong_deng_switch_1", "name": "筒灯开关1"},
                {"id": "switch.ke_ting_tong_deng_switch_2", "name": "筒灯开关2"},
                {"id": "switch.dooya_c1_f2db_mode_2", "name": "窗帘模式2"},
                {"id": "switch.dooya_c1_cc3d_mode_2", "name": "窗帘模式2"},
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
            "switches": [
                {"id": "switch.sheng_huo_yang_tai_switch_1", "name": "阳台开关1"},
                {"id": "switch.yszn01_ys2102_c8c6_dryer", "name": "烘干"},
                {"id": "switch.yszn01_ys2102_c8c6_uv", "name": "杀菌"},
            ],
            "devices": [
                "cover.yszn01_ys2102_c8c6_airer",
                "light.yszn01_ys2102_c8c6_light"
            ]
        },
        "书房": {
            "switches": [
                {"id": "switch.shu_fang_switch_1", "name": "书房开关1"},
                {"id": "switch.shu_fang_switch_2", "name": "书房开关2"},
                {"id": "switch.shu_fang_switch_3", "name": "书房开关3"},
                {"id": "switch.xiaomi_m4_549b_dryer", "name": "空调干燥"},
                {"id": "switch.xiaomi_m4_549b_eco", "name": "空调ECO"},
                {"id": "switch.xiaomi_m4_549b_heater_2", "name": "空调加热"},
                {"id": "switch.xiaomi_m4_549b_sleep_mode", "name": "睡眠模式"},
                {"id": "switch.xiaomi_m4_549b_switch_status", "name": "状态显示"},
                {"id": "switch.xiaomi_m4_549b_unstraight_blowing", "name": "防直吹"},
                {"id": "switch.xiaomi_m4_549b_alarm", "name": "警报"},
                {"id": "switch.xiaomi_lx06_843f_sleep_mode", "name": "音箱睡眠"},
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
            "switches": [
                {"id": "switch.xuan_guan_switch_1", "name": "玄关开关1"},
                {"id": "switch.xuan_guan_switch_2", "name": "玄关开关2"},
            ],
            "sensors": [
                "binary_sensor.xuan_guan_men_ci_door"
            ]
        },
        "阳台": {
            "switches": [
                {"id": "switch.yang_tai_switch_1", "name": "阳台开关1"},
                {"id": "switch.yang_tai_switch_2", "name": "阳台开关2"},
                {"id": "switch.yang_tai_switch_3", "name": "阳台开关3"},
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
            "switches": [
                {"id": "switch.zhu_wo_switch_1", "name": "主卧开关1"},
                {"id": "switch.zhu_wo_switch_2", "name": "主卧开关2"},
                {"id": "switch.zhu_wo_switch_3", "name": "主卧开关3"},
                {"id": "switch.zhu_wo_switch_4", "name": "主卧开关4"},
                {"id": "switch.xiaomi_m4_1c38_dryer", "name": "空调干燥"},
                {"id": "switch.xiaomi_m4_1c38_eco", "name": "空调ECO"},
                {"id": "switch.xiaomi_m4_1c38_heater_2", "name": "空调加热"},
                {"id": "switch.xiaomi_m4_1c38_sleep_mode", "name": "睡眠模式"},
                {"id": "switch.xiaomi_m4_1c38_switch_status", "name": "状态显示"},
                {"id": "switch.xiaomi_m4_1c38_unstraight_blowing", "name": "防直吹"},
                {"id": "switch.xiaomi_m4_1c38_alarm", "name": "警报"},
                {"id": "switch.zhu_wo_men_deng_switch_1", "name": "门灯开关"},
                {"id": "switch.zhu_wo_she_deng_tai_deng_switch_1", "name": "射灯开关1"},
                {"id": "switch.zhu_wo_she_deng_tai_deng_switch_2", "name": "射灯开关2"},
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
             "switches": [
                {"id": "switch.zhu_wei_switch_1", "name": "主卫开关1"},
                {"id": "switch.zhu_wei_switch_2", "name": "主卫开关2"},
                {"id": "switch.zhu_wei_kai_guan_switch_1", "name": "内部开关1"},
                {"id": "switch.zhu_wei_kai_guan_switch_2", "name": "内部开关2"},
             ]
        }
    }

    colors = ["#ff007f", "#00d2ff", "#00ffcc", "#ffaa00", "#7700ff", "#ff00bb", "#0088ff", "#00efff"]
    
    yaml_out = """title: 赛博中控 - CyberHome
button_card_templates:
  cyber_glow_box:
    styles:
      card:
        - background: "rgba(10, 15, 25, 0.4)"
        - backdrop-filter: "blur(10px)"
        - border-radius: "16px"
        - padding: "16px"
        - margin-bottom: "16px"
        - border: "1px solid rgba(0, 210, 255, 0.2)"
        - box-shadow: "0 0 20px rgba(0, 210, 255, 0.1)"
  room_nav_btn:
    show_name: true
    show_icon: false
    styles:
      card:
        - height: "55px"
        - background: "rgba(255, 255, 255, 0.03)"
        - backdrop-filter: "blur(8px)"
        - border: "1px solid rgba(255, 255, 255, 0.05)"
        - border-radius: "12px"
        - transition: "all 0.3s ease"
        - color: "#ccc"
        - margin-bottom: "12px"
        - box-shadow: "0 4px 6px rgba(0,0,0,0.1)"
      name:
        - font-size: "16px"
        - font-weight: "bold"
        - letter-spacing: "2px"
    state:
      - operator: template
        value: >
          [[[ return states['input_select.room_select'].state === variables.room_name; ]]]
        styles:
          card:
            - background: "rgba(0, 210, 255, 0.1)"
            - border: "1px solid #00d2ff"
            - transform: "translateX(-10px) scale(1.02)"
            - box-shadow: "0 0 20px rgba(0, 210, 255, 0.5), inset 0 0 10px rgba(0, 210, 255, 0.2)"
          name:
            - color: "#ffffff"
            - text-shadow: "0 0 8px #00d2ff"
    tap_action:
      action: call-service
      service: input_select.select_option
      service_data:
        entity_id: input_select.room_select
        option: "[[[ return variables.room_name; ]]]"
  cyber_switch:
    show_state: false
    show_name: true
    show_icon: true
    styles:
      card:
        - height: "80px"
        - background: "rgba(20, 20, 25, 0.6)"
        - border-radius: "12px"
        - border: "1px solid rgba(255,255,255,0.05)"
        - padding: "10px"
        - transition: "all 0.3s ease"
        - margin-bottom: "8px"
      grid:
        - grid-template-areas: '"i n"'
        - grid-template-columns: "40% 60%"
      icon:
        - color: "#444"
        - width: "28px"
        - transition: "all 0.3s ease"
      name:
        - color: "#777"
        - font-size: "14px"
        - justify-self: "start"
        - align-self: "center"
    state:
      - value: "on"
        styles:
          card:
            - background: "rgba(30, 35, 45, 0.8)"
            - border: "1px solid var(--accent-color, #ff007f)"
            - box-shadow: "0 0 15px var(--accent-color, rgba(255, 0, 127, 0.3))"
          icon:
            - color: "var(--accent-color, #ff007f)"
            - filter: "drop-shadow(0 0 8px var(--accent-color, #ff007f))"
          name:
            - color: "#fff"
            - text-shadow: "0 0 2px rgba(255,255,255,0.2)"
  cyber_round_btn:
    show_name: true
    show_state: true
    styles:
      card:
        - aspect-ratio: "1/1"
        - border-radius: "20%"
        - background: "rgba(20, 20, 25, 0.6)"
        - border: "1px solid rgba(255,255,255,0.05)"
        - margin-bottom: "8px"
      icon:
        - color: "#444"
        - width: "30%"
      name:
        - color: "#777"
        - font-size: "12px"
        - margin-top: "4%"
      state:
        - color: "#999"
        - font-size: "10px"
    state:
      - value: "on"
        styles:
          card:
            - border: "1px solid #00efff"
            - box-shadow: "0 0 15px rgba(0, 239, 255, 0.3)"
          icon:
            - color: "#00efff"
          name:
            - color: "#fff"

views:
  - path: default_view
    title: 赛博主控界面
    background: "linear-gradient(135deg, #0f1016 0%, #171824 50%, #0d0e15 100%)"
    panel: true
    cards:
      - type: grid
        columns: 3
        card_mod:
          style: |
            div#root {
              grid-template-columns: 20% 65% 15% !important;
              gap: 16px;
              padding: 16px;
            }
        cards:
          
          # 1. ==== 左栏 ====
          - type: vertical-stack
            cards:
              - type: custom:button-card
                template: cyber_glow_box
                custom_fields:
                  weather:
                    card:
                      type: weather-forecast
                      entity: weather.forecast_wo_de_jia
                      show_forecast: false
                      card_mod:
                        style: |
                          ha-card { background: none !important; border: none !important; box-shadow: none !important; }

              - type: custom:button-card
                template: cyber_glow_box
                custom_fields:
                  persons:
                    card:
                      type: horizontal-stack
                      cards:
                        - type: custom:mushroom-person-card
                          entity: person.zuo_deng_zhen_xiang
                          icon_type: entity-picture
                          layout: vertical
                        - type: custom:mushroom-person-card
                          entity: person.jing_jing_jing
                          icon_type: entity-picture
                          layout: vertical

              - type: custom:button-card
                template: cyber_glow_box
                name: "SYS//STATUS_OK"
                styles:
                  name: [color: "#00d2ff", font-family: "monospace", font-size: "12px", justify-self: "start"]
                custom_fields:
                  server:
                    card:
                      type: entities
                      entities:
                        - entity: sensor.mi_1329721117_message
                          name: 系统信息
                      card_mod:
                        style: |
                          ha-card { background: none; border: none; box-shadow: none; color: white;}

          # 2. ==== 中栏 ====
          - type: custom:button-card
            template: cyber_glow_box
            styles:
              card: [ height: "95vh", overflow-y: "auto" ]
            custom_fields:
"""
    for room, data in rooms_data.items():
        yaml_out += f"""
              room_{room}:
                card:
                  type: conditional
                  conditions:
                    - entity: input_select.room_select
                      state: "{room}"
                  card:
                    type: grid
                    columns: 2
                    card_mod:
                      style: |
                        div#root {{
                          grid-template-columns: 25% 75% !important;
                          gap: 16px;
                        }}
                    cards:
                      - type: vertical-stack
                        cards:
"""
        # Add Switches
        c_idx = 0
        for sw in data.get("switches", []):
            yaml_out += f"""                          - type: custom:button-card
                            entity: {sw['id']}
                            name: "{sw['name']}"
                            template: cyber_switch
                            variables: {{ accent_color: "{colors[c_idx % len(colors)]}" }}
"""
            c_idx += 1
            
        yaml_out += f"""                      - type: vertical-stack
                        cards:
"""
        # Add Climates
        for clim in data.get("climates", []):
            yaml_out += f"""                          - type: thermostat
                            entity: {clim}
                            card_mod:
                              style: |
                                ha-card {{ background: rgba(0,0,0,0.3) !important; border: 1px solid rgba(0,255,255,0.2) !important; }}
"""

        # Add media
        for med in data.get("media", []):
            yaml_out += f"""                          - type: media-control
                            entity: {med}
"""
        
        # Add Devices
        if data.get("devices"):
            yaml_out += f"""                          - type: grid
                            columns: 2
                            cards:
"""
            for dev in data.get("devices", []):
                if dev.startswith("light."):
                    yaml_out += f"""                              - type: custom:mushroom-light-card
                                entity: {dev}
                                show_brightness_control: true
"""
                elif dev.startswith("cover."):
                    yaml_out += f"""                              - type: custom:mushroom-cover-card
                                entity: {dev}
                                show_position_control: true
                                show_buttons_control: true
"""
        
        # Add Sensors
        if data.get("sensors"):
            yaml_out += f"""                          - type: grid
                            columns: 4
                            cards:
"""
            for sens in data.get("sensors", []):
                yaml_out += f"""                              - type: custom:button-card
                                entity: {sens}
                                template: cyber_round_btn
"""

    yaml_out += """
          # 3. ==== 右栏 ====
          - type: vertical-stack
            cards:
"""
    for room in rooms_data.keys():
        yaml_out += f"""              - type: custom:button-card
                name: {room}
                template: room_nav_btn
                variables:
                  room_name: "{room}"
"""

    with open("c:/Users/zhong/Downloads/Compressed/files/HA-UI/ha_cyber_ui.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_out)

if __name__ == "__main__":
    generate_yaml()
