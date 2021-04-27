<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" version="3.16.3-Hannover" styleCategories="Symbology|Labeling">
  <renderer-v2 enableorderby="0" forceraster="0" symbollevels="0" type="RuleRenderer">
    <rules key="{fa6c4aa2-b507-461c-b67d-18ef4ebe3184}">
      <rule filter=" &quot;surfacecategory&quot; ='FLO'" label="Flore" key="{fe098b19-9d6e-4752-925a-8aad2ced2f5d}" symbol="0">
        <rule filter=" $area &lt;5" key="{8b6acef9-2e40-44b7-89d8-a43d6e586441}" symbol="1"/>
        <rule filter="ELSE" label="Flore" key="{c35bf1bf-0a47-4010-acb1-6445b0807dec}" symbol="2"/>
      </rule>
      <rule filter=" &quot;surfacecategory&quot; ='HAB'" label="Habitat" key="{dfa059cb-e59c-47af-8e4a-c5d78a49d73b}" symbol="3"/>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" force_rhr="0" name="0" alpha="1" type="fill">
        <layer pass="0" locked="0" enabled="1" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,255,255,0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,255,255,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="1" alpha="1" type="fill">
        <layer pass="0" locked="0" enabled="1" class="CentroidFill">
          <prop k="clip_on_current_part_only" v="0"/>
          <prop k="clip_points" v="0"/>
          <prop k="point_on_all_parts" v="1"/>
          <prop k="point_on_surface" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@1@0" alpha="1" type="marker">
            <layer pass="0" locked="0" enabled="1" class="SvgMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,255,255,255"/>
              <prop k="fixedAspectRatio" v="0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgo8c3ZnCiAgICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgICBpZD0ic3ZnMzIyOCIKICAgIHNvZGlwb2RpOmRvY25hbWU9Il9zdmdjbGVhbjIuc3ZnIgogICAgdmlld0JveD0iMCAwIDY2NS4yMyA5MzAuMDUiCiAgICBzb2RpcG9kaTp2ZXJzaW9uPSIwLjMyIgogICAgdmVyc2lvbj0iMS4xIgogICAgaW5rc2NhcGU6b3V0cHV0X2V4dGVuc2lvbj0ib3JnLmlua3NjYXBlLm91dHB1dC5zdmcuaW5rc2NhcGUiCiAgICBpbmtzY2FwZTp2ZXJzaW9uPSIwLjQ4LjMuMSByOTg4NiIKICA+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgICBpZD0ibmFtZWR2aWV3MzIzMiIKICAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjY0NSIKICAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMCIKICAgICAgaW5rc2NhcGU6em9vbT0iMC41NDg0ODQ4NSIKICAgICAgaW5rc2NhcGU6d2luZG93LXg9IjAiCiAgICAgIHNob3dncmlkPSJmYWxzZSIKICAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJsYXllcjEiCiAgICAgIGlua3NjYXBlOmN4PSIzNDEuMDcxMTYiCiAgICAgIGlua3NjYXBlOmN5PSIzOTIuMDgzNTIiCiAgICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iNjc0IgogICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0iaW4iCiAgLz4KICA8ZwogICAgICBpZD0ibGF5ZXIxIgogICAgICBpbmtzY2FwZTpsYWJlbD0iTGF5ZXIgMSIKICAgICAgaW5rc2NhcGU6Z3JvdXBtb2RlPSJsYXllciIKICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQxLjQyOSAtMTkuMzkyKSIKICAgID4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODA2IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2NjY2NjY2NjY2NjY2NjY2NjY2NjYyIKICAgICAgICBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjQuMTM3MjtmaWxsOiM1NzU4ZjUiCiAgICAgICAgZD0ibTM3OS4yMyA0MzguMjRjLTQuOTUgNTkuNzktNDIuMDUgMTE3LjktOTQuOTcgMTQ3LjE0LTQ5LjY0IDI2LjY2LTEyMCA3LjIzLTE0Mi45NC00My44LTE3Ljc2LTQ1Ljc5LTEuMDgtOTkuMjEgMzEuMzQtMTM0LjYyIDI0LjkyLTI3Ljg5IDYxLjgxLTM5LjA0IDk1LjY3LTU0LjMxLTUyLjU0IDYuNjgtMTA4LjI4LTMuOC0xNDkuMzgtMzYuMS0yNS4xNS0xOC4zMS00OS45ODItNDUuNzgtNDguOTM1LTc4LjQgMi41MjItNDguMTYgNTMuMzI1LTg3LjQ5IDEwMi42Ni03OS44OSA2MS4xNiA4Ljg0IDEwOC4xOSA1Mi43MyAxNDYuNTYgOTcuMjQtMTMuNzEtMTIuMzMtMjYuNDYtMzEuOS0zMi4xNy00OS4wOS0xNy4yMy03MS41MiAyMy4zMS0xNTEuNTkgOTIuNi0xODEuMTQgMTQuNTctNy4wMDQgMzIuNDMtNC4wMjQgNDUuMTEgNi4yNjMgMzMuMzkgMjQuOTk4IDU1LjkgNjUuMjMgNTMuOSAxMDYuNS01LjE2IDQ0Ljk3LTI4LjQ0IDgzLjg4LTUzLjI0IDEyMS41IDIwLjkyLTM3LjIgNDguNzMtNjkgOTEuNjItODYuNTEgNTQuNzEtMjIuNTUgMTI3LjM5LTIyLjE1IDE2OS43NyAyMy43MyAyNy4wNSAyNi4xMyAyMS40NiA3Mi44Ni00Ljk0IDk3LjQ2LTI5LjY4IDI3LjE3LTcwLjM1IDM3LjA2LTEwOC4wNiA0Ny4yNi0zMi40MiAxMC4zLTcyLjM4IDAuNjItMTA1LjE1IDAuMjUgMzAuMDkgMS40NiA2OC42IDEuODcgOTEuMzEgMTcuNDQgMzUuMDggMjQuMjggNzAuNTMgNTguODIgNjQuODQgMTA0LjQxLTYuOTYgNTAuODQtNTEuNTIgMTA2LjczLTEwOS4yIDk3LjU5LTYwLjExLTEwLjA3LTEwOS4zNC03MS42OC0xMzYuNC0xMjIuOTJ6IgogICAgLz4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODAwIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6My44OTgyO2ZpbGw6I2ZkZmYwOCIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIGQ9Im00MDguNTkgMjU4LjMyYzU0LjczIDI2LjYxIDY1LjA3IDExMC4xMSAxOS42OSAxNTAuMjEtNDAuNDYgNDAuMTktMTE2Ljk5IDMxLjM3LTE0NC41Mi0xOS41Mi0yOC41LTQzLjcxLTEwLjU0LTEwOS42MyAzNy41OS0xMzEuNDUgMjYuNTMtMTMuODYgNTkuODMtMTMuMDkgODcuMjQgMC43NnoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDM4IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDo1LjM1Mjk7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im01OTcuNDQgNjMwLjcyYzQ2LjcyIDE5Ny41OC0xMTYuNzIgMjUzLjU4LTIzNy41IDMxNC41NCAyOS43Ny0xMjIuNjQgNy42NC0yNzQuNDcgMjM3LjUtMzE0LjU0eiIKICAgIC8+CiAgICA8cGF0aAogICAgICAgIGlkPSJwYXRoMzc4OSIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIHNvZGlwb2RpOm5vZGV0eXBlcz0iY2NjIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6NS4zMzc4O2ZpbGw6IzM3ZGMxMSIKICAgICAgICBkPSJtNDQuMTU5IDY1NC4zM2MtNC4wMDIgMTk5LjM4IDE4OSAyMjkuNzEgMzA5LjQ0IDI5MC41LTMyLjA1LTEyNC42Ni0xMTAuOTgtMjg4LjM5LTMwOS40NC0yOTAuNXoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDMyIgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyLjg1MTQ7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im0zNTcuMTkgOTQ4LjAyYy00OC42OC0yOTUuODUgNDIuNDItMjk5LjY0IDIxLjM5LTUxMS45NiA0OC4zMSAxNDIuNTQtMzUuMyAxODguMzItMjEuMzkgNTExLjk2eiIKICAgIC8+CiAgPC9nCiAgPgogIDxtZXRhZGF0YQogICAgICBpZD0ibWV0YWRhdGExMCIKICAgID4KICAgIDxyZGY6UkRGCiAgICAgID4KICAgICAgPGNjOldvcmsKICAgICAgICA+CiAgICAgICAgPGRjOmZvcm1hdAogICAgICAgICAgPmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdAogICAgICAgID4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIgogICAgICAgIC8+CiAgICAgICAgPGNjOmxpY2Vuc2UKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9saWNlbnNlcy9wdWJsaWNkb21haW4vIgogICAgICAgIC8+CiAgICAgICAgPGRjOnB1Ymxpc2hlcgogICAgICAgICAgPgogICAgICAgICAgPGNjOkFnZW50CiAgICAgICAgICAgICAgcmRmOmFib3V0PSJodHRwOi8vb3BlbmNsaXBhcnQub3JnLyIKICAgICAgICAgICAgPgogICAgICAgICAgICA8ZGM6dGl0bGUKICAgICAgICAgICAgICA+T3BlbmNsaXBhcnQ8L2RjOnRpdGxlCiAgICAgICAgICAgID4KICAgICAgICAgIDwvY2M6QWdlbnQKICAgICAgICAgID4KICAgICAgICA8L2RjOnB1Ymxpc2hlcgogICAgICAgID4KICAgICAgPC9jYzpXb3JrCiAgICAgID4KICAgICAgPGNjOkxpY2Vuc2UKICAgICAgICAgIHJkZjphYm91dD0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbGljZW5zZXMvcHVibGljZG9tYWluLyIKICAgICAgICA+CiAgICAgICAgPGNjOnBlcm1pdHMKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyNSZXByb2R1Y3Rpb24iCiAgICAgICAgLz4KICAgICAgICA8Y2M6cGVybWl0cwogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL25zI0Rpc3RyaWJ1dGlvbiIKICAgICAgICAvPgogICAgICAgIDxjYzpwZXJtaXRzCiAgICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjRGVyaXZhdGl2ZVdvcmtzIgogICAgICAgIC8+CiAgICAgIDwvY2M6TGljZW5zZQogICAgICA+CiAgICA8L3JkZjpSREYKICAgID4KICA8L21ldGFkYXRhCiAgPgo8L3N2Zwo+Cg=="/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="5.2"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="2" alpha="1" type="fill">
        <layer pass="0" locked="0" enabled="1" class="ShapeburstFill">
          <prop k="blur_radius" v="2"/>
          <prop k="color" v="113,214,118,255"/>
          <prop k="color1" v="13,8,135,255"/>
          <prop k="color2" v="166,206,227,255"/>
          <prop k="color_type" v="0"/>
          <prop k="discrete" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MM"/>
          <prop k="gradient_color2" v="255,255,255,0"/>
          <prop k="ignore_rings" v="0"/>
          <prop k="max_distance" v="2"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="rampType" v="gradient"/>
          <prop k="stops" v="0.0196078;27,6,141,255:0.0392157;38,5,145,255:0.0588235;47,5,150,255:0.0784314;56,4,154,255:0.0980392;65,4,157,255:0.117647;73,3,160,255:0.137255;81,2,163,255:0.156863;89,1,165,255:0.176471;97,0,167,255:0.196078;105,0,168,255:0.215686;113,0,168,255:0.235294;120,1,168,255:0.254902;128,4,168,255:0.27451;135,7,166,255:0.294118;142,12,164,255:0.313725;149,17,161,255:0.333333;156,23,158,255:0.352941;162,29,154,255:0.372549;168,34,150,255:0.392157;174,40,146,255:0.411765;180,46,141,255:0.431373;186,51,136,255:0.45098;191,57,132,255:0.470588;196,62,127,255:0.490196;201,68,122,255:0.509804;205,74,118,255:0.529412;210,79,113,255:0.54902;214,85,109,255:0.568627;218,91,105,255:0.588235;222,97,100,255:0.607843;226,102,96,255:0.627451;230,108,92,255:0.647059;233,114,87,255:0.666667;237,121,83,255:0.686275;240,127,79,255:0.705882;243,133,75,255:0.72549;245,140,70,255:0.745098;247,147,66,255:0.764706;249,154,62,255:0.784314;251,161,57,255:0.803922;252,168,53,255:0.823529;253,175,49,255:0.843137;254,183,45,255:0.862745;254,190,42,255:0.882353;253,198,39,255:0.901961;252,206,37,255:0.921569;251,215,36,255:0.941176;248,223,37,255:0.960784;246,232,38,255:0.980392;243,240,39,255"/>
          <prop k="use_whole_shape" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="0" locked="0" enabled="1" class="SVGFill">
          <prop k="angle" v="0"/>
          <prop k="color" v="51,131,44,255"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgo8c3ZnCiAgICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgICBpZD0ic3ZnMzIyOCIKICAgIHNvZGlwb2RpOmRvY25hbWU9Il9zdmdjbGVhbjIuc3ZnIgogICAgdmlld0JveD0iMCAwIDY2NS4yMyA5MzAuMDUiCiAgICBzb2RpcG9kaTp2ZXJzaW9uPSIwLjMyIgogICAgdmVyc2lvbj0iMS4xIgogICAgaW5rc2NhcGU6b3V0cHV0X2V4dGVuc2lvbj0ib3JnLmlua3NjYXBlLm91dHB1dC5zdmcuaW5rc2NhcGUiCiAgICBpbmtzY2FwZTp2ZXJzaW9uPSIwLjQ4LjMuMSByOTg4NiIKICA+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgICBpZD0ibmFtZWR2aWV3MzIzMiIKICAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjY0NSIKICAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMCIKICAgICAgaW5rc2NhcGU6em9vbT0iMC41NDg0ODQ4NSIKICAgICAgaW5rc2NhcGU6d2luZG93LXg9IjAiCiAgICAgIHNob3dncmlkPSJmYWxzZSIKICAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJsYXllcjEiCiAgICAgIGlua3NjYXBlOmN4PSIzNDEuMDcxMTYiCiAgICAgIGlua3NjYXBlOmN5PSIzOTIuMDgzNTIiCiAgICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iNjc0IgogICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0iaW4iCiAgLz4KICA8ZwogICAgICBpZD0ibGF5ZXIxIgogICAgICBpbmtzY2FwZTpsYWJlbD0iTGF5ZXIgMSIKICAgICAgaW5rc2NhcGU6Z3JvdXBtb2RlPSJsYXllciIKICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQxLjQyOSAtMTkuMzkyKSIKICAgID4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODA2IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2NjY2NjY2NjY2NjY2NjY2NjY2NjYyIKICAgICAgICBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjQuMTM3MjtmaWxsOiM1NzU4ZjUiCiAgICAgICAgZD0ibTM3OS4yMyA0MzguMjRjLTQuOTUgNTkuNzktNDIuMDUgMTE3LjktOTQuOTcgMTQ3LjE0LTQ5LjY0IDI2LjY2LTEyMCA3LjIzLTE0Mi45NC00My44LTE3Ljc2LTQ1Ljc5LTEuMDgtOTkuMjEgMzEuMzQtMTM0LjYyIDI0LjkyLTI3Ljg5IDYxLjgxLTM5LjA0IDk1LjY3LTU0LjMxLTUyLjU0IDYuNjgtMTA4LjI4LTMuOC0xNDkuMzgtMzYuMS0yNS4xNS0xOC4zMS00OS45ODItNDUuNzgtNDguOTM1LTc4LjQgMi41MjItNDguMTYgNTMuMzI1LTg3LjQ5IDEwMi42Ni03OS44OSA2MS4xNiA4Ljg0IDEwOC4xOSA1Mi43MyAxNDYuNTYgOTcuMjQtMTMuNzEtMTIuMzMtMjYuNDYtMzEuOS0zMi4xNy00OS4wOS0xNy4yMy03MS41MiAyMy4zMS0xNTEuNTkgOTIuNi0xODEuMTQgMTQuNTctNy4wMDQgMzIuNDMtNC4wMjQgNDUuMTEgNi4yNjMgMzMuMzkgMjQuOTk4IDU1LjkgNjUuMjMgNTMuOSAxMDYuNS01LjE2IDQ0Ljk3LTI4LjQ0IDgzLjg4LTUzLjI0IDEyMS41IDIwLjkyLTM3LjIgNDguNzMtNjkgOTEuNjItODYuNTEgNTQuNzEtMjIuNTUgMTI3LjM5LTIyLjE1IDE2OS43NyAyMy43MyAyNy4wNSAyNi4xMyAyMS40NiA3Mi44Ni00Ljk0IDk3LjQ2LTI5LjY4IDI3LjE3LTcwLjM1IDM3LjA2LTEwOC4wNiA0Ny4yNi0zMi40MiAxMC4zLTcyLjM4IDAuNjItMTA1LjE1IDAuMjUgMzAuMDkgMS40NiA2OC42IDEuODcgOTEuMzEgMTcuNDQgMzUuMDggMjQuMjggNzAuNTMgNTguODIgNjQuODQgMTA0LjQxLTYuOTYgNTAuODQtNTEuNTIgMTA2LjczLTEwOS4yIDk3LjU5LTYwLjExLTEwLjA3LTEwOS4zNC03MS42OC0xMzYuNC0xMjIuOTJ6IgogICAgLz4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODAwIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6My44OTgyO2ZpbGw6I2ZkZmYwOCIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIGQ9Im00MDguNTkgMjU4LjMyYzU0LjczIDI2LjYxIDY1LjA3IDExMC4xMSAxOS42OSAxNTAuMjEtNDAuNDYgNDAuMTktMTE2Ljk5IDMxLjM3LTE0NC41Mi0xOS41Mi0yOC41LTQzLjcxLTEwLjU0LTEwOS42MyAzNy41OS0xMzEuNDUgMjYuNTMtMTMuODYgNTkuODMtMTMuMDkgODcuMjQgMC43NnoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDM4IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDo1LjM1Mjk7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im01OTcuNDQgNjMwLjcyYzQ2LjcyIDE5Ny41OC0xMTYuNzIgMjUzLjU4LTIzNy41IDMxNC41NCAyOS43Ny0xMjIuNjQgNy42NC0yNzQuNDcgMjM3LjUtMzE0LjU0eiIKICAgIC8+CiAgICA8cGF0aAogICAgICAgIGlkPSJwYXRoMzc4OSIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIHNvZGlwb2RpOm5vZGV0eXBlcz0iY2NjIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6NS4zMzc4O2ZpbGw6IzM3ZGMxMSIKICAgICAgICBkPSJtNDQuMTU5IDY1NC4zM2MtNC4wMDIgMTk5LjM4IDE4OSAyMjkuNzEgMzA5LjQ0IDI5MC41LTMyLjA1LTEyNC42Ni0xMTAuOTgtMjg4LjM5LTMwOS40NC0yOTAuNXoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDMyIgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyLjg1MTQ7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im0zNTcuMTkgOTQ4LjAyYy00OC42OC0yOTUuODUgNDIuNDItMjk5LjY0IDIxLjM5LTUxMS45NiA0OC4zMSAxNDIuNTQtMzUuMyAxODguMzItMjEuMzkgNTExLjk2eiIKICAgIC8+CiAgPC9nCiAgPgogIDxtZXRhZGF0YQogICAgICBpZD0ibWV0YWRhdGExMCIKICAgID4KICAgIDxyZGY6UkRGCiAgICAgID4KICAgICAgPGNjOldvcmsKICAgICAgICA+CiAgICAgICAgPGRjOmZvcm1hdAogICAgICAgICAgPmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdAogICAgICAgID4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIgogICAgICAgIC8+CiAgICAgICAgPGNjOmxpY2Vuc2UKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9saWNlbnNlcy9wdWJsaWNkb21haW4vIgogICAgICAgIC8+CiAgICAgICAgPGRjOnB1Ymxpc2hlcgogICAgICAgICAgPgogICAgICAgICAgPGNjOkFnZW50CiAgICAgICAgICAgICAgcmRmOmFib3V0PSJodHRwOi8vb3BlbmNsaXBhcnQub3JnLyIKICAgICAgICAgICAgPgogICAgICAgICAgICA8ZGM6dGl0bGUKICAgICAgICAgICAgICA+T3BlbmNsaXBhcnQ8L2RjOnRpdGxlCiAgICAgICAgICAgID4KICAgICAgICAgIDwvY2M6QWdlbnQKICAgICAgICAgID4KICAgICAgICA8L2RjOnB1Ymxpc2hlcgogICAgICAgID4KICAgICAgPC9jYzpXb3JrCiAgICAgID4KICAgICAgPGNjOkxpY2Vuc2UKICAgICAgICAgIHJkZjphYm91dD0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbGljZW5zZXMvcHVibGljZG9tYWluLyIKICAgICAgICA+CiAgICAgICAgPGNjOnBlcm1pdHMKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyNSZXByb2R1Y3Rpb24iCiAgICAgICAgLz4KICAgICAgICA8Y2M6cGVybWl0cwogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL25zI0Rpc3RyaWJ1dGlvbiIKICAgICAgICAvPgogICAgICAgIDxjYzpwZXJtaXRzCiAgICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjRGVyaXZhdGl2ZVdvcmtzIgogICAgICAgIC8+CiAgICAgIDwvY2M6TGljZW5zZQogICAgICA+CiAgICA8L3JkZjpSREYKICAgID4KICA8L21ldGFkYXRhCiAgPgo8L3N2Zwo+Cg=="/>
          <prop k="svg_outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="5"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@2@1" alpha="1" type="line">
            <layer pass="0" locked="0" enabled="1" class="SimpleLine">
              <prop k="align_dash_pattern" v="0"/>
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="dash_pattern_offset" v="0"/>
              <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="dash_pattern_offset_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="51,131,44,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0.26"/>
              <prop k="line_width_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="tweak_dash_pattern_on_corners" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="3" alpha="1" type="fill">
        <layer pass="0" locked="0" enabled="1" class="ShapeburstFill">
          <prop k="blur_radius" v="2"/>
          <prop k="color" v="227,26,28,255"/>
          <prop k="color1" v="0,0,255,255"/>
          <prop k="color2" v="0,255,0,255"/>
          <prop k="color_type" v="0"/>
          <prop k="discrete" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MM"/>
          <prop k="gradient_color2" v="255,255,255,0"/>
          <prop k="ignore_rings" v="0"/>
          <prop k="max_distance" v="2"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="rampType" v="gradient"/>
          <prop k="use_whole_shape" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontItalic="0" capitalization="0" fontLetterSpacing="0" textOrientation="horizontal" fontWeight="75" fontFamily="MS Shell Dlg 2" multilineHeight="1" allowHtml="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" blendMode="0" fontSizeUnit="Point" fontStrikeout="0" fontUnderline="0" fontSize="7" textColor="75,56,169,255" isExpression="0" fieldName="commonname" namedStyle="Bold" previewBkgrdColor="255,255,255,255" fontWordSpacing="0" useSubstitutions="0" fontKerning="1" textOpacity="1">
        <text-buffer bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferNoFill="1" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferDraw="1" bufferJoinStyle="128"/>
        <text-mask maskedSymbolLayers="" maskType="0" maskSizeUnits="MM" maskSize="0" maskJoinStyle="128" maskEnabled="0" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskOpacity="1"/>
        <background shapeRotationType="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeSizeType="0" shapeType="0" shapeRotation="0" shapeBorderWidth="0" shapeOpacity="1" shapeOffsetX="0" shapeOffsetY="0" shapeSizeUnit="MM" shapeSizeY="0" shapeRadiiY="0" shapeSizeX="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeSVGFile="" shapeRadiiUnit="MM" shapeDraw="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeBlendMode="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0">
          <symbol clip_to_extent="1" force_rhr="0" name="markerSymbol" alpha="1" type="marker">
            <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="225,89,137,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowDraw="0" shadowOffsetDist="1" shadowOpacity="0.7" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowUnder="0" shadowRadiusAlphaOnly="0" shadowScale="100" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" autoWrapLength="15" reverseDirectionSymbol="0" placeDirectionSymbol="0" multilineAlign="0" formatNumbers="0" decimals="3" wrapChar="" rightDirectionSymbol=">" addDirectionSymbol="0" plussign="0"/>
      <placement placement="0" centroidInside="0" geometryGeneratorEnabled="0" polygonPlacementFlags="2" repeatDistance="0" centroidWhole="0" offsetUnits="MM" quadOffset="4" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" lineAnchorPercent="0.5" xOffset="0" priority="5" dist="1" fitInPolygonOnly="0" geometryGeneratorType="PointGeometry" preserveRotation="1" lineAnchorType="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" maxCurvedCharAngleIn="25" repeatDistanceUnits="MM" distUnits="MM" offsetType="0" overrunDistanceUnit="MM" yOffset="0" maxCurvedCharAngleOut="-25" placementFlags="10" layerType="PolygonGeometry"/>
      <rendering obstacle="1" scaleVisibility="0" fontLimitPixelSize="0" upsidedownLabels="0" fontMaxPixelSize="10000" maxNumLabels="2000" limitNumLabels="0" labelPerPart="0" displayAll="0" obstacleFactor="1" minFeatureSize="0" fontMinPixelSize="3" scaleMax="0" mergeLines="0" drawLabels="1" scaleMin="0" zIndex="0" obstacleType="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" name="anchorPoint" type="QString"/>
          <Option name="ddProperties" type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
          <Option value="false" name="drawToAllParts" type="bool"/>
          <Option value="0" name="enabled" type="QString"/>
          <Option value="point_on_exterior" name="labelAnchorPoint" type="QString"/>
          <Option value="&lt;symbol clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; type=&quot;line&quot;>&lt;layer pass=&quot;0&quot; locked=&quot;0&quot; enabled=&quot;1&quot; class=&quot;SimpleLine&quot;>&lt;prop k=&quot;align_dash_pattern&quot; v=&quot;0&quot;/>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;dash_pattern_offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;dash_pattern_offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;dash_pattern_offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;tweak_dash_pattern_on_corners&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
          <Option value="0" name="minLength" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale" type="QString"/>
          <Option value="MM" name="minLengthUnit" type="QString"/>
          <Option value="0" name="offsetFromAnchor" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromAnchorUnit" type="QString"/>
          <Option value="0" name="offsetFromLabel" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromLabelUnit" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>2</layerGeometryType>
</qgis>
