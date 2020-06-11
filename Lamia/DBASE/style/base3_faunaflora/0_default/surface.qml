<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" labelsEnabled="0" simplifyDrawingTol="1" simplifyLocal="1" simplifyMaxScale="1" version="3.10.0-A CoruÃ±a" minScale="1e+08" simplifyAlgorithm="0" styleCategories="Symbology|Labeling|Rendering" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1">
  <renderer-v2 enableorderby="0" type="RuleRenderer" symbollevels="0" forceraster="0">
    <rules key="{fa6c4aa2-b507-461c-b67d-18ef4ebe3184}">
      <rule key="{fe098b19-9d6e-4752-925a-8aad2ced2f5d}" filter=" &quot;surfacecategory&quot; ='FLO'" symbol="0" label="Flore">
        <rule key="{8b6acef9-2e40-44b7-89d8-a43d6e586441}" filter=" $area &lt;5" symbol="1"/>
        <rule key="{c35bf1bf-0a47-4010-acb1-6445b0807dec}" filter="ELSE" symbol="2" label="Flore"/>
      </rule>
      <rule key="{dfa059cb-e59c-47af-8e4a-c5d78a49d73b}" filter=" &quot;surfacecategory&quot; ='HAB'" symbol="3" label="Habitat"/>
    </rules>
    <symbols>
      <symbol type="fill" name="0" alpha="1" force_rhr="0" clip_to_extent="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="fill" name="1" alpha="1" force_rhr="0" clip_to_extent="1">
        <layer class="CentroidFill" pass="0" enabled="1" locked="0">
          <prop k="point_on_all_parts" v="1"/>
          <prop k="point_on_surface" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@1@0" alpha="1" force_rhr="0" clip_to_extent="1">
            <layer class="SvgMarker" pass="0" enabled="1" locked="0">
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
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="fill" name="2" alpha="1" force_rhr="0" clip_to_extent="1">
        <layer class="ShapeburstFill" pass="0" enabled="1" locked="0">
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SVGFill" pass="0" enabled="1" locked="0">
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="line" name="@2@1" alpha="1" force_rhr="0" clip_to_extent="1">
            <layer class="SimpleLine" pass="0" enabled="1" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
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
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="fill" name="3" alpha="1" force_rhr="0" clip_to_extent="1">
        <layer class="ShapeburstFill" pass="0" enabled="1" locked="0">
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{7ed8990a-f96e-456d-b2da-23f7823c879d}">
      <rule key="{ce819559-9395-4865-9644-67b4a977edc9}" filter=" &quot;surfacecategory&quot;  =  'FLO' ">
        <settings calloutType="simple">
          <text-style fontStrikeout="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" blendMode="0" textOrientation="horizontal" textOpacity="1" previewBkgrdColor="255,255,255,255" useSubstitutions="0" fontKerning="1" fontWordSpacing="0" namedStyle="Normal" fieldName="scientificname" textColor="51,131,44,255" fontSize="8" multilineHeight="1" fontItalic="0" fontWeight="50" fontLetterSpacing="0" isExpression="0" fontSizeUnit="Point" fontFamily="MS Shell Dlg 2" fontCapitals="0">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferSizeUnits="MM" bufferOpacity="1" bufferJoinStyle="128" bufferSize="1" bufferNoFill="1" bufferDraw="1" bufferBlendMode="0"/>
            <background shapeDraw="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeSVGFile="" shapeSizeY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeBorderWidth="0" shapeFillColor="255,255,255,255" shapeSizeUnit="MM" shapeRadiiUnit="MM" shapeRotationType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeRadiiX="0" shapeBorderWidthUnit="MM" shapeSizeX="0" shapeType="0" shapeBorderColor="128,128,128,255" shapeRadiiY="0" shapeRotation="0" shapeJoinStyle="64" shapeOpacity="1" shapeBlendMode="0" shapeOffsetUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0">
              <symbol type="marker" name="markerSymbol" alpha="1" force_rhr="0" clip_to_extent="1">
                <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowColor="0,0,0,255" shadowOffsetUnit="MM" shadowRadius="1.5" shadowRadiusUnit="MM" shadowOffsetGlobal="1" shadowOpacity="0.7" shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowOffsetDist="1" shadowRadiusAlphaOnly="0" shadowBlendMode="6" shadowUnder="0"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format formatNumbers="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" decimals="3" addDirectionSymbol="0" autoWrapLength="0" wrapChar="" reverseDirectionSymbol="0" multilineAlign="0" useMaxLineLengthForAutoWrap="1" plussign="0"/>
          <placement distMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" quadOffset="4" offsetUnits="MM" repeatDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PolygonGeometry" overrunDistance="0" centroidInside="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" centroidWhole="0" maxCurvedCharAngleOut="-25" offsetType="0" priority="5" repeatDistanceUnits="MM" geometryGeneratorEnabled="0" fitInPolygonOnly="0" rotationAngle="0" placementFlags="10" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" overrunDistanceUnit="MM" yOffset="0" distUnits="MM" placement="0" geometryGenerator="" geometryGeneratorType="PointGeometry" xOffset="0" dist="0"/>
          <rendering scaleVisibility="0" displayAll="0" mergeLines="0" fontMinPixelSize="3" zIndex="0" fontMaxPixelSize="10000" scaleMin="0" minFeatureSize="0" upsidedownLabels="0" obstacle="1" limitNumLabels="0" scaleMax="0" labelPerPart="0" obstacleFactor="1" fontLimitPixelSize="0" drawLabels="1" maxNumLabels="2000" obstacleType="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
              <Option type="bool" name="drawToAllParts" value="false"/>
              <Option type="QString" name="enabled" value="0"/>
              <Option type="QString" name="lineSymbol" value="&lt;symbol type=&quot;line&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot;>&lt;layer class=&quot;SimpleLine&quot; pass=&quot;0&quot; enabled=&quot;1&quot; locked=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option type="double" name="minLength" value="0"/>
              <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="minLengthUnit" value="MM"/>
              <Option type="double" name="offsetFromAnchor" value="0"/>
              <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
              <Option type="double" name="offsetFromLabel" value="0"/>
              <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule key="{5eb1e256-95b0-49c1-a182-51df94837c17}" filter=" &quot;surfacecategory&quot;  =  'HAB' ">
        <settings calloutType="simple">
          <text-style fontStrikeout="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" blendMode="0" textOrientation="horizontal" textOpacity="1" previewBkgrdColor="255,255,255,255" useSubstitutions="0" fontKerning="1" fontWordSpacing="0" namedStyle="Normal" fieldName="habitatname" textColor="227,26,28,255" fontSize="8" multilineHeight="1" fontItalic="0" fontWeight="50" fontLetterSpacing="0" isExpression="0" fontSizeUnit="Point" fontFamily="MS Shell Dlg 2" fontCapitals="0">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferSizeUnits="MM" bufferOpacity="1" bufferJoinStyle="128" bufferSize="1" bufferNoFill="1" bufferDraw="1" bufferBlendMode="0"/>
            <background shapeDraw="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeSVGFile="" shapeSizeY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeBorderWidth="0" shapeFillColor="255,255,255,255" shapeSizeUnit="MM" shapeRadiiUnit="MM" shapeRotationType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeRadiiX="0" shapeBorderWidthUnit="MM" shapeSizeX="0" shapeType="0" shapeBorderColor="128,128,128,255" shapeRadiiY="0" shapeRotation="0" shapeJoinStyle="64" shapeOpacity="1" shapeBlendMode="0" shapeOffsetUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0">
              <symbol type="marker" name="markerSymbol" alpha="1" force_rhr="0" clip_to_extent="1">
                <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="190,207,80,255"/>
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
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowColor="0,0,0,255" shadowOffsetUnit="MM" shadowRadius="1.5" shadowRadiusUnit="MM" shadowOffsetGlobal="1" shadowOpacity="0.7" shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowOffsetDist="1" shadowRadiusAlphaOnly="0" shadowBlendMode="6" shadowUnder="0"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format formatNumbers="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" decimals="3" addDirectionSymbol="0" autoWrapLength="0" wrapChar="" reverseDirectionSymbol="0" multilineAlign="0" useMaxLineLengthForAutoWrap="1" plussign="0"/>
          <placement distMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" quadOffset="4" offsetUnits="MM" repeatDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PolygonGeometry" overrunDistance="0" centroidInside="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" centroidWhole="0" maxCurvedCharAngleOut="-25" offsetType="0" priority="5" repeatDistanceUnits="MM" geometryGeneratorEnabled="0" fitInPolygonOnly="0" rotationAngle="0" placementFlags="10" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" overrunDistanceUnit="MM" yOffset="0" distUnits="MM" placement="0" geometryGenerator="" geometryGeneratorType="PointGeometry" xOffset="0" dist="0"/>
          <rendering scaleVisibility="0" displayAll="0" mergeLines="0" fontMinPixelSize="3" zIndex="0" fontMaxPixelSize="10000" scaleMin="0" minFeatureSize="0" upsidedownLabels="0" obstacle="1" limitNumLabels="0" scaleMax="0" labelPerPart="0" obstacleFactor="1" fontLimitPixelSize="0" drawLabels="1" maxNumLabels="2000" obstacleType="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
              <Option type="bool" name="drawToAllParts" value="false"/>
              <Option type="QString" name="enabled" value="0"/>
              <Option type="QString" name="lineSymbol" value="&lt;symbol type=&quot;line&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot;>&lt;layer class=&quot;SimpleLine&quot; pass=&quot;0&quot; enabled=&quot;1&quot; locked=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option type="double" name="minLength" value="0"/>
              <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="minLengthUnit" value="MM"/>
              <Option type="double" name="offsetFromAnchor" value="0"/>
              <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
              <Option type="double" name="offsetFromLabel" value="0"/>
              <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
              <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
    </rules>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>2</layerGeometryType>
</qgis>
