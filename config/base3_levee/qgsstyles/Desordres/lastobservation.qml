<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" labelsEnabled="1" styleCategories="AllStyleCategories" minScale="1e+08" simplifyDrawingHints="1" hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyDrawingTol="1" version="3.10.6-A Coruña" simplifyAlgorithm="0" simplifyMaxScale="1" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="1" enableorderby="0" type="RuleRenderer">
    <rules key="{814f4a1d-ecf8-4ab4-af4f-b8f84c22d0bd}">
      <rule filter=" $length &lt; 0.1" key="{fa0d3033-37e3-409e-8d76-755c28454d6b}">
        <rule label="Etat des équipements (id equipement)" filter="&quot;deficiencycategory&quot; = 'EQP'" key="{04751dbd-23be-4734-b884-3638cd9b7a71}">
          <rule label="Gravité : 0" filter="&quot;gravity&quot; = '0'" key="{4da501d8-e5eb-4b40-b835-1d9dc5866b1e}" symbol="0"/>
          <rule label="Gravité : 1" filter="&quot;gravity&quot; = '1'" key="{d16f1327-2754-4ab4-8831-4bf842ea24d3}" symbol="1"/>
          <rule label="Gravité : 2" filter="&quot;gravity&quot; = '2'" key="{bb70b1e6-9fad-4143-b9d2-a14340d5fef3}" symbol="2"/>
          <rule label="Gravité : 3" filter="&quot;gravity&quot; = '3'" key="{fcb4df14-40ab-4159-96e3-57a2be1b1140}" symbol="3"/>
          <rule label="Gravité : NR" filter="&quot;gravity&quot; = '' OR &quot;gravity&quot; IS NULL" key="{859985df-ec09-4177-9185-5ae2b10ad263}" symbol="4"/>
        </rule>
        <rule label="Desordres ponctuels (id desordre)" filter="&quot;deficiencycategory&quot; = 'INF'" key="{1a361c06-ab6f-40af-9f80-f793a0b12258}">
          <rule label="Gravité : 0" filter="&quot;gravity&quot; = '0'" key="{107d75fc-9bbe-429b-946c-2f502081289e}" symbol="5"/>
          <rule label="Gravité : 1" filter="&quot;gravity&quot; = '1'" key="{5c7726a4-0319-4691-bf51-cf626c4d67e0}" symbol="6"/>
          <rule label="Gravité : 2" filter="&quot;gravity&quot; = '2'" key="{637b40c0-3b06-4119-af3c-a06ef6ad80ae}" symbol="7"/>
          <rule label="Gravité : 3" filter="&quot;gravity&quot; = '3'" key="{80d67ee1-e22b-467e-9622-b42497b16b95}" symbol="8"/>
          <rule label="Gravité : BR" filter="&quot;gravity&quot; = '' OR &quot;gravity&quot; IS NULL" key="{ca51d5c3-4200-4ac2-bbc1-016c5b6248da}" symbol="9"/>
        </rule>
        <rule label="Desordre non affecté" filter="&quot;deficiencycategory&quot; = ''" key="{f49f47f5-eebd-45ba-b141-234f8d402c62}" symbol="10"/>
      </rule>
      <rule label="Désordres linéaires (id désordre)" filter=" $length > 0.1" key="{830c67d5-7aea-4bc5-8f87-a47209708db8}" symbol="11">
        <rule label="Gravité : 0" filter="&quot;gravity&quot; = '0'" key="{47ffba28-13c7-400a-8ed5-ddf1f8b5179b}" symbol="12"/>
        <rule label="Gravité : 1" filter="&quot;gravity&quot; = '1'" key="{fcf2ac5a-37d5-4ef7-a53c-3ebf062f4416}" symbol="13"/>
        <rule label="Gravité : 2" filter="&quot;gravity&quot; = '2'" key="{ba462ac4-b0fa-45b6-8542-9d8ee50b0405}" symbol="14"/>
        <rule label="Gravité : 3" filter="&quot;gravity&quot; = '3'" key="{28661a57-b1fe-47a1-b02b-a642052cdf72}" symbol="15"/>
        <rule label="Gravité : NR" filter="&quot;gravity&quot; = '' OR &quot;gravity&quot; IS NULL" key="{bf795e48-82f6-44de-94b6-2bccd5e74af9}" symbol="16"/>
      </rule>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" name="0" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@0@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="58,211,49,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="1" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@1@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="255,255,1,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="10" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@10@0" force_rhr="0" alpha="1" type="marker">
            <layer class="FontMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="?" k="chr"/>
              <prop v="0,0,0,255" k="color"/>
              <prop v="Dingbats" k="font"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="3.6" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol clip_to_extent="1" name="11" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.06" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="12" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="0" pass="1" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="58,211,49,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.86" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="13" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="0" pass="1" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.66" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="14" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="0" pass="1" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,127,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.66" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="15" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="0" pass="1" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="227,26,28,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.66" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="16" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.66" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="2" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@2@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="255,127,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="3" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@3@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="227,26,28,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="4" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@4@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="255,255,255,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="5" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@5@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="58,211,49,255" k="color"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="6" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@6@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="255,255,1,255" k="color"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="7" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@7@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="255,127,0,255" k="color"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="8" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@8@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="227,26,28,255" k="color"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="9" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="2" enabled="1">
          <prop v="4" k="average_angle_length"/>
          <prop v="3x:0,0,0,0,0,0" k="average_angle_map_unit_scale"/>
          <prop v="MM" k="average_angle_unit"/>
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="firstvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@9@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="255,255,255,255" k="color"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
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
      <text-style fontCapitals="0" blendMode="0" multilineHeight="1" fieldName="CASE WHEN  &quot;deficiencycategory&quot; = 'EQP' THEN   &quot;id_equipment&quot;  ELSE   &quot;id_deficiency&quot;   END" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontItalic="0" fontUnderline="0" previewBkgrdColor="255,255,255,255" fontKerning="1" fontFamily="MS Shell Dlg 2" textOrientation="horizontal" useSubstitutions="0" fontLetterSpacing="0" textColor="0,0,0,255" fontSizeUnit="Point" fontWordSpacing="0" namedStyle="Normal" fontSize="10" fontStrikeout="0" fontWeight="50" textOpacity="1" isExpression="1">
        <text-buffer bufferDraw="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferJoinStyle="128" bufferColor="255,255,255,255" bufferSize="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferNoFill="1" bufferOpacity="1"/>
        <background shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeOffsetX="0" shapeSizeX="0" shapeSVGFile="" shapeOffsetUnit="MM" shapeSizeUnit="MM" shapeOpacity="1" shapeRadiiX="0" shapeBorderWidth="0" shapeRadiiY="0" shapeType="0" shapeJoinStyle="64" shapeDraw="0" shapeRotation="0" shapeSizeType="0" shapeFillColor="255,255,255,255" shapeRotationType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeBlendMode="0" shapeBorderWidthUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0">
          <symbol clip_to_extent="1" name="markerSymbol" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="190,178,151,255" k="color"/>
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetDist="1" shadowUnder="0" shadowRadius="1.5" shadowDraw="0" shadowScale="100" shadowBlendMode="6" shadowRadiusAlphaOnly="0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowRadiusUnit="MM" shadowOffsetAngle="135"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format multilineAlign="0" leftDirectionSymbol="&lt;" addDirectionSymbol="0" plussign="0" wrapChar="" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" placeDirectionSymbol="0" reverseDirectionSymbol="0" autoWrapLength="0" formatNumbers="0" decimals="3"/>
      <placement offsetUnits="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" yOffset="0" priority="5" overrunDistance="0" placementFlags="10" centroidInside="0" overrunDistanceUnit="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" quadOffset="4" maxCurvedCharAngleIn="25" rotationAngle="0" centroidWhole="0" repeatDistanceUnits="MM" distUnits="MM" fitInPolygonOnly="0" maxCurvedCharAngleOut="-25" distMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" geometryGeneratorEnabled="1" xOffset="0" preserveRotation="1" geometryGenerator="CASE WHEN   $length &lt; 0.1 THEN start_point(  $geometry ) ELSE   line_interpolate_point($geometry, $length /2) END" placement="0" dist="1.1" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" layerType="LineGeometry" repeatDistance="0"/>
      <rendering obstacleFactor="1" obstacle="1" labelPerPart="0" fontMinPixelSize="3" scaleVisibility="0" scaleMin="0" zIndex="0" mergeLines="0" fontMaxPixelSize="10000" displayAll="1" minFeatureSize="0" drawLabels="1" maxNumLabels="2000" upsidedownLabels="0" obstacleType="0" fontLimitPixelSize="0" scaleMax="0" limitNumLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties" type="Map">
            <Option name="Color" type="Map">
              <Option value="true" name="active" type="bool"/>
              <Option value="CASE WHEN  &quot;deficiencycategory&quot; ='EQP' THEN 'blue' ELSE 'black' END" name="expression" type="QString"/>
              <Option value="3" name="type" type="int"/>
            </Option>
          </Option>
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
          <Option value="&lt;symbol clip_to_extent=&quot;1&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; alpha=&quot;1&quot; type=&quot;line&quot;>&lt;layer class=&quot;SimpleLine&quot; locked=&quot;0&quot; pass=&quot;0&quot; enabled=&quot;1&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
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
  <customproperties>
    <property value="lid_descriptionsystem" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory diagramOrientation="Up" backgroundAlpha="255" labelPlacementMethod="XHeight" barWidth="5" width="15" enabled="0" penColor="#000000" height="15" backgroundColor="#ffffff" sizeType="MM" minimumSize="0" rotationOffset="270" lineSizeType="MM" minScaleDenominator="0" scaleDependency="Area" penAlpha="255" scaleBasedVisibility="0" maxScaleDenominator="1e+08" sizeScale="3x:0,0,0,0,0,0" lineSizeScale="3x:0,0,0,0,0,0" penWidth="0" opacity="1">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" label="" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" linePlacementFlags="18" placement="2" priority="0" dist="0" obstacle="0" zIndex="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
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
    <alias name="" index="0" field="pk_observation"/>
    <alias name="" index="1" field="id_observation"/>
    <alias name="" index="2" field="lpk_object"/>
    <alias name="" index="3" field="datetimeobservation"/>
    <alias name="" index="4" field="source"/>
    <alias name="" index="5" field="number"/>
    <alias name="" index="6" field="conditionglobal"/>
    <alias name="" index="7" field="gravity"/>
    <alias name="" index="8" field="progression"/>
    <alias name="" index="9" field="nextactiontype"/>
    <alias name="" index="10" field="nextactioncomment"/>
    <alias name="" index="11" field="nextactiontypecomment"/>
    <alias name="" index="12" field="lid_delivery"/>
    <alias name="" index="13" field="lid_deficiency"/>
    <alias name="" index="14" field="oh_etatvantellerie"/>
    <alias name="" index="15" field="oh_etatvantelleriecom"/>
    <alias name="" index="16" field="eqconditioncivilwork"/>
    <alias name="" index="17" field="eqconditioncivilworkcom"/>
    <alias name="" index="18" field="eqhandlingtest"/>
    <alias name="" index="19" field="eqhandlingtestcom"/>
    <alias name="" index="20" field="eqconditionsealing"/>
    <alias name="" index="21" field="eqconditionsealingcom"/>
    <alias name="" index="22" field="eqconditionsedimentation"/>
    <alias name="" index="23" field="eqconditionsedimentationcom"/>
    <alias name="" index="24" field="conditionglobalcom"/>
    <alias name="" index="25" field="specificlenght"/>
    <alias name="" index="26" field="datetimedestructiontemp"/>
    <alias name="" index="27" field="pk_deficiency"/>
    <alias name="" index="28" field="id_deficiency"/>
    <alias name="" index="29" field="lpk_object:1"/>
    <alias name="" index="30" field="deficiencycategory"/>
    <alias name="" index="31" field="impact"/>
    <alias name="" index="32" field="priority"/>
    <alias name="" index="33" field="risks"/>
    <alias name="" index="34" field="sector1"/>
    <alias name="" index="35" field="sector2"/>
    <alias name="" index="36" field="sector3"/>
    <alias name="" index="37" field="lid_descriptionsystem"/>
    <alias name="" index="38" field="side"/>
    <alias name="" index="39" field="position"/>
    <alias name="" index="40" field="deficiencytype"/>
    <alias name="" index="41" field="deficiencysubtype"/>
    <alias name="" index="42" field="deficiencysubsubtype"/>
    <alias name="" index="43" field="defdatetimedestruction"/>
    <alias name="" index="44" field="lpk_revision_begin"/>
    <alias name="" index="45" field="lpk_revision_end"/>
    <alias name="" index="46" field="datetimecreation"/>
    <alias name="" index="47" field="datetimedestruction"/>
    <alias name="" index="48" field="comment"/>
    <alias name="" index="49" field="id_equipment"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="pk_observation"/>
    <default applyOnUpdate="0" expression="" field="id_observation"/>
    <default applyOnUpdate="0" expression="" field="lpk_object"/>
    <default applyOnUpdate="0" expression="" field="datetimeobservation"/>
    <default applyOnUpdate="0" expression="" field="source"/>
    <default applyOnUpdate="0" expression="" field="number"/>
    <default applyOnUpdate="0" expression="" field="conditionglobal"/>
    <default applyOnUpdate="0" expression="" field="gravity"/>
    <default applyOnUpdate="0" expression="" field="progression"/>
    <default applyOnUpdate="0" expression="" field="nextactiontype"/>
    <default applyOnUpdate="0" expression="" field="nextactioncomment"/>
    <default applyOnUpdate="0" expression="" field="nextactiontypecomment"/>
    <default applyOnUpdate="0" expression="" field="lid_delivery"/>
    <default applyOnUpdate="0" expression="" field="lid_deficiency"/>
    <default applyOnUpdate="0" expression="" field="oh_etatvantellerie"/>
    <default applyOnUpdate="0" expression="" field="oh_etatvantelleriecom"/>
    <default applyOnUpdate="0" expression="" field="eqconditioncivilwork"/>
    <default applyOnUpdate="0" expression="" field="eqconditioncivilworkcom"/>
    <default applyOnUpdate="0" expression="" field="eqhandlingtest"/>
    <default applyOnUpdate="0" expression="" field="eqhandlingtestcom"/>
    <default applyOnUpdate="0" expression="" field="eqconditionsealing"/>
    <default applyOnUpdate="0" expression="" field="eqconditionsealingcom"/>
    <default applyOnUpdate="0" expression="" field="eqconditionsedimentation"/>
    <default applyOnUpdate="0" expression="" field="eqconditionsedimentationcom"/>
    <default applyOnUpdate="0" expression="" field="conditionglobalcom"/>
    <default applyOnUpdate="0" expression="" field="specificlenght"/>
    <default applyOnUpdate="0" expression="" field="datetimedestructiontemp"/>
    <default applyOnUpdate="0" expression="" field="pk_deficiency"/>
    <default applyOnUpdate="0" expression="" field="id_deficiency"/>
    <default applyOnUpdate="0" expression="" field="lpk_object:1"/>
    <default applyOnUpdate="0" expression="" field="deficiencycategory"/>
    <default applyOnUpdate="0" expression="" field="impact"/>
    <default applyOnUpdate="0" expression="" field="priority"/>
    <default applyOnUpdate="0" expression="" field="risks"/>
    <default applyOnUpdate="0" expression="" field="sector1"/>
    <default applyOnUpdate="0" expression="" field="sector2"/>
    <default applyOnUpdate="0" expression="" field="sector3"/>
    <default applyOnUpdate="0" expression="" field="lid_descriptionsystem"/>
    <default applyOnUpdate="0" expression="" field="side"/>
    <default applyOnUpdate="0" expression="" field="position"/>
    <default applyOnUpdate="0" expression="" field="deficiencytype"/>
    <default applyOnUpdate="0" expression="" field="deficiencysubtype"/>
    <default applyOnUpdate="0" expression="" field="deficiencysubsubtype"/>
    <default applyOnUpdate="0" expression="" field="defdatetimedestruction"/>
    <default applyOnUpdate="0" expression="" field="lpk_revision_begin"/>
    <default applyOnUpdate="0" expression="" field="lpk_revision_end"/>
    <default applyOnUpdate="0" expression="" field="datetimecreation"/>
    <default applyOnUpdate="0" expression="" field="datetimedestruction"/>
    <default applyOnUpdate="0" expression="" field="comment"/>
    <default applyOnUpdate="0" expression="" field="id_equipment"/>
  </defaults>
  <constraints>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="pk_observation"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="id_observation"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_object"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimeobservation"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="source"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="number"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="conditionglobal"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="gravity"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="progression"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="nextactiontype"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="nextactioncomment"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="nextactiontypecomment"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_delivery"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_deficiency"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="oh_etatvantellerie"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="oh_etatvantelleriecom"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqconditioncivilwork"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqconditioncivilworkcom"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqhandlingtest"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqhandlingtestcom"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqconditionsealing"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqconditionsealingcom"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqconditionsedimentation"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="eqconditionsedimentationcom"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="conditionglobalcom"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="specificlenght"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimedestructiontemp"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="pk_deficiency"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="id_deficiency"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_object:1"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="deficiencycategory"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="impact"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="priority"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="risks"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="sector1"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="sector2"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="sector3"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_descriptionsystem"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="side"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="position"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="deficiencytype"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="deficiencysubtype"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="deficiencysubsubtype"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="defdatetimedestruction"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_revision_begin"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_revision_end"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimecreation"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimedestruction"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="comment"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="id_equipment"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="pk_observation" exp=""/>
    <constraint desc="" field="id_observation" exp=""/>
    <constraint desc="" field="lpk_object" exp=""/>
    <constraint desc="" field="datetimeobservation" exp=""/>
    <constraint desc="" field="source" exp=""/>
    <constraint desc="" field="number" exp=""/>
    <constraint desc="" field="conditionglobal" exp=""/>
    <constraint desc="" field="gravity" exp=""/>
    <constraint desc="" field="progression" exp=""/>
    <constraint desc="" field="nextactiontype" exp=""/>
    <constraint desc="" field="nextactioncomment" exp=""/>
    <constraint desc="" field="nextactiontypecomment" exp=""/>
    <constraint desc="" field="lid_delivery" exp=""/>
    <constraint desc="" field="lid_deficiency" exp=""/>
    <constraint desc="" field="oh_etatvantellerie" exp=""/>
    <constraint desc="" field="oh_etatvantelleriecom" exp=""/>
    <constraint desc="" field="eqconditioncivilwork" exp=""/>
    <constraint desc="" field="eqconditioncivilworkcom" exp=""/>
    <constraint desc="" field="eqhandlingtest" exp=""/>
    <constraint desc="" field="eqhandlingtestcom" exp=""/>
    <constraint desc="" field="eqconditionsealing" exp=""/>
    <constraint desc="" field="eqconditionsealingcom" exp=""/>
    <constraint desc="" field="eqconditionsedimentation" exp=""/>
    <constraint desc="" field="eqconditionsedimentationcom" exp=""/>
    <constraint desc="" field="conditionglobalcom" exp=""/>
    <constraint desc="" field="specificlenght" exp=""/>
    <constraint desc="" field="datetimedestructiontemp" exp=""/>
    <constraint desc="" field="pk_deficiency" exp=""/>
    <constraint desc="" field="id_deficiency" exp=""/>
    <constraint desc="" field="lpk_object:1" exp=""/>
    <constraint desc="" field="deficiencycategory" exp=""/>
    <constraint desc="" field="impact" exp=""/>
    <constraint desc="" field="priority" exp=""/>
    <constraint desc="" field="risks" exp=""/>
    <constraint desc="" field="sector1" exp=""/>
    <constraint desc="" field="sector2" exp=""/>
    <constraint desc="" field="sector3" exp=""/>
    <constraint desc="" field="lid_descriptionsystem" exp=""/>
    <constraint desc="" field="side" exp=""/>
    <constraint desc="" field="position" exp=""/>
    <constraint desc="" field="deficiencytype" exp=""/>
    <constraint desc="" field="deficiencysubtype" exp=""/>
    <constraint desc="" field="deficiencysubsubtype" exp=""/>
    <constraint desc="" field="defdatetimedestruction" exp=""/>
    <constraint desc="" field="lpk_revision_begin" exp=""/>
    <constraint desc="" field="lpk_revision_end" exp=""/>
    <constraint desc="" field="datetimecreation" exp=""/>
    <constraint desc="" field="datetimedestruction" exp=""/>
    <constraint desc="" field="comment" exp=""/>
    <constraint desc="" field="id_equipment" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;deficiencycategory&quot;" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" name="pk_observation" hidden="0" type="field"/>
      <column width="-1" name="id_observation" hidden="0" type="field"/>
      <column width="-1" name="lpk_object" hidden="0" type="field"/>
      <column width="-1" name="datetimeobservation" hidden="0" type="field"/>
      <column width="-1" name="source" hidden="0" type="field"/>
      <column width="-1" name="number" hidden="0" type="field"/>
      <column width="-1" name="conditionglobal" hidden="0" type="field"/>
      <column width="-1" name="gravity" hidden="0" type="field"/>
      <column width="-1" name="progression" hidden="0" type="field"/>
      <column width="-1" name="nextactiontype" hidden="0" type="field"/>
      <column width="-1" name="nextactioncomment" hidden="0" type="field"/>
      <column width="-1" name="nextactiontypecomment" hidden="0" type="field"/>
      <column width="-1" name="lid_delivery" hidden="0" type="field"/>
      <column width="-1" name="lid_deficiency" hidden="0" type="field"/>
      <column width="-1" name="oh_etatvantellerie" hidden="0" type="field"/>
      <column width="-1" name="oh_etatvantelleriecom" hidden="0" type="field"/>
      <column width="-1" name="eqconditioncivilwork" hidden="0" type="field"/>
      <column width="-1" name="eqconditioncivilworkcom" hidden="0" type="field"/>
      <column width="-1" name="eqhandlingtest" hidden="0" type="field"/>
      <column width="-1" name="eqhandlingtestcom" hidden="0" type="field"/>
      <column width="-1" name="eqconditionsealing" hidden="0" type="field"/>
      <column width="-1" name="eqconditionsealingcom" hidden="0" type="field"/>
      <column width="-1" name="eqconditionsedimentation" hidden="0" type="field"/>
      <column width="-1" name="eqconditionsedimentationcom" hidden="0" type="field"/>
      <column width="-1" name="conditionglobalcom" hidden="0" type="field"/>
      <column width="-1" name="specificlenght" hidden="0" type="field"/>
      <column width="-1" name="datetimedestructiontemp" hidden="0" type="field"/>
      <column width="-1" name="pk_deficiency" hidden="0" type="field"/>
      <column width="-1" name="id_deficiency" hidden="0" type="field"/>
      <column width="-1" name="lpk_object:1" hidden="0" type="field"/>
      <column width="-1" name="deficiencycategory" hidden="0" type="field"/>
      <column width="-1" name="impact" hidden="0" type="field"/>
      <column width="-1" name="priority" hidden="0" type="field"/>
      <column width="-1" name="risks" hidden="0" type="field"/>
      <column width="-1" name="sector1" hidden="0" type="field"/>
      <column width="-1" name="sector2" hidden="0" type="field"/>
      <column width="-1" name="sector3" hidden="0" type="field"/>
      <column width="180" name="lid_descriptionsystem" hidden="0" type="field"/>
      <column width="-1" name="side" hidden="0" type="field"/>
      <column width="-1" name="position" hidden="0" type="field"/>
      <column width="-1" name="deficiencytype" hidden="0" type="field"/>
      <column width="-1" name="deficiencysubtype" hidden="0" type="field"/>
      <column width="-1" name="deficiencysubsubtype" hidden="0" type="field"/>
      <column width="-1" name="defdatetimedestruction" hidden="0" type="field"/>
      <column width="-1" name="lpk_revision_begin" hidden="0" type="field"/>
      <column width="-1" name="lpk_revision_end" hidden="0" type="field"/>
      <column width="-1" name="datetimecreation" hidden="0" type="field"/>
      <column width="-1" name="datetimedestruction" hidden="0" type="field"/>
      <column width="-1" name="comment" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" name="id_equipment" hidden="0" type="field"/>
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
