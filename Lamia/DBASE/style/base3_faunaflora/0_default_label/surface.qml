<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingHints="1" minScale="1e+08" version="3.10.0-A CoruÃ±a" styleCategories="Symbology|Labeling|Rendering" hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" simplifyDrawingTol="1" maxScale="0" simplifyMaxScale="1" labelsEnabled="1" simplifyLocal="1">
  <renderer-v2 symbollevels="0" enableorderby="0" forceraster="0" type="RuleRenderer">
    <rules key="{fa6c4aa2-b507-461c-b67d-18ef4ebe3184}">
      <rule symbol="0" key="{dfa059cb-e59c-47af-8e4a-c5d78a49d73b}" label="Habitat" filter=" &quot;surfacecategory&quot; ='HAB'"/>
      <rule symbol="1" key="{d1364d6c-3202-4337-98c3-0b939010bb89}" label="Flore" filter=" &quot;surfacecategory&quot; ='FLO'">
        <rule symbol="2" key="{f2e1ab8b-ab2e-46d7-a752-c15d6a7f2cfe}" filter=" $area &lt;5"/>
        <rule symbol="3" key="{e2638bd1-7a5a-4394-becf-bcfbb538c163}" label="Flore" filter="ELSE"/>
      </rule>
    </rules>
    <symbols>
      <symbol name="0" alpha="1" clip_to_extent="1" force_rhr="0" type="fill">
        <layer enabled="1" class="ShapeburstFill" locked="0" pass="0">
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" alpha="1" clip_to_extent="1" force_rhr="0" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" alpha="1" clip_to_extent="1" force_rhr="0" type="fill">
        <layer enabled="1" class="CentroidFill" locked="0" pass="0">
          <prop k="point_on_all_parts" v="1"/>
          <prop k="point_on_surface" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol name="@2@0" alpha="1" clip_to_extent="1" force_rhr="0" type="marker">
            <layer enabled="1" class="SvgMarker" locked="0" pass="0">
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
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="3" alpha="1" clip_to_extent="1" force_rhr="0" type="fill">
        <layer enabled="1" class="ShapeburstFill" locked="0" pass="0">
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" class="SVGFill" locked="0" pass="0">
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol name="@3@1" alpha="1" clip_to_extent="1" force_rhr="0" type="line">
            <layer enabled="1" class="SimpleLine" locked="0" pass="0">
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
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{3d4cc884-08b7-4a75-aab9-bb1751b0ff1e}">
      <rule key="{2cff1c8a-504e-4fa0-88a5-9311f944d1af}" filter=" &quot;surfacecategory&quot;  =  'FLO' ">
        <settings calloutType="simple">
          <text-style fontUnderline="0" fontFamily="MS Shell Dlg 2" textOrientation="horizontal" fontWordSpacing="0" namedStyle="Normal" previewBkgrdColor="255,255,255,255" blendMode="0" useSubstitutions="0" fontKerning="1" textOpacity="1" fontStrikeout="0" fontItalic="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" isExpression="0" fontWeight="50" fontSize="8" fontLetterSpacing="0" textColor="51,131,44,255" fontSizeUnit="Point" fieldName="scientificname" fontCapitals="0" multilineHeight="1">
            <text-buffer bufferBlendMode="0" bufferJoinStyle="128" bufferDraw="1" bufferSize="1" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1"/>
            <background shapeFillColor="255,255,255,255" shapeRadiiUnit="MM" shapeBorderWidthUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeRadiiX="0" shapeDraw="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeSVGFile="" shapeJoinStyle="64" shapeRadiiY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeType="0" shapeOffsetY="0" shapeSizeType="0" shapeOffsetUnit="MM" shapeBorderWidth="0" shapeOffsetX="0" shapeSizeY="0" shapeBlendMode="0" shapeSizeUnit="MM">
              <symbol name="markerSymbol" alpha="1" clip_to_extent="1" force_rhr="0" type="marker">
                <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
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
                      <Option name="name" value="" type="QString"/>
                      <Option name="properties"/>
                      <Option name="type" value="collection" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetGlobal="1" shadowRadiusAlphaOnly="0" shadowRadius="1.5" shadowDraw="0" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowUnder="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowScale="100" shadowBlendMode="6" shadowOffsetUnit="MM" shadowOpacity="0.7"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format rightDirectionSymbol=">" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" addDirectionSymbol="0" formatNumbers="0" wrapChar="" plussign="0" reverseDirectionSymbol="0" decimals="3" autoWrapLength="0" multilineAlign="0"/>
          <placement fitInPolygonOnly="0" repeatDistance="0" maxCurvedCharAngleIn="25" geometryGeneratorEnabled="0" dist="0" yOffset="0" repeatDistanceUnits="MM" overrunDistanceUnit="MM" centroidWhole="0" centroidInside="0" distUnits="MM" geometryGenerator="" placement="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" rotationAngle="0" geometryGeneratorType="PointGeometry" priority="5" maxCurvedCharAngleOut="-25" layerType="PolygonGeometry" distMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" offsetType="0" xOffset="0" preserveRotation="1" quadOffset="4"/>
          <rendering fontLimitPixelSize="0" zIndex="0" obstacleType="0" displayAll="0" drawLabels="1" scaleMax="0" labelPerPart="0" scaleVisibility="0" limitNumLabels="0" minFeatureSize="0" fontMaxPixelSize="10000" maxNumLabels="2000" upsidedownLabels="0" obstacleFactor="1" scaleMin="0" obstacle="1" fontMinPixelSize="3" mergeLines="0"/>
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
              <Option name="lineSymbol" value="&lt;symbol name=&quot;symbol&quot; alpha=&quot;1&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; type=&quot;line&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
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
      </rule>
      <rule key="{436da63c-0d94-4de4-98fa-fda83fcc4c58}" filter=" &quot;surfacecategory&quot;  =  'HAB' ">
        <settings calloutType="simple">
          <text-style fontUnderline="0" fontFamily="MS Shell Dlg 2" textOrientation="horizontal" fontWordSpacing="0" namedStyle="Normal" previewBkgrdColor="255,255,255,255" blendMode="0" useSubstitutions="0" fontKerning="1" textOpacity="1" fontStrikeout="0" fontItalic="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" isExpression="0" fontWeight="50" fontSize="8" fontLetterSpacing="0" textColor="227,26,28,255" fontSizeUnit="Point" fieldName="habitatname" fontCapitals="0" multilineHeight="1">
            <text-buffer bufferBlendMode="0" bufferJoinStyle="128" bufferDraw="1" bufferSize="1" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1"/>
            <background shapeFillColor="255,255,255,255" shapeRadiiUnit="MM" shapeBorderWidthUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeRadiiX="0" shapeDraw="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeSVGFile="" shapeJoinStyle="64" shapeRadiiY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeType="0" shapeOffsetY="0" shapeSizeType="0" shapeOffsetUnit="MM" shapeBorderWidth="0" shapeOffsetX="0" shapeSizeY="0" shapeBlendMode="0" shapeSizeUnit="MM">
              <symbol name="markerSymbol" alpha="1" clip_to_extent="1" force_rhr="0" type="marker">
                <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
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
                      <Option name="name" value="" type="QString"/>
                      <Option name="properties"/>
                      <Option name="type" value="collection" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetGlobal="1" shadowRadiusAlphaOnly="0" shadowRadius="1.5" shadowDraw="0" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowUnder="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowScale="100" shadowBlendMode="6" shadowOffsetUnit="MM" shadowOpacity="0.7"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format rightDirectionSymbol=">" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" addDirectionSymbol="0" formatNumbers="0" wrapChar="" plussign="0" reverseDirectionSymbol="0" decimals="3" autoWrapLength="20" multilineAlign="1"/>
          <placement fitInPolygonOnly="0" repeatDistance="0" maxCurvedCharAngleIn="25" geometryGeneratorEnabled="0" dist="0" yOffset="0" repeatDistanceUnits="MM" overrunDistanceUnit="MM" centroidWhole="0" centroidInside="0" distUnits="MM" geometryGenerator="" placement="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" rotationAngle="0" geometryGeneratorType="PointGeometry" priority="5" maxCurvedCharAngleOut="-25" layerType="PolygonGeometry" distMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" offsetType="0" xOffset="0" preserveRotation="1" quadOffset="4"/>
          <rendering fontLimitPixelSize="0" zIndex="0" obstacleType="0" displayAll="0" drawLabels="1" scaleMax="0" labelPerPart="0" scaleVisibility="0" limitNumLabels="0" minFeatureSize="0" fontMaxPixelSize="10000" maxNumLabels="2000" upsidedownLabels="0" obstacleFactor="1" scaleMin="0" obstacle="1" fontMinPixelSize="3" mergeLines="0"/>
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
              <Option name="lineSymbol" value="&lt;symbol name=&quot;symbol&quot; alpha=&quot;1&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; type=&quot;line&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
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
      </rule>
    </rules>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>2</layerGeometryType>
</qgis>
