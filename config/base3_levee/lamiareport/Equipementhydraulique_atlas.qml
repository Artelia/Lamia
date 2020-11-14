<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" labelsEnabled="0" styleCategories="AllStyleCategories" minScale="1e+08" simplifyDrawingHints="1" hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyDrawingTol="1" version="3.10.6-A Coruña" simplifyAlgorithm="0" simplifyMaxScale="1" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" enableorderby="0" type="RuleRenderer">
    <rules key="{3d8ee8f0-d537-4fa5-947d-d08e912ad749}">
      <rule filter="$id = @atlas_featureid or  &quot;lid_descriptionsystem_1&quot;  = attribute(@atlas_feature , 'id_descriptionsystem')" key="{f1475460-b36a-453a-96c0-527428cac7ea}" symbol="0">
        <rule label="RTE" filter="&quot;equipmentcategory&quot; = 'RTE'" key="{83715408-1e8f-4284-9bc7-328180b02de0}" symbol="1"/>
        <rule label="OUH" filter="&quot;equipmentcategory&quot; = 'OUH'" key="{f2060580-7cd8-4794-aa97-487a980a1d1d}" symbol="2"/>
        <rule label="OUP" filter="&quot;equipmentcategory&quot; = 'OUP'" key="{e1f0059c-21bf-4df3-8c5f-5ef7bbf68691}" symbol="3"/>
        <rule label="RHF" filter="&quot;equipmentcategory&quot; = 'RHF'" key="{3e4c80b6-d5ea-4838-a534-cf8e9298bbed}" symbol="4"/>
        <rule label="RHO" filter="&quot;equipmentcategory&quot; = 'RHO'" key="{bb1b5cb8-6b69-480c-9a96-8fbf6ef16aa4}" symbol="5"/>
        <rule label="OUT" filter="&quot;equipmentcategory&quot; = 'OUT'" key="{3dcc5c08-9aec-4880-98e9-14ab34cce785}" symbol="6"/>
      </rule>
      <rule filter="ELSE" key="{560ca9be-e6b0-49ae-950e-4fb7645df1a9}" symbol="7">
        <rule label="RTE" filter="&quot;equipmentcategory&quot; = 'RTE'" key="{219156d1-d03b-4a10-a792-21f18b169701}" symbol="8"/>
        <rule label="OUH" filter="&quot;equipmentcategory&quot; = 'OUH'" key="{4c5ce736-affe-4fa2-a9f0-c38a9de96abd}" symbol="9"/>
        <rule label="OUP" filter="&quot;equipmentcategory&quot; = 'OUP'" key="{ca44e1e1-1723-4895-a152-6c34a7a034b6}" symbol="10"/>
        <rule label="RHF" filter="&quot;equipmentcategory&quot; = 'RHF'" key="{ac011160-7fe1-4383-9f0f-674f2076f1ef}" symbol="11"/>
        <rule label="RHO" filter="&quot;equipmentcategory&quot; = 'RHO'" key="{30ef1a4a-be0d-4015-ba7c-7cabbf78ad31}" symbol="12"/>
        <rule label="OUT" filter="&quot;equipmentcategory&quot; = 'OUT'" key="{bd0b718c-77b4-4271-8f08-b64fc52cb1f3}" symbol="13"/>
      </rule>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" name="0" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="41,93,130,255" k="line_color"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="1" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="1" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.2" k="line_width"/>
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
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,29,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.7" k="line_width"/>
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
      <symbol clip_to_extent="1" name="10" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="1" enabled="1">
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
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="181,181,181,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
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
      <symbol clip_to_extent="1" name="11" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="1" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.2" k="line_width"/>
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
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="181,181,181,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="0.7" k="line_width"/>
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
        <layer class="SimpleLine" locked="1" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.2" k="line_width"/>
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
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="181,181,181,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.7" k="line_width"/>
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
        <layer class="MarkerLine" locked="0" pass="1" enabled="1">
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
          <symbol clip_to_extent="1" name="@13@0" force_rhr="0" alpha="1" type="marker">
            <layer class="SimpleMarker" locked="0" pass="0" enabled="1">
              <prop v="0" k="angle"/>
              <prop v="181,181,181,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="triangle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="245,5,0,255" k="outline_color"/>
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
      <symbol clip_to_extent="1" name="2" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="1" enabled="1">
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
              <prop v="0,95,255,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="area" k="scale_method"/>
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
        <layer class="MarkerLine" locked="0" pass="1" enabled="1">
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
              <prop v="0,0,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
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
        <layer class="SimpleLine" locked="1" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.2" k="line_width"/>
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
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,95,255,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="0.7" k="line_width"/>
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
      <symbol clip_to_extent="1" name="5" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="1" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.2" k="line_width"/>
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
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,95,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.7" k="line_width"/>
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
      <symbol clip_to_extent="1" name="6" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="0" enabled="1">
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
              <prop v="245,5,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="triangle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="245,5,0,255" k="outline_color"/>
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
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="161,48,25,255" k="line_color"/>
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="8" force_rhr="0" alpha="1" type="line">
        <layer class="SimpleLine" locked="1" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,255,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.2" k="line_width"/>
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
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="181,181,181,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.7" k="line_width"/>
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
      <symbol clip_to_extent="1" name="9" force_rhr="0" alpha="1" type="line">
        <layer class="MarkerLine" locked="0" pass="1" enabled="1">
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
              <prop v="181,181,181,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="area" k="scale_method"/>
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
  <customproperties>
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
    <field name="pk_equipment">
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
    <field name="lpk_descriptionsystem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="equipmentcategory">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="RHF" name="Lineaire - Hydrau enterre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RHO" name="Lineaire - Hydrau ciel ouvert" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RTE" name="Lineaire - Telecom/Energie" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="OUH" name="Ponctuel - Hydraulique" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="OUT" name="Ponctuel - Telecom/Energie" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="OUP" name="Ponctuel - Particulier" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="lid_resource_1">
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
    <field name="equipmenttype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CLA" name="Clapet" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="VAN" name="Vanne" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="EXU" name="Exutoire" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BIN" name="Borne incendie" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FLO" name="Porte à flot" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FOD" name="Fosse de decantation" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="POS" name="Poste de refoulement, pompage" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="REG" name="Regard, bouche a clef" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RES" name="Reservoir, chateau d eau" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RES" name="Station d epuration" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="GRI" name="Grille, degrillage" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BOR" name="Borne (Gaz...)" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CDB" name="Coffret de branchement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CHT" name="Chambre Telecom" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="POT" name="Poteau (EDF,PTT)" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TRA" name="Transformateur" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BAT" name="Batiment encastre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BOK" name="Borne PK" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BRE" name="Borne reseau d eau" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CAV" name="Cave encastree" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CLO" name="Cloture encastree" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ECH" name="Echelle Limnimetrique" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ESC" name="Escalier" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MOU" name="Monument" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="OUA" name="Ouvrage alimentant champs inond." type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PAN" name="Panneau d'information divers" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PAS" name="Passe a poissons" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PIE" name="Piezometre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PON" name="Ponton" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RDN" name="Repere de nivellement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SOB" name="Socle beton" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="STA" name="Station de mesure" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CAN" name="Pompage, prise d eau" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CON" name="Canalisation (AEP,EU...)" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="AFL" name="Affluent" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CAI" name="Caniveau beton" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CAN" name="Canal" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CHAN" name="Chantourne" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PRO" name="Porteaux" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CCU" name="Chauffage urbain" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="EFT" name="EDF ou PTT" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="EFT" name="EDF ou PTT" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FIB" name="Fibre optique" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="GDF" name="Gaz" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="HYD" name="Hydrocarbure" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SAU" name="Saumure" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indefini" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="equipmentsubtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BUS" name="Buse" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BUB" name="Buse avec encadrement béton" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="GRA" name="Grille Avaloir" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MUR" name="Sur Muret" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MAC" name="Maçonné" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="NOB" name="Non observé" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="location">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="AER" name="Aerien" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ENT" name="Enterre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ENT" name="Superficiel" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indefini" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="flowtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="GRA" name="Gravitaire" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PRE" name="Sous pression" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="usage">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DRA" name="Drainage" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="EDI" name="AEP" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="EPL" name="Eaux pluviales" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="EUS" name="Eaux usees" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IRR" name="Irrigation" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ERI" name="Eaux residuaires indus." type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ACIC" name="Alimentation champ d inonation" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indefini" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="height">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="width">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="invert">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="safety">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="2" name="Visitable en securite" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="1" name="Non visitable - cadenassé" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="0" name="Non visitable en securite" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="side">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RIV" name="Eau" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TER" name="Terre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ETG" name="Etang" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MER" name="Ocean" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DEU" name="Deux cotes" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CRE" name="Crete" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indefini" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="position">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CRE" name="Crete" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TAD" name="Talus digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SOR" name="Sommet risberme" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TAR" name="Talus risberme" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TRP" name="Talus risberme - pied de digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PDI" name="Pied de digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FRB" name="Franc-bord" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BER" name="Berge" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="HOR" name="Hors digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PLU" name="Plusieurs parties" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indefini" type="QString"/>
              </Option>
            </Option>
          </Option>
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
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="1" name="Oui" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="0" name="Non" type="QString"/>
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
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="A" name="A" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="B" name="B" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="C" name="C" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="NC" name="NC" type="QString"/>
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
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="1" name="Classe A" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="2" name="Classe B" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="3" name="Classe C" type="QString"/>
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
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="1" name="Classe A" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="2" name="Classe B" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="3" name="Classe C" type="QString"/>
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
    <field name="fonctionnalcondition">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="0" name="Hors service" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="1" name="Mauvais" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="2" name="Moyen" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="3" name="Bon" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="4" name="Excellent" type="QString"/>
              </Option>
            </Option>
          </Option>
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
    <field name="lid_actor_creator">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sirsid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" index="0" field="pk_equipment"/>
    <alias name="" index="1" field="id_equipment"/>
    <alias name="" index="2" field="lpk_descriptionsystem"/>
    <alias name="" index="3" field="equipmentcategory"/>
    <alias name="" index="4" field="lid_resource_1"/>
    <alias name="" index="5" field="lid_descriptionsystem_1"/>
    <alias name="" index="6" field="equipmenttype"/>
    <alias name="" index="7" field="equipmentsubtype"/>
    <alias name="" index="8" field="location"/>
    <alias name="" index="9" field="flowtype"/>
    <alias name="" index="10" field="usage"/>
    <alias name="" index="11" field="height"/>
    <alias name="" index="12" field="width"/>
    <alias name="" index="13" field="invert"/>
    <alias name="" index="14" field="safety"/>
    <alias name="" index="15" field="side"/>
    <alias name="" index="16" field="position"/>
    <alias name="" index="17" field="pk_descriptionsystem"/>
    <alias name="" index="18" field="id_descriptionsystem"/>
    <alias name="" index="19" field="lpk_object"/>
    <alias name="" index="20" field="strategicvalue"/>
    <alias name="" index="21" field="operational"/>
    <alias name="" index="22" field="structuralstate"/>
    <alias name="" index="23" field="operationalstate"/>
    <alias name="" index="24" field="dateoperationalcreation"/>
    <alias name="" index="25" field="dateoperationalcreationupper"/>
    <alias name="" index="26" field="operationaldatecreationaccuracy"/>
    <alias name="" index="27" field="datetimeoperationaldestruction"/>
    <alias name="" index="28" field="geotrackingxyquality"/>
    <alias name="" index="29" field="geotrackingzquality"/>
    <alias name="" index="30" field="geotrackingdate"/>
    <alias name="" index="31" field="geotrackingsource"/>
    <alias name="" index="32" field="parameters"/>
    <alias name="" index="33" field="parameterslist"/>
    <alias name="" index="34" field="city"/>
    <alias name="" index="35" field="streetname"/>
    <alias name="" index="36" field="streetupname"/>
    <alias name="" index="37" field="streetdownname"/>
    <alias name="" index="38" field="streetcomment"/>
    <alias name="" index="39" field="lid_actor_1"/>
    <alias name="" index="40" field="lid_actor_2"/>
    <alias name="" index="41" field="lid_actor_3"/>
    <alias name="" index="42" field="lid_facility"/>
    <alias name="" index="43" field="float_1"/>
    <alias name="" index="44" field="float_2"/>
    <alias name="" index="45" field="float_3"/>
    <alias name="" index="46" field="float_4"/>
    <alias name="" index="47" field="float_5"/>
    <alias name="" index="48" field="float_6"/>
    <alias name="" index="49" field="float_7"/>
    <alias name="" index="50" field="float_8"/>
    <alias name="" index="51" field="float_9"/>
    <alias name="" index="52" field="float_10"/>
    <alias name="" index="53" field="string_1"/>
    <alias name="" index="54" field="string_2"/>
    <alias name="" index="55" field="string_3"/>
    <alias name="" index="56" field="string_4"/>
    <alias name="" index="57" field="string_5"/>
    <alias name="" index="58" field="string_6"/>
    <alias name="" index="59" field="string_7"/>
    <alias name="" index="60" field="string_8"/>
    <alias name="" index="61" field="string_9"/>
    <alias name="" index="62" field="string_10"/>
    <alias name="" index="63" field="fonctionnalcondition"/>
    <alias name="" index="64" field="pk_object"/>
    <alias name="" index="65" field="id_object"/>
    <alias name="" index="66" field="lpk_revision_begin"/>
    <alias name="" index="67" field="lpk_revision_end"/>
    <alias name="" index="68" field="datetimecreation"/>
    <alias name="" index="69" field="datetimemodification"/>
    <alias name="" index="70" field="datetimedestruction"/>
    <alias name="" index="71" field="comment"/>
    <alias name="" index="72" field="name"/>
    <alias name="" index="73" field="importid"/>
    <alias name="" index="74" field="importtable"/>
    <alias name="" index="75" field="lid_actor_creator"/>
    <alias name="" index="76" field="sirsid"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="pk_equipment"/>
    <default applyOnUpdate="0" expression="" field="id_equipment"/>
    <default applyOnUpdate="0" expression="" field="lpk_descriptionsystem"/>
    <default applyOnUpdate="0" expression="" field="equipmentcategory"/>
    <default applyOnUpdate="0" expression="" field="lid_resource_1"/>
    <default applyOnUpdate="0" expression="" field="lid_descriptionsystem_1"/>
    <default applyOnUpdate="0" expression="" field="equipmenttype"/>
    <default applyOnUpdate="0" expression="" field="equipmentsubtype"/>
    <default applyOnUpdate="0" expression="" field="location"/>
    <default applyOnUpdate="0" expression="" field="flowtype"/>
    <default applyOnUpdate="0" expression="" field="usage"/>
    <default applyOnUpdate="0" expression="" field="height"/>
    <default applyOnUpdate="0" expression="" field="width"/>
    <default applyOnUpdate="0" expression="" field="invert"/>
    <default applyOnUpdate="0" expression="" field="safety"/>
    <default applyOnUpdate="0" expression="" field="side"/>
    <default applyOnUpdate="0" expression="" field="position"/>
    <default applyOnUpdate="0" expression="" field="pk_descriptionsystem"/>
    <default applyOnUpdate="0" expression="" field="id_descriptionsystem"/>
    <default applyOnUpdate="0" expression="" field="lpk_object"/>
    <default applyOnUpdate="0" expression="" field="strategicvalue"/>
    <default applyOnUpdate="0" expression="" field="operational"/>
    <default applyOnUpdate="0" expression="" field="structuralstate"/>
    <default applyOnUpdate="0" expression="" field="operationalstate"/>
    <default applyOnUpdate="0" expression="" field="dateoperationalcreation"/>
    <default applyOnUpdate="0" expression="" field="dateoperationalcreationupper"/>
    <default applyOnUpdate="0" expression="" field="operationaldatecreationaccuracy"/>
    <default applyOnUpdate="0" expression="" field="datetimeoperationaldestruction"/>
    <default applyOnUpdate="0" expression="" field="geotrackingxyquality"/>
    <default applyOnUpdate="0" expression="" field="geotrackingzquality"/>
    <default applyOnUpdate="0" expression="" field="geotrackingdate"/>
    <default applyOnUpdate="0" expression="" field="geotrackingsource"/>
    <default applyOnUpdate="0" expression="" field="parameters"/>
    <default applyOnUpdate="0" expression="" field="parameterslist"/>
    <default applyOnUpdate="0" expression="" field="city"/>
    <default applyOnUpdate="0" expression="" field="streetname"/>
    <default applyOnUpdate="0" expression="" field="streetupname"/>
    <default applyOnUpdate="0" expression="" field="streetdownname"/>
    <default applyOnUpdate="0" expression="" field="streetcomment"/>
    <default applyOnUpdate="0" expression="" field="lid_actor_1"/>
    <default applyOnUpdate="0" expression="" field="lid_actor_2"/>
    <default applyOnUpdate="0" expression="" field="lid_actor_3"/>
    <default applyOnUpdate="0" expression="" field="lid_facility"/>
    <default applyOnUpdate="0" expression="" field="float_1"/>
    <default applyOnUpdate="0" expression="" field="float_2"/>
    <default applyOnUpdate="0" expression="" field="float_3"/>
    <default applyOnUpdate="0" expression="" field="float_4"/>
    <default applyOnUpdate="0" expression="" field="float_5"/>
    <default applyOnUpdate="0" expression="" field="float_6"/>
    <default applyOnUpdate="0" expression="" field="float_7"/>
    <default applyOnUpdate="0" expression="" field="float_8"/>
    <default applyOnUpdate="0" expression="" field="float_9"/>
    <default applyOnUpdate="0" expression="" field="float_10"/>
    <default applyOnUpdate="0" expression="" field="string_1"/>
    <default applyOnUpdate="0" expression="" field="string_2"/>
    <default applyOnUpdate="0" expression="" field="string_3"/>
    <default applyOnUpdate="0" expression="" field="string_4"/>
    <default applyOnUpdate="0" expression="" field="string_5"/>
    <default applyOnUpdate="0" expression="" field="string_6"/>
    <default applyOnUpdate="0" expression="" field="string_7"/>
    <default applyOnUpdate="0" expression="" field="string_8"/>
    <default applyOnUpdate="0" expression="" field="string_9"/>
    <default applyOnUpdate="0" expression="" field="string_10"/>
    <default applyOnUpdate="0" expression="" field="fonctionnalcondition"/>
    <default applyOnUpdate="0" expression="" field="pk_object"/>
    <default applyOnUpdate="0" expression="" field="id_object"/>
    <default applyOnUpdate="0" expression="" field="lpk_revision_begin"/>
    <default applyOnUpdate="0" expression="" field="lpk_revision_end"/>
    <default applyOnUpdate="0" expression="" field="datetimecreation"/>
    <default applyOnUpdate="0" expression="" field="datetimemodification"/>
    <default applyOnUpdate="0" expression="" field="datetimedestruction"/>
    <default applyOnUpdate="0" expression="" field="comment"/>
    <default applyOnUpdate="0" expression="" field="name"/>
    <default applyOnUpdate="0" expression="" field="importid"/>
    <default applyOnUpdate="0" expression="" field="importtable"/>
    <default applyOnUpdate="0" expression="" field="lid_actor_creator"/>
    <default applyOnUpdate="0" expression="" field="sirsid"/>
  </defaults>
  <constraints>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="pk_equipment"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="id_equipment"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_descriptionsystem"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="equipmentcategory"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_resource_1"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_descriptionsystem_1"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="equipmenttype"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="equipmentsubtype"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="location"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="flowtype"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="usage"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="height"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="width"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="invert"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="safety"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="side"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="position"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="pk_descriptionsystem"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="id_descriptionsystem"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_object"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="strategicvalue"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="operational"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="structuralstate"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="operationalstate"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="dateoperationalcreation"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="dateoperationalcreationupper"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="operationaldatecreationaccuracy"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimeoperationaldestruction"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="geotrackingxyquality"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="geotrackingzquality"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="geotrackingdate"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="geotrackingsource"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="parameters"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="parameterslist"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="city"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="streetname"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="streetupname"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="streetdownname"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="streetcomment"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_actor_1"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_actor_2"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_actor_3"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_facility"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_1"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_2"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_3"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_4"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_5"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_6"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_7"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_8"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_9"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="float_10"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_1"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_2"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_3"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_4"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_5"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_6"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_7"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_8"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_9"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="string_10"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="fonctionnalcondition"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="pk_object"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="id_object"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_revision_begin"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lpk_revision_end"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimecreation"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimemodification"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="datetimedestruction"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="comment"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="name"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="importid"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="importtable"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="lid_actor_creator"/>
    <constraint constraints="0" exp_strength="0" unique_strength="0" notnull_strength="0" field="sirsid"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="pk_equipment" exp=""/>
    <constraint desc="" field="id_equipment" exp=""/>
    <constraint desc="" field="lpk_descriptionsystem" exp=""/>
    <constraint desc="" field="equipmentcategory" exp=""/>
    <constraint desc="" field="lid_resource_1" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_1" exp=""/>
    <constraint desc="" field="equipmenttype" exp=""/>
    <constraint desc="" field="equipmentsubtype" exp=""/>
    <constraint desc="" field="location" exp=""/>
    <constraint desc="" field="flowtype" exp=""/>
    <constraint desc="" field="usage" exp=""/>
    <constraint desc="" field="height" exp=""/>
    <constraint desc="" field="width" exp=""/>
    <constraint desc="" field="invert" exp=""/>
    <constraint desc="" field="safety" exp=""/>
    <constraint desc="" field="side" exp=""/>
    <constraint desc="" field="position" exp=""/>
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
    <constraint desc="" field="fonctionnalcondition" exp=""/>
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
    <constraint desc="" field="lid_actor_creator" exp=""/>
    <constraint desc="" field="sirsid" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" name="position" hidden="0" type="field"/>
      <column width="-1" name="id_descriptionsystem" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" name="pk_equipment" hidden="0" type="field"/>
      <column width="-1" name="id_equipment" hidden="0" type="field"/>
      <column width="-1" name="lpk_descriptionsystem" hidden="0" type="field"/>
      <column width="-1" name="equipmentcategory" hidden="0" type="field"/>
      <column width="-1" name="lid_resource_1" hidden="0" type="field"/>
      <column width="-1" name="lid_descriptionsystem_1" hidden="0" type="field"/>
      <column width="-1" name="equipmenttype" hidden="0" type="field"/>
      <column width="-1" name="equipmentsubtype" hidden="0" type="field"/>
      <column width="-1" name="location" hidden="0" type="field"/>
      <column width="-1" name="flowtype" hidden="0" type="field"/>
      <column width="-1" name="usage" hidden="0" type="field"/>
      <column width="-1" name="height" hidden="0" type="field"/>
      <column width="-1" name="width" hidden="0" type="field"/>
      <column width="-1" name="invert" hidden="0" type="field"/>
      <column width="-1" name="safety" hidden="0" type="field"/>
      <column width="-1" name="side" hidden="0" type="field"/>
      <column width="-1" name="pk_descriptionsystem" hidden="0" type="field"/>
      <column width="-1" name="lpk_object" hidden="0" type="field"/>
      <column width="-1" name="strategicvalue" hidden="0" type="field"/>
      <column width="-1" name="operational" hidden="0" type="field"/>
      <column width="-1" name="structuralstate" hidden="0" type="field"/>
      <column width="-1" name="operationalstate" hidden="0" type="field"/>
      <column width="-1" name="dateoperationalcreation" hidden="0" type="field"/>
      <column width="-1" name="dateoperationalcreationupper" hidden="0" type="field"/>
      <column width="-1" name="operationaldatecreationaccuracy" hidden="0" type="field"/>
      <column width="-1" name="datetimeoperationaldestruction" hidden="0" type="field"/>
      <column width="-1" name="geotrackingxyquality" hidden="0" type="field"/>
      <column width="-1" name="geotrackingzquality" hidden="0" type="field"/>
      <column width="-1" name="geotrackingdate" hidden="0" type="field"/>
      <column width="-1" name="geotrackingsource" hidden="0" type="field"/>
      <column width="-1" name="parameters" hidden="0" type="field"/>
      <column width="-1" name="parameterslist" hidden="0" type="field"/>
      <column width="-1" name="city" hidden="0" type="field"/>
      <column width="-1" name="streetname" hidden="0" type="field"/>
      <column width="-1" name="streetupname" hidden="0" type="field"/>
      <column width="-1" name="streetdownname" hidden="0" type="field"/>
      <column width="-1" name="streetcomment" hidden="0" type="field"/>
      <column width="-1" name="lid_actor_1" hidden="0" type="field"/>
      <column width="-1" name="lid_actor_2" hidden="0" type="field"/>
      <column width="-1" name="lid_actor_3" hidden="0" type="field"/>
      <column width="-1" name="lid_facility" hidden="0" type="field"/>
      <column width="-1" name="float_1" hidden="0" type="field"/>
      <column width="-1" name="float_2" hidden="0" type="field"/>
      <column width="-1" name="float_3" hidden="0" type="field"/>
      <column width="-1" name="float_4" hidden="0" type="field"/>
      <column width="-1" name="float_5" hidden="0" type="field"/>
      <column width="-1" name="float_6" hidden="0" type="field"/>
      <column width="-1" name="float_7" hidden="0" type="field"/>
      <column width="-1" name="float_8" hidden="0" type="field"/>
      <column width="-1" name="float_9" hidden="0" type="field"/>
      <column width="-1" name="float_10" hidden="0" type="field"/>
      <column width="-1" name="string_1" hidden="0" type="field"/>
      <column width="-1" name="string_2" hidden="0" type="field"/>
      <column width="-1" name="string_3" hidden="0" type="field"/>
      <column width="-1" name="string_4" hidden="0" type="field"/>
      <column width="-1" name="string_5" hidden="0" type="field"/>
      <column width="-1" name="string_6" hidden="0" type="field"/>
      <column width="-1" name="string_7" hidden="0" type="field"/>
      <column width="-1" name="string_8" hidden="0" type="field"/>
      <column width="-1" name="string_9" hidden="0" type="field"/>
      <column width="-1" name="string_10" hidden="0" type="field"/>
      <column width="-1" name="fonctionnalcondition" hidden="0" type="field"/>
      <column width="-1" name="pk_object" hidden="0" type="field"/>
      <column width="-1" name="id_object" hidden="0" type="field"/>
      <column width="-1" name="lpk_revision_begin" hidden="0" type="field"/>
      <column width="-1" name="lpk_revision_end" hidden="0" type="field"/>
      <column width="-1" name="datetimecreation" hidden="0" type="field"/>
      <column width="-1" name="datetimemodification" hidden="0" type="field"/>
      <column width="-1" name="datetimedestruction" hidden="0" type="field"/>
      <column width="-1" name="comment" hidden="0" type="field"/>
      <column width="-1" name="name" hidden="0" type="field"/>
      <column width="-1" name="importid" hidden="0" type="field"/>
      <column width="-1" name="importtable" hidden="0" type="field"/>
      <column width="-1" name="lid_actor_creator" hidden="0" type="field"/>
      <column width="-1" name="sirsid" hidden="0" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1">.</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>.</editforminitfilepath>
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
    <field name="dateoperationalcreation" editable="1"/>
    <field name="dateoperationalcreationupper" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimemodification" editable="1"/>
    <field name="datetimeoperationaldestruction" editable="1"/>
    <field name="equipmentcategory" editable="1"/>
    <field name="equipmentsubtype" editable="1"/>
    <field name="equipmenttype" editable="1"/>
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
    <field name="flowtype" editable="1"/>
    <field name="fonctionnalcondition" editable="1"/>
    <field name="geotrackingdate" editable="1"/>
    <field name="geotrackingsource" editable="1"/>
    <field name="geotrackingxyquality" editable="1"/>
    <field name="geotrackingzquality" editable="1"/>
    <field name="height" editable="1"/>
    <field name="id_descriptionsystem" editable="1"/>
    <field name="id_equipment" editable="1"/>
    <field name="id_object" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="invert" editable="1"/>
    <field name="lid_actor_1" editable="1"/>
    <field name="lid_actor_2" editable="1"/>
    <field name="lid_actor_3" editable="1"/>
    <field name="lid_actor_creator" editable="1"/>
    <field name="lid_descriptionsystem_1" editable="1"/>
    <field name="lid_facility" editable="1"/>
    <field name="lid_resource_1" editable="1"/>
    <field name="location" editable="1"/>
    <field name="lpk_descriptionsystem" editable="1"/>
    <field name="lpk_object" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="name" editable="1"/>
    <field name="operational" editable="1"/>
    <field name="operationaldatecreationaccuracy" editable="1"/>
    <field name="operationalstate" editable="1"/>
    <field name="parameters" editable="1"/>
    <field name="parameterslist" editable="1"/>
    <field name="pk_descriptionsystem" editable="1"/>
    <field name="pk_equipment" editable="1"/>
    <field name="pk_object" editable="1"/>
    <field name="position" editable="1"/>
    <field name="safety" editable="1"/>
    <field name="side" editable="1"/>
    <field name="sirsid" editable="1"/>
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
    <field name="usage" editable="1"/>
    <field name="width" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="city"/>
    <field labelOnTop="0" name="comment"/>
    <field labelOnTop="0" name="dateoperationalcreation"/>
    <field labelOnTop="0" name="dateoperationalcreationupper"/>
    <field labelOnTop="0" name="datetimecreation"/>
    <field labelOnTop="0" name="datetimedestruction"/>
    <field labelOnTop="0" name="datetimemodification"/>
    <field labelOnTop="0" name="datetimeoperationaldestruction"/>
    <field labelOnTop="0" name="equipmentcategory"/>
    <field labelOnTop="0" name="equipmentsubtype"/>
    <field labelOnTop="0" name="equipmenttype"/>
    <field labelOnTop="0" name="float_1"/>
    <field labelOnTop="0" name="float_10"/>
    <field labelOnTop="0" name="float_2"/>
    <field labelOnTop="0" name="float_3"/>
    <field labelOnTop="0" name="float_4"/>
    <field labelOnTop="0" name="float_5"/>
    <field labelOnTop="0" name="float_6"/>
    <field labelOnTop="0" name="float_7"/>
    <field labelOnTop="0" name="float_8"/>
    <field labelOnTop="0" name="float_9"/>
    <field labelOnTop="0" name="flowtype"/>
    <field labelOnTop="0" name="fonctionnalcondition"/>
    <field labelOnTop="0" name="geotrackingdate"/>
    <field labelOnTop="0" name="geotrackingsource"/>
    <field labelOnTop="0" name="geotrackingxyquality"/>
    <field labelOnTop="0" name="geotrackingzquality"/>
    <field labelOnTop="0" name="height"/>
    <field labelOnTop="0" name="id_descriptionsystem"/>
    <field labelOnTop="0" name="id_equipment"/>
    <field labelOnTop="0" name="id_object"/>
    <field labelOnTop="0" name="importid"/>
    <field labelOnTop="0" name="importtable"/>
    <field labelOnTop="0" name="invert"/>
    <field labelOnTop="0" name="lid_actor_1"/>
    <field labelOnTop="0" name="lid_actor_2"/>
    <field labelOnTop="0" name="lid_actor_3"/>
    <field labelOnTop="0" name="lid_actor_creator"/>
    <field labelOnTop="0" name="lid_descriptionsystem_1"/>
    <field labelOnTop="0" name="lid_facility"/>
    <field labelOnTop="0" name="lid_resource_1"/>
    <field labelOnTop="0" name="location"/>
    <field labelOnTop="0" name="lpk_descriptionsystem"/>
    <field labelOnTop="0" name="lpk_object"/>
    <field labelOnTop="0" name="lpk_revision_begin"/>
    <field labelOnTop="0" name="lpk_revision_end"/>
    <field labelOnTop="0" name="name"/>
    <field labelOnTop="0" name="operational"/>
    <field labelOnTop="0" name="operationaldatecreationaccuracy"/>
    <field labelOnTop="0" name="operationalstate"/>
    <field labelOnTop="0" name="parameters"/>
    <field labelOnTop="0" name="parameterslist"/>
    <field labelOnTop="0" name="pk_descriptionsystem"/>
    <field labelOnTop="0" name="pk_equipment"/>
    <field labelOnTop="0" name="pk_object"/>
    <field labelOnTop="0" name="position"/>
    <field labelOnTop="0" name="safety"/>
    <field labelOnTop="0" name="side"/>
    <field labelOnTop="0" name="sirsid"/>
    <field labelOnTop="0" name="strategicvalue"/>
    <field labelOnTop="0" name="streetcomment"/>
    <field labelOnTop="0" name="streetdownname"/>
    <field labelOnTop="0" name="streetname"/>
    <field labelOnTop="0" name="streetupname"/>
    <field labelOnTop="0" name="string_1"/>
    <field labelOnTop="0" name="string_10"/>
    <field labelOnTop="0" name="string_2"/>
    <field labelOnTop="0" name="string_3"/>
    <field labelOnTop="0" name="string_4"/>
    <field labelOnTop="0" name="string_5"/>
    <field labelOnTop="0" name="string_6"/>
    <field labelOnTop="0" name="string_7"/>
    <field labelOnTop="0" name="string_8"/>
    <field labelOnTop="0" name="string_9"/>
    <field labelOnTop="0" name="structuralstate"/>
    <field labelOnTop="0" name="usage"/>
    <field labelOnTop="0" name="width"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE( "id_descriptionsystem", '&lt;NULL>' )</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
