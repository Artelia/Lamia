<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyLocal="1" maxScale="0" version="3.10.0-A CoruÃ±a" simplifyDrawingHints="1" styleCategories="Symbology|Labeling|Rendering" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" minScale="1e+08" labelsEnabled="0" simplifyAlgorithm="0" simplifyMaxScale="1">
  <renderer-v2 symbollevels="0" forceraster="0" type="RuleRenderer" enableorderby="0">
    <rules key="{fa6c4aa2-b507-461c-b67d-18ef4ebe3184}">
      <rule symbol="0" label="Flore" key="{fe098b19-9d6e-4752-925a-8aad2ced2f5d}" filter=" &quot;surfacecategory&quot; ='FLO'">
        <rule symbol="1" key="{8b6acef9-2e40-44b7-89d8-a43d6e586441}" filter=" $area &lt;5"/>
        <rule symbol="2" label="Flore" key="{c35bf1bf-0a47-4010-acb1-6445b0807dec}" filter="ELSE"/>
      </rule>
      <rule symbol="3" label="Habitat" key="{dfa059cb-e59c-47af-8e4a-c5d78a49d73b}" filter=" &quot;surfacecategory&quot; ='HAB'"/>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" alpha="1" name="0" type="fill" force_rhr="0">
        <layer class="SimpleFill" locked="0" pass="0" enabled="1">
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
      <symbol clip_to_extent="1" alpha="1" name="1" type="fill" force_rhr="0">
        <layer class="CentroidFill" locked="0" pass="0" enabled="1">
          <prop k="point_on_all_parts" v="1"/>
          <prop k="point_on_surface" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" alpha="1" name="@1@0" type="marker" force_rhr="0">
            <layer class="SvgMarker" locked="0" pass="0" enabled="1">
              <prop k="angle" v="0"/>
              <prop k="color" v="51,131,44,255"/>
              <prop k="fixedAspectRatio" v="0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iODkyLjAwMDAwMHB0IiBoZWlnaHQ9IjEyODAuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCA4OTIuMDAwMDAwIDEyODAuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+CjxtZXRhZGF0YT4KQ3JlYXRlZCBieSBwb3RyYWNlIDEuMTUsIHdyaXR0ZW4gYnkgUGV0ZXIgU2VsaW5nZXIgMjAwMS0yMDE3CjwvbWV0YWRhdGE+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuMDAwMDAwLDEyODAuMDAwMDAwKSBzY2FsZSgwLjEwMDAwMCwtMC4xMDAwMDApIgpmaWxsPSJwYXJhbShmaWxsKSAjRkZGIiBzdHJva2U9Im5vbmUiPgo8cGF0aCBkPSJNNTE2NSAxMjc4NyBjLTIzMSAtNzggLTQ4NiAtMzUxIC03MjUgLTc3OSAtMjMzIC00MTcgLTM3NCAtODYyIC0zOTYKLTEyNTkgLTEwIC0xNjUgNiAtMTg1IDEwNyAtMTM0IDYzIDMyIDMxMSAxODYgNDQ1IDI3NSA0MzAgMjg5IDgxNyA3MTEgOTg0CjEwNzUgMTkyIDQxNyAxMjYgNzE3IC0xNzcgODEwIC03MCAyMiAtMTkwIDI4IC0yMzggMTJ6Ii8+CjxwYXRoIGQ9Ik0zMDIwIDEyNDYxIGMtMTk3IC02MCAtMjY5IC0yODQgLTI1NyAtODAzIDUgLTI1NiAyMiAtMzgzIDc4IC01ODMKNTQgLTE5OCAxNjkgLTQwMyAyNzEgLTQ4NyA1NiAtNDYgMjEyIC0xMjggMjQzIC0xMjggMzYgMCA1MiAzMSAxMDAgMjA3IDUzCjE5MSAxMjIgMzk2IDIwNCA2MDEgNjkgMTcyIDEzNCAzNTYgMTU2IDQ0MyA0MiAxNjIgMzkgMzAzIC0xMCAzOTggLTM2IDcxCi0xMjggMTUwIC0yNDQgMjEwIC0yMzMgMTIwIC00MzcgMTczIC01NDEgMTQyeiIvPgo8cGF0aCBkPSJNNjg3NSAxMTc5NCBjLTIwOSAtMjAgLTM4NiAtNTggLTU4MiAtMTI1IC0xMzggLTQ3IC0zOTkgLTE3MyAtNTI4Ci0yNTQgLTM2MCAtMjI3IC02MjIgLTUyNCAtNjkwIC03ODQgLTIzIC04OSAtMjYgLTg4IDIyMiAtNjIgMTA4MCAxMTQgMTQwNAoxODAgMTYzNiAzMzQgMTEyIDc1IDI2MiAyMzEgMzA4IDMyMiA2MCAxMTYgNzQgMTY4IDc0IDI4NSAwIDk1IC0zIDExMCAtMjgKMTYyIC0zMCA2MSAtNjAgODggLTExNyAxMDYgLTM4IDEyIC0yMjkgMjIgLTI5NSAxNnoiLz4KPHBhdGggZD0iTTE0OTAgMTEzMjkgYy0xODYgLTIxIC0zMTcgLTYzIC0zOTkgLTEyOCAtNDYgLTM3IC05NSAtMTI2IC0xMTIKLTIwNiAtNyAtMzMgLTEzIC0xMTggLTEzIC0xOTAgMCAtMTE5IDIgLTEzNSAyNiAtMTg2IDU1IC0xMjAgMTcwIC0xNjQgNTY4Ci0yMTkgMzcwIC01MiA0ODEgLTcxIDYxOSAtMTA2IDE1MiAtMzggMjQ2IC03OSAzNzYgLTE2NSA1MCAtMzIgOTggLTU5IDEwNwotNTkgNDAgMCAyOSA3OCAtNDcgMzQzIC0xNjcgNTgxIC0zNjkgODQyIC03MDcgOTExIC04NCAxNyAtMjg3IDIwIC00MTggNXoiLz4KPHBhdGggZD0iTTQxNjAgMTAzMjMgYy0xMDQgLTggLTI5MyAtNDQgLTQwNSAtNzcgLTQ4MyAtMTQwIC05MDEgLTQ0OCAtMTA1NAotNzc3IC05MiAtMTk4IC03NyAtMzc4IDQzIC01MTYgNTYgLTY0IDE3NSAtMTM5IDI0MyAtMTU0IDgwIC0xNiAzNTMgLTEzIDQ5OAo2IDE1NCAyMCAyNTIgNDYgMzk1IDEwMiA0OTYgMTk1IDgyNCA0ODYgOTE1IDgxMyAyMyA4NCAyNCAyMjMgMSAzMTAgLTkgMzYKLTQxIDExNSAtNzAgMTc2IGwtNTMgMTExIC0xNjggNiBjLTE2NyA3IC0yNTkgNyAtMzQ1IDB6Ii8+CjxwYXRoIGQ9Ik02NzE1IDEwMjk5IGMtMjIyIC0yNyAtNDM4IC05MyAtNzY4IC0yMzMgLTI1OSAtMTExIC00NjYgLTE5MiAtNjI3Ci0yNDggLTYzIC0yMiAtMTM0IC01MSAtMTU3IC02NCAtNjYgLTM4IC01NCAtNjQgMjcgLTY0IDgzIDAgNDU1IC0xMjcgNjMxCi0yMTUgMzYgLTE5IDE1OCAtOTAgMjcyIC0xNTggMjg0IC0xNzIgMzg5IC0yMDUgNjIxIC0xOTQgMTkzIDkgMzY5IDY0IDUxNwoxNjMgMjMyIDE1NCAzMzIgMzYyIDI4NSA1OTQgLTQzIDIxMCAtMTc2IDM0MyAtNDAxIDQwMCAtOTUgMjQgLTI4MyAzMyAtNDAwCjE5eiIvPgo8cGF0aCBkPSJNNzMwIDEwMTAzIGMtMjUgLTIgLTgzIC0xMCAtMTMwIC0xOSAtNDMyIC03NyAtNjU1IC0zNDMgLTU4NyAtNzAyCjE3IC04OSA1NSAtMTgzIDg5IC0yMTkgNzkgLTg0IDUwNCAtMzcgMTAzMSAxMTYgMjk2IDg2IDY2OSAxNzMgOTc3IDIyNyAxMTMKMjAgMjA2IDM3IDIwNyAzOCA0IDQgLTE5MiAxNDUgLTI3NSAxOTkgLTEyOCA4MSAtMzg3IDIwNCAtNTM0IDI1MSAtMjcyIDg5Ci01NDcgMTI3IC03NzggMTA5eiIvPgo8cGF0aCBkPSJNNDY3OCA5MDE5IGMtMzEgLTQgLTczIC0xNSAtOTMgLTI0IC0zNSAtMTQgLTM3IC0xNyAtMzEgLTQ4IDI2IC0xMzIKNTQ0IC03OTUgODM0IC0xMDY4IDE0MiAtMTM0IDI0NCAtMTc0IDQzMiAtMTcyIDIyNyAzIDQyOCAxMDAgNDk2IDIzOSAyNSA1MgoyNyA2MCAyMSAxNjIgLTE1IDMwMiAtMjE1IDY0OCAtNDQ1IDc3MCAtMTE4IDYzIC0zNDEgMTEwIC02NDcgMTM3IC0xODEgMTYKLTQ3MyAxOCAtNTY3IDR6Ii8+CjxwYXRoIGQ9Ik0xODQ1IDg5MzMgYy0xNzggLTEzIC01ODcgLTg2IC04MDUgLTE0NCAtNDQ1IC0xMTggLTU4MiAtMTk5IC03MzYKLTQzNCAtMTAyIC0xNTcgLTE1MiAtMzA4IC0xNjEgLTQ4NSAtOCAtMTcxIDIyIC0yNzMgMTA3IC0zNTggOTEgLTkwIDI0MSAtMTA4CjM3MSAtNDMgMzcgMTggMTA3IDYzIDE1NSA5OSA4NyA2NCA0MjMgMzk0IDgxNCA3OTggMjE5IDIyNSAzMzEgMzIxIDUzOSA0NTgKbDE1NCAxMDEgLTQ5IDcgYy01MCA2IC0zMDAgNyAtMzg5IDF6Ii8+CjxwYXRoIGQ9Ik0zODUzIDg2MDMgYy0xNjEgLTE1NSAtNTc0IC03NzQgLTc0NSAtMTExOCAtMjExIC00MjEgLTIxNyAtNjM4IC0yMgotODQ0IDEyOCAtMTM3IDI0NiAtMTc1IDQxNCAtMTM1IDE0NyAzNCAyOTEgMTI3IDUxNSAzMzIgbDE0MiAxMzAgNiAxMzggYzIzCjQ3NyAtOSA3MzIgLTE2NSAxMzI3IC0zNCAxMzAgLTY1IDIzNyAtNjkgMjM3IC0zIDAgLTM4IC0zMCAtNzYgLTY3eiIvPgo8cGF0aCBkPSJNMjgzMSA4NDY0IGMtMTM0IC0xNiAtMjM0IC00MyAtMzUxIC05MyAtMzI3IC0xNDEgLTY5MSAtNDY5IC04ODEKLTc5MyAtMTA2IC0xODAgLTE2MSAtMzgwIC0xMzkgLTUwNiAxNSAtODYgMzggLTEzMyAxMTQgLTIyOCA4NCAtMTA0IDI4NSAtMjk4CjM2NCAtMzUxIDEzNyAtOTIgMjQyIC04MCAzNjAgMzggMTYxIDE2MSAyODIgNDY1IDM4NiA5NjkgODUgNDExIDE2NiA2ODIgMjYxCjg3MCBsNTUgMTEwIC0yNyAtMSBjLTE2IC0xIC03OSAtNyAtMTQyIC0xNXoiLz4KPHBhdGggZD0iTTQ1MjYgNzk0OCBjLTQgLTEwMSAtMTEgLTI4MCAtMTYgLTM5OCAtMjggLTYxNiAtNzQgLTc2NyAtMjc5IC05MjAKLTMzIC0yNSAtNjEgLTQ4IC02MSAtNTEgMCAtNCA2NCAtOSAxNDMgLTEyIDE2MCAtNiAyMzEgLTIyIDM2MiAtODUgNTc3IC0yNzgKOTUxIC0xMjI3IDEwNjAgLTI2OTAgMjAgLTI3NiAzNyAtODExIDMzIC0xMDY4IGwtMyAtMjEyIC0zMDEgMzM3IGMtNjUwIDcyNAotMTAzMCAxMDk2IC0xNDI5IDEzOTYgLTU2MyA0MjQgLTEwMTYgNTYxIC0xNTE0IDQ1OSAtNDIgLTkgLTEzOSAtMzcgLTIxNiAtNjQKLTYzNSAtMjIwIC03ODIgLTI2NSAtMTAxNyAtMzE1IC0xMjcgLTI3IC0xNjggLTQyIC0xNjggLTYxIDAgLTE4IDMyIC0yMyAyNDYKLTM0IDI4MyAtMTQgNDg2IC01MSA3NTMgLTEzOSA0MjYgLTE0MSA4NzAgLTQwNSAxMzMxIC03OTEgNDk3IC00MTYgMTI2NSAtOTI2CjE4NDAgLTEyMjMgOTYgLTUwIDIwOCAtMTEzIDI0OCAtMTM5IDMwOCAtMjA2IDQ3NiAtNDgzIDU0OCAtODk4IDExIC02OCAxOAotMjAwIDI0IC00NjAgNSAtMjM2IDEyIC0zODAgMjAgLTQwOCAzMyAtMTEzIDE3NCAtMTcxIDQxOCAtMTcyIGwxMDIgMCAwIDE2OApjMCAzMTIgLTE3IDQyOCAtMTM1IDkxMiAtMTUwIDYxNyAtMjIwIDk1OCAtMjY3IDEzMDAgLTE5IDE0MCAtMjIgMjEwIC0yMyA0NjAKMCAyNjcgMiAzMDcgMjMgNDI1IDY1IDM1OSAyMDYgNjc2IDQ2OSAxMDUyIDIwMyAyOTEgNDU5IDU5NSA5NjcgMTE1MiA0NTggNTAxCjYyNCA2OTAgNzgwIDg4OSAyMzUgMzAwIDM1OSA1NDEgNDMxIDgzMiA5IDM2IDE4IDczIDIxIDgzIDUgMTQgLTEgMTcgLTM4IDE3Ci04MyAwIC0yNzMgLTI5IC0zNjMgLTU1IC0yNzggLTgxIC05NTIgLTQxMyAtMTMzNSAtNjU3IC01MTYgLTMzMCAtODU1IC02OTkKLTEwMDUgLTEwOTYgLTQ4IC0xMjkgLTc0IC0yNDIgLTEwNiAtNDU3IC0zNCAtMjQwIC02MCAtMzUyIC05OCAtNDM5IGwtMjggLTYxCi02IDE5NSBjLTEwIDMxMCAtNTAgNjEwIC0xNDggMTA5MCAtMTMyIDY0OSAtMjI2IDEyMjIgLTI1NCAxNTQzIGwtNyA3NyAtMTMxCi0yIGMtMTI1IC0yIC0xMzUgLTEgLTE4MiAyNCAtNjAgMzIgLTE1MSAxMjQgLTI3MCAyNzMgLTEzMSAxNjUgLTIyOCAyNjggLTMyMAozNDAgLTQ2IDM2IC04NSA2NSAtODggNjUgLTIgMCAtNyAtODIgLTExIC0xODJ6Ii8+CjwvZz4KPC9zdmc+Cg=="/>
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
      <symbol clip_to_extent="1" alpha="1" name="2" type="fill" force_rhr="0">
        <layer class="ShapeburstFill" locked="0" pass="0" enabled="1">
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
        <layer class="SVGFill" locked="0" pass="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="51,131,44,255"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="base64:PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI+CjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iODkyLjAwMDAwMHB0IiBoZWlnaHQ9IjEyODAuMDAwMDAwcHQiIHZpZXdCb3g9IjAgMCA4OTIuMDAwMDAwIDEyODAuMDAwMDAwIgogcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCI+CjxtZXRhZGF0YT4KQ3JlYXRlZCBieSBwb3RyYWNlIDEuMTUsIHdyaXR0ZW4gYnkgUGV0ZXIgU2VsaW5nZXIgMjAwMS0yMDE3CjwvbWV0YWRhdGE+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuMDAwMDAwLDEyODAuMDAwMDAwKSBzY2FsZSgwLjEwMDAwMCwtMC4xMDAwMDApIgpmaWxsPSJwYXJhbShmaWxsKSAjRkZGIiBzdHJva2U9Im5vbmUiPgo8cGF0aCBkPSJNNTE2NSAxMjc4NyBjLTIzMSAtNzggLTQ4NiAtMzUxIC03MjUgLTc3OSAtMjMzIC00MTcgLTM3NCAtODYyIC0zOTYKLTEyNTkgLTEwIC0xNjUgNiAtMTg1IDEwNyAtMTM0IDYzIDMyIDMxMSAxODYgNDQ1IDI3NSA0MzAgMjg5IDgxNyA3MTEgOTg0CjEwNzUgMTkyIDQxNyAxMjYgNzE3IC0xNzcgODEwIC03MCAyMiAtMTkwIDI4IC0yMzggMTJ6Ii8+CjxwYXRoIGQ9Ik0zMDIwIDEyNDYxIGMtMTk3IC02MCAtMjY5IC0yODQgLTI1NyAtODAzIDUgLTI1NiAyMiAtMzgzIDc4IC01ODMKNTQgLTE5OCAxNjkgLTQwMyAyNzEgLTQ4NyA1NiAtNDYgMjEyIC0xMjggMjQzIC0xMjggMzYgMCA1MiAzMSAxMDAgMjA3IDUzCjE5MSAxMjIgMzk2IDIwNCA2MDEgNjkgMTcyIDEzNCAzNTYgMTU2IDQ0MyA0MiAxNjIgMzkgMzAzIC0xMCAzOTggLTM2IDcxCi0xMjggMTUwIC0yNDQgMjEwIC0yMzMgMTIwIC00MzcgMTczIC01NDEgMTQyeiIvPgo8cGF0aCBkPSJNNjg3NSAxMTc5NCBjLTIwOSAtMjAgLTM4NiAtNTggLTU4MiAtMTI1IC0xMzggLTQ3IC0zOTkgLTE3MyAtNTI4Ci0yNTQgLTM2MCAtMjI3IC02MjIgLTUyNCAtNjkwIC03ODQgLTIzIC04OSAtMjYgLTg4IDIyMiAtNjIgMTA4MCAxMTQgMTQwNAoxODAgMTYzNiAzMzQgMTEyIDc1IDI2MiAyMzEgMzA4IDMyMiA2MCAxMTYgNzQgMTY4IDc0IDI4NSAwIDk1IC0zIDExMCAtMjgKMTYyIC0zMCA2MSAtNjAgODggLTExNyAxMDYgLTM4IDEyIC0yMjkgMjIgLTI5NSAxNnoiLz4KPHBhdGggZD0iTTE0OTAgMTEzMjkgYy0xODYgLTIxIC0zMTcgLTYzIC0zOTkgLTEyOCAtNDYgLTM3IC05NSAtMTI2IC0xMTIKLTIwNiAtNyAtMzMgLTEzIC0xMTggLTEzIC0xOTAgMCAtMTE5IDIgLTEzNSAyNiAtMTg2IDU1IC0xMjAgMTcwIC0xNjQgNTY4Ci0yMTkgMzcwIC01MiA0ODEgLTcxIDYxOSAtMTA2IDE1MiAtMzggMjQ2IC03OSAzNzYgLTE2NSA1MCAtMzIgOTggLTU5IDEwNwotNTkgNDAgMCAyOSA3OCAtNDcgMzQzIC0xNjcgNTgxIC0zNjkgODQyIC03MDcgOTExIC04NCAxNyAtMjg3IDIwIC00MTggNXoiLz4KPHBhdGggZD0iTTQxNjAgMTAzMjMgYy0xMDQgLTggLTI5MyAtNDQgLTQwNSAtNzcgLTQ4MyAtMTQwIC05MDEgLTQ0OCAtMTA1NAotNzc3IC05MiAtMTk4IC03NyAtMzc4IDQzIC01MTYgNTYgLTY0IDE3NSAtMTM5IDI0MyAtMTU0IDgwIC0xNiAzNTMgLTEzIDQ5OAo2IDE1NCAyMCAyNTIgNDYgMzk1IDEwMiA0OTYgMTk1IDgyNCA0ODYgOTE1IDgxMyAyMyA4NCAyNCAyMjMgMSAzMTAgLTkgMzYKLTQxIDExNSAtNzAgMTc2IGwtNTMgMTExIC0xNjggNiBjLTE2NyA3IC0yNTkgNyAtMzQ1IDB6Ii8+CjxwYXRoIGQ9Ik02NzE1IDEwMjk5IGMtMjIyIC0yNyAtNDM4IC05MyAtNzY4IC0yMzMgLTI1OSAtMTExIC00NjYgLTE5MiAtNjI3Ci0yNDggLTYzIC0yMiAtMTM0IC01MSAtMTU3IC02NCAtNjYgLTM4IC01NCAtNjQgMjcgLTY0IDgzIDAgNDU1IC0xMjcgNjMxCi0yMTUgMzYgLTE5IDE1OCAtOTAgMjcyIC0xNTggMjg0IC0xNzIgMzg5IC0yMDUgNjIxIC0xOTQgMTkzIDkgMzY5IDY0IDUxNwoxNjMgMjMyIDE1NCAzMzIgMzYyIDI4NSA1OTQgLTQzIDIxMCAtMTc2IDM0MyAtNDAxIDQwMCAtOTUgMjQgLTI4MyAzMyAtNDAwCjE5eiIvPgo8cGF0aCBkPSJNNzMwIDEwMTAzIGMtMjUgLTIgLTgzIC0xMCAtMTMwIC0xOSAtNDMyIC03NyAtNjU1IC0zNDMgLTU4NyAtNzAyCjE3IC04OSA1NSAtMTgzIDg5IC0yMTkgNzkgLTg0IDUwNCAtMzcgMTAzMSAxMTYgMjk2IDg2IDY2OSAxNzMgOTc3IDIyNyAxMTMKMjAgMjA2IDM3IDIwNyAzOCA0IDQgLTE5MiAxNDUgLTI3NSAxOTkgLTEyOCA4MSAtMzg3IDIwNCAtNTM0IDI1MSAtMjcyIDg5Ci01NDcgMTI3IC03NzggMTA5eiIvPgo8cGF0aCBkPSJNNDY3OCA5MDE5IGMtMzEgLTQgLTczIC0xNSAtOTMgLTI0IC0zNSAtMTQgLTM3IC0xNyAtMzEgLTQ4IDI2IC0xMzIKNTQ0IC03OTUgODM0IC0xMDY4IDE0MiAtMTM0IDI0NCAtMTc0IDQzMiAtMTcyIDIyNyAzIDQyOCAxMDAgNDk2IDIzOSAyNSA1MgoyNyA2MCAyMSAxNjIgLTE1IDMwMiAtMjE1IDY0OCAtNDQ1IDc3MCAtMTE4IDYzIC0zNDEgMTEwIC02NDcgMTM3IC0xODEgMTYKLTQ3MyAxOCAtNTY3IDR6Ii8+CjxwYXRoIGQ9Ik0xODQ1IDg5MzMgYy0xNzggLTEzIC01ODcgLTg2IC04MDUgLTE0NCAtNDQ1IC0xMTggLTU4MiAtMTk5IC03MzYKLTQzNCAtMTAyIC0xNTcgLTE1MiAtMzA4IC0xNjEgLTQ4NSAtOCAtMTcxIDIyIC0yNzMgMTA3IC0zNTggOTEgLTkwIDI0MSAtMTA4CjM3MSAtNDMgMzcgMTggMTA3IDYzIDE1NSA5OSA4NyA2NCA0MjMgMzk0IDgxNCA3OTggMjE5IDIyNSAzMzEgMzIxIDUzOSA0NTgKbDE1NCAxMDEgLTQ5IDcgYy01MCA2IC0zMDAgNyAtMzg5IDF6Ii8+CjxwYXRoIGQ9Ik0zODUzIDg2MDMgYy0xNjEgLTE1NSAtNTc0IC03NzQgLTc0NSAtMTExOCAtMjExIC00MjEgLTIxNyAtNjM4IC0yMgotODQ0IDEyOCAtMTM3IDI0NiAtMTc1IDQxNCAtMTM1IDE0NyAzNCAyOTEgMTI3IDUxNSAzMzIgbDE0MiAxMzAgNiAxMzggYzIzCjQ3NyAtOSA3MzIgLTE2NSAxMzI3IC0zNCAxMzAgLTY1IDIzNyAtNjkgMjM3IC0zIDAgLTM4IC0zMCAtNzYgLTY3eiIvPgo8cGF0aCBkPSJNMjgzMSA4NDY0IGMtMTM0IC0xNiAtMjM0IC00MyAtMzUxIC05MyAtMzI3IC0xNDEgLTY5MSAtNDY5IC04ODEKLTc5MyAtMTA2IC0xODAgLTE2MSAtMzgwIC0xMzkgLTUwNiAxNSAtODYgMzggLTEzMyAxMTQgLTIyOCA4NCAtMTA0IDI4NSAtMjk4CjM2NCAtMzUxIDEzNyAtOTIgMjQyIC04MCAzNjAgMzggMTYxIDE2MSAyODIgNDY1IDM4NiA5NjkgODUgNDExIDE2NiA2ODIgMjYxCjg3MCBsNTUgMTEwIC0yNyAtMSBjLTE2IC0xIC03OSAtNyAtMTQyIC0xNXoiLz4KPHBhdGggZD0iTTQ1MjYgNzk0OCBjLTQgLTEwMSAtMTEgLTI4MCAtMTYgLTM5OCAtMjggLTYxNiAtNzQgLTc2NyAtMjc5IC05MjAKLTMzIC0yNSAtNjEgLTQ4IC02MSAtNTEgMCAtNCA2NCAtOSAxNDMgLTEyIDE2MCAtNiAyMzEgLTIyIDM2MiAtODUgNTc3IC0yNzgKOTUxIC0xMjI3IDEwNjAgLTI2OTAgMjAgLTI3NiAzNyAtODExIDMzIC0xMDY4IGwtMyAtMjEyIC0zMDEgMzM3IGMtNjUwIDcyNAotMTAzMCAxMDk2IC0xNDI5IDEzOTYgLTU2MyA0MjQgLTEwMTYgNTYxIC0xNTE0IDQ1OSAtNDIgLTkgLTEzOSAtMzcgLTIxNiAtNjQKLTYzNSAtMjIwIC03ODIgLTI2NSAtMTAxNyAtMzE1IC0xMjcgLTI3IC0xNjggLTQyIC0xNjggLTYxIDAgLTE4IDMyIC0yMyAyNDYKLTM0IDI4MyAtMTQgNDg2IC01MSA3NTMgLTEzOSA0MjYgLTE0MSA4NzAgLTQwNSAxMzMxIC03OTEgNDk3IC00MTYgMTI2NSAtOTI2CjE4NDAgLTEyMjMgOTYgLTUwIDIwOCAtMTEzIDI0OCAtMTM5IDMwOCAtMjA2IDQ3NiAtNDgzIDU0OCAtODk4IDExIC02OCAxOAotMjAwIDI0IC00NjAgNSAtMjM2IDEyIC0zODAgMjAgLTQwOCAzMyAtMTEzIDE3NCAtMTcxIDQxOCAtMTcyIGwxMDIgMCAwIDE2OApjMCAzMTIgLTE3IDQyOCAtMTM1IDkxMiAtMTUwIDYxNyAtMjIwIDk1OCAtMjY3IDEzMDAgLTE5IDE0MCAtMjIgMjEwIC0yMyA0NjAKMCAyNjcgMiAzMDcgMjMgNDI1IDY1IDM1OSAyMDYgNjc2IDQ2OSAxMDUyIDIwMyAyOTEgNDU5IDU5NSA5NjcgMTE1MiA0NTggNTAxCjYyNCA2OTAgNzgwIDg4OSAyMzUgMzAwIDM1OSA1NDEgNDMxIDgzMiA5IDM2IDE4IDczIDIxIDgzIDUgMTQgLTEgMTcgLTM4IDE3Ci04MyAwIC0yNzMgLTI5IC0zNjMgLTU1IC0yNzggLTgxIC05NTIgLTQxMyAtMTMzNSAtNjU3IC01MTYgLTMzMCAtODU1IC02OTkKLTEwMDUgLTEwOTYgLTQ4IC0xMjkgLTc0IC0yNDIgLTEwNiAtNDU3IC0zNCAtMjQwIC02MCAtMzUyIC05OCAtNDM5IGwtMjggLTYxCi02IDE5NSBjLTEwIDMxMCAtNTAgNjEwIC0xNDggMTA5MCAtMTMyIDY0OSAtMjI2IDEyMjIgLTI1NCAxNTQzIGwtNyA3NyAtMTMxCi0yIGMtMTI1IC0yIC0xMzUgLTEgLTE4MiAyNCAtNjAgMzIgLTE1MSAxMjQgLTI3MCAyNzMgLTEzMSAxNjUgLTIyOCAyNjggLTMyMAozNDAgLTQ2IDM2IC04NSA2NSAtODggNjUgLTIgMCAtNyAtODIgLTExIC0xODJ6Ii8+CjwvZz4KPC9zdmc+Cg=="/>
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
          <symbol clip_to_extent="1" alpha="1" name="@2@1" type="line" force_rhr="0">
            <layer class="SimpleLine" locked="0" pass="0" enabled="1">
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" alpha="1" name="3" type="fill" force_rhr="0">
        <layer class="ShapeburstFill" locked="0" pass="0" enabled="1">
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
  <labeling type="rule-based">
    <rules key="{7ed8990a-f96e-456d-b2da-23f7823c879d}">
      <rule key="{ce819559-9395-4865-9644-67b4a977edc9}" filter=" &quot;surfacecategory&quot;  =  'FLO' ">
        <settings calloutType="simple">
          <text-style useSubstitutions="0" fontFamily="MS Shell Dlg 2" fontSize="8" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" namedStyle="Normal" fontSizeUnit="Point" fontCapitals="0" fontItalic="0" isExpression="0" fontWordSpacing="0" fontStrikeout="0" textOrientation="horizontal" blendMode="0" multilineHeight="1" fontUnderline="0" textColor="51,131,44,255" fieldName="scientificname" previewBkgrdColor="255,255,255,255" fontKerning="1" fontWeight="50" fontLetterSpacing="0">
            <text-buffer bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferDraw="1" bufferNoFill="1"/>
            <background shapeDraw="0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeOffsetX="0" shapeRadiiX="0" shapeBorderWidth="0" shapeFillColor="255,255,255,255" shapeRadiiY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeRadiiUnit="MM" shapeSizeY="0" shapeType="0" shapeRotation="0" shapeSizeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeJoinStyle="64" shapeBlendMode="0" shapeSVGFile="" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeOpacity="1" shapeOffsetY="0">
              <symbol clip_to_extent="1" alpha="1" name="markerSymbol" type="marker" force_rhr="0">
                <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
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
            <shadow shadowOpacity="0.7" shadowOffsetAngle="135" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowBlendMode="6" shadowUnder="0" shadowRadiusAlphaOnly="0" shadowDraw="0" shadowRadiusUnit="MM" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowRadius="1.5" shadowScale="100" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
            <dd_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format leftDirectionSymbol="&lt;" placeDirectionSymbol="0" formatNumbers="0" plussign="0" rightDirectionSymbol=">" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" autoWrapLength="0" reverseDirectionSymbol="0" decimals="3" multilineAlign="0" wrapChar=""/>
          <placement quadOffset="4" maxCurvedCharAngleIn="25" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" priority="5" geometryGeneratorEnabled="0" yOffset="0" centroidWhole="0" placementFlags="10" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" repeatDistance="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" xOffset="0" overrunDistance="0" fitInPolygonOnly="0" overrunDistanceUnit="MM" centroidInside="0" distUnits="MM" geometryGeneratorType="PointGeometry" layerType="PolygonGeometry" offsetType="0" placement="0" repeatDistanceUnits="MM" dist="0" rotationAngle="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM"/>
          <rendering displayAll="0" upsidedownLabels="0" obstacle="1" scaleMin="0" fontLimitPixelSize="0" fontMaxPixelSize="10000" minFeatureSize="0" maxNumLabels="2000" fontMinPixelSize="3" mergeLines="0" zIndex="0" obstacleType="0" labelPerPart="0" drawLabels="1" scaleVisibility="0" scaleMax="0" limitNumLabels="0" obstacleFactor="1"/>
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
              <Option value="&lt;symbol clip_to_extent=&quot;1&quot; alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; locked=&quot;0&quot; pass=&quot;0&quot; enabled=&quot;1&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
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
      </rule>
      <rule key="{5eb1e256-95b0-49c1-a182-51df94837c17}" filter=" &quot;surfacecategory&quot;  =  'HAB' ">
        <settings calloutType="simple">
          <text-style useSubstitutions="0" fontFamily="MS Shell Dlg 2" fontSize="8" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" namedStyle="Normal" fontSizeUnit="Point" fontCapitals="0" fontItalic="0" isExpression="0" fontWordSpacing="0" fontStrikeout="0" textOrientation="horizontal" blendMode="0" multilineHeight="1" fontUnderline="0" textColor="227,26,28,255" fieldName="habitatname" previewBkgrdColor="255,255,255,255" fontKerning="1" fontWeight="50" fontLetterSpacing="0">
            <text-buffer bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferDraw="1" bufferNoFill="1"/>
            <background shapeDraw="0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeOffsetX="0" shapeRadiiX="0" shapeBorderWidth="0" shapeFillColor="255,255,255,255" shapeRadiiY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeRadiiUnit="MM" shapeSizeY="0" shapeType="0" shapeRotation="0" shapeSizeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeJoinStyle="64" shapeBlendMode="0" shapeSVGFile="" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeOpacity="1" shapeOffsetY="0">
              <symbol clip_to_extent="1" alpha="1" name="markerSymbol" type="marker" force_rhr="0">
                <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
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
                      <Option value="" name="name" type="QString"/>
                      <Option name="properties"/>
                      <Option value="collection" name="type" type="QString"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOpacity="0.7" shadowOffsetAngle="135" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowBlendMode="6" shadowUnder="0" shadowRadiusAlphaOnly="0" shadowDraw="0" shadowRadiusUnit="MM" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowRadius="1.5" shadowScale="100" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
            <dd_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format leftDirectionSymbol="&lt;" placeDirectionSymbol="0" formatNumbers="0" plussign="0" rightDirectionSymbol=">" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" autoWrapLength="0" reverseDirectionSymbol="0" decimals="3" multilineAlign="0" wrapChar=""/>
          <placement quadOffset="4" maxCurvedCharAngleIn="25" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" priority="5" geometryGeneratorEnabled="0" yOffset="0" centroidWhole="0" placementFlags="10" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" repeatDistance="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" xOffset="0" overrunDistance="0" fitInPolygonOnly="0" overrunDistanceUnit="MM" centroidInside="0" distUnits="MM" geometryGeneratorType="PointGeometry" layerType="PolygonGeometry" offsetType="0" placement="0" repeatDistanceUnits="MM" dist="0" rotationAngle="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" offsetUnits="MM"/>
          <rendering displayAll="0" upsidedownLabels="0" obstacle="1" scaleMin="0" fontLimitPixelSize="0" fontMaxPixelSize="10000" minFeatureSize="0" maxNumLabels="2000" fontMinPixelSize="3" mergeLines="0" zIndex="0" obstacleType="0" labelPerPart="0" drawLabels="1" scaleVisibility="0" scaleMax="0" limitNumLabels="0" obstacleFactor="1"/>
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
              <Option value="&lt;symbol clip_to_extent=&quot;1&quot; alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; locked=&quot;0&quot; pass=&quot;0&quot; enabled=&quot;1&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
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
      </rule>
    </rules>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>2</layerGeometryType>
</qgis>
