import yaml
import json

def generate_yaml_v2():
    # Same data but organized cleaner
    rooms_data = {
        "餐厅": {
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
            "switches": [
                {"id": "switch.shu_fang_switch_1", "name": "书房主灯"},
                {"id": "switch.shu_fang_switch_2", "name": "氛围灯"},
                {"id": "switch.shu_fang_switch_3", "name": "射灯"},
                {"id": "switch.xiaomi_m4_549b_dryer", "name": "空调干燥"},
                {"id": "switch.xiaomi_m4_549b_eco", "name": "空调ECO"},
                {"id": "switch.xiaomi_m4_549b_heater_2", "name": "辅热"},
                {"id": "switch.xiaomi_m4_549b_sleep_mode", "name": "睡眠模式"},
                {"id": "switch.xiaomi_m4_549b_switch_status", "name": "指示灯"},
                {"id": "switch.xiaomi_m4_549b_unstraight_blowing", "name": "防直吹"},
                {"id": "switch.xiaomi_m4_549b_alarm", "name": "提示音"},
                {"id": "switch.xiaomi_lx06_843f_sleep_mode", "name": "安静模式"},
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
                {"id": "switch.xuan_guan_switch_1", "name": "入户顶灯"},
                {"id": "switch.xuan_guan_switch_2", "name": "鞋柜灯带"},
            ],
            "sensors": [
                "binary_sensor.xuan_guan_men_ci_door"
            ]
        },
        "阳台": {
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
             "switches": [
                {"id": "switch.zhu_wei_switch_1", "name": "镜前灯"},
                {"id": "switch.zhu_wei_switch_2", "name": "主顶灯"},
                {"id": "switch.zhu_wei_kai_guan_switch_1", "name": "换气"},
                {"id": "switch.zhu_wei_kai_guan_switch_2", "name": "送风"},
             ]
        }
    }

    yaml_out = """title: "NEON HOME 2.0"
theme: default
button_card_templates:
  # -----------------------------------------------
  # 全局容器：导航按钮专用，毛玻璃+选中高亮特效
  # -----------------------------------------------
  cyber_nav:
    show_name: true
    show_icon: true
    styles:
      card:
        - height: "60px"
        - background: "rgba(30, 32, 40, 0.4)" # 深邃毛玻璃
        - backdrop-filter: "blur(12px)"
        - border: "1px solid rgba(255, 255, 255, 0.05)"
        - border-radius: "16px"
        - transition: "all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)"
        - color: "#8a91a6"
        - margin-bottom: "10px"
        - box-shadow: "0 4px 15px rgba(0,0,0,0.2)"
      name:
        - font-size: "16px"
        - font-weight: "600"
        - letter-spacing: "1px"
        - justify-self: "start"
        - padding-left: "15px"
      icon:
        - color: "#8a91a6"
        - justify-self: "end"
        - padding-right: "15px"
        - width: "24px"
      grid:
        - grid-template-areas: '"n i"'
        - grid-template-columns: "1fr 1fr"
    state:
      - operator: template
        value: >
          [[[ return states['input_select.room_select'].state === variables.room_name; ]]]
        styles:
          card:
            - background: "linear-gradient(90deg, rgba(0, 210, 255, 0.15) 0%, rgba(30,32,40,0.4) 100%)"
            - border-left: "4px solid #00d2ff"
            - border-top: "1px solid rgba(0, 210, 255, 0.3)"
            - border-bottom: "1px solid rgba(0, 210, 255, 0.3)"
            - border-right: "1px solid rgba(255, 255, 255, 0.05)"
            - transform: "translateX(5px)"
            - box-shadow: "0 0 25px rgba(0, 210, 255, 0.15)"
          name:
            - color: "#ffffff"
          icon:
            - color: "#00d2ff"
            - filter: "drop-shadow(0 0 5px #00d2ff)"
    tap_action:
      action: call-service
      service: input_select.select_option
      service_data:
        entity_id: input_select.room_select
        option: "[[[ return variables.room_name; ]]]"

  # -----------------------------------------------
  # Bento 磁贴：适用于小型开关，只有开启状态才亮主色调
  # -----------------------------------------------
  bento_switch:
    show_state: false
    show_name: true
    show_icon: true
    styles:
      card:
        - aspect-ratio: "3/1" # 长方形磁贴
        - background: "rgba(22, 24, 29, 0.7)" # 极深色底框
        - border-radius: "16px"
        - border: "1px solid rgba(255, 255, 255, 0.05)"
        - padding: "10px 15px"
        - transition: "all 0.3s ease"
      grid:
        - grid-template-areas: '"i n"'
        - grid-template-columns: "40px auto"
      icon:
        - color: "#4b5162" # 熄灭时发灰
        - width: "22px"
        - justify-self: "start"
      name:
        - color: "#6e7587"
        - font-size: "13px"
        - font-weight: "500"
        - justify-self: "start"
        - align-self: "center"
    state:
      - value: "on"
        styles:
          card:
            - background: "rgba(30, 34, 42, 0.9)"
            - border: "1px solid var(--accent, #00d2ff)"
            - box-shadow: "0 4px 15px var(--glow, rgba(0, 210, 255, 0.2))"
          icon:
            - color: "var(--accent, #00d2ff)"
            - filter: "drop-shadow(0 0 5px var(--accent, #00d2ff))"
          name:
            - color: "#ffffff"

views:
  - path: default_view
    title: 赛博中控室
    background: "#0b0c10" # 深邃纯黑赛博背景
    panel: true
    cards:
      - type: grid
        columns: 2
        card_mod:
          style: |
            div#root {
              grid-template-columns: 75% 25% !important; /* 75/25黄金分割 */
              gap: 24px;
              padding: 24px 32px;
              max-width: 100%;
              margin: 0 auto;
            }
        cards:
          
          # ====================================================
          # 左侧：动态主场馆舞台 (75%宽区)
          # ====================================================
          - type: vertical-stack
            cards:
"""
    # Define accent colors corresponding to zones/types
    switch_colors = [
        {"accent": "#ff2a5f", "glow": "rgba(255, 42, 95, 0.2)"}, 
        {"accent": "#00d2ff", "glow": "rgba(0, 210, 255, 0.2)"},
        {"accent": "#00ffcc", "glow": "rgba(0, 255, 204, 0.2)"},
        {"accent": "#b366ff", "glow": "rgba(179, 102, 255, 0.2)"},
        {"accent": "#ffaa00", "glow": "rgba(255, 170, 0, 0.2)"}
    ]

    for room, data in rooms_data.items():
        yaml_out += f"""
              # --- {room} 面板 ---
              - type: conditional
                conditions:
                  - entity: input_select.room_select
                    state: "{room}"
                card:
                  type: vertical-stack
                  cards:
"""
        # 1. 顶部大看板：媒体或空调 (如果有则横跨)
        has_top_widgets = data.get("climates") or data.get("media")
        if has_top_widgets:
            yaml_out += f"""                    # 顶级面板聚合
                    - type: custom:mushroom-title-card
                      title: 🌡️ 环境与音视频
                      title_tap_action:
                        action: none
                      subtitle_tap_action:
                        action: none
                      card_mod:
                        style: |
                          ha-card {{ padding: 0px 8px; margin-bottom: -10px; --title-color: #8a91a6; --title-font-size: 16px; --title-font-weight: 500; }}
                    - type: grid
                      columns: 2
                      cards:
"""
            for clim in data.get("climates", []):
                yaml_out += f"""                        - type: custom:mushroom-climate-card
                          entity: {clim}
                          show_temperature_control: true
                          collapsible_controls: false
                          layout: horizontal
                          card_mod:
                            style: |
                              ha-card {{ background: rgba(22, 24, 29, 0.6); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
"""
            for med in data.get("media", []):
                yaml_out += f"""                        - type: custom:mushroom-media-player-card
                          entity: {med}
                          use_media_info: true
                          show_volume_level: true
                          layout: horizontal
                          card_mod:
                            style: |
                              ha-card {{ background: rgba(22, 24, 29, 0.6); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
"""

        # 2. 中间区：灯光流明系统
        light_devices = [d for d in data.get("devices", []) if d.startswith("light.")]
        cover_devices = [d for d in data.get("devices", []) if d.startswith("cover.")]
        
        if light_devices or cover_devices:
            yaml_out += f"""                    # 灯光与窗帘聚合
                    - type: custom:mushroom-title-card
                      title: 💡 照明与开合
                      title_tap_action:
                        action: none
                      card_mod:
                        style: |
                          ha-card {{ padding: 20px 8px 0px 8px; margin-bottom: -10px; --title-color: #8a91a6; --title-font-size: 16px; --title-font-weight: 500; }}
                    - type: grid
                      columns: 3
                      cards:
"""
            for light in light_devices:
                yaml_out += f"""                        - type: custom:mushroom-light-card
                          entity: {light}
                          show_brightness_control: true
                          show_color_temp_control: false
                          layout: vertical
                          card_mod:
                            style: |
                              ha-card {{ background: rgba(22, 24, 29, 0.5); border: 1px solid rgba(255,255,255,0.03); border-radius: 16px; transition: all 0.3s ease; }}
"""
            for cov in cover_devices:
                yaml_out += f"""                        - type: custom:mushroom-cover-card
                          entity: {cov}
                          show_position_control: true
                          show_buttons_control: true
                          layout: vertical
                          card_mod:
                            style: |
                              ha-card {{ background: rgba(22, 24, 29, 0.5); border: 1px solid rgba(255,255,255,0.03); border-radius: 16px; transition: all 0.3s ease; }}
"""

        # 3. 物理开关磁贴阵列
        if data.get("switches"):
            yaml_out += f"""                    # 物理按键磁贴阵列
                    - type: custom:mushroom-title-card
                      title: ⚙️ 控制矩阵
                      title_tap_action:
                        action: none
                      card_mod:
                        style: |
                          ha-card {{ padding: 20px 8px 0px 8px; margin-bottom: -10px; --title-color: #8a91a6; --title-font-size: 16px; --title-font-weight: 500; }}
                    - type: grid
                      columns: 4
                      card_mod:
                        style: |
                          div#root {{ gap: 12px; }}
                      cards:
"""
            c_idx = 0
            for sw in data.get("switches", []):
                color_set = switch_colors[c_idx % len(switch_colors)]
                yaml_out += f"""                        - type: custom:button-card
                          entity: {sw['id']}
                          name: "{sw['name']}"
                          template: bento_switch
                          variables: 
                            accent: "{color_set['accent']}"
                            glow: "{color_set['glow']}"
"""
                c_idx += 1

        # 4. 传感器小圆粒阵列
        if data.get("sensors"):
            yaml_out += f"""                    # 传感器阵列
                    - type: custom:mushroom-title-card
                      title: 📡 环境节点探测
                      title_tap_action:
                        action: none
                      card_mod:
                        style: |
                          ha-card {{ padding: 20px 8px 0px 8px; margin-bottom: -10px; --title-color: #8a91a6; --title-font-size: 16px; --title-font-weight: 500; }}
                    - type: grid
                      columns: 5
                      cards:
"""
            # Add mushrooms instead of round buttons
            for sens in data.get("sensors", []):
                yaml_out += f"""                        - type: custom:mushroom-entity-card
                          entity: {sens}
                          layout: vertical
                          primary_info: state
                          secondary_info: name
                          icon_color: cyan
                          card_mod:
                            style: |
                              ha-card {{ background: rgba(22, 24, 29, 0.6); border: 1px dashed rgba(0, 210, 255, 0.2); border-radius: 16px; }}
"""

    yaml_out += """
          # ====================================================
          # 右侧：常驻导航与总览中框 (25%宽区)
          # ====================================================
          - type: vertical-stack
            cards:
              
              # 顶端天气与人物 (去边框融合)
              - type: custom:mushroom-title-card
                title: NEON HOME
                subtitle: 实时状态终端
                title_tap_action:
                  action: none
                card_mod:
                  style: |
                    ha-card { padding: 0 0 10px 0; --title-color: #ffffff; --title-font-size: 26px; --subtitle-color: #00d2ff; --subtitle-font-size: 14px; letter-spacing: 1px; font-weight: 800; }
              
              - type: weather-forecast
                entity: weather.forecast_wo_de_jia
                show_forecast: false
                card_mod:
                  style: |
                    ha-card { background: none !important; border: none !important; box-shadow: none !important; padding-left: 0; }
              
              - type: custom:mushroom-person-card
                entity: person.zuo_deng_zhen_xiang
                icon_type: entity-picture
                layout: horizontal
                card_mod:
                  style: |
                     ha-card { background: rgba(30,32,40,0.4); border: 1px solid rgba(255,255,255,0.05); }
              
              - type: custom:mushroom-person-card
                entity: person.jing_jing_jing
                icon_type: entity-picture
                layout: horizontal
                card_mod:
                  style: |
                     ha-card { background: rgba(30,32,40,0.4); border: 1px solid rgba(255,255,255,0.05); }

              # 导航房间分隔线
              - type: custom:mushroom-title-card
                title: 
                subtitle: 区域导航系统
                card_mod:
                  style: |
                    ha-card {border-top: 1px solid rgba(255,255,255,0.1); margin-top: 15px; padding-top: 15px; margin-bottom: -5px; --subtitle-color: #6e7587;}

              # 动态房间按钮群
"""
    # 注入右侧所有房间切换按钮
    icon_map = {
        "餐厅": "mdi:silverware-fork-knife",
        "厨房": "mdi:stove",
        "次卧": "mdi:bed-empty",
        "过道": "mdi:transit-connection-horizontal",
        "客厅": "mdi:sofa",
        "生活阳台": "mdi:washing-machine",
        "书房": "mdi:laptop",
        "玄关": "mdi:door-open",
        "阳台": "mdi:flower",
        "主卧": "mdi:bed-double",
        "主卫": "mdi:shower"
    }

    for room in rooms_data.keys():
        yaml_out += f"""              - type: custom:button-card
                name: "{room}"
                template: cyber_nav
                icon: "{icon_map.get(room, 'mdi:cube-outline')}"
                variables:
                  room_name: "{room}"
"""

    with open("c:/Users/zhong/Downloads/Compressed/files/HA-UI/ha_cyber_ui_v2.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_out)
    
    print("Created ha_cyber_ui_v2.yaml successfully!")

if __name__ == "__main__":
    generate_yaml_v2()

