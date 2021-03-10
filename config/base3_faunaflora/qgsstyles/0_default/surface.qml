<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingHints="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" readOnly="0" styleCategories="AllStyleCategories" simplifyAlgorithm="0" labelsEnabled="0" simplifyDrawingTol="1" minScale="0" version="3.10.6-A Coruña" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="RuleRenderer">
    <rules key="{fa6c4aa2-b507-461c-b67d-18ef4ebe3184}">
      <rule key="{fe098b19-9d6e-4752-925a-8aad2ced2f5d}" symbol="0" filter=" &quot;surfacecategory&quot; ='FLO'" label="Flore">
        <rule key="{8b6acef9-2e40-44b7-89d8-a43d6e586441}" symbol="1" filter=" $area &lt;5"/>
        <rule key="{c35bf1bf-0a47-4010-acb1-6445b0807dec}" symbol="2" filter="ELSE" label="Flore"/>
      </rule>
      <rule key="{dfa059cb-e59c-47af-8e4a-c5d78a49d73b}" symbol="3" filter=" &quot;surfacecategory&quot; ='HAB'" label="Habitat"/>
    </rules>
    <symbols>
      <symbol force_rhr="0" name="0" clip_to_extent="1" type="fill" alpha="1">
        <layer enabled="1" class="SimpleFill" pass="0" locked="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,255,255,0" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,255,255,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="1" clip_to_extent="1" type="fill" alpha="1">
        <layer enabled="1" class="CentroidFill" pass="0" locked="0">
          <prop v="1" k="point_on_all_parts"/>
          <prop v="0" k="point_on_surface"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" name="@1@0" clip_to_extent="1" type="marker" alpha="1">
            <layer enabled="1" class="SvgMarker" pass="0" locked="0">
              <prop v="0" k="angle"/>
              <prop v="255,255,255,255" k="color"/>
              <prop v="0" k="fixedAspectRatio"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgo8c3ZnCiAgICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgICBpZD0ic3ZnMzIyOCIKICAgIHNvZGlwb2RpOmRvY25hbWU9Il9zdmdjbGVhbjIuc3ZnIgogICAgdmlld0JveD0iMCAwIDY2NS4yMyA5MzAuMDUiCiAgICBzb2RpcG9kaTp2ZXJzaW9uPSIwLjMyIgogICAgdmVyc2lvbj0iMS4xIgogICAgaW5rc2NhcGU6b3V0cHV0X2V4dGVuc2lvbj0ib3JnLmlua3NjYXBlLm91dHB1dC5zdmcuaW5rc2NhcGUiCiAgICBpbmtzY2FwZTp2ZXJzaW9uPSIwLjQ4LjMuMSByOTg4NiIKICA+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgICBpZD0ibmFtZWR2aWV3MzIzMiIKICAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjY0NSIKICAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMCIKICAgICAgaW5rc2NhcGU6em9vbT0iMC41NDg0ODQ4NSIKICAgICAgaW5rc2NhcGU6d2luZG93LXg9IjAiCiAgICAgIHNob3dncmlkPSJmYWxzZSIKICAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJsYXllcjEiCiAgICAgIGlua3NjYXBlOmN4PSIzNDEuMDcxMTYiCiAgICAgIGlua3NjYXBlOmN5PSIzOTIuMDgzNTIiCiAgICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iNjc0IgogICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0iaW4iCiAgLz4KICA8ZwogICAgICBpZD0ibGF5ZXIxIgogICAgICBpbmtzY2FwZTpsYWJlbD0iTGF5ZXIgMSIKICAgICAgaW5rc2NhcGU6Z3JvdXBtb2RlPSJsYXllciIKICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQxLjQyOSAtMTkuMzkyKSIKICAgID4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODA2IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2NjY2NjY2NjY2NjY2NjY2NjY2NjYyIKICAgICAgICBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjQuMTM3MjtmaWxsOiM1NzU4ZjUiCiAgICAgICAgZD0ibTM3OS4yMyA0MzguMjRjLTQuOTUgNTkuNzktNDIuMDUgMTE3LjktOTQuOTcgMTQ3LjE0LTQ5LjY0IDI2LjY2LTEyMCA3LjIzLTE0Mi45NC00My44LTE3Ljc2LTQ1Ljc5LTEuMDgtOTkuMjEgMzEuMzQtMTM0LjYyIDI0LjkyLTI3Ljg5IDYxLjgxLTM5LjA0IDk1LjY3LTU0LjMxLTUyLjU0IDYuNjgtMTA4LjI4LTMuOC0xNDkuMzgtMzYuMS0yNS4xNS0xOC4zMS00OS45ODItNDUuNzgtNDguOTM1LTc4LjQgMi41MjItNDguMTYgNTMuMzI1LTg3LjQ5IDEwMi42Ni03OS44OSA2MS4xNiA4Ljg0IDEwOC4xOSA1Mi43MyAxNDYuNTYgOTcuMjQtMTMuNzEtMTIuMzMtMjYuNDYtMzEuOS0zMi4xNy00OS4wOS0xNy4yMy03MS41MiAyMy4zMS0xNTEuNTkgOTIuNi0xODEuMTQgMTQuNTctNy4wMDQgMzIuNDMtNC4wMjQgNDUuMTEgNi4yNjMgMzMuMzkgMjQuOTk4IDU1LjkgNjUuMjMgNTMuOSAxMDYuNS01LjE2IDQ0Ljk3LTI4LjQ0IDgzLjg4LTUzLjI0IDEyMS41IDIwLjkyLTM3LjIgNDguNzMtNjkgOTEuNjItODYuNTEgNTQuNzEtMjIuNTUgMTI3LjM5LTIyLjE1IDE2OS43NyAyMy43MyAyNy4wNSAyNi4xMyAyMS40NiA3Mi44Ni00Ljk0IDk3LjQ2LTI5LjY4IDI3LjE3LTcwLjM1IDM3LjA2LTEwOC4wNiA0Ny4yNi0zMi40MiAxMC4zLTcyLjM4IDAuNjItMTA1LjE1IDAuMjUgMzAuMDkgMS40NiA2OC42IDEuODcgOTEuMzEgMTcuNDQgMzUuMDggMjQuMjggNzAuNTMgNTguODIgNjQuODQgMTA0LjQxLTYuOTYgNTAuODQtNTEuNTIgMTA2LjczLTEwOS4yIDk3LjU5LTYwLjExLTEwLjA3LTEwOS4zNC03MS42OC0xMzYuNC0xMjIuOTJ6IgogICAgLz4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODAwIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6My44OTgyO2ZpbGw6I2ZkZmYwOCIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIGQ9Im00MDguNTkgMjU4LjMyYzU0LjczIDI2LjYxIDY1LjA3IDExMC4xMSAxOS42OSAxNTAuMjEtNDAuNDYgNDAuMTktMTE2Ljk5IDMxLjM3LTE0NC41Mi0xOS41Mi0yOC41LTQzLjcxLTEwLjU0LTEwOS42MyAzNy41OS0xMzEuNDUgMjYuNTMtMTMuODYgNTkuODMtMTMuMDkgODcuMjQgMC43NnoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDM4IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDo1LjM1Mjk7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im01OTcuNDQgNjMwLjcyYzQ2LjcyIDE5Ny41OC0xMTYuNzIgMjUzLjU4LTIzNy41IDMxNC41NCAyOS43Ny0xMjIuNjQgNy42NC0yNzQuNDcgMjM3LjUtMzE0LjU0eiIKICAgIC8+CiAgICA8cGF0aAogICAgICAgIGlkPSJwYXRoMzc4OSIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIHNvZGlwb2RpOm5vZGV0eXBlcz0iY2NjIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6NS4zMzc4O2ZpbGw6IzM3ZGMxMSIKICAgICAgICBkPSJtNDQuMTU5IDY1NC4zM2MtNC4wMDIgMTk5LjM4IDE4OSAyMjkuNzEgMzA5LjQ0IDI5MC41LTMyLjA1LTEyNC42Ni0xMTAuOTgtMjg4LjM5LTMwOS40NC0yOTAuNXoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDMyIgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyLjg1MTQ7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im0zNTcuMTkgOTQ4LjAyYy00OC42OC0yOTUuODUgNDIuNDItMjk5LjY0IDIxLjM5LTUxMS45NiA0OC4zMSAxNDIuNTQtMzUuMyAxODguMzItMjEuMzkgNTExLjk2eiIKICAgIC8+CiAgPC9nCiAgPgogIDxtZXRhZGF0YQogICAgICBpZD0ibWV0YWRhdGExMCIKICAgID4KICAgIDxyZGY6UkRGCiAgICAgID4KICAgICAgPGNjOldvcmsKICAgICAgICA+CiAgICAgICAgPGRjOmZvcm1hdAogICAgICAgICAgPmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdAogICAgICAgID4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIgogICAgICAgIC8+CiAgICAgICAgPGNjOmxpY2Vuc2UKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9saWNlbnNlcy9wdWJsaWNkb21haW4vIgogICAgICAgIC8+CiAgICAgICAgPGRjOnB1Ymxpc2hlcgogICAgICAgICAgPgogICAgICAgICAgPGNjOkFnZW50CiAgICAgICAgICAgICAgcmRmOmFib3V0PSJodHRwOi8vb3BlbmNsaXBhcnQub3JnLyIKICAgICAgICAgICAgPgogICAgICAgICAgICA8ZGM6dGl0bGUKICAgICAgICAgICAgICA+T3BlbmNsaXBhcnQ8L2RjOnRpdGxlCiAgICAgICAgICAgID4KICAgICAgICAgIDwvY2M6QWdlbnQKICAgICAgICAgID4KICAgICAgICA8L2RjOnB1Ymxpc2hlcgogICAgICAgID4KICAgICAgPC9jYzpXb3JrCiAgICAgID4KICAgICAgPGNjOkxpY2Vuc2UKICAgICAgICAgIHJkZjphYm91dD0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbGljZW5zZXMvcHVibGljZG9tYWluLyIKICAgICAgICA+CiAgICAgICAgPGNjOnBlcm1pdHMKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyNSZXByb2R1Y3Rpb24iCiAgICAgICAgLz4KICAgICAgICA8Y2M6cGVybWl0cwogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL25zI0Rpc3RyaWJ1dGlvbiIKICAgICAgICAvPgogICAgICAgIDxjYzpwZXJtaXRzCiAgICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjRGVyaXZhdGl2ZVdvcmtzIgogICAgICAgIC8+CiAgICAgIDwvY2M6TGljZW5zZQogICAgICA+CiAgICA8L3JkZjpSREYKICAgID4KICA8L21ldGFkYXRhCiAgPgo8L3N2Zwo+Cg==" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="5.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="2" clip_to_extent="1" type="fill" alpha="1">
        <layer enabled="1" class="ShapeburstFill" pass="0" locked="0">
          <prop v="2" k="blur_radius"/>
          <prop v="113,214,118,255" k="color"/>
          <prop v="13,8,135,255" k="color1"/>
          <prop v="166,206,227,255" k="color2"/>
          <prop v="0" k="color_type"/>
          <prop v="0" k="discrete"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="255,255,255,0" k="gradient_color2"/>
          <prop v="0" k="ignore_rings"/>
          <prop v="2" k="max_distance"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="gradient" k="rampType"/>
          <prop v="0.0196078;27,6,141,255:0.0392157;38,5,145,255:0.0588235;47,5,150,255:0.0784314;56,4,154,255:0.0980392;65,4,157,255:0.117647;73,3,160,255:0.137255;81,2,163,255:0.156863;89,1,165,255:0.176471;97,0,167,255:0.196078;105,0,168,255:0.215686;113,0,168,255:0.235294;120,1,168,255:0.254902;128,4,168,255:0.27451;135,7,166,255:0.294118;142,12,164,255:0.313725;149,17,161,255:0.333333;156,23,158,255:0.352941;162,29,154,255:0.372549;168,34,150,255:0.392157;174,40,146,255:0.411765;180,46,141,255:0.431373;186,51,136,255:0.45098;191,57,132,255:0.470588;196,62,127,255:0.490196;201,68,122,255:0.509804;205,74,118,255:0.529412;210,79,113,255:0.54902;214,85,109,255:0.568627;218,91,105,255:0.588235;222,97,100,255:0.607843;226,102,96,255:0.627451;230,108,92,255:0.647059;233,114,87,255:0.666667;237,121,83,255:0.686275;240,127,79,255:0.705882;243,133,75,255:0.72549;245,140,70,255:0.745098;247,147,66,255:0.764706;249,154,62,255:0.784314;251,161,57,255:0.803922;252,168,53,255:0.823529;253,175,49,255:0.843137;254,183,45,255:0.862745;254,190,42,255:0.882353;253,198,39,255:0.901961;252,206,37,255:0.921569;251,215,36,255:0.941176;248,223,37,255:0.960784;246,232,38,255:0.980392;243,240,39,255" k="stops"/>
          <prop v="0" k="use_whole_shape"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" class="SVGFill" pass="0" locked="0">
          <prop v="0" k="angle"/>
          <prop v="51,131,44,255" k="color"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="pattern_width_map_unit_scale"/>
          <prop v="MM" k="pattern_width_unit"/>
          <prop v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgo8c3ZnCiAgICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIKICAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgICBpZD0ic3ZnMzIyOCIKICAgIHNvZGlwb2RpOmRvY25hbWU9Il9zdmdjbGVhbjIuc3ZnIgogICAgdmlld0JveD0iMCAwIDY2NS4yMyA5MzAuMDUiCiAgICBzb2RpcG9kaTp2ZXJzaW9uPSIwLjMyIgogICAgdmVyc2lvbj0iMS4xIgogICAgaW5rc2NhcGU6b3V0cHV0X2V4dGVuc2lvbj0ib3JnLmlua3NjYXBlLm91dHB1dC5zdmcuaW5rc2NhcGUiCiAgICBpbmtzY2FwZTp2ZXJzaW9uPSIwLjQ4LjMuMSByOTg4NiIKICA+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgICBpZD0ibmFtZWR2aWV3MzIzMiIKICAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjY0NSIKICAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMCIKICAgICAgaW5rc2NhcGU6em9vbT0iMC41NDg0ODQ4NSIKICAgICAgaW5rc2NhcGU6d2luZG93LXg9IjAiCiAgICAgIHNob3dncmlkPSJmYWxzZSIKICAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJsYXllcjEiCiAgICAgIGlua3NjYXBlOmN4PSIzNDEuMDcxMTYiCiAgICAgIGlua3NjYXBlOmN5PSIzOTIuMDgzNTIiCiAgICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iNjc0IgogICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0iaW4iCiAgLz4KICA8ZwogICAgICBpZD0ibGF5ZXIxIgogICAgICBpbmtzY2FwZTpsYWJlbD0iTGF5ZXIgMSIKICAgICAgaW5rc2NhcGU6Z3JvdXBtb2RlPSJsYXllciIKICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQxLjQyOSAtMTkuMzkyKSIKICAgID4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODA2IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2NjY2NjY2NjY2NjY2NjY2NjY2NjYyIKICAgICAgICBzdHlsZT0ic3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjQuMTM3MjtmaWxsOiM1NzU4ZjUiCiAgICAgICAgZD0ibTM3OS4yMyA0MzguMjRjLTQuOTUgNTkuNzktNDIuMDUgMTE3LjktOTQuOTcgMTQ3LjE0LTQ5LjY0IDI2LjY2LTEyMCA3LjIzLTE0Mi45NC00My44LTE3Ljc2LTQ1Ljc5LTEuMDgtOTkuMjEgMzEuMzQtMTM0LjYyIDI0LjkyLTI3Ljg5IDYxLjgxLTM5LjA0IDk1LjY3LTU0LjMxLTUyLjU0IDYuNjgtMTA4LjI4LTMuOC0xNDkuMzgtMzYuMS0yNS4xNS0xOC4zMS00OS45ODItNDUuNzgtNDguOTM1LTc4LjQgMi41MjItNDguMTYgNTMuMzI1LTg3LjQ5IDEwMi42Ni03OS44OSA2MS4xNiA4Ljg0IDEwOC4xOSA1Mi43MyAxNDYuNTYgOTcuMjQtMTMuNzEtMTIuMzMtMjYuNDYtMzEuOS0zMi4xNy00OS4wOS0xNy4yMy03MS41MiAyMy4zMS0xNTEuNTkgOTIuNi0xODEuMTQgMTQuNTctNy4wMDQgMzIuNDMtNC4wMjQgNDUuMTEgNi4yNjMgMzMuMzkgMjQuOTk4IDU1LjkgNjUuMjMgNTMuOSAxMDYuNS01LjE2IDQ0Ljk3LTI4LjQ0IDgzLjg4LTUzLjI0IDEyMS41IDIwLjkyLTM3LjIgNDguNzMtNjkgOTEuNjItODYuNTEgNTQuNzEtMjIuNTUgMTI3LjM5LTIyLjE1IDE2OS43NyAyMy43MyAyNy4wNSAyNi4xMyAyMS40NiA3Mi44Ni00Ljk0IDk3LjQ2LTI5LjY4IDI3LjE3LTcwLjM1IDM3LjA2LTEwOC4wNiA0Ny4yNi0zMi40MiAxMC4zLTcyLjM4IDAuNjItMTA1LjE1IDAuMjUgMzAuMDkgMS40NiA2OC42IDEuODcgOTEuMzEgMTcuNDQgMzUuMDggMjQuMjggNzAuNTMgNTguODIgNjQuODQgMTA0LjQxLTYuOTYgNTAuODQtNTEuNTIgMTA2LjczLTEwOS4yIDk3LjU5LTYwLjExLTEwLjA3LTEwOS4zNC03MS42OC0xMzYuNC0xMjIuOTJ6IgogICAgLz4KICAgIDxwYXRoCiAgICAgICAgaWQ9InBhdGgzODAwIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6My44OTgyO2ZpbGw6I2ZkZmYwOCIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIGQ9Im00MDguNTkgMjU4LjMyYzU0LjczIDI2LjYxIDY1LjA3IDExMC4xMSAxOS42OSAxNTAuMjEtNDAuNDYgNDAuMTktMTE2Ljk5IDMxLjM3LTE0NC41Mi0xOS41Mi0yOC41LTQzLjcxLTEwLjU0LTEwOS42MyAzNy41OS0xMzEuNDUgMjYuNTMtMTMuODYgNTkuODMtMTMuMDkgODcuMjQgMC43NnoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDM4IgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDo1LjM1Mjk7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im01OTcuNDQgNjMwLjcyYzQ2LjcyIDE5Ny41OC0xMTYuNzIgMjUzLjU4LTIzNy41IDMxNC41NCAyOS43Ny0xMjIuNjQgNy42NC0yNzQuNDcgMjM3LjUtMzE0LjU0eiIKICAgIC8+CiAgICA8cGF0aAogICAgICAgIGlkPSJwYXRoMzc4OSIKICAgICAgICBpbmtzY2FwZTpjb25uZWN0b3ItY3VydmF0dXJlPSIwIgogICAgICAgIHNvZGlwb2RpOm5vZGV0eXBlcz0iY2NjIgogICAgICAgIHN0eWxlPSJzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6NS4zMzc4O2ZpbGw6IzM3ZGMxMSIKICAgICAgICBkPSJtNDQuMTU5IDY1NC4zM2MtNC4wMDIgMTk5LjM4IDE4OSAyMjkuNzEgMzA5LjQ0IDI5MC41LTMyLjA1LTEyNC42Ni0xMTAuOTgtMjg4LjM5LTMwOS40NC0yOTAuNXoiCiAgICAvPgogICAgPHBhdGgKICAgICAgICBpZD0icGF0aDMyIgogICAgICAgIGlua3NjYXBlOmNvbm5lY3Rvci1jdXJ2YXR1cmU9IjAiCiAgICAgICAgc29kaXBvZGk6bm9kZXR5cGVzPSJjY2MiCiAgICAgICAgc3R5bGU9InN0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoyLjg1MTQ7ZmlsbDojMzdkYzExIgogICAgICAgIGQ9Im0zNTcuMTkgOTQ4LjAyYy00OC42OC0yOTUuODUgNDIuNDItMjk5LjY0IDIxLjM5LTUxMS45NiA0OC4zMSAxNDIuNTQtMzUuMyAxODguMzItMjEuMzkgNTExLjk2eiIKICAgIC8+CiAgPC9nCiAgPgogIDxtZXRhZGF0YQogICAgICBpZD0ibWV0YWRhdGExMCIKICAgID4KICAgIDxyZGY6UkRGCiAgICAgID4KICAgICAgPGNjOldvcmsKICAgICAgICA+CiAgICAgICAgPGRjOmZvcm1hdAogICAgICAgICAgPmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdAogICAgICAgID4KICAgICAgICA8ZGM6dHlwZQogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9wdXJsLm9yZy9kYy9kY21pdHlwZS9TdGlsbEltYWdlIgogICAgICAgIC8+CiAgICAgICAgPGNjOmxpY2Vuc2UKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9saWNlbnNlcy9wdWJsaWNkb21haW4vIgogICAgICAgIC8+CiAgICAgICAgPGRjOnB1Ymxpc2hlcgogICAgICAgICAgPgogICAgICAgICAgPGNjOkFnZW50CiAgICAgICAgICAgICAgcmRmOmFib3V0PSJodHRwOi8vb3BlbmNsaXBhcnQub3JnLyIKICAgICAgICAgICAgPgogICAgICAgICAgICA8ZGM6dGl0bGUKICAgICAgICAgICAgICA+T3BlbmNsaXBhcnQ8L2RjOnRpdGxlCiAgICAgICAgICAgID4KICAgICAgICAgIDwvY2M6QWdlbnQKICAgICAgICAgID4KICAgICAgICA8L2RjOnB1Ymxpc2hlcgogICAgICAgID4KICAgICAgPC9jYzpXb3JrCiAgICAgID4KICAgICAgPGNjOkxpY2Vuc2UKICAgICAgICAgIHJkZjphYm91dD0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbGljZW5zZXMvcHVibGljZG9tYWluLyIKICAgICAgICA+CiAgICAgICAgPGNjOnBlcm1pdHMKICAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyNSZXByb2R1Y3Rpb24iCiAgICAgICAgLz4KICAgICAgICA8Y2M6cGVybWl0cwogICAgICAgICAgICByZGY6cmVzb3VyY2U9Imh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL25zI0Rpc3RyaWJ1dGlvbiIKICAgICAgICAvPgogICAgICAgIDxjYzpwZXJtaXRzCiAgICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjRGVyaXZhdGl2ZVdvcmtzIgogICAgICAgIC8+CiAgICAgIDwvY2M6TGljZW5zZQogICAgICA+CiAgICA8L3JkZjpSREYKICAgID4KICA8L21ldGFkYXRhCiAgPgo8L3N2Zwo+Cg==" k="svgFile"/>
          <prop v="3x:0,0,0,0,0,0" k="svg_outline_width_map_unit_scale"/>
          <prop v="MM" k="svg_outline_width_unit"/>
          <prop v="5" k="width"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" name="@2@1" clip_to_extent="1" type="line" alpha="1">
            <layer enabled="1" class="SimpleLine" pass="0" locked="0">
              <prop v="square" k="capstyle"/>
              <prop v="5;2" k="customdash"/>
              <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
              <prop v="MM" k="customdash_unit"/>
              <prop v="0" k="draw_inside_polygon"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="51,131,44,255" k="line_color"/>
              <prop v="solid" k="line_style"/>
              <prop v="0.26" k="line_width"/>
              <prop v="MM" k="line_width_unit"/>
              <prop v="0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0" k="ring_filter"/>
              <prop v="0" k="use_custom_dash"/>
              <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="3" clip_to_extent="1" type="fill" alpha="1">
        <layer enabled="1" class="ShapeburstFill" pass="0" locked="0">
          <prop v="2" k="blur_radius"/>
          <prop v="227,26,28,255" k="color"/>
          <prop v="0,0,255,255" k="color1"/>
          <prop v="0,255,0,255" k="color2"/>
          <prop v="0" k="color_type"/>
          <prop v="0" k="discrete"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="255,255,255,0" k="gradient_color2"/>
          <prop v="0" k="ignore_rings"/>
          <prop v="2" k="max_distance"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="gradient" k="rampType"/>
          <prop v="0" k="use_whole_shape"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontSize="7" textOrientation="horizontal" fontWeight="75" isExpression="0" textOpacity="1" previewBkgrdColor="255,255,255,255" fontFamily="MS Shell Dlg 2" blendMode="0" fontLetterSpacing="0" useSubstitutions="0" fontUnderline="0" fontWordSpacing="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textColor="75,56,169,255" multilineHeight="1" fontItalic="0" namedStyle="Bold" fontStrikeout="0" fontSizeUnit="Point" fontCapitals="0" fontKerning="1" fieldName="commonname">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="1" bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferJoinStyle="128" bufferColor="255,255,255,255"/>
        <background shapeRadiiX="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeSizeType="0" shapeRadiiY="0" shapeOpacity="1" shapeBorderWidth="0" shapeRotationType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeSizeY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeJoinStyle="64" shapeOffsetUnit="MM" shapeOffsetY="0" shapeBorderWidthUnit="MM" shapeBlendMode="0" shapeRotation="0" shapeSVGFile="" shapeDraw="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0">
          <symbol force_rhr="0" name="markerSymbol" clip_to_extent="1" type="marker" alpha="1">
            <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
              <prop v="0" k="angle"/>
              <prop v="225,89,137,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetGlobal="1" shadowRadius="1.5" shadowColor="0,0,0,255" shadowBlendMode="6" shadowOffsetAngle="135" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowScale="100" shadowOpacity="0.7" shadowOffsetUnit="MM" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" autoWrapLength="15" addDirectionSymbol="0" leftDirectionSymbol="&lt;" formatNumbers="0" multilineAlign="0" placeDirectionSymbol="0" rightDirectionSymbol=">" decimals="3" plussign="0" wrapChar="" reverseDirectionSymbol="0"/>
      <placement priority="5" quadOffset="4" geometryGenerator="" offsetType="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistanceUnits="MM" fitInPolygonOnly="0" maxCurvedCharAngleIn="25" rotationAngle="0" layerType="PolygonGeometry" maxCurvedCharAngleOut="-25" xOffset="0" placementFlags="10" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" offsetUnits="MM" placement="0" centroidInside="0" distMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceUnit="MM" dist="1" distUnits="MM" preserveRotation="1" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0" repeatDistance="0" yOffset="0" overrunDistance="0" geometryGeneratorEnabled="0"/>
      <rendering fontMinPixelSize="3" fontMaxPixelSize="10000" minFeatureSize="0" obstacleFactor="1" upsidedownLabels="0" scaleMax="0" drawLabels="1" scaleVisibility="0" obstacleType="0" scaleMin="0" limitNumLabels="0" fontLimitPixelSize="0" zIndex="0" obstacle="1" labelPerPart="0" maxNumLabels="2000" mergeLines="0" displayAll="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties"/>
          <Option name="type" value="collection" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option name="anchorPoint" value="pole_of_inaccessibility" type="QString"/>
          <Option name="ddProperties" type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
          <Option name="drawToAllParts" value="false" type="bool"/>
          <Option name="enabled" value="0" type="QString"/>
          <Option name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot; locked=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
          <Option name="minLength" value="0" type="double"/>
          <Option name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="minLengthUnit" value="MM" type="QString"/>
          <Option name="offsetFromAnchor" value="0" type="double"/>
          <Option name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="offsetFromAnchorUnit" value="MM" type="QString"/>
          <Option name="offsetFromLabel" value="0" type="double"/>
          <Option name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="offsetFromLabelUnit" value="MM" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory opacity="1" penColor="#000000" rotationOffset="270" height="15" barWidth="5" minScaleDenominator="0" minimumSize="0" backgroundColor="#ffffff" scaleBasedVisibility="0" sizeType="MM" penAlpha="255" enabled="0" penWidth="0" sizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" width="15" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" backgroundAlpha="255" maxScaleDenominator="0" lineSizeType="MM" diagramOrientation="Up">
      <fontProperties style="" description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" zIndex="0" dist="0" linePlacementFlags="18" placement="1" priority="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option name="allowedGapsBuffer" value="0" type="double"/>
        <Option name="allowedGapsEnabled" value="false" type="bool"/>
        <Option name="allowedGapsLayer" value="" type="QString"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <fieldConfiguration>
    <field name="pk_surface">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_surface">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="surfacetype">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lpk_descriptionsystem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_4">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_5">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_6">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_7">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_8">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_9">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem_10">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="surfacecategory">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="Flore" value="FLO" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Faune" value="FAU" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="number">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="florainvasive">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="floraprotected">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pk_descriptionsystem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_descriptionsystem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lpk_object">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="strategicvalue">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="operational">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Oui" value="1" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Non" value="0" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="structuralstate">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="operationalstate">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dateoperationalcreation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dateoperationalcreationupper">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="operationaldatecreationaccuracy">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="A" value="A" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="B" value="B" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="C" value="C" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="NC" value="NC" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="datetimeoperationaldestruction">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="geotrackingxyquality">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe A" value="1" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe B" value="2" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe C" value="3" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="geotrackingzquality">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe A" value="1" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe B" value="2" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe C" value="3" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="geotrackingdate">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="geotrackingsource">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="parameters">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="parameterslist">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="city">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="streetname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="streetupname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="streetdownname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="streetcomment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_actor_1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_actor_2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_actor_3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_facility">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_4">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_5">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_6">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_7">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_8">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_9">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="float_10">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_4">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_5">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_6">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_7">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_8">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_9">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="string_10">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="commonname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="scientificname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="orderclass">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pk_object">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_object">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lpk_revision_begin">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lpk_revision_end">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="datetimecreation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="datetimemodification">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="datetimedestruction">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="comment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="importid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="importtable">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_actor">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="pk_surface" index="0"/>
    <alias name="" field="id_surface" index="1"/>
    <alias name="" field="surfacetype" index="2"/>
    <alias name="" field="lpk_descriptionsystem" index="3"/>
    <alias name="" field="lid_descriptionsystem_1" index="4"/>
    <alias name="" field="lid_descriptionsystem_2" index="5"/>
    <alias name="" field="lid_descriptionsystem_3" index="6"/>
    <alias name="" field="lid_descriptionsystem_4" index="7"/>
    <alias name="" field="lid_descriptionsystem_5" index="8"/>
    <alias name="" field="lid_descriptionsystem_6" index="9"/>
    <alias name="" field="lid_descriptionsystem_7" index="10"/>
    <alias name="" field="lid_descriptionsystem_8" index="11"/>
    <alias name="" field="lid_descriptionsystem_9" index="12"/>
    <alias name="" field="lid_descriptionsystem_10" index="13"/>
    <alias name="" field="surfacecategory" index="14"/>
    <alias name="" field="number" index="15"/>
    <alias name="" field="florainvasive" index="16"/>
    <alias name="" field="floraprotected" index="17"/>
    <alias name="" field="pk_descriptionsystem" index="18"/>
    <alias name="" field="id_descriptionsystem" index="19"/>
    <alias name="" field="lpk_object" index="20"/>
    <alias name="" field="strategicvalue" index="21"/>
    <alias name="" field="operational" index="22"/>
    <alias name="" field="structuralstate" index="23"/>
    <alias name="" field="operationalstate" index="24"/>
    <alias name="" field="dateoperationalcreation" index="25"/>
    <alias name="" field="dateoperationalcreationupper" index="26"/>
    <alias name="" field="operationaldatecreationaccuracy" index="27"/>
    <alias name="" field="datetimeoperationaldestruction" index="28"/>
    <alias name="" field="geotrackingxyquality" index="29"/>
    <alias name="" field="geotrackingzquality" index="30"/>
    <alias name="" field="geotrackingdate" index="31"/>
    <alias name="" field="geotrackingsource" index="32"/>
    <alias name="" field="parameters" index="33"/>
    <alias name="" field="parameterslist" index="34"/>
    <alias name="" field="city" index="35"/>
    <alias name="" field="streetname" index="36"/>
    <alias name="" field="streetupname" index="37"/>
    <alias name="" field="streetdownname" index="38"/>
    <alias name="" field="streetcomment" index="39"/>
    <alias name="" field="lid_actor_1" index="40"/>
    <alias name="" field="lid_actor_2" index="41"/>
    <alias name="" field="lid_actor_3" index="42"/>
    <alias name="" field="lid_facility" index="43"/>
    <alias name="" field="float_1" index="44"/>
    <alias name="" field="float_2" index="45"/>
    <alias name="" field="float_3" index="46"/>
    <alias name="" field="float_4" index="47"/>
    <alias name="" field="float_5" index="48"/>
    <alias name="" field="float_6" index="49"/>
    <alias name="" field="float_7" index="50"/>
    <alias name="" field="float_8" index="51"/>
    <alias name="" field="float_9" index="52"/>
    <alias name="" field="float_10" index="53"/>
    <alias name="" field="string_1" index="54"/>
    <alias name="" field="string_2" index="55"/>
    <alias name="" field="string_3" index="56"/>
    <alias name="" field="string_4" index="57"/>
    <alias name="" field="string_5" index="58"/>
    <alias name="" field="string_6" index="59"/>
    <alias name="" field="string_7" index="60"/>
    <alias name="" field="string_8" index="61"/>
    <alias name="" field="string_9" index="62"/>
    <alias name="" field="string_10" index="63"/>
    <alias name="" field="commonname" index="64"/>
    <alias name="" field="scientificname" index="65"/>
    <alias name="" field="orderclass" index="66"/>
    <alias name="" field="pk_object" index="67"/>
    <alias name="" field="id_object" index="68"/>
    <alias name="" field="lpk_revision_begin" index="69"/>
    <alias name="" field="lpk_revision_end" index="70"/>
    <alias name="" field="datetimecreation" index="71"/>
    <alias name="" field="datetimemodification" index="72"/>
    <alias name="" field="datetimedestruction" index="73"/>
    <alias name="" field="comment" index="74"/>
    <alias name="" field="name" index="75"/>
    <alias name="" field="importid" index="76"/>
    <alias name="" field="importtable" index="77"/>
    <alias name="" field="lid_actor" index="78"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="pk_surface" applyOnUpdate="0"/>
    <default expression="" field="id_surface" applyOnUpdate="0"/>
    <default expression="" field="surfacetype" applyOnUpdate="0"/>
    <default expression="" field="lpk_descriptionsystem" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_1" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_2" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_3" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_4" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_5" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_6" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_7" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_8" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_9" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_10" applyOnUpdate="0"/>
    <default expression="" field="surfacecategory" applyOnUpdate="0"/>
    <default expression="" field="number" applyOnUpdate="0"/>
    <default expression="" field="florainvasive" applyOnUpdate="0"/>
    <default expression="" field="floraprotected" applyOnUpdate="0"/>
    <default expression="" field="pk_descriptionsystem" applyOnUpdate="0"/>
    <default expression="" field="id_descriptionsystem" applyOnUpdate="0"/>
    <default expression="" field="lpk_object" applyOnUpdate="0"/>
    <default expression="" field="strategicvalue" applyOnUpdate="0"/>
    <default expression="" field="operational" applyOnUpdate="0"/>
    <default expression="" field="structuralstate" applyOnUpdate="0"/>
    <default expression="" field="operationalstate" applyOnUpdate="0"/>
    <default expression="" field="dateoperationalcreation" applyOnUpdate="0"/>
    <default expression="" field="dateoperationalcreationupper" applyOnUpdate="0"/>
    <default expression="" field="operationaldatecreationaccuracy" applyOnUpdate="0"/>
    <default expression="" field="datetimeoperationaldestruction" applyOnUpdate="0"/>
    <default expression="" field="geotrackingxyquality" applyOnUpdate="0"/>
    <default expression="" field="geotrackingzquality" applyOnUpdate="0"/>
    <default expression="" field="geotrackingdate" applyOnUpdate="0"/>
    <default expression="" field="geotrackingsource" applyOnUpdate="0"/>
    <default expression="" field="parameters" applyOnUpdate="0"/>
    <default expression="" field="parameterslist" applyOnUpdate="0"/>
    <default expression="" field="city" applyOnUpdate="0"/>
    <default expression="" field="streetname" applyOnUpdate="0"/>
    <default expression="" field="streetupname" applyOnUpdate="0"/>
    <default expression="" field="streetdownname" applyOnUpdate="0"/>
    <default expression="" field="streetcomment" applyOnUpdate="0"/>
    <default expression="" field="lid_actor_1" applyOnUpdate="0"/>
    <default expression="" field="lid_actor_2" applyOnUpdate="0"/>
    <default expression="" field="lid_actor_3" applyOnUpdate="0"/>
    <default expression="" field="lid_facility" applyOnUpdate="0"/>
    <default expression="" field="float_1" applyOnUpdate="0"/>
    <default expression="" field="float_2" applyOnUpdate="0"/>
    <default expression="" field="float_3" applyOnUpdate="0"/>
    <default expression="" field="float_4" applyOnUpdate="0"/>
    <default expression="" field="float_5" applyOnUpdate="0"/>
    <default expression="" field="float_6" applyOnUpdate="0"/>
    <default expression="" field="float_7" applyOnUpdate="0"/>
    <default expression="" field="float_8" applyOnUpdate="0"/>
    <default expression="" field="float_9" applyOnUpdate="0"/>
    <default expression="" field="float_10" applyOnUpdate="0"/>
    <default expression="" field="string_1" applyOnUpdate="0"/>
    <default expression="" field="string_2" applyOnUpdate="0"/>
    <default expression="" field="string_3" applyOnUpdate="0"/>
    <default expression="" field="string_4" applyOnUpdate="0"/>
    <default expression="" field="string_5" applyOnUpdate="0"/>
    <default expression="" field="string_6" applyOnUpdate="0"/>
    <default expression="" field="string_7" applyOnUpdate="0"/>
    <default expression="" field="string_8" applyOnUpdate="0"/>
    <default expression="" field="string_9" applyOnUpdate="0"/>
    <default expression="" field="string_10" applyOnUpdate="0"/>
    <default expression="" field="commonname" applyOnUpdate="0"/>
    <default expression="" field="scientificname" applyOnUpdate="0"/>
    <default expression="" field="orderclass" applyOnUpdate="0"/>
    <default expression="" field="pk_object" applyOnUpdate="0"/>
    <default expression="" field="id_object" applyOnUpdate="0"/>
    <default expression="" field="lpk_revision_begin" applyOnUpdate="0"/>
    <default expression="" field="lpk_revision_end" applyOnUpdate="0"/>
    <default expression="" field="datetimecreation" applyOnUpdate="0"/>
    <default expression="" field="datetimemodification" applyOnUpdate="0"/>
    <default expression="" field="datetimedestruction" applyOnUpdate="0"/>
    <default expression="" field="comment" applyOnUpdate="0"/>
    <default expression="" field="name" applyOnUpdate="0"/>
    <default expression="" field="importid" applyOnUpdate="0"/>
    <default expression="" field="importtable" applyOnUpdate="0"/>
    <default expression="" field="lid_actor" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="pk_surface"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="id_surface"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="surfacetype"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_descriptionsystem"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_3"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_4"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_5"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_6"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_7"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_8"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_9"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_10"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="surfacecategory"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="number"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="florainvasive"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="floraprotected"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="pk_descriptionsystem"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="id_descriptionsystem"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_object"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="strategicvalue"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="operational"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="structuralstate"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="operationalstate"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="dateoperationalcreation"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="dateoperationalcreationupper"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="operationaldatecreationaccuracy"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimeoperationaldestruction"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingxyquality"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingzquality"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingdate"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingsource"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="parameters"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="parameterslist"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="city"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetupname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetdownname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetcomment"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor_3"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_facility"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_3"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_4"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_5"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_6"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_7"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_8"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_9"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_10"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_3"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_4"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_5"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_6"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_7"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_8"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_9"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_10"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="commonname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="scientificname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="orderclass"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="pk_object"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="id_object"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_revision_begin"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_revision_end"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimecreation"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimemodification"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimedestruction"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="comment"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="name"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="importid"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="importtable"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="pk_surface" exp=""/>
    <constraint desc="" field="id_surface" exp=""/>
    <constraint desc="" field="surfacetype" exp=""/>
    <constraint desc="" field="lpk_descriptionsystem" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_1" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_2" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_3" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_4" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_5" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_6" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_7" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_8" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_9" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_10" exp=""/>
    <constraint desc="" field="surfacecategory" exp=""/>
    <constraint desc="" field="number" exp=""/>
    <constraint desc="" field="florainvasive" exp=""/>
    <constraint desc="" field="floraprotected" exp=""/>
    <constraint desc="" field="pk_descriptionsystem" exp=""/>
    <constraint desc="" field="id_descriptionsystem" exp=""/>
    <constraint desc="" field="lpk_object" exp=""/>
    <constraint desc="" field="strategicvalue" exp=""/>
    <constraint desc="" field="operational" exp=""/>
    <constraint desc="" field="structuralstate" exp=""/>
    <constraint desc="" field="operationalstate" exp=""/>
    <constraint desc="" field="dateoperationalcreation" exp=""/>
    <constraint desc="" field="dateoperationalcreationupper" exp=""/>
    <constraint desc="" field="operationaldatecreationaccuracy" exp=""/>
    <constraint desc="" field="datetimeoperationaldestruction" exp=""/>
    <constraint desc="" field="geotrackingxyquality" exp=""/>
    <constraint desc="" field="geotrackingzquality" exp=""/>
    <constraint desc="" field="geotrackingdate" exp=""/>
    <constraint desc="" field="geotrackingsource" exp=""/>
    <constraint desc="" field="parameters" exp=""/>
    <constraint desc="" field="parameterslist" exp=""/>
    <constraint desc="" field="city" exp=""/>
    <constraint desc="" field="streetname" exp=""/>
    <constraint desc="" field="streetupname" exp=""/>
    <constraint desc="" field="streetdownname" exp=""/>
    <constraint desc="" field="streetcomment" exp=""/>
    <constraint desc="" field="lid_actor_1" exp=""/>
    <constraint desc="" field="lid_actor_2" exp=""/>
    <constraint desc="" field="lid_actor_3" exp=""/>
    <constraint desc="" field="lid_facility" exp=""/>
    <constraint desc="" field="float_1" exp=""/>
    <constraint desc="" field="float_2" exp=""/>
    <constraint desc="" field="float_3" exp=""/>
    <constraint desc="" field="float_4" exp=""/>
    <constraint desc="" field="float_5" exp=""/>
    <constraint desc="" field="float_6" exp=""/>
    <constraint desc="" field="float_7" exp=""/>
    <constraint desc="" field="float_8" exp=""/>
    <constraint desc="" field="float_9" exp=""/>
    <constraint desc="" field="float_10" exp=""/>
    <constraint desc="" field="string_1" exp=""/>
    <constraint desc="" field="string_2" exp=""/>
    <constraint desc="" field="string_3" exp=""/>
    <constraint desc="" field="string_4" exp=""/>
    <constraint desc="" field="string_5" exp=""/>
    <constraint desc="" field="string_6" exp=""/>
    <constraint desc="" field="string_7" exp=""/>
    <constraint desc="" field="string_8" exp=""/>
    <constraint desc="" field="string_9" exp=""/>
    <constraint desc="" field="string_10" exp=""/>
    <constraint desc="" field="commonname" exp=""/>
    <constraint desc="" field="scientificname" exp=""/>
    <constraint desc="" field="orderclass" exp=""/>
    <constraint desc="" field="pk_object" exp=""/>
    <constraint desc="" field="id_object" exp=""/>
    <constraint desc="" field="lpk_revision_begin" exp=""/>
    <constraint desc="" field="lpk_revision_end" exp=""/>
    <constraint desc="" field="datetimecreation" exp=""/>
    <constraint desc="" field="datetimemodification" exp=""/>
    <constraint desc="" field="datetimedestruction" exp=""/>
    <constraint desc="" field="comment" exp=""/>
    <constraint desc="" field="name" exp=""/>
    <constraint desc="" field="importid" exp=""/>
    <constraint desc="" field="importtable" exp=""/>
    <constraint desc="" field="lid_actor" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column width="-1" hidden="0" name="pk_surface" type="field"/>
      <column width="-1" hidden="0" name="id_surface" type="field"/>
      <column width="-1" hidden="0" name="surfacetype" type="field"/>
      <column width="-1" hidden="0" name="lpk_descriptionsystem" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_1" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_2" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_3" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_4" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_5" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_6" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_7" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_8" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_9" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_10" type="field"/>
      <column width="-1" hidden="0" name="surfacecategory" type="field"/>
      <column width="-1" hidden="0" name="number" type="field"/>
      <column width="-1" hidden="0" name="florainvasive" type="field"/>
      <column width="-1" hidden="0" name="floraprotected" type="field"/>
      <column width="-1" hidden="0" name="pk_descriptionsystem" type="field"/>
      <column width="-1" hidden="0" name="id_descriptionsystem" type="field"/>
      <column width="-1" hidden="0" name="lpk_object" type="field"/>
      <column width="-1" hidden="0" name="strategicvalue" type="field"/>
      <column width="-1" hidden="0" name="operational" type="field"/>
      <column width="-1" hidden="0" name="structuralstate" type="field"/>
      <column width="-1" hidden="0" name="operationalstate" type="field"/>
      <column width="-1" hidden="0" name="dateoperationalcreation" type="field"/>
      <column width="-1" hidden="0" name="dateoperationalcreationupper" type="field"/>
      <column width="-1" hidden="0" name="operationaldatecreationaccuracy" type="field"/>
      <column width="-1" hidden="0" name="datetimeoperationaldestruction" type="field"/>
      <column width="-1" hidden="0" name="geotrackingxyquality" type="field"/>
      <column width="-1" hidden="0" name="geotrackingzquality" type="field"/>
      <column width="-1" hidden="0" name="geotrackingdate" type="field"/>
      <column width="-1" hidden="0" name="geotrackingsource" type="field"/>
      <column width="-1" hidden="0" name="parameters" type="field"/>
      <column width="-1" hidden="0" name="parameterslist" type="field"/>
      <column width="-1" hidden="0" name="city" type="field"/>
      <column width="-1" hidden="0" name="streetname" type="field"/>
      <column width="-1" hidden="0" name="streetupname" type="field"/>
      <column width="-1" hidden="0" name="streetdownname" type="field"/>
      <column width="-1" hidden="0" name="streetcomment" type="field"/>
      <column width="-1" hidden="0" name="lid_actor_1" type="field"/>
      <column width="-1" hidden="0" name="lid_actor_2" type="field"/>
      <column width="-1" hidden="0" name="lid_actor_3" type="field"/>
      <column width="-1" hidden="0" name="lid_facility" type="field"/>
      <column width="-1" hidden="0" name="float_1" type="field"/>
      <column width="-1" hidden="0" name="float_2" type="field"/>
      <column width="-1" hidden="0" name="float_3" type="field"/>
      <column width="-1" hidden="0" name="float_4" type="field"/>
      <column width="-1" hidden="0" name="float_5" type="field"/>
      <column width="-1" hidden="0" name="float_6" type="field"/>
      <column width="-1" hidden="0" name="float_7" type="field"/>
      <column width="-1" hidden="0" name="float_8" type="field"/>
      <column width="-1" hidden="0" name="float_9" type="field"/>
      <column width="-1" hidden="0" name="float_10" type="field"/>
      <column width="-1" hidden="0" name="string_1" type="field"/>
      <column width="-1" hidden="0" name="string_2" type="field"/>
      <column width="-1" hidden="0" name="string_3" type="field"/>
      <column width="-1" hidden="0" name="string_4" type="field"/>
      <column width="-1" hidden="0" name="string_5" type="field"/>
      <column width="-1" hidden="0" name="string_6" type="field"/>
      <column width="-1" hidden="0" name="string_7" type="field"/>
      <column width="-1" hidden="0" name="string_8" type="field"/>
      <column width="-1" hidden="0" name="string_9" type="field"/>
      <column width="-1" hidden="0" name="string_10" type="field"/>
      <column width="-1" hidden="0" name="commonname" type="field"/>
      <column width="-1" hidden="0" name="scientificname" type="field"/>
      <column width="-1" hidden="0" name="orderclass" type="field"/>
      <column width="-1" hidden="0" name="pk_object" type="field"/>
      <column width="-1" hidden="0" name="id_object" type="field"/>
      <column width="-1" hidden="0" name="lpk_revision_begin" type="field"/>
      <column width="-1" hidden="0" name="lpk_revision_end" type="field"/>
      <column width="-1" hidden="0" name="datetimecreation" type="field"/>
      <column width="-1" hidden="0" name="datetimemodification" type="field"/>
      <column width="-1" hidden="0" name="datetimedestruction" type="field"/>
      <column width="-1" hidden="0" name="comment" type="field"/>
      <column width="-1" hidden="0" name="name" type="field"/>
      <column width="-1" hidden="0" name="importid" type="field"/>
      <column width="-1" hidden="0" name="importtable" type="field"/>
      <column width="-1" hidden="0" name="lid_actor" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="city" editable="1"/>
    <field name="comment" editable="1"/>
    <field name="commonname" editable="1"/>
    <field name="dateoperationalcreation" editable="1"/>
    <field name="dateoperationalcreationupper" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimemodification" editable="1"/>
    <field name="datetimeoperationaldestruction" editable="1"/>
    <field name="float_1" editable="1"/>
    <field name="float_10" editable="1"/>
    <field name="float_2" editable="1"/>
    <field name="float_3" editable="1"/>
    <field name="float_4" editable="1"/>
    <field name="float_5" editable="1"/>
    <field name="float_6" editable="1"/>
    <field name="float_7" editable="1"/>
    <field name="float_8" editable="1"/>
    <field name="float_9" editable="1"/>
    <field name="florainvasive" editable="1"/>
    <field name="floraprotected" editable="1"/>
    <field name="geotrackingdate" editable="1"/>
    <field name="geotrackingsource" editable="1"/>
    <field name="geotrackingxyquality" editable="1"/>
    <field name="geotrackingzquality" editable="1"/>
    <field name="id_descriptionsystem" editable="1"/>
    <field name="id_object" editable="1"/>
    <field name="id_surface" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="lid_actor" editable="1"/>
    <field name="lid_actor_1" editable="1"/>
    <field name="lid_actor_2" editable="1"/>
    <field name="lid_actor_3" editable="1"/>
    <field name="lid_descriptionsystem_1" editable="1"/>
    <field name="lid_descriptionsystem_10" editable="1"/>
    <field name="lid_descriptionsystem_2" editable="1"/>
    <field name="lid_descriptionsystem_3" editable="1"/>
    <field name="lid_descriptionsystem_4" editable="1"/>
    <field name="lid_descriptionsystem_5" editable="1"/>
    <field name="lid_descriptionsystem_6" editable="1"/>
    <field name="lid_descriptionsystem_7" editable="1"/>
    <field name="lid_descriptionsystem_8" editable="1"/>
    <field name="lid_descriptionsystem_9" editable="1"/>
    <field name="lid_facility" editable="1"/>
    <field name="lpk_descriptionsystem" editable="1"/>
    <field name="lpk_object" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="name" editable="1"/>
    <field name="number" editable="1"/>
    <field name="operational" editable="1"/>
    <field name="operationaldatecreationaccuracy" editable="1"/>
    <field name="operationalstate" editable="1"/>
    <field name="orderclass" editable="1"/>
    <field name="parameters" editable="1"/>
    <field name="parameterslist" editable="1"/>
    <field name="pk_descriptionsystem" editable="1"/>
    <field name="pk_object" editable="1"/>
    <field name="pk_surface" editable="1"/>
    <field name="scientificname" editable="1"/>
    <field name="strategicvalue" editable="1"/>
    <field name="streetcomment" editable="1"/>
    <field name="streetdownname" editable="1"/>
    <field name="streetname" editable="1"/>
    <field name="streetupname" editable="1"/>
    <field name="string_1" editable="1"/>
    <field name="string_10" editable="1"/>
    <field name="string_2" editable="1"/>
    <field name="string_3" editable="1"/>
    <field name="string_4" editable="1"/>
    <field name="string_5" editable="1"/>
    <field name="string_6" editable="1"/>
    <field name="string_7" editable="1"/>
    <field name="string_8" editable="1"/>
    <field name="string_9" editable="1"/>
    <field name="structuralstate" editable="1"/>
    <field name="surfacecategory" editable="1"/>
    <field name="surfacetype" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="city" labelOnTop="0"/>
    <field name="comment" labelOnTop="0"/>
    <field name="commonname" labelOnTop="0"/>
    <field name="dateoperationalcreation" labelOnTop="0"/>
    <field name="dateoperationalcreationupper" labelOnTop="0"/>
    <field name="datetimecreation" labelOnTop="0"/>
    <field name="datetimedestruction" labelOnTop="0"/>
    <field name="datetimemodification" labelOnTop="0"/>
    <field name="datetimeoperationaldestruction" labelOnTop="0"/>
    <field name="float_1" labelOnTop="0"/>
    <field name="float_10" labelOnTop="0"/>
    <field name="float_2" labelOnTop="0"/>
    <field name="float_3" labelOnTop="0"/>
    <field name="float_4" labelOnTop="0"/>
    <field name="float_5" labelOnTop="0"/>
    <field name="float_6" labelOnTop="0"/>
    <field name="float_7" labelOnTop="0"/>
    <field name="float_8" labelOnTop="0"/>
    <field name="float_9" labelOnTop="0"/>
    <field name="florainvasive" labelOnTop="0"/>
    <field name="floraprotected" labelOnTop="0"/>
    <field name="geotrackingdate" labelOnTop="0"/>
    <field name="geotrackingsource" labelOnTop="0"/>
    <field name="geotrackingxyquality" labelOnTop="0"/>
    <field name="geotrackingzquality" labelOnTop="0"/>
    <field name="id_descriptionsystem" labelOnTop="0"/>
    <field name="id_object" labelOnTop="0"/>
    <field name="id_surface" labelOnTop="0"/>
    <field name="importid" labelOnTop="0"/>
    <field name="importtable" labelOnTop="0"/>
    <field name="lid_actor" labelOnTop="0"/>
    <field name="lid_actor_1" labelOnTop="0"/>
    <field name="lid_actor_2" labelOnTop="0"/>
    <field name="lid_actor_3" labelOnTop="0"/>
    <field name="lid_descriptionsystem_1" labelOnTop="0"/>
    <field name="lid_descriptionsystem_10" labelOnTop="0"/>
    <field name="lid_descriptionsystem_2" labelOnTop="0"/>
    <field name="lid_descriptionsystem_3" labelOnTop="0"/>
    <field name="lid_descriptionsystem_4" labelOnTop="0"/>
    <field name="lid_descriptionsystem_5" labelOnTop="0"/>
    <field name="lid_descriptionsystem_6" labelOnTop="0"/>
    <field name="lid_descriptionsystem_7" labelOnTop="0"/>
    <field name="lid_descriptionsystem_8" labelOnTop="0"/>
    <field name="lid_descriptionsystem_9" labelOnTop="0"/>
    <field name="lid_facility" labelOnTop="0"/>
    <field name="lpk_descriptionsystem" labelOnTop="0"/>
    <field name="lpk_object" labelOnTop="0"/>
    <field name="lpk_revision_begin" labelOnTop="0"/>
    <field name="lpk_revision_end" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="number" labelOnTop="0"/>
    <field name="operational" labelOnTop="0"/>
    <field name="operationaldatecreationaccuracy" labelOnTop="0"/>
    <field name="operationalstate" labelOnTop="0"/>
    <field name="orderclass" labelOnTop="0"/>
    <field name="parameters" labelOnTop="0"/>
    <field name="parameterslist" labelOnTop="0"/>
    <field name="pk_descriptionsystem" labelOnTop="0"/>
    <field name="pk_object" labelOnTop="0"/>
    <field name="pk_surface" labelOnTop="0"/>
    <field name="scientificname" labelOnTop="0"/>
    <field name="strategicvalue" labelOnTop="0"/>
    <field name="streetcomment" labelOnTop="0"/>
    <field name="streetdownname" labelOnTop="0"/>
    <field name="streetname" labelOnTop="0"/>
    <field name="streetupname" labelOnTop="0"/>
    <field name="string_1" labelOnTop="0"/>
    <field name="string_10" labelOnTop="0"/>
    <field name="string_2" labelOnTop="0"/>
    <field name="string_3" labelOnTop="0"/>
    <field name="string_4" labelOnTop="0"/>
    <field name="string_5" labelOnTop="0"/>
    <field name="string_6" labelOnTop="0"/>
    <field name="string_7" labelOnTop="0"/>
    <field name="string_8" labelOnTop="0"/>
    <field name="string_9" labelOnTop="0"/>
    <field name="structuralstate" labelOnTop="0"/>
    <field name="surfacecategory" labelOnTop="0"/>
    <field name="surfacetype" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>streetname</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
