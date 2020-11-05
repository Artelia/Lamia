<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyLocal="1" maxScale="0" version="3.10.6-A Coruña" simplifyDrawingTol="1" simplifyDrawingHints="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" minScale="1e+08" labelsEnabled="1" simplifyAlgorithm="0" simplifyMaxScale="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="RuleRenderer" enableorderby="0" symbollevels="1" forceraster="0">
    <rules key="{814f4a1d-ecf8-4ab4-af4f-b8f84c22d0bd}">
      <rule key="{fa0d3033-37e3-409e-8d76-755c28454d6b}" filter=" $length &lt; 0.1">
        <rule key="{04751dbd-23be-4734-b884-3638cd9b7a71}" filter="&quot;deficiencycategory&quot; = 'EQP'" label="Etat des équipements (id equipement)">
          <rule key="{4da501d8-e5eb-4b40-b835-1d9dc5866b1e}" filter="&quot;gravity&quot; = '0'" symbol="0" label="Gravité : 0"/>
          <rule key="{d16f1327-2754-4ab4-8831-4bf842ea24d3}" filter="&quot;gravity&quot; = '1'" symbol="1" label="Gravité : 1"/>
          <rule key="{bb70b1e6-9fad-4143-b9d2-a14340d5fef3}" filter="&quot;gravity&quot; = '2'" symbol="2" label="Gravité : 2"/>
          <rule key="{fcb4df14-40ab-4159-96e3-57a2be1b1140}" filter="&quot;gravity&quot; = '3'" symbol="3" label="Gravité : 3"/>
          <rule key="{859985df-ec09-4177-9185-5ae2b10ad263}" filter="&quot;gravity&quot; = '' OR &quot;gravity&quot; IS NULL" symbol="4" label="Gravité : NR"/>
        </rule>
        <rule key="{1a361c06-ab6f-40af-9f80-f793a0b12258}" filter="&quot;deficiencycategory&quot; = 'INF'" label="Desordres ponctuels (id desordre)">
          <rule key="{107d75fc-9bbe-429b-946c-2f502081289e}" filter="&quot;gravity&quot; = '0'" symbol="5" label="Gravité : 0"/>
          <rule key="{5c7726a4-0319-4691-bf51-cf626c4d67e0}" filter="&quot;gravity&quot; = '1'" symbol="6" label="Gravité : 1"/>
          <rule key="{637b40c0-3b06-4119-af3c-a06ef6ad80ae}" filter="&quot;gravity&quot; = '2'" symbol="7" label="Gravité : 2"/>
          <rule key="{80d67ee1-e22b-467e-9622-b42497b16b95}" filter="&quot;gravity&quot; = '3'" symbol="8" label="Gravité : 3"/>
          <rule key="{ca51d5c3-4200-4ac2-bbc1-016c5b6248da}" filter="&quot;gravity&quot; = '' OR &quot;gravity&quot; IS NULL" symbol="9" label="Gravité : BR"/>
        </rule>
        <rule key="{f49f47f5-eebd-45ba-b141-234f8d402c62}" filter="&quot;deficiencycategory&quot; = ''" symbol="10" label="Desordre non affecté"/>
      </rule>
      <rule key="{830c67d5-7aea-4bc5-8f87-a47209708db8}" filter="ELSE" symbol="11" label="Désordres linéaires (id désordre)">
        <rule key="{47ffba28-13c7-400a-8ed5-ddf1f8b5179b}" filter="&quot;gravity&quot; = '0'" symbol="12" label="Gravité : 0"/>
        <rule key="{fcf2ac5a-37d5-4ef7-a53c-3ebf062f4416}" filter="&quot;gravity&quot; = '1'" symbol="13" label="Gravité : 1"/>
        <rule key="{ba462ac4-b0fa-45b6-8542-9d8ee50b0405}" filter="&quot;gravity&quot; = '2'" symbol="14" label="Gravité : 2"/>
        <rule key="{28661a57-b1fe-47a1-b02b-a642052cdf72}" filter="&quot;gravity&quot; = '3'" symbol="15" label="Gravité : 3"/>
        <rule key="{bf795e48-82f6-44de-94b6-2bccd5e74af9}" filter="&quot;gravity&quot; = '' OR &quot;gravity&quot; IS NULL" symbol="16" label="Gravité : NR"/>
      </rule>
    </rules>
    <symbols>
      <symbol name="0" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@0@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="58,211,49,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="square"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="1" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@1@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,255,1,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="square"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="10" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@10@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="FontMarker">
              <prop k="angle" v="0"/>
              <prop k="chr" v="?"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="font" v="Dingbats"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="3.6"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="11" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="0" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="1.06"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="12" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="1" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="58,211,49,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.86"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="13" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="1" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,255,1,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.66"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="14" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="1" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,127,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.66"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="15" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="1" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="227,26,28,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.66"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="16" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="0" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,255,255,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.66"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@2@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,127,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="square"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="3" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@3@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="227,26,28,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="square"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="4" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@4@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,255,255,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="square"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="5" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@5@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="58,211,49,255"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="6" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@6@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,255,1,255"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="7" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@7@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,127,0,255"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="8" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@8@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="227,26,28,255"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="9" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer locked="0" enabled="1" pass="2" class="MarkerLine">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@9@0" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,255,255,255"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style previewBkgrdColor="255,255,255,255" textOrientation="horizontal" fontKerning="1" fontItalic="0" fontWordSpacing="0" fontWeight="50" multilineHeight="1" fontSize="10" textColor="0,0,0,255" blendMode="0" textOpacity="1" useSubstitutions="0" fontFamily="MS Shell Dlg 2" fontStrikeout="0" fontSizeUnit="Point" isExpression="1" fontUnderline="0" namedStyle="Normal" fontLetterSpacing="0" fontCapitals="0" fieldName="CASE WHEN  &quot;deficiencycategory&quot; = 'EQP' THEN   &quot;id_equipment&quot;  ELSE   &quot;id_deficiency&quot;   END" fontSizeMapUnitScale="3x:0,0,0,0,0,0">
        <text-buffer bufferSizeUnits="MM" bufferDraw="1" bufferNoFill="1" bufferOpacity="1" bufferSize="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferBlendMode="0"/>
        <background shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeRotationType="0" shapeBorderWidth="0" shapeSizeUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeFillColor="255,255,255,255" shapeOpacity="1" shapeSizeY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeRadiiY="0" shapeBorderColor="128,128,128,255" shapeSizeType="0" shapeRadiiUnit="MM" shapeOffsetUnit="MM" shapeOffsetX="0" shapeOffsetY="0" shapeSVGFile="" shapeJoinStyle="64" shapeBlendMode="0" shapeDraw="0" shapeRadiiX="0" shapeRotation="0">
          <symbol name="markerSymbol" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="190,178,151,255"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowRadius="1.5" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowRadiusUnit="MM" shadowOffsetAngle="135" shadowUnder="0" shadowOffsetUnit="MM" shadowScale="100" shadowOffsetGlobal="1" shadowBlendMode="6" shadowOpacity="0.7" shadowOffsetDist="1"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" wrapChar="" autoWrapLength="0" formatNumbers="0" plussign="0" decimals="3" reverseDirectionSymbol="0" addDirectionSymbol="0" rightDirectionSymbol=">" multilineAlign="0"/>
      <placement xOffset="0" geometryGeneratorType="PointGeometry" placementFlags="10" placement="0" centroidWhole="0" maxCurvedCharAngleIn="25" layerType="LineGeometry" yOffset="0" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceUnit="MM" distMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorEnabled="1" geometryGenerator="CASE WHEN   $length &lt; 0.1 THEN start_point(  $geometry ) ELSE   line_interpolate_point($geometry, $length /2) END" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" distUnits="MM" priority="5" preserveRotation="1" fitInPolygonOnly="0" offsetType="0" overrunDistance="0" dist="1.1" offsetUnits="MM" maxCurvedCharAngleOut="-25" repeatDistance="0" rotationAngle="0" centroidInside="0" quadOffset="4"/>
      <rendering labelPerPart="0" fontLimitPixelSize="0" drawLabels="1" fontMaxPixelSize="10000" zIndex="0" mergeLines="0" fontMinPixelSize="3" obstacle="1" obstacleFactor="1" displayAll="1" minFeatureSize="0" scaleVisibility="0" obstacleType="0" scaleMax="0" scaleMin="0" maxNumLabels="2000" upsidedownLabels="0" limitNumLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties" type="Map">
            <Option name="Color" type="Map">
              <Option name="active" type="bool" value="true"/>
              <Option name="expression" type="QString" value="CASE WHEN  &quot;deficiencycategory&quot; ='EQP' THEN 'blue' ELSE 'black' END"/>
              <Option name="type" type="int" value="3"/>
            </Option>
          </Option>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
          <Option name="ddProperties" type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
          <Option name="drawToAllParts" type="bool" value="false"/>
          <Option name="enabled" type="QString" value="0"/>
          <Option name="lineSymbol" type="QString" value="&lt;symbol name=&quot;symbol&quot; force_rhr=&quot;0&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; alpha=&quot;1&quot;>&lt;layer locked=&quot;0&quot; enabled=&quot;1&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
          <Option name="minLength" type="double" value="0"/>
          <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="minLengthUnit" type="QString" value="MM"/>
          <Option name="offsetFromAnchor" type="double" value="0"/>
          <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
          <Option name="offsetFromLabel" type="double" value="0"/>
          <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>lid_descriptionsystem</value>
    </property>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory minimumSize="0" minScaleDenominator="0" sizeScale="3x:0,0,0,0,0,0" enabled="0" penColor="#000000" diagramOrientation="Up" backgroundColor="#ffffff" scaleDependency="Area" height="15" width="15" penAlpha="255" scaleBasedVisibility="0" backgroundAlpha="255" opacity="1" lineSizeType="MM" sizeType="MM" maxScaleDenominator="1e+08" barWidth="5" labelPlacementMethod="XHeight" lineSizeScale="3x:0,0,0,0,0,0" penWidth="0" rotationOffset="270">
      <fontProperties style="" description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" field="" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="2" priority="0" obstacle="0" dist="0" linePlacementFlags="18" zIndex="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="pk_observation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_observation">
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
    <field name="datetimeobservation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="source">
      <editWidget type="TextEdit">
        <config>
          <Option/>
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
    <field name="conditionglobal">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gravity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="progression">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nextactiontype">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nextactioncomment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nextactiontypecomment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_delivery">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_deficiency">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="oh_etatvantellerie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="oh_etatvantelleriecom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqconditioncivilwork">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqconditioncivilworkcom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqhandlingtest">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqhandlingtestcom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqconditionsealing">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqconditionsealingcom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqconditionsedimentation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eqconditionsedimentationcom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="conditionglobalcom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="specificlenght">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="datetimedestructiontemp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pk_deficiency">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_deficiency">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lpk_object:1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="deficiencycategory">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="impact">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="priority">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="risks">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sector1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sector2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sector3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="side">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="position">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="deficiencytype">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="deficiencysubtype">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="deficiencysubsubtype">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="defdatetimedestruction">
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
    <field name="id_equipment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="pk_observation" index="0"/>
    <alias name="" field="id_observation" index="1"/>
    <alias name="" field="lpk_object" index="2"/>
    <alias name="" field="datetimeobservation" index="3"/>
    <alias name="" field="source" index="4"/>
    <alias name="" field="number" index="5"/>
    <alias name="" field="conditionglobal" index="6"/>
    <alias name="" field="gravity" index="7"/>
    <alias name="" field="progression" index="8"/>
    <alias name="" field="nextactiontype" index="9"/>
    <alias name="" field="nextactioncomment" index="10"/>
    <alias name="" field="nextactiontypecomment" index="11"/>
    <alias name="" field="lid_delivery" index="12"/>
    <alias name="" field="lid_deficiency" index="13"/>
    <alias name="" field="oh_etatvantellerie" index="14"/>
    <alias name="" field="oh_etatvantelleriecom" index="15"/>
    <alias name="" field="eqconditioncivilwork" index="16"/>
    <alias name="" field="eqconditioncivilworkcom" index="17"/>
    <alias name="" field="eqhandlingtest" index="18"/>
    <alias name="" field="eqhandlingtestcom" index="19"/>
    <alias name="" field="eqconditionsealing" index="20"/>
    <alias name="" field="eqconditionsealingcom" index="21"/>
    <alias name="" field="eqconditionsedimentation" index="22"/>
    <alias name="" field="eqconditionsedimentationcom" index="23"/>
    <alias name="" field="conditionglobalcom" index="24"/>
    <alias name="" field="specificlenght" index="25"/>
    <alias name="" field="datetimedestructiontemp" index="26"/>
    <alias name="" field="pk_deficiency" index="27"/>
    <alias name="" field="id_deficiency" index="28"/>
    <alias name="" field="lpk_object:1" index="29"/>
    <alias name="" field="deficiencycategory" index="30"/>
    <alias name="" field="impact" index="31"/>
    <alias name="" field="priority" index="32"/>
    <alias name="" field="risks" index="33"/>
    <alias name="" field="sector1" index="34"/>
    <alias name="" field="sector2" index="35"/>
    <alias name="" field="sector3" index="36"/>
    <alias name="" field="lid_descriptionsystem" index="37"/>
    <alias name="" field="side" index="38"/>
    <alias name="" field="position" index="39"/>
    <alias name="" field="deficiencytype" index="40"/>
    <alias name="" field="deficiencysubtype" index="41"/>
    <alias name="" field="deficiencysubsubtype" index="42"/>
    <alias name="" field="defdatetimedestruction" index="43"/>
    <alias name="" field="lpk_revision_begin" index="44"/>
    <alias name="" field="lpk_revision_end" index="45"/>
    <alias name="" field="datetimecreation" index="46"/>
    <alias name="" field="datetimedestruction" index="47"/>
    <alias name="" field="comment" index="48"/>
    <alias name="" field="id_equipment" index="49"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="pk_observation"/>
    <default expression="" applyOnUpdate="0" field="id_observation"/>
    <default expression="" applyOnUpdate="0" field="lpk_object"/>
    <default expression="" applyOnUpdate="0" field="datetimeobservation"/>
    <default expression="" applyOnUpdate="0" field="source"/>
    <default expression="" applyOnUpdate="0" field="number"/>
    <default expression="" applyOnUpdate="0" field="conditionglobal"/>
    <default expression="" applyOnUpdate="0" field="gravity"/>
    <default expression="" applyOnUpdate="0" field="progression"/>
    <default expression="" applyOnUpdate="0" field="nextactiontype"/>
    <default expression="" applyOnUpdate="0" field="nextactioncomment"/>
    <default expression="" applyOnUpdate="0" field="nextactiontypecomment"/>
    <default expression="" applyOnUpdate="0" field="lid_delivery"/>
    <default expression="" applyOnUpdate="0" field="lid_deficiency"/>
    <default expression="" applyOnUpdate="0" field="oh_etatvantellerie"/>
    <default expression="" applyOnUpdate="0" field="oh_etatvantelleriecom"/>
    <default expression="" applyOnUpdate="0" field="eqconditioncivilwork"/>
    <default expression="" applyOnUpdate="0" field="eqconditioncivilworkcom"/>
    <default expression="" applyOnUpdate="0" field="eqhandlingtest"/>
    <default expression="" applyOnUpdate="0" field="eqhandlingtestcom"/>
    <default expression="" applyOnUpdate="0" field="eqconditionsealing"/>
    <default expression="" applyOnUpdate="0" field="eqconditionsealingcom"/>
    <default expression="" applyOnUpdate="0" field="eqconditionsedimentation"/>
    <default expression="" applyOnUpdate="0" field="eqconditionsedimentationcom"/>
    <default expression="" applyOnUpdate="0" field="conditionglobalcom"/>
    <default expression="" applyOnUpdate="0" field="specificlenght"/>
    <default expression="" applyOnUpdate="0" field="datetimedestructiontemp"/>
    <default expression="" applyOnUpdate="0" field="pk_deficiency"/>
    <default expression="" applyOnUpdate="0" field="id_deficiency"/>
    <default expression="" applyOnUpdate="0" field="lpk_object:1"/>
    <default expression="" applyOnUpdate="0" field="deficiencycategory"/>
    <default expression="" applyOnUpdate="0" field="impact"/>
    <default expression="" applyOnUpdate="0" field="priority"/>
    <default expression="" applyOnUpdate="0" field="risks"/>
    <default expression="" applyOnUpdate="0" field="sector1"/>
    <default expression="" applyOnUpdate="0" field="sector2"/>
    <default expression="" applyOnUpdate="0" field="sector3"/>
    <default expression="" applyOnUpdate="0" field="lid_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="side"/>
    <default expression="" applyOnUpdate="0" field="position"/>
    <default expression="" applyOnUpdate="0" field="deficiencytype"/>
    <default expression="" applyOnUpdate="0" field="deficiencysubtype"/>
    <default expression="" applyOnUpdate="0" field="deficiencysubsubtype"/>
    <default expression="" applyOnUpdate="0" field="defdatetimedestruction"/>
    <default expression="" applyOnUpdate="0" field="lpk_revision_begin"/>
    <default expression="" applyOnUpdate="0" field="lpk_revision_end"/>
    <default expression="" applyOnUpdate="0" field="datetimecreation"/>
    <default expression="" applyOnUpdate="0" field="datetimedestruction"/>
    <default expression="" applyOnUpdate="0" field="comment"/>
    <default expression="" applyOnUpdate="0" field="id_equipment"/>
  </defaults>
  <constraints>
    <constraint constraints="0" field="pk_observation" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="id_observation" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="lpk_object" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="datetimeobservation" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="source" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="number" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="conditionglobal" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="gravity" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="progression" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="nextactiontype" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="nextactioncomment" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="nextactiontypecomment" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="lid_delivery" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="lid_deficiency" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="oh_etatvantellerie" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="oh_etatvantelleriecom" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqconditioncivilwork" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqconditioncivilworkcom" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqhandlingtest" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqhandlingtestcom" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqconditionsealing" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqconditionsealingcom" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqconditionsedimentation" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="eqconditionsedimentationcom" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="conditionglobalcom" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="specificlenght" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="datetimedestructiontemp" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="pk_deficiency" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="id_deficiency" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="lpk_object:1" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="deficiencycategory" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="impact" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="priority" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="risks" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="sector1" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="sector2" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="sector3" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="lid_descriptionsystem" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="side" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="position" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="deficiencytype" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="deficiencysubtype" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="deficiencysubsubtype" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="defdatetimedestruction" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="lpk_revision_begin" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="lpk_revision_end" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="datetimecreation" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="datetimedestruction" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="comment" unique_strength="0" exp_strength="0" notnull_strength="0"/>
    <constraint constraints="0" field="id_equipment" unique_strength="0" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="pk_observation"/>
    <constraint desc="" exp="" field="id_observation"/>
    <constraint desc="" exp="" field="lpk_object"/>
    <constraint desc="" exp="" field="datetimeobservation"/>
    <constraint desc="" exp="" field="source"/>
    <constraint desc="" exp="" field="number"/>
    <constraint desc="" exp="" field="conditionglobal"/>
    <constraint desc="" exp="" field="gravity"/>
    <constraint desc="" exp="" field="progression"/>
    <constraint desc="" exp="" field="nextactiontype"/>
    <constraint desc="" exp="" field="nextactioncomment"/>
    <constraint desc="" exp="" field="nextactiontypecomment"/>
    <constraint desc="" exp="" field="lid_delivery"/>
    <constraint desc="" exp="" field="lid_deficiency"/>
    <constraint desc="" exp="" field="oh_etatvantellerie"/>
    <constraint desc="" exp="" field="oh_etatvantelleriecom"/>
    <constraint desc="" exp="" field="eqconditioncivilwork"/>
    <constraint desc="" exp="" field="eqconditioncivilworkcom"/>
    <constraint desc="" exp="" field="eqhandlingtest"/>
    <constraint desc="" exp="" field="eqhandlingtestcom"/>
    <constraint desc="" exp="" field="eqconditionsealing"/>
    <constraint desc="" exp="" field="eqconditionsealingcom"/>
    <constraint desc="" exp="" field="eqconditionsedimentation"/>
    <constraint desc="" exp="" field="eqconditionsedimentationcom"/>
    <constraint desc="" exp="" field="conditionglobalcom"/>
    <constraint desc="" exp="" field="specificlenght"/>
    <constraint desc="" exp="" field="datetimedestructiontemp"/>
    <constraint desc="" exp="" field="pk_deficiency"/>
    <constraint desc="" exp="" field="id_deficiency"/>
    <constraint desc="" exp="" field="lpk_object:1"/>
    <constraint desc="" exp="" field="deficiencycategory"/>
    <constraint desc="" exp="" field="impact"/>
    <constraint desc="" exp="" field="priority"/>
    <constraint desc="" exp="" field="risks"/>
    <constraint desc="" exp="" field="sector1"/>
    <constraint desc="" exp="" field="sector2"/>
    <constraint desc="" exp="" field="sector3"/>
    <constraint desc="" exp="" field="lid_descriptionsystem"/>
    <constraint desc="" exp="" field="side"/>
    <constraint desc="" exp="" field="position"/>
    <constraint desc="" exp="" field="deficiencytype"/>
    <constraint desc="" exp="" field="deficiencysubtype"/>
    <constraint desc="" exp="" field="deficiencysubsubtype"/>
    <constraint desc="" exp="" field="defdatetimedestruction"/>
    <constraint desc="" exp="" field="lpk_revision_begin"/>
    <constraint desc="" exp="" field="lpk_revision_end"/>
    <constraint desc="" exp="" field="datetimecreation"/>
    <constraint desc="" exp="" field="datetimedestruction"/>
    <constraint desc="" exp="" field="comment"/>
    <constraint desc="" exp="" field="id_equipment"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="&quot;deficiencycategory&quot;" sortOrder="0">
    <columns>
      <column name="pk_observation" hidden="0" type="field" width="-1"/>
      <column name="id_observation" hidden="0" type="field" width="-1"/>
      <column name="lpk_object" hidden="0" type="field" width="-1"/>
      <column name="datetimeobservation" hidden="0" type="field" width="-1"/>
      <column name="source" hidden="0" type="field" width="-1"/>
      <column name="number" hidden="0" type="field" width="-1"/>
      <column name="conditionglobal" hidden="0" type="field" width="-1"/>
      <column name="gravity" hidden="0" type="field" width="-1"/>
      <column name="progression" hidden="0" type="field" width="-1"/>
      <column name="nextactiontype" hidden="0" type="field" width="-1"/>
      <column name="nextactioncomment" hidden="0" type="field" width="-1"/>
      <column name="nextactiontypecomment" hidden="0" type="field" width="-1"/>
      <column name="lid_delivery" hidden="0" type="field" width="-1"/>
      <column name="lid_deficiency" hidden="0" type="field" width="-1"/>
      <column name="oh_etatvantellerie" hidden="0" type="field" width="-1"/>
      <column name="oh_etatvantelleriecom" hidden="0" type="field" width="-1"/>
      <column name="eqconditioncivilwork" hidden="0" type="field" width="-1"/>
      <column name="eqconditioncivilworkcom" hidden="0" type="field" width="-1"/>
      <column name="eqhandlingtest" hidden="0" type="field" width="-1"/>
      <column name="eqhandlingtestcom" hidden="0" type="field" width="-1"/>
      <column name="eqconditionsealing" hidden="0" type="field" width="-1"/>
      <column name="eqconditionsealingcom" hidden="0" type="field" width="-1"/>
      <column name="eqconditionsedimentation" hidden="0" type="field" width="-1"/>
      <column name="eqconditionsedimentationcom" hidden="0" type="field" width="-1"/>
      <column name="conditionglobalcom" hidden="0" type="field" width="-1"/>
      <column name="specificlenght" hidden="0" type="field" width="-1"/>
      <column name="datetimedestructiontemp" hidden="0" type="field" width="-1"/>
      <column name="pk_deficiency" hidden="0" type="field" width="-1"/>
      <column name="id_deficiency" hidden="0" type="field" width="-1"/>
      <column name="lpk_object:1" hidden="0" type="field" width="-1"/>
      <column name="deficiencycategory" hidden="0" type="field" width="-1"/>
      <column name="impact" hidden="0" type="field" width="-1"/>
      <column name="priority" hidden="0" type="field" width="-1"/>
      <column name="risks" hidden="0" type="field" width="-1"/>
      <column name="sector1" hidden="0" type="field" width="-1"/>
      <column name="sector2" hidden="0" type="field" width="-1"/>
      <column name="sector3" hidden="0" type="field" width="-1"/>
      <column name="lid_descriptionsystem" hidden="0" type="field" width="180"/>
      <column name="side" hidden="0" type="field" width="-1"/>
      <column name="position" hidden="0" type="field" width="-1"/>
      <column name="deficiencytype" hidden="0" type="field" width="-1"/>
      <column name="deficiencysubtype" hidden="0" type="field" width="-1"/>
      <column name="deficiencysubsubtype" hidden="0" type="field" width="-1"/>
      <column name="defdatetimedestruction" hidden="0" type="field" width="-1"/>
      <column name="lpk_revision_begin" hidden="0" type="field" width="-1"/>
      <column name="lpk_revision_end" hidden="0" type="field" width="-1"/>
      <column name="datetimecreation" hidden="0" type="field" width="-1"/>
      <column name="datetimedestruction" hidden="0" type="field" width="-1"/>
      <column name="comment" hidden="0" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
      <column name="id_equipment" hidden="0" type="field" width="-1"/>
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
    <field name="comment" editable="1"/>
    <field name="conditionglobal" editable="1"/>
    <field name="conditionglobalcom" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimedestructiontemp" editable="1"/>
    <field name="datetimeobservation" editable="1"/>
    <field name="defdatetimedestruction" editable="1"/>
    <field name="deficiencycategory" editable="1"/>
    <field name="deficiencysubsubtype" editable="1"/>
    <field name="deficiencysubtype" editable="1"/>
    <field name="deficiencytype" editable="1"/>
    <field name="eqconditioncivilwork" editable="1"/>
    <field name="eqconditioncivilworkcom" editable="1"/>
    <field name="eqconditionsealing" editable="1"/>
    <field name="eqconditionsealingcom" editable="1"/>
    <field name="eqconditionsedimentation" editable="1"/>
    <field name="eqconditionsedimentationcom" editable="1"/>
    <field name="eqhandlingtest" editable="1"/>
    <field name="eqhandlingtestcom" editable="1"/>
    <field name="gravity" editable="1"/>
    <field name="id_deficiency" editable="1"/>
    <field name="id_equipment" editable="1"/>
    <field name="id_observation" editable="1"/>
    <field name="impact" editable="1"/>
    <field name="lid_deficiency" editable="1"/>
    <field name="lid_delivery" editable="1"/>
    <field name="lid_descriptionsystem" editable="1"/>
    <field name="lpk_object" editable="1"/>
    <field name="lpk_object:1" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="nextactioncomment" editable="1"/>
    <field name="nextactiontype" editable="1"/>
    <field name="nextactiontypecomment" editable="1"/>
    <field name="number" editable="1"/>
    <field name="oh_etatvantellerie" editable="1"/>
    <field name="oh_etatvantelleriecom" editable="1"/>
    <field name="pk_deficiency" editable="1"/>
    <field name="pk_observation" editable="1"/>
    <field name="position" editable="1"/>
    <field name="priority" editable="1"/>
    <field name="progression" editable="1"/>
    <field name="risks" editable="1"/>
    <field name="sector1" editable="1"/>
    <field name="sector2" editable="1"/>
    <field name="sector3" editable="1"/>
    <field name="side" editable="1"/>
    <field name="source" editable="1"/>
    <field name="specificlenght" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="comment"/>
    <field labelOnTop="0" name="conditionglobal"/>
    <field labelOnTop="0" name="conditionglobalcom"/>
    <field labelOnTop="0" name="datetimecreation"/>
    <field labelOnTop="0" name="datetimedestruction"/>
    <field labelOnTop="0" name="datetimedestructiontemp"/>
    <field labelOnTop="0" name="datetimeobservation"/>
    <field labelOnTop="0" name="defdatetimedestruction"/>
    <field labelOnTop="0" name="deficiencycategory"/>
    <field labelOnTop="0" name="deficiencysubsubtype"/>
    <field labelOnTop="0" name="deficiencysubtype"/>
    <field labelOnTop="0" name="deficiencytype"/>
    <field labelOnTop="0" name="eqconditioncivilwork"/>
    <field labelOnTop="0" name="eqconditioncivilworkcom"/>
    <field labelOnTop="0" name="eqconditionsealing"/>
    <field labelOnTop="0" name="eqconditionsealingcom"/>
    <field labelOnTop="0" name="eqconditionsedimentation"/>
    <field labelOnTop="0" name="eqconditionsedimentationcom"/>
    <field labelOnTop="0" name="eqhandlingtest"/>
    <field labelOnTop="0" name="eqhandlingtestcom"/>
    <field labelOnTop="0" name="gravity"/>
    <field labelOnTop="0" name="id_deficiency"/>
    <field labelOnTop="0" name="id_equipment"/>
    <field labelOnTop="0" name="id_observation"/>
    <field labelOnTop="0" name="impact"/>
    <field labelOnTop="0" name="lid_deficiency"/>
    <field labelOnTop="0" name="lid_delivery"/>
    <field labelOnTop="0" name="lid_descriptionsystem"/>
    <field labelOnTop="0" name="lpk_object"/>
    <field labelOnTop="0" name="lpk_object:1"/>
    <field labelOnTop="0" name="lpk_revision_begin"/>
    <field labelOnTop="0" name="lpk_revision_end"/>
    <field labelOnTop="0" name="nextactioncomment"/>
    <field labelOnTop="0" name="nextactiontype"/>
    <field labelOnTop="0" name="nextactiontypecomment"/>
    <field labelOnTop="0" name="number"/>
    <field labelOnTop="0" name="oh_etatvantellerie"/>
    <field labelOnTop="0" name="oh_etatvantelleriecom"/>
    <field labelOnTop="0" name="pk_deficiency"/>
    <field labelOnTop="0" name="pk_observation"/>
    <field labelOnTop="0" name="position"/>
    <field labelOnTop="0" name="priority"/>
    <field labelOnTop="0" name="progression"/>
    <field labelOnTop="0" name="risks"/>
    <field labelOnTop="0" name="sector1"/>
    <field labelOnTop="0" name="sector2"/>
    <field labelOnTop="0" name="sector3"/>
    <field labelOnTop="0" name="side"/>
    <field labelOnTop="0" name="source"/>
    <field labelOnTop="0" name="specificlenght"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>lid_descriptionsystem</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
