<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" minScale="10000" simplifyAlgorithm="0" simplifyDrawingTol="1" hasScaleBasedVisibilityFlag="1" version="3.10.0-A CoruÃ±a" styleCategories="AllStyleCategories" simplifyMaxScale="1" readOnly="0" labelsEnabled="0" simplifyLocal="1" simplifyDrawingHints="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="RuleRenderer" enableorderby="0" forceraster="0" symbollevels="0">
    <rules key="{814f4a1d-ecf8-4ab4-af4f-b8f84c22d0bd}">
      <rule key="{2dd8eb8c-4590-4a4c-bc04-b6df342c8f7e}" filter=" &quot;groupedesordre&quot; =  'NCO' " symbol="0">
        <rule label="Decrit (nca)" key="{7c5e48b5-6021-4673-9b7f-fb448bb48eed}" filter=" &quot;ncacount&quot; >0 AND &quot;ncbcount&quot; =0 AND  &quot;ncccount&quot; =0" symbol="1">
          <rule key="{9769dd1b-e072-48af-99c4-cd669c479780}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) !=  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="2"/>
          <rule key="{a6a35c7b-f67d-42a4-bea9-aee3ab0c5e32}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) =  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="3"/>
        </rule>
        <rule label="solution validee (ncb)" key="{35db32bc-bdee-41a6-a1b3-13da534f1515}" filter=" &quot;ncacount&quot; >0 AND  &quot;ncbcount&quot; >0 AND  &quot;ncccount&quot; =0" symbol="4">
          <rule key="{bea0e0f2-c698-4335-a576-7c19cc7d5186}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) !=  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="5"/>
          <rule key="{33b961ab-8f2b-464f-aeb4-15f79adc590f}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) =  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="6"/>
        </rule>
        <rule label="verification faite (ncc)" key="{b151e90a-42f9-46d1-aa82-e4151974434b}" filter=" &quot;ncacount&quot; >0 AND  &quot;ncbcount&quot; >0 AND  &quot;ncccount&quot; >0" symbol="7">
          <rule key="{a85708b2-4d01-4f9b-b307-7248a2e341cc}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) !=  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="8"/>
          <rule key="{59838e9e-462e-4d81-b1cf-83b7f8c42a41}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) =  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="9"/>
        </rule>
        <rule label="autre" key="{abf4c826-911a-4d62-95d2-86d97ba13c31}" filter="ELSE" symbol="10">
          <rule key="{d01c7025-08de-4ca6-92a4-7be20395e164}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) !=  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="11"/>
          <rule key="{00d6d039-ed3f-416d-a384-994e846d8cba}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) =  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="12"/>
        </rule>
      </rule>
      <rule key="{761ed2ca-397d-4b94-bb51-aae2104eb816}" filter="ELSE" symbol="13">
        <rule key="{3c160eed-45a9-4410-9c80-138a90202ae4}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) !=  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="14"/>
        <rule key="{439b26e4-02d6-4d94-acc2-127f03cf6e42}" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) =  &#xa;geom_to_wkt( start_point(  $geometry ))" symbol="15"/>
      </rule>
    </rules>
    <symbols>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="0">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="141,90,153,255" k="line_color"/>
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="243,166,178,255" k="line_color"/>
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="10">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="114,155,111,255" k="line_color"/>
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="11">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,255,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleLine" locked="1" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,255,0,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="12">
        <layer class="MarkerLine" locked="0" enabled="1" pass="1">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" clip_to_extent="1" force_rhr="0" alpha="1" name="@12@0">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop v="0" k="angle"/>
              <prop v="255,255,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="star" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,255,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="13">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="114,155,111,255" k="line_color"/>
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="14">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="140,140,140,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.56" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleLine" locked="1" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="140,140,140,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="1.36" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="15">
        <layer class="MarkerLine" locked="0" enabled="1" pass="1">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" clip_to_extent="1" force_rhr="0" alpha="1" name="@15@0">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop v="0" k="angle"/>
              <prop v="140,140,140,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="star" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="4" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="2">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,255,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleLine" locked="1" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,1,1,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="3">
        <layer class="MarkerLine" locked="0" enabled="1" pass="1">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" clip_to_extent="1" force_rhr="0" alpha="1" name="@3@0">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop v="0" k="angle"/>
              <prop v="255,0,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="star" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,255,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="4">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="243,166,178,255" k="line_color"/>
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="5">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,255,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleLine" locked="1" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="51,160,44,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="6">
        <layer class="MarkerLine" locked="0" enabled="1" pass="1">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" clip_to_extent="1" force_rhr="0" alpha="1" name="@6@0">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop v="0" k="angle"/>
              <prop v="51,160,44,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="star" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,255,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="7">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,127,0,255" k="line_color"/>
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="8">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,255,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleLine" locked="1" enabled="1" pass="0">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="166,206,227,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" clip_to_extent="1" force_rhr="0" alpha="1" name="9">
        <layer class="MarkerLine" locked="0" enabled="1" pass="1">
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" clip_to_extent="1" force_rhr="0" alpha="1" name="@9@0">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop v="0" k="angle"/>
              <prop v="166,206,227,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="star" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,255,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions" value="COALESCE(&quot;ID&quot;, '&lt;NULL>')"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory sizeType="MM" height="15" lineSizeType="MM" maxScaleDenominator="1e+08" scaleBasedVisibility="0" backgroundColor="#ffffff" enabled="0" scaleDependency="Area" sizeScale="3x:0,0,0,0,0,0" penWidth="0" penColor="#000000" width="15" penAlpha="255" backgroundAlpha="255" opacity="1" diagramOrientation="Up" barWidth="5" rotationOffset="270" minimumSize="0" minScaleDenominator="0" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute label="" color="#000000" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" placement="2" obstacle="0" showAll="1" dist="0" linePlacementFlags="2" zIndex="0">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="pk_desordre">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_desordre">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lpk_objet">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="groupedesordre">
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
    <field name="priorite">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="risques">
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
    <field name="detecteur">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="detecteur_com">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_marche">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pk_objet">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_objet">
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
    <field name="commentaire">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="libelle">
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
    <field name="ncacount">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ncbcount">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ncccount">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="pk_desordre" name=""/>
    <alias index="1" field="id_desordre" name=""/>
    <alias index="2" field="lpk_objet" name=""/>
    <alias index="3" field="groupedesordre" name=""/>
    <alias index="4" field="impact" name=""/>
    <alias index="5" field="priorite" name=""/>
    <alias index="6" field="risques" name=""/>
    <alias index="7" field="lid_descriptionsystem" name=""/>
    <alias index="8" field="detecteur" name=""/>
    <alias index="9" field="detecteur_com" name=""/>
    <alias index="10" field="lid_marche" name=""/>
    <alias index="11" field="pk_objet" name=""/>
    <alias index="12" field="id_objet" name=""/>
    <alias index="13" field="lpk_revision_begin" name=""/>
    <alias index="14" field="lpk_revision_end" name=""/>
    <alias index="15" field="datetimecreation" name=""/>
    <alias index="16" field="datetimemodification" name=""/>
    <alias index="17" field="datetimedestruction" name=""/>
    <alias index="18" field="commentaire" name=""/>
    <alias index="19" field="libelle" name=""/>
    <alias index="20" field="importid" name=""/>
    <alias index="21" field="importtable" name=""/>
    <alias index="22" field="ncacount" name=""/>
    <alias index="23" field="ncbcount" name=""/>
    <alias index="24" field="ncccount" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="pk_desordre"/>
    <default applyOnUpdate="0" expression="" field="id_desordre"/>
    <default applyOnUpdate="0" expression="" field="lpk_objet"/>
    <default applyOnUpdate="0" expression="" field="groupedesordre"/>
    <default applyOnUpdate="0" expression="" field="impact"/>
    <default applyOnUpdate="0" expression="" field="priorite"/>
    <default applyOnUpdate="0" expression="" field="risques"/>
    <default applyOnUpdate="0" expression="" field="lid_descriptionsystem"/>
    <default applyOnUpdate="0" expression="" field="detecteur"/>
    <default applyOnUpdate="0" expression="" field="detecteur_com"/>
    <default applyOnUpdate="0" expression="" field="lid_marche"/>
    <default applyOnUpdate="0" expression="" field="pk_objet"/>
    <default applyOnUpdate="0" expression="" field="id_objet"/>
    <default applyOnUpdate="0" expression="" field="lpk_revision_begin"/>
    <default applyOnUpdate="0" expression="" field="lpk_revision_end"/>
    <default applyOnUpdate="0" expression="" field="datetimecreation"/>
    <default applyOnUpdate="0" expression="" field="datetimemodification"/>
    <default applyOnUpdate="0" expression="" field="datetimedestruction"/>
    <default applyOnUpdate="0" expression="" field="commentaire"/>
    <default applyOnUpdate="0" expression="" field="libelle"/>
    <default applyOnUpdate="0" expression="" field="importid"/>
    <default applyOnUpdate="0" expression="" field="importtable"/>
    <default applyOnUpdate="0" expression="" field="ncacount"/>
    <default applyOnUpdate="0" expression="" field="ncbcount"/>
    <default applyOnUpdate="0" expression="" field="ncccount"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="pk_desordre" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="id_desordre" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="lpk_objet" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="groupedesordre" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="impact" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="priorite" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="risques" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="lid_descriptionsystem" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="detecteur" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="detecteur_com" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="lid_marche" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="pk_objet" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="id_objet" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="lpk_revision_begin" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="lpk_revision_end" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="datetimecreation" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="datetimemodification" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="datetimedestruction" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="commentaire" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="libelle" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="importid" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="importtable" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="ncacount" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="ncbcount" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="ncccount" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="pk_desordre"/>
    <constraint desc="" exp="" field="id_desordre"/>
    <constraint desc="" exp="" field="lpk_objet"/>
    <constraint desc="" exp="" field="groupedesordre"/>
    <constraint desc="" exp="" field="impact"/>
    <constraint desc="" exp="" field="priorite"/>
    <constraint desc="" exp="" field="risques"/>
    <constraint desc="" exp="" field="lid_descriptionsystem"/>
    <constraint desc="" exp="" field="detecteur"/>
    <constraint desc="" exp="" field="detecteur_com"/>
    <constraint desc="" exp="" field="lid_marche"/>
    <constraint desc="" exp="" field="pk_objet"/>
    <constraint desc="" exp="" field="id_objet"/>
    <constraint desc="" exp="" field="lpk_revision_begin"/>
    <constraint desc="" exp="" field="lpk_revision_end"/>
    <constraint desc="" exp="" field="datetimecreation"/>
    <constraint desc="" exp="" field="datetimemodification"/>
    <constraint desc="" exp="" field="datetimedestruction"/>
    <constraint desc="" exp="" field="commentaire"/>
    <constraint desc="" exp="" field="libelle"/>
    <constraint desc="" exp="" field="importid"/>
    <constraint desc="" exp="" field="importtable"/>
    <constraint desc="" exp="" field="ncacount"/>
    <constraint desc="" exp="" field="ncbcount"/>
    <constraint desc="" exp="" field="ncccount"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column hidden="1" type="actions" width="-1"/>
      <column hidden="0" type="field" width="-1" name="id_desordre"/>
      <column hidden="0" type="field" width="-1" name="id_objet"/>
      <column hidden="0" type="field" width="-1" name="impact"/>
      <column hidden="0" type="field" width="-1" name="priorite"/>
      <column hidden="0" type="field" width="-1" name="risques"/>
      <column hidden="0" type="field" width="-1" name="pk_desordre"/>
      <column hidden="0" type="field" width="-1" name="lpk_objet"/>
      <column hidden="0" type="field" width="-1" name="groupedesordre"/>
      <column hidden="0" type="field" width="-1" name="lid_descriptionsystem"/>
      <column hidden="0" type="field" width="-1" name="detecteur"/>
      <column hidden="0" type="field" width="-1" name="detecteur_com"/>
      <column hidden="0" type="field" width="-1" name="lid_marche"/>
      <column hidden="0" type="field" width="-1" name="pk_objet"/>
      <column hidden="0" type="field" width="-1" name="lpk_revision_begin"/>
      <column hidden="0" type="field" width="-1" name="lpk_revision_end"/>
      <column hidden="0" type="field" width="-1" name="datetimecreation"/>
      <column hidden="0" type="field" width="-1" name="datetimemodification"/>
      <column hidden="0" type="field" width="-1" name="datetimedestruction"/>
      <column hidden="0" type="field" width="-1" name="commentaire"/>
      <column hidden="0" type="field" width="-1" name="libelle"/>
      <column hidden="0" type="field" width="-1" name="importid"/>
      <column hidden="0" type="field" width="-1" name="importtable"/>
      <column hidden="0" type="field" width="-1" name="ncacount"/>
      <column hidden="0" type="field" width="-1" name="ncbcount"/>
      <column hidden="0" type="field" width="-1" name="ncccount"/>
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
    <field editable="1" name="commentaire"/>
    <field editable="1" name="datetimecreation"/>
    <field editable="1" name="datetimedestruction"/>
    <field editable="1" name="datetimemodification"/>
    <field editable="1" name="detecteur"/>
    <field editable="1" name="detecteur_com"/>
    <field editable="1" name="groupedesordre"/>
    <field editable="1" name="id_desordre"/>
    <field editable="1" name="id_objet"/>
    <field editable="1" name="impact"/>
    <field editable="1" name="importid"/>
    <field editable="1" name="importtable"/>
    <field editable="1" name="libelle"/>
    <field editable="1" name="lid_descriptionsystem"/>
    <field editable="1" name="lid_marche"/>
    <field editable="1" name="lpk_objet"/>
    <field editable="1" name="lpk_revision_begin"/>
    <field editable="1" name="lpk_revision_end"/>
    <field editable="1" name="ncacount"/>
    <field editable="1" name="ncbcount"/>
    <field editable="1" name="ncccount"/>
    <field editable="1" name="pk_desordre"/>
    <field editable="1" name="pk_objet"/>
    <field editable="1" name="priorite"/>
    <field editable="1" name="risques"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="commentaire"/>
    <field labelOnTop="0" name="datetimecreation"/>
    <field labelOnTop="0" name="datetimedestruction"/>
    <field labelOnTop="0" name="datetimemodification"/>
    <field labelOnTop="0" name="detecteur"/>
    <field labelOnTop="0" name="detecteur_com"/>
    <field labelOnTop="0" name="groupedesordre"/>
    <field labelOnTop="0" name="id_desordre"/>
    <field labelOnTop="0" name="id_objet"/>
    <field labelOnTop="0" name="impact"/>
    <field labelOnTop="0" name="importid"/>
    <field labelOnTop="0" name="importtable"/>
    <field labelOnTop="0" name="libelle"/>
    <field labelOnTop="0" name="lid_descriptionsystem"/>
    <field labelOnTop="0" name="lid_marche"/>
    <field labelOnTop="0" name="lpk_objet"/>
    <field labelOnTop="0" name="lpk_revision_begin"/>
    <field labelOnTop="0" name="lpk_revision_end"/>
    <field labelOnTop="0" name="ncacount"/>
    <field labelOnTop="0" name="ncbcount"/>
    <field labelOnTop="0" name="ncccount"/>
    <field labelOnTop="0" name="pk_desordre"/>
    <field labelOnTop="0" name="pk_objet"/>
    <field labelOnTop="0" name="priorite"/>
    <field labelOnTop="0" name="risques"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE("ID", '&lt;NULL>')</previewExpression>
  <mapTip>ID</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
