<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyMaxScale="1" minScale="1e+08" hasScaleBasedVisibilityFlag="0" maxScale="0" version="3.10.6-A Coruña" simplifyDrawingTol="1" simplifyDrawingHints="1" simplifyLocal="1" readOnly="0" labelsEnabled="1" simplifyAlgorithm="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" type="RuleRenderer" symbollevels="0">
    <rules key="{5e78f11d-4178-4ed7-8af6-f80178c4ba25}">
      <rule label="Branchement" key="{c647d32b-b632-485f-bd3c-91150bd75a8b}" filter=" &quot;laterals&quot; = 1">
        <rule key="{c64b87c5-2e70-47ec-a94f-a9b46d7ca120}" filter="&quot;lid_descriptionsystem_1&quot; IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL">
          <rule label="Eaux usées" symbol="0" key="{9739976b-e285-47e5-a9b3-f03be0ead4d2}" filter="&quot;networktype&quot; IN ('USE','02')">
            <rule scalemindenom="5000" label="0 - 5000" symbol="1" key="{33fbb348-5c57-44e8-b6fc-be6c61d5397f}"/>
          </rule>
          <rule label="Unitaire" symbol="2" key="{b58611c9-3fed-43bb-b53c-b9e470bd0e7a}" filter="&quot;networktype&quot; IN ('UNI','01')">
            <rule scalemindenom="5000" label="0 - 5000" symbol="3" key="{aadc49a6-4a5f-49a6-b31e-fb53caa7da29}"/>
          </rule>
          <rule label="Eaux pluviales" symbol="4" key="{79228b2f-3bcc-41db-b9b2-7a63236519b9}" filter="&quot;networktype&quot; IN ('PLU','03')">
            <rule scalemindenom="5000" label="0 - 5000" symbol="5" key="{557f2669-c040-4245-b628-e29d512012e9}"/>
          </rule>
        </rule>
        <rule key="{766e1a38-f6d0-4e9e-9f69-8e4b0e647dbd}" filter="ELSE">
          <rule label="Eaux usées" symbol="6" key="{056c6700-936d-4dc5-94bb-444be6ac21c1}" filter="&quot;networktype&quot; IN ('USE','02')">
            <rule scalemindenom="5000" label="0 - 5000" symbol="7" key="{e16e7031-5f55-4999-9a28-5147490d9c50}"/>
          </rule>
          <rule label="Unitaire" symbol="8" key="{d02aedf7-0a96-43e6-b6e4-05de94c29c01}" filter="&quot;networktype&quot; IN ('UNI','01')">
            <rule scalemindenom="5000" label="0 - 5000" symbol="9" key="{05870733-4af5-4c67-9521-0638e39097b8}"/>
          </rule>
          <rule label="Eaux pluviales" symbol="10" key="{e5d88765-3a5e-45c9-9d40-4f4ccb76f3d1}" filter="&quot;networktype&quot; IN ('PLU','03')">
            <rule scalemindenom="5000" label="0 - 5000" symbol="11" key="{59da33b5-8378-418d-8d13-e3d77b53db3b}"/>
          </rule>
        </rule>
      </rule>
      <rule label="Branchement" key="{06826450-6078-4741-8f6d-022aaa3d991c}" filter=" &quot;laterals&quot; = 0">
        <rule key="{88663e10-e0fc-4596-9b17-73b72cdd6b17}" filter=" &quot;lid_descriptionsystem_1&quot;  IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL">
          <rule label="Eaux usées" symbol="12" key="{1a389d12-0d10-440b-bc98-99359171cecd}" filter="&quot;networktype&quot; IN ('USE','02')">
            <rule label="0 - 5000" symbol="13" scalemaxdenom="5000" key="{7ea2414d-2527-4219-bd96-abcaebd05d23}"/>
          </rule>
          <rule label="Unitaire" symbol="14" key="{68b407af-ccdc-4174-9cf3-b76afd97b02a}" filter="&quot;networktype&quot; IN ('UNI','01')">
            <rule label="0 - 5000" symbol="15" scalemaxdenom="5000" key="{a3bf1739-5ac1-4b64-b6bc-d90c27195dff}"/>
          </rule>
          <rule label="Eaux pluviales" symbol="16" key="{63296647-4e1b-4afe-b24e-22e8e31ff386}" filter="&quot;networktype&quot; IN ('PLU','03')">
            <rule label="0 - 5000" symbol="17" scalemaxdenom="5000" key="{ac2c4c84-b8b9-4622-9ad9-2f34d7a3a2d5}"/>
          </rule>
          <rule label="Refoulement eaux usées" symbol="18" key="{3f65b50e-0bf2-40c6-a77b-07ef1672c36e}" filter="&quot;networktype&quot; IN ('USE','02') and &quot;systemfunction&quot;  =   '02' "/>
        </rule>
        <rule key="{33f84cfd-6977-4c2a-9cb5-fc1b120f5186}" filter="ELSE">
          <rule label="Eaux usées" symbol="19" key="{d06eff82-6570-49e6-a3db-2f57ba6f18f1}" filter="&quot;networktype&quot; IN ('USE','02') and &quot;systemfunction&quot;  =   '01'">
            <rule label="0 - 5000" symbol="20" scalemaxdenom="5000" key="{9da33136-3b87-432c-acbd-8f6df6ab8b99}"/>
          </rule>
          <rule label="Unitaire" symbol="21" key="{a3ec9bfa-cfb2-481e-bc88-423fe89f7a96}" filter="&quot;networktype&quot; IN ('UNI','01')">
            <rule label="0 - 5000" symbol="22" scalemaxdenom="5000" key="{582a22e5-bd4f-47aa-a7fd-95ffaeac2744}"/>
          </rule>
          <rule label="Eaux pluviales" symbol="23" key="{0120d564-3526-4085-b40c-57703191a0c7}" filter="&quot;networktype&quot; IN ('PLU','03') and &quot;systemfunction&quot;  =   '01'">
            <rule label="0 - 5000" symbol="24" scalemaxdenom="5000" key="{bd85613e-74eb-4a63-93b8-65e0b1a9c295}"/>
          </rule>
          <rule label="Refoulement eaux pluviales " symbol="25" key="{95b411e6-2b95-4638-810c-cebf2f9a9a05}" filter=" &quot;networktype&quot; IN ('PLU','03') and  &quot;systemfunction&quot; = '02'"/>
        </rule>
      </rule>
      <rule symbol="26" key="{146b5a78-5b72-4838-8cb1-ae306bc010b5}" filter="ELSE">
        <rule label="0 - 5000" symbol="27" scalemaxdenom="5000" key="{d337d640-72b2-476f-9aeb-813fdd0a2e58}"/>
      </rule>
    </rules>
    <symbols>
      <symbol force_rhr="0" type="line" name="0" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,1,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="1" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@1@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,1,1,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2.8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="10" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,255,255" k="line_color"/>
          <prop v="dash" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="11" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@11@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="0,0,255,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,255,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2.8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="12" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,1,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.8" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="13" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@13@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,1,1,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="3.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="14" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,127,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.8" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="15" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@15@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,127,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,127,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="3.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="16" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.8" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="17" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@17@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="0,0,255,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,255,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="3.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="18" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="213,116,255,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="19" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,1,1,255" k="line_color"/>
          <prop v="dash" k="line_style"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="2" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,127,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="20" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@20@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,1,1,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="3.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="21" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,127,0,255" k="line_color"/>
          <prop v="dash" k="line_style"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="22" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@22@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,127,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,127,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="3.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="23" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,255,255" k="line_color"/>
          <prop v="dash" k="line_style"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="24" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@24@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="0,0,255,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,255,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="3.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="25" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="11,202,255,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="26" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="112,112,112,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="27" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@27@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="112,112,112,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="112,112,112,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="3.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="3" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@3@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,127,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,127,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2.8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="4" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="5" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@5@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="0,0,255,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,255,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2.8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="6" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,1,1,255" k="line_color"/>
          <prop v="dash" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="7" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@7@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,1,1,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2.8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol force_rhr="0" type="line" name="8" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,127,0,255" k="line_color"/>
          <prop v="dash" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="line" name="9" alpha="1" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="marker" name="@9@0" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,127,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="filled_arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="255,127,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2.8" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontSize="8.25" fontStrikeout="0" fontWordSpacing="0" fieldName=" &quot;nominaldiameter&quot;  *1000" fontItalic="0" fontKerning="1" previewBkgrdColor="255,255,255,255" blendMode="0" textColor="0,0,0,255" multilineHeight="1" useSubstitutions="0" fontFamily="MS Shell Dlg 2" isExpression="1" namedStyle="Normal" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" fontWeight="50" fontCapitals="0" fontLetterSpacing="0" fontSizeUnit="Point" textOrientation="horizontal" fontUnderline="0">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferNoFill="0" bufferJoinStyle="128" bufferOpacity="1" bufferBlendMode="0" bufferDraw="1" bufferSizeUnits="MM" bufferSize="1"/>
        <background shapeSVGFile="" shapeOffsetX="0" shapeRadiiX="0" shapeSizeX="0" shapeJoinStyle="64" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeSizeY="0" shapeOpacity="1" shapeSizeUnit="MM" shapeFillColor="255,255,255,255" shapeType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiUnit="MM" shapeRadiiY="0" shapeOffsetY="0" shapeBorderColor="128,128,128,255" shapeRotation="0" shapeBlendMode="0" shapeBorderWidthUnit="MM">
          <symbol force_rhr="0" type="marker" name="markerSymbol" alpha="1" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="133,182,111,255" k="color"/>
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
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowUnder="0" shadowOpacity="0.7" shadowDraw="0" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowBlendMode="6" shadowRadiusUnit="MM" shadowScale="100"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" multilineAlign="4294967295" reverseDirectionSymbol="0" addDirectionSymbol="0" autoWrapLength="0" rightDirectionSymbol=">" wrapChar="" formatNumbers="0" plussign="0" decimals="3"/>
      <placement geometryGeneratorEnabled="0" quadOffset="4" placementFlags="2" yOffset="0" fitInPolygonOnly="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" repeatDistanceUnits="MM" xOffset="0" preserveRotation="1" maxCurvedCharAngleIn="25" layerType="LineGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" repeatDistance="0" centroidWhole="0" offsetType="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" dist="0.5" centroidInside="0" geometryGenerator="" overrunDistance="0" geometryGeneratorType="PointGeometry" offsetUnits="MapUnit" priority="5" placement="3" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" distMapUnitScale="3x:0,0,0,0,0,0" distUnits="MM" maxCurvedCharAngleOut="-25" overrunDistanceUnit="MM"/>
      <rendering displayAll="0" obstacle="1" zIndex="0" limitNumLabels="0" maxNumLabels="2000" labelPerPart="0" obstacleFactor="1" fontMinPixelSize="3" scaleVisibility="1" fontLimitPixelSize="0" mergeLines="1" scaleMin="1" drawLabels="1" minFeatureSize="2" obstacleType="0" fontMaxPixelSize="10000" upsidedownLabels="0" scaleMax="5000"/>
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
          <Option type="QString" name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; type=&quot;line&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; clip_to_extent=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
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
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>COALESCE( "TYP_RESEAU", '&lt;NULL>' )</value>
    </property>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory labelPlacementMethod="XHeight" sizeType="MM" width="15" backgroundColor="#ffffff" backgroundAlpha="255" penColor="#000000" enabled="0" lineSizeType="MM" maxScaleDenominator="1e+08" scaleDependency="Area" minScaleDenominator="0" height="15" sizeScale="3x:0,0,0,0,0,0" opacity="1" scaleBasedVisibility="0" penWidth="0" barWidth="5" rotationOffset="270" minimumSize="0" penAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="2" obstacle="0" zIndex="0" linePlacementFlags="2" priority="0" dist="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="pk_edge">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_edge">
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
    <field name="lid_descriptionsystem_2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="material">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Acier" value="01"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Amiante-ciment" value="02"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Béton arme tole" value="03"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Beton arme" value="04"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Beton fibre" value="05"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Beton non arme" value="06"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Cuivre" value="07"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fibre ciment" value="08"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fibre de verre" value="09"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fibrociment" value="10"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fonte ductile" value="11"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fonte grise" value="12"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Gres" value="13"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Maconnerie" value="14"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Meuliere" value="15"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PEBD" value="16"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PEHD annele" value="17"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PEHD lisse" value="18"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Plomb" value="19"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PP annele" value="20"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PP lisse" value="21"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PRV A" value="22"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PRV B" value="23"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PVC ancien" value="24"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PVC BO" value="25"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PVC U annele" value="26"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PVC U lisse" value="27"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tole galvanisee" value="28"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Autre" value="00"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Indetermine" value="99"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="nominaldiameter">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pipetype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="Collecteur enterré" value="COL"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fossé" value="FOS"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tranchée" value="TRA"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Chemin agricole" value="CHE"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Noue" value="NOU"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Caniveau" value="CAN"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Haie" value="HAI"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fascine" value="FAS"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Chevets" value="CHV"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="pipesubtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Bétonné" value="BET"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Revêtu" value="REV"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Enherbé" value="ENH"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Terre à nue" value="NUE"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tranchée simple à double vidange" value="TSD"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tranchée compose à double vidange" value="TCD"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tranchée composée stockante" value="TCS"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tranchée infiltrante" value="TIN"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tranchée composée infiltrante" value="TCI"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Noue d'infiltration" value="NIN"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Noue stockante" value="NST"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Noue à double vidange" value="NDV"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Circulaire" value="CIR"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Aqueduc" value="AQU"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Ovoide" value="OVO"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="pipeshape">
      <editWidget type="TextEdit">
        <config>
          <Option/>
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
    <field name="laterals">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="Non" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Oui" value="1"/>
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
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Gravitaire" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Force" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sous-vide" value="3"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Autre" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Indetermine" value="99"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="elevationup">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="elevationdown">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="depthup">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="depthdown">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="domain">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="location">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="accessibility">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="beddingmaterial">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="soiltype">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="soilmoisture">
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
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Oui" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Non" value="0"/>
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
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="A" value="A"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="B" value="B"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="C" value="C"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="NC" value="NC"/>
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
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Classe A" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Classe B" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Classe C" value="3"/>
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
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Classe A" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Classe B" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Classe C" value="3"/>
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
    <field name="networktype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Pluvial" value="PLU"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Eaux usees" value="USE"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Unitaire" value="UNI"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Industriel" value="IND"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="flowconditionupstream">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Gravitaire" value="GRA"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Ruissellement diffus" value="DIF"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="En chute" value="CHU"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Régulé" value="REG"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sous-pression" value="PRE"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="flowconditiondownstream">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Gravitaire" value="GRA"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Régulé" value="REG"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Infiltration" value="INF"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sous pressions" value="PRE"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="systemfunction">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Transport" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Collecte" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Stockage" value="3"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Régulation" value="4"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Traitement" value="5"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Autre" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Indetermine" value="99"/>
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
  </fieldConfiguration>
  <aliases>
    <alias field="pk_edge" index="0" name=""/>
    <alias field="id_edge" index="1" name=""/>
    <alias field="lpk_descriptionsystem" index="2" name=""/>
    <alias field="lid_resource_1" index="3" name=""/>
    <alias field="lid_descriptionsystem_1" index="4" name=""/>
    <alias field="lid_descriptionsystem_2" index="5" name=""/>
    <alias field="material" index="6" name=""/>
    <alias field="nominaldiameter" index="7" name=""/>
    <alias field="pipetype" index="8" name=""/>
    <alias field="pipesubtype" index="9" name=""/>
    <alias field="pipeshape" index="10" name=""/>
    <alias field="height" index="11" name=""/>
    <alias field="laterals" index="12" name=""/>
    <alias field="flowtype" index="13" name=""/>
    <alias field="elevationup" index="14" name=""/>
    <alias field="elevationdown" index="15" name=""/>
    <alias field="depthup" index="16" name=""/>
    <alias field="depthdown" index="17" name=""/>
    <alias field="domain" index="18" name=""/>
    <alias field="location" index="19" name=""/>
    <alias field="accessibility" index="20" name=""/>
    <alias field="beddingmaterial" index="21" name=""/>
    <alias field="soiltype" index="22" name=""/>
    <alias field="soilmoisture" index="23" name=""/>
    <alias field="pk_descriptionsystem" index="24" name=""/>
    <alias field="id_descriptionsystem" index="25" name=""/>
    <alias field="lpk_object" index="26" name=""/>
    <alias field="strategicvalue" index="27" name=""/>
    <alias field="operational" index="28" name=""/>
    <alias field="structuralstate" index="29" name=""/>
    <alias field="operationalstate" index="30" name=""/>
    <alias field="dateoperationalcreation" index="31" name=""/>
    <alias field="dateoperationalcreationupper" index="32" name=""/>
    <alias field="operationaldatecreationaccuracy" index="33" name=""/>
    <alias field="datetimeoperationaldestruction" index="34" name=""/>
    <alias field="geotrackingxyquality" index="35" name=""/>
    <alias field="geotrackingzquality" index="36" name=""/>
    <alias field="geotrackingdate" index="37" name=""/>
    <alias field="geotrackingsource" index="38" name=""/>
    <alias field="parameters" index="39" name=""/>
    <alias field="parameterslist" index="40" name=""/>
    <alias field="city" index="41" name=""/>
    <alias field="streetname" index="42" name=""/>
    <alias field="streetupname" index="43" name=""/>
    <alias field="streetdownname" index="44" name=""/>
    <alias field="streetcomment" index="45" name=""/>
    <alias field="lid_actor_1" index="46" name=""/>
    <alias field="lid_actor_2" index="47" name=""/>
    <alias field="lid_actor_3" index="48" name=""/>
    <alias field="lid_facility" index="49" name=""/>
    <alias field="float_1" index="50" name=""/>
    <alias field="float_2" index="51" name=""/>
    <alias field="float_3" index="52" name=""/>
    <alias field="float_4" index="53" name=""/>
    <alias field="float_5" index="54" name=""/>
    <alias field="float_6" index="55" name=""/>
    <alias field="float_7" index="56" name=""/>
    <alias field="float_8" index="57" name=""/>
    <alias field="float_9" index="58" name=""/>
    <alias field="float_10" index="59" name=""/>
    <alias field="string_1" index="60" name=""/>
    <alias field="string_2" index="61" name=""/>
    <alias field="string_3" index="62" name=""/>
    <alias field="string_4" index="63" name=""/>
    <alias field="string_5" index="64" name=""/>
    <alias field="string_6" index="65" name=""/>
    <alias field="string_7" index="66" name=""/>
    <alias field="string_8" index="67" name=""/>
    <alias field="string_9" index="68" name=""/>
    <alias field="string_10" index="69" name=""/>
    <alias field="networktype" index="70" name=""/>
    <alias field="flowconditionupstream" index="71" name=""/>
    <alias field="flowconditiondownstream" index="72" name=""/>
    <alias field="systemfunction" index="73" name=""/>
    <alias field="pk_object" index="74" name=""/>
    <alias field="id_object" index="75" name=""/>
    <alias field="lpk_revision_begin" index="76" name=""/>
    <alias field="lpk_revision_end" index="77" name=""/>
    <alias field="datetimecreation" index="78" name=""/>
    <alias field="datetimemodification" index="79" name=""/>
    <alias field="datetimedestruction" index="80" name=""/>
    <alias field="comment" index="81" name=""/>
    <alias field="name" index="82" name=""/>
    <alias field="importid" index="83" name=""/>
    <alias field="importtable" index="84" name=""/>
    <alias field="lid_actor_creator" index="85" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="pk_edge" expression="" applyOnUpdate="0"/>
    <default field="id_edge" expression="" applyOnUpdate="0"/>
    <default field="lpk_descriptionsystem" expression="" applyOnUpdate="0"/>
    <default field="lid_resource_1" expression="" applyOnUpdate="0"/>
    <default field="lid_descriptionsystem_1" expression="" applyOnUpdate="0"/>
    <default field="lid_descriptionsystem_2" expression="" applyOnUpdate="0"/>
    <default field="material" expression="" applyOnUpdate="0"/>
    <default field="nominaldiameter" expression="" applyOnUpdate="0"/>
    <default field="pipetype" expression="" applyOnUpdate="0"/>
    <default field="pipesubtype" expression="" applyOnUpdate="0"/>
    <default field="pipeshape" expression="" applyOnUpdate="0"/>
    <default field="height" expression="" applyOnUpdate="0"/>
    <default field="laterals" expression="" applyOnUpdate="0"/>
    <default field="flowtype" expression="" applyOnUpdate="0"/>
    <default field="elevationup" expression="" applyOnUpdate="0"/>
    <default field="elevationdown" expression="" applyOnUpdate="0"/>
    <default field="depthup" expression="" applyOnUpdate="0"/>
    <default field="depthdown" expression="" applyOnUpdate="0"/>
    <default field="domain" expression="" applyOnUpdate="0"/>
    <default field="location" expression="" applyOnUpdate="0"/>
    <default field="accessibility" expression="" applyOnUpdate="0"/>
    <default field="beddingmaterial" expression="" applyOnUpdate="0"/>
    <default field="soiltype" expression="" applyOnUpdate="0"/>
    <default field="soilmoisture" expression="" applyOnUpdate="0"/>
    <default field="pk_descriptionsystem" expression="" applyOnUpdate="0"/>
    <default field="id_descriptionsystem" expression="" applyOnUpdate="0"/>
    <default field="lpk_object" expression="" applyOnUpdate="0"/>
    <default field="strategicvalue" expression="" applyOnUpdate="0"/>
    <default field="operational" expression="" applyOnUpdate="0"/>
    <default field="structuralstate" expression="" applyOnUpdate="0"/>
    <default field="operationalstate" expression="" applyOnUpdate="0"/>
    <default field="dateoperationalcreation" expression="" applyOnUpdate="0"/>
    <default field="dateoperationalcreationupper" expression="" applyOnUpdate="0"/>
    <default field="operationaldatecreationaccuracy" expression="" applyOnUpdate="0"/>
    <default field="datetimeoperationaldestruction" expression="" applyOnUpdate="0"/>
    <default field="geotrackingxyquality" expression="" applyOnUpdate="0"/>
    <default field="geotrackingzquality" expression="" applyOnUpdate="0"/>
    <default field="geotrackingdate" expression="" applyOnUpdate="0"/>
    <default field="geotrackingsource" expression="" applyOnUpdate="0"/>
    <default field="parameters" expression="" applyOnUpdate="0"/>
    <default field="parameterslist" expression="" applyOnUpdate="0"/>
    <default field="city" expression="" applyOnUpdate="0"/>
    <default field="streetname" expression="" applyOnUpdate="0"/>
    <default field="streetupname" expression="" applyOnUpdate="0"/>
    <default field="streetdownname" expression="" applyOnUpdate="0"/>
    <default field="streetcomment" expression="" applyOnUpdate="0"/>
    <default field="lid_actor_1" expression="" applyOnUpdate="0"/>
    <default field="lid_actor_2" expression="" applyOnUpdate="0"/>
    <default field="lid_actor_3" expression="" applyOnUpdate="0"/>
    <default field="lid_facility" expression="" applyOnUpdate="0"/>
    <default field="float_1" expression="" applyOnUpdate="0"/>
    <default field="float_2" expression="" applyOnUpdate="0"/>
    <default field="float_3" expression="" applyOnUpdate="0"/>
    <default field="float_4" expression="" applyOnUpdate="0"/>
    <default field="float_5" expression="" applyOnUpdate="0"/>
    <default field="float_6" expression="" applyOnUpdate="0"/>
    <default field="float_7" expression="" applyOnUpdate="0"/>
    <default field="float_8" expression="" applyOnUpdate="0"/>
    <default field="float_9" expression="" applyOnUpdate="0"/>
    <default field="float_10" expression="" applyOnUpdate="0"/>
    <default field="string_1" expression="" applyOnUpdate="0"/>
    <default field="string_2" expression="" applyOnUpdate="0"/>
    <default field="string_3" expression="" applyOnUpdate="0"/>
    <default field="string_4" expression="" applyOnUpdate="0"/>
    <default field="string_5" expression="" applyOnUpdate="0"/>
    <default field="string_6" expression="" applyOnUpdate="0"/>
    <default field="string_7" expression="" applyOnUpdate="0"/>
    <default field="string_8" expression="" applyOnUpdate="0"/>
    <default field="string_9" expression="" applyOnUpdate="0"/>
    <default field="string_10" expression="" applyOnUpdate="0"/>
    <default field="networktype" expression="" applyOnUpdate="0"/>
    <default field="flowconditionupstream" expression="" applyOnUpdate="0"/>
    <default field="flowconditiondownstream" expression="" applyOnUpdate="0"/>
    <default field="systemfunction" expression="" applyOnUpdate="0"/>
    <default field="pk_object" expression="" applyOnUpdate="0"/>
    <default field="id_object" expression="" applyOnUpdate="0"/>
    <default field="lpk_revision_begin" expression="" applyOnUpdate="0"/>
    <default field="lpk_revision_end" expression="" applyOnUpdate="0"/>
    <default field="datetimecreation" expression="" applyOnUpdate="0"/>
    <default field="datetimemodification" expression="" applyOnUpdate="0"/>
    <default field="datetimedestruction" expression="" applyOnUpdate="0"/>
    <default field="comment" expression="" applyOnUpdate="0"/>
    <default field="name" expression="" applyOnUpdate="0"/>
    <default field="importid" expression="" applyOnUpdate="0"/>
    <default field="importtable" expression="" applyOnUpdate="0"/>
    <default field="lid_actor_creator" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="pk_edge" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="id_edge" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lpk_descriptionsystem" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_resource_1" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_descriptionsystem_1" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_descriptionsystem_2" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="material" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="nominaldiameter" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="pipetype" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="pipesubtype" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="pipeshape" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="height" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="laterals" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="flowtype" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="elevationup" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="elevationdown" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="depthup" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="depthdown" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="domain" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="location" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="accessibility" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="beddingmaterial" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="soiltype" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="soilmoisture" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="pk_descriptionsystem" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="id_descriptionsystem" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lpk_object" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="strategicvalue" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="operational" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="structuralstate" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="operationalstate" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="dateoperationalcreation" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="dateoperationalcreationupper" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="operationaldatecreationaccuracy" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="datetimeoperationaldestruction" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="geotrackingxyquality" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="geotrackingzquality" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="geotrackingdate" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="geotrackingsource" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="parameters" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="parameterslist" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="city" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="streetname" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="streetupname" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="streetdownname" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="streetcomment" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_actor_1" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_actor_2" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_actor_3" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_facility" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_1" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_2" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_3" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_4" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_5" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_6" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_7" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_8" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_9" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="float_10" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_1" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_2" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_3" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_4" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_5" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_6" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_7" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_8" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_9" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="string_10" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="networktype" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="flowconditionupstream" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="flowconditiondownstream" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="systemfunction" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="pk_object" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="id_object" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lpk_revision_begin" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lpk_revision_end" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="datetimecreation" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="datetimemodification" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="datetimedestruction" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="comment" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="name" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="importid" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="importtable" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
    <constraint field="lid_actor_creator" exp_strength="0" constraints="0" unique_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="pk_edge" desc="" exp=""/>
    <constraint field="id_edge" desc="" exp=""/>
    <constraint field="lpk_descriptionsystem" desc="" exp=""/>
    <constraint field="lid_resource_1" desc="" exp=""/>
    <constraint field="lid_descriptionsystem_1" desc="" exp=""/>
    <constraint field="lid_descriptionsystem_2" desc="" exp=""/>
    <constraint field="material" desc="" exp=""/>
    <constraint field="nominaldiameter" desc="" exp=""/>
    <constraint field="pipetype" desc="" exp=""/>
    <constraint field="pipesubtype" desc="" exp=""/>
    <constraint field="pipeshape" desc="" exp=""/>
    <constraint field="height" desc="" exp=""/>
    <constraint field="laterals" desc="" exp=""/>
    <constraint field="flowtype" desc="" exp=""/>
    <constraint field="elevationup" desc="" exp=""/>
    <constraint field="elevationdown" desc="" exp=""/>
    <constraint field="depthup" desc="" exp=""/>
    <constraint field="depthdown" desc="" exp=""/>
    <constraint field="domain" desc="" exp=""/>
    <constraint field="location" desc="" exp=""/>
    <constraint field="accessibility" desc="" exp=""/>
    <constraint field="beddingmaterial" desc="" exp=""/>
    <constraint field="soiltype" desc="" exp=""/>
    <constraint field="soilmoisture" desc="" exp=""/>
    <constraint field="pk_descriptionsystem" desc="" exp=""/>
    <constraint field="id_descriptionsystem" desc="" exp=""/>
    <constraint field="lpk_object" desc="" exp=""/>
    <constraint field="strategicvalue" desc="" exp=""/>
    <constraint field="operational" desc="" exp=""/>
    <constraint field="structuralstate" desc="" exp=""/>
    <constraint field="operationalstate" desc="" exp=""/>
    <constraint field="dateoperationalcreation" desc="" exp=""/>
    <constraint field="dateoperationalcreationupper" desc="" exp=""/>
    <constraint field="operationaldatecreationaccuracy" desc="" exp=""/>
    <constraint field="datetimeoperationaldestruction" desc="" exp=""/>
    <constraint field="geotrackingxyquality" desc="" exp=""/>
    <constraint field="geotrackingzquality" desc="" exp=""/>
    <constraint field="geotrackingdate" desc="" exp=""/>
    <constraint field="geotrackingsource" desc="" exp=""/>
    <constraint field="parameters" desc="" exp=""/>
    <constraint field="parameterslist" desc="" exp=""/>
    <constraint field="city" desc="" exp=""/>
    <constraint field="streetname" desc="" exp=""/>
    <constraint field="streetupname" desc="" exp=""/>
    <constraint field="streetdownname" desc="" exp=""/>
    <constraint field="streetcomment" desc="" exp=""/>
    <constraint field="lid_actor_1" desc="" exp=""/>
    <constraint field="lid_actor_2" desc="" exp=""/>
    <constraint field="lid_actor_3" desc="" exp=""/>
    <constraint field="lid_facility" desc="" exp=""/>
    <constraint field="float_1" desc="" exp=""/>
    <constraint field="float_2" desc="" exp=""/>
    <constraint field="float_3" desc="" exp=""/>
    <constraint field="float_4" desc="" exp=""/>
    <constraint field="float_5" desc="" exp=""/>
    <constraint field="float_6" desc="" exp=""/>
    <constraint field="float_7" desc="" exp=""/>
    <constraint field="float_8" desc="" exp=""/>
    <constraint field="float_9" desc="" exp=""/>
    <constraint field="float_10" desc="" exp=""/>
    <constraint field="string_1" desc="" exp=""/>
    <constraint field="string_2" desc="" exp=""/>
    <constraint field="string_3" desc="" exp=""/>
    <constraint field="string_4" desc="" exp=""/>
    <constraint field="string_5" desc="" exp=""/>
    <constraint field="string_6" desc="" exp=""/>
    <constraint field="string_7" desc="" exp=""/>
    <constraint field="string_8" desc="" exp=""/>
    <constraint field="string_9" desc="" exp=""/>
    <constraint field="string_10" desc="" exp=""/>
    <constraint field="networktype" desc="" exp=""/>
    <constraint field="flowconditionupstream" desc="" exp=""/>
    <constraint field="flowconditiondownstream" desc="" exp=""/>
    <constraint field="systemfunction" desc="" exp=""/>
    <constraint field="pk_object" desc="" exp=""/>
    <constraint field="id_object" desc="" exp=""/>
    <constraint field="lpk_revision_begin" desc="" exp=""/>
    <constraint field="lpk_revision_end" desc="" exp=""/>
    <constraint field="datetimecreation" desc="" exp=""/>
    <constraint field="datetimemodification" desc="" exp=""/>
    <constraint field="datetimedestruction" desc="" exp=""/>
    <constraint field="comment" desc="" exp=""/>
    <constraint field="name" desc="" exp=""/>
    <constraint field="importid" desc="" exp=""/>
    <constraint field="importtable" desc="" exp=""/>
    <constraint field="lid_actor_creator" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column type="actions" hidden="1" width="-1"/>
      <column type="field" name="id_descriptionsystem" hidden="0" width="-1"/>
      <column type="field" name="lpk_descriptionsystem" hidden="0" width="-1"/>
      <column type="field" name="lid_descriptionsystem_1" hidden="0" width="-1"/>
      <column type="field" name="lid_descriptionsystem_2" hidden="0" width="-1"/>
      <column type="field" name="pk_descriptionsystem" hidden="0" width="-1"/>
      <column type="field" name="lpk_revision_begin" hidden="0" width="-1"/>
      <column type="field" name="lpk_revision_end" hidden="0" width="-1"/>
      <column type="field" name="datetimecreation" hidden="0" width="-1"/>
      <column type="field" name="datetimemodification" hidden="0" width="-1"/>
      <column type="field" name="datetimedestruction" hidden="0" width="-1"/>
      <column type="field" name="importid" hidden="0" width="-1"/>
      <column type="field" name="importtable" hidden="0" width="-1"/>
      <column type="field" name="pk_edge" hidden="0" width="-1"/>
      <column type="field" name="id_edge" hidden="0" width="-1"/>
      <column type="field" name="lid_resource_1" hidden="0" width="-1"/>
      <column type="field" name="material" hidden="0" width="-1"/>
      <column type="field" name="nominaldiameter" hidden="0" width="-1"/>
      <column type="field" name="pipetype" hidden="0" width="-1"/>
      <column type="field" name="pipesubtype" hidden="0" width="-1"/>
      <column type="field" name="pipeshape" hidden="0" width="-1"/>
      <column type="field" name="height" hidden="0" width="-1"/>
      <column type="field" name="laterals" hidden="0" width="-1"/>
      <column type="field" name="flowtype" hidden="0" width="-1"/>
      <column type="field" name="elevationup" hidden="0" width="-1"/>
      <column type="field" name="elevationdown" hidden="0" width="-1"/>
      <column type="field" name="depthup" hidden="0" width="-1"/>
      <column type="field" name="depthdown" hidden="0" width="-1"/>
      <column type="field" name="domain" hidden="0" width="-1"/>
      <column type="field" name="location" hidden="0" width="-1"/>
      <column type="field" name="accessibility" hidden="0" width="-1"/>
      <column type="field" name="beddingmaterial" hidden="0" width="-1"/>
      <column type="field" name="soiltype" hidden="0" width="-1"/>
      <column type="field" name="soilmoisture" hidden="0" width="-1"/>
      <column type="field" name="lpk_object" hidden="0" width="-1"/>
      <column type="field" name="strategicvalue" hidden="0" width="-1"/>
      <column type="field" name="operational" hidden="0" width="-1"/>
      <column type="field" name="structuralstate" hidden="0" width="-1"/>
      <column type="field" name="operationalstate" hidden="0" width="-1"/>
      <column type="field" name="dateoperationalcreation" hidden="0" width="-1"/>
      <column type="field" name="dateoperationalcreationupper" hidden="0" width="-1"/>
      <column type="field" name="operationaldatecreationaccuracy" hidden="0" width="-1"/>
      <column type="field" name="datetimeoperationaldestruction" hidden="0" width="-1"/>
      <column type="field" name="geotrackingxyquality" hidden="0" width="-1"/>
      <column type="field" name="geotrackingzquality" hidden="0" width="-1"/>
      <column type="field" name="geotrackingdate" hidden="0" width="-1"/>
      <column type="field" name="geotrackingsource" hidden="0" width="-1"/>
      <column type="field" name="parameters" hidden="0" width="-1"/>
      <column type="field" name="parameterslist" hidden="0" width="-1"/>
      <column type="field" name="city" hidden="0" width="-1"/>
      <column type="field" name="streetname" hidden="0" width="-1"/>
      <column type="field" name="streetupname" hidden="0" width="-1"/>
      <column type="field" name="streetdownname" hidden="0" width="-1"/>
      <column type="field" name="streetcomment" hidden="0" width="-1"/>
      <column type="field" name="lid_actor_1" hidden="0" width="-1"/>
      <column type="field" name="lid_actor_2" hidden="0" width="-1"/>
      <column type="field" name="lid_actor_3" hidden="0" width="-1"/>
      <column type="field" name="lid_facility" hidden="0" width="-1"/>
      <column type="field" name="float_1" hidden="0" width="-1"/>
      <column type="field" name="float_2" hidden="0" width="-1"/>
      <column type="field" name="float_3" hidden="0" width="-1"/>
      <column type="field" name="float_4" hidden="0" width="-1"/>
      <column type="field" name="float_5" hidden="0" width="-1"/>
      <column type="field" name="float_6" hidden="0" width="-1"/>
      <column type="field" name="float_7" hidden="0" width="-1"/>
      <column type="field" name="float_8" hidden="0" width="-1"/>
      <column type="field" name="float_9" hidden="0" width="-1"/>
      <column type="field" name="float_10" hidden="0" width="-1"/>
      <column type="field" name="string_1" hidden="0" width="-1"/>
      <column type="field" name="string_2" hidden="0" width="-1"/>
      <column type="field" name="string_3" hidden="0" width="-1"/>
      <column type="field" name="string_4" hidden="0" width="-1"/>
      <column type="field" name="string_5" hidden="0" width="-1"/>
      <column type="field" name="string_6" hidden="0" width="-1"/>
      <column type="field" name="string_7" hidden="0" width="-1"/>
      <column type="field" name="string_8" hidden="0" width="-1"/>
      <column type="field" name="string_9" hidden="0" width="-1"/>
      <column type="field" name="string_10" hidden="0" width="-1"/>
      <column type="field" name="networktype" hidden="0" width="-1"/>
      <column type="field" name="flowconditionupstream" hidden="0" width="-1"/>
      <column type="field" name="flowconditiondownstream" hidden="0" width="-1"/>
      <column type="field" name="systemfunction" hidden="0" width="-1"/>
      <column type="field" name="pk_object" hidden="0" width="-1"/>
      <column type="field" name="id_object" hidden="0" width="-1"/>
      <column type="field" name="comment" hidden="0" width="-1"/>
      <column type="field" name="name" hidden="0" width="-1"/>
      <column type="field" name="lid_actor_creator" hidden="0" width="-1"/>
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
  <editforminitfilepath>../../Données/Tables ARTELIA2</editforminitfilepath>
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
  <editorlayout>tablayout</editorlayout>
  <attributeEditorForm>
    <attributeEditorContainer columnCount="1" name="Réseaux" groupBox="0" visibilityExpressionEnabled="0" showLabel="1" visibilityExpression="">
      <attributeEditorField name="TYP_RESEAU" index="-1" showLabel="1"/>
      <attributeEditorField name="NAT_RESEAU" index="-1" showLabel="1"/>
      <attributeEditorField name="TYP_ECOUL" index="-1" showLabel="1"/>
      <attributeEditorField name="FORME_CANA" index="-1" showLabel="1"/>
      <attributeEditorField name="DIAMETRE" index="-1" showLabel="1"/>
      <attributeEditorField name="MATERIAUX" index="-1" showLabel="1"/>
      <attributeEditorField name="HAUTEUR" index="-1" showLabel="1"/>
      <attributeEditorField name="LARGEUR" index="-1" showLabel="1"/>
      <attributeEditorField name="ANNEEPOSE" index="-1" showLabel="1"/>
      <attributeEditorField name="OBSERVATIO" index="-1" showLabel="1"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field name="accessibility" editable="1"/>
    <field name="altAmont" editable="1"/>
    <field name="altAval" editable="1"/>
    <field name="annee_debut_pose" editable="1"/>
    <field name="annee_fin_pose" editable="1"/>
    <field name="beddingmaterial" editable="1"/>
    <field name="branchement" editable="1"/>
    <field name="city" editable="1"/>
    <field name="comment" editable="1"/>
    <field name="commentaire" editable="1"/>
    <field name="dateGeoloc" editable="1"/>
    <field name="date_miseHorsService" editable="1"/>
    <field name="dateoperationalcreation" editable="1"/>
    <field name="dateoperationalcreationupper" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimemodification" editable="1"/>
    <field name="datetimeoperationaldestruction" editable="1"/>
    <field name="depthdown" editable="1"/>
    <field name="depthup" editable="1"/>
    <field name="diametreNominal" editable="1"/>
    <field name="domain" editable="1"/>
    <field name="domaine" editable="1"/>
    <field name="elevationdown" editable="1"/>
    <field name="elevationup" editable="1"/>
    <field name="enservice" editable="1"/>
    <field name="etatfonct" editable="1"/>
    <field name="etatsol" editable="1"/>
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
    <field name="flowconditiondownstream" editable="1"/>
    <field name="flowconditionupstream" editable="1"/>
    <field name="flowtype" editable="1"/>
    <field name="fonctionCannAss" editable="1"/>
    <field name="formecanalisation" editable="1"/>
    <field name="geotrackingdate" editable="1"/>
    <field name="geotrackingsource" editable="1"/>
    <field name="geotrackingxyquality" editable="1"/>
    <field name="geotrackingzquality" editable="1"/>
    <field name="hauteur" editable="1"/>
    <field name="height" editable="1"/>
    <field name="id_descriptionsystem" editable="1"/>
    <field name="id_edge" editable="1"/>
    <field name="id_infralineaire" editable="1"/>
    <field name="id_object" editable="1"/>
    <field name="id_objet" editable="1"/>
    <field name="implantation" editable="1"/>
    <field name="importancestrat" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="intervenant_1" editable="1"/>
    <field name="laterals" editable="1"/>
    <field name="libelle" editable="1"/>
    <field name="lid_actor_1" editable="1"/>
    <field name="lid_actor_2" editable="1"/>
    <field name="lid_actor_3" editable="1"/>
    <field name="lid_actor_creator" editable="1"/>
    <field name="lid_descriptionsystem_1" editable="1"/>
    <field name="lid_descriptionsystem_2" editable="1"/>
    <field name="lid_facility" editable="1"/>
    <field name="lid_resource_1" editable="1"/>
    <field name="lid_ressource_1" editable="1"/>
    <field name="listeparametres" editable="1"/>
    <field name="litdepose" editable="1"/>
    <field name="location" editable="1"/>
    <field name="lpk_descriptionsystem" editable="1"/>
    <field name="lpk_object" editable="1"/>
    <field name="lpk_objet" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="material" editable="1"/>
    <field name="materiau" editable="1"/>
    <field name="modeCirculation" editable="1"/>
    <field name="name" editable="1"/>
    <field name="networktype" editable="1"/>
    <field name="nominaldiameter" editable="1"/>
    <field name="operational" editable="1"/>
    <field name="operationaldatecreationaccuracy" editable="1"/>
    <field name="operationalstate" editable="1"/>
    <field name="parameters" editable="1"/>
    <field name="parameterslist" editable="1"/>
    <field name="parametres" editable="1"/>
    <field name="pipeshape" editable="1"/>
    <field name="pipesubtype" editable="1"/>
    <field name="pipetype" editable="1"/>
    <field name="pk_descriptionsystem" editable="1"/>
    <field name="pk_edge" editable="1"/>
    <field name="pk_infralineaire" editable="1"/>
    <field name="pk_object" editable="1"/>
    <field name="pk_objet" editable="1"/>
    <field name="precision_pose" editable="1"/>
    <field name="profamont" editable="1"/>
    <field name="profaval" editable="1"/>
    <field name="qualiteGeolocZ" editable="1"/>
    <field name="qualitegeolocXY" editable="1"/>
    <field name="rue_complement" editable="1"/>
    <field name="rue_libdebut" editable="1"/>
    <field name="rue_libelle" editable="1"/>
    <field name="rue_libfin" editable="1"/>
    <field name="soilmoisture" editable="1"/>
    <field name="soiltype" editable="1"/>
    <field name="sourceGeoloc" editable="1"/>
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
    <field name="systemfunction" editable="1"/>
    <field name="typeReseau" editable="1"/>
    <field name="typesol" editable="1"/>
    <field name="visitable" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="accessibility" labelOnTop="0"/>
    <field name="altAmont" labelOnTop="0"/>
    <field name="altAval" labelOnTop="0"/>
    <field name="annee_debut_pose" labelOnTop="0"/>
    <field name="annee_fin_pose" labelOnTop="0"/>
    <field name="beddingmaterial" labelOnTop="0"/>
    <field name="branchement" labelOnTop="0"/>
    <field name="city" labelOnTop="0"/>
    <field name="comment" labelOnTop="0"/>
    <field name="commentaire" labelOnTop="0"/>
    <field name="dateGeoloc" labelOnTop="0"/>
    <field name="date_miseHorsService" labelOnTop="0"/>
    <field name="dateoperationalcreation" labelOnTop="0"/>
    <field name="dateoperationalcreationupper" labelOnTop="0"/>
    <field name="datetimecreation" labelOnTop="0"/>
    <field name="datetimedestruction" labelOnTop="0"/>
    <field name="datetimemodification" labelOnTop="0"/>
    <field name="datetimeoperationaldestruction" labelOnTop="0"/>
    <field name="depthdown" labelOnTop="0"/>
    <field name="depthup" labelOnTop="0"/>
    <field name="diametreNominal" labelOnTop="0"/>
    <field name="domain" labelOnTop="0"/>
    <field name="domaine" labelOnTop="0"/>
    <field name="elevationdown" labelOnTop="0"/>
    <field name="elevationup" labelOnTop="0"/>
    <field name="enservice" labelOnTop="0"/>
    <field name="etatfonct" labelOnTop="0"/>
    <field name="etatsol" labelOnTop="0"/>
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
    <field name="flowconditiondownstream" labelOnTop="0"/>
    <field name="flowconditionupstream" labelOnTop="0"/>
    <field name="flowtype" labelOnTop="0"/>
    <field name="fonctionCannAss" labelOnTop="0"/>
    <field name="formecanalisation" labelOnTop="0"/>
    <field name="geotrackingdate" labelOnTop="0"/>
    <field name="geotrackingsource" labelOnTop="0"/>
    <field name="geotrackingxyquality" labelOnTop="0"/>
    <field name="geotrackingzquality" labelOnTop="0"/>
    <field name="hauteur" labelOnTop="0"/>
    <field name="height" labelOnTop="0"/>
    <field name="id_descriptionsystem" labelOnTop="0"/>
    <field name="id_edge" labelOnTop="0"/>
    <field name="id_infralineaire" labelOnTop="0"/>
    <field name="id_object" labelOnTop="0"/>
    <field name="id_objet" labelOnTop="0"/>
    <field name="implantation" labelOnTop="0"/>
    <field name="importancestrat" labelOnTop="0"/>
    <field name="importid" labelOnTop="0"/>
    <field name="importtable" labelOnTop="0"/>
    <field name="intervenant_1" labelOnTop="0"/>
    <field name="laterals" labelOnTop="0"/>
    <field name="libelle" labelOnTop="0"/>
    <field name="lid_actor_1" labelOnTop="0"/>
    <field name="lid_actor_2" labelOnTop="0"/>
    <field name="lid_actor_3" labelOnTop="0"/>
    <field name="lid_actor_creator" labelOnTop="0"/>
    <field name="lid_descriptionsystem_1" labelOnTop="0"/>
    <field name="lid_descriptionsystem_2" labelOnTop="0"/>
    <field name="lid_facility" labelOnTop="0"/>
    <field name="lid_resource_1" labelOnTop="0"/>
    <field name="lid_ressource_1" labelOnTop="0"/>
    <field name="listeparametres" labelOnTop="0"/>
    <field name="litdepose" labelOnTop="0"/>
    <field name="location" labelOnTop="0"/>
    <field name="lpk_descriptionsystem" labelOnTop="0"/>
    <field name="lpk_object" labelOnTop="0"/>
    <field name="lpk_objet" labelOnTop="0"/>
    <field name="lpk_revision_begin" labelOnTop="0"/>
    <field name="lpk_revision_end" labelOnTop="0"/>
    <field name="material" labelOnTop="0"/>
    <field name="materiau" labelOnTop="0"/>
    <field name="modeCirculation" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="networktype" labelOnTop="0"/>
    <field name="nominaldiameter" labelOnTop="0"/>
    <field name="operational" labelOnTop="0"/>
    <field name="operationaldatecreationaccuracy" labelOnTop="0"/>
    <field name="operationalstate" labelOnTop="0"/>
    <field name="parameters" labelOnTop="0"/>
    <field name="parameterslist" labelOnTop="0"/>
    <field name="parametres" labelOnTop="0"/>
    <field name="pipeshape" labelOnTop="0"/>
    <field name="pipesubtype" labelOnTop="0"/>
    <field name="pipetype" labelOnTop="0"/>
    <field name="pk_descriptionsystem" labelOnTop="0"/>
    <field name="pk_edge" labelOnTop="0"/>
    <field name="pk_infralineaire" labelOnTop="0"/>
    <field name="pk_object" labelOnTop="0"/>
    <field name="pk_objet" labelOnTop="0"/>
    <field name="precision_pose" labelOnTop="0"/>
    <field name="profamont" labelOnTop="0"/>
    <field name="profaval" labelOnTop="0"/>
    <field name="qualiteGeolocZ" labelOnTop="0"/>
    <field name="qualitegeolocXY" labelOnTop="0"/>
    <field name="rue_complement" labelOnTop="0"/>
    <field name="rue_libdebut" labelOnTop="0"/>
    <field name="rue_libelle" labelOnTop="0"/>
    <field name="rue_libfin" labelOnTop="0"/>
    <field name="soilmoisture" labelOnTop="0"/>
    <field name="soiltype" labelOnTop="0"/>
    <field name="sourceGeoloc" labelOnTop="0"/>
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
    <field name="systemfunction" labelOnTop="0"/>
    <field name="typeReseau" labelOnTop="0"/>
    <field name="typesol" labelOnTop="0"/>
    <field name="visitable" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE( "TYP_RESEAU", '&lt;NULL>' )</previewExpression>
  <mapTip>TYP_RESEAU</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
