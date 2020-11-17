<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyDrawingHints="1" labelsEnabled="1" simplifyLocal="1" simplifyMaxScale="1" version="3.10.0-A CoruÃ±a" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" minScale="1e+08" simplifyAlgorithm="0" maxScale="0" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" type="RuleRenderer" symbollevels="0" forceraster="0">
    <rules key="{5e78f11d-4178-4ed7-8af6-f80178c4ba25}">
      <rule filter=" &quot;branchement&quot; = 1" label="Branchement" key="{c647d32b-b632-485f-bd3c-91150bd75a8b}">
        <rule filter="&quot;lid_descriptionsystem_1&quot; IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL" key="{c64b87c5-2e70-47ec-a94f-a9b46d7ca120}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02')" symbol="0" label="Eaux usées" key="{9739976b-e285-47e5-a9b3-f03be0ead4d2}">
            <rule filter=" $length >0.01" scalemindenom="5000" checkstate="0" symbol="1" label="0 - 5000" key="{33fbb348-5c57-44e8-b6fc-be6c61d5397f}"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="2" label="Unitaire" key="{b58611c9-3fed-43bb-b53c-b9e470bd0e7a}">
            <rule filter=" $length >0.01" scalemindenom="5000" checkstate="0" symbol="3" label="0 - 5000" key="{aadc49a6-4a5f-49a6-b31e-fb53caa7da29}"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03')" symbol="4" label="Eaux pluviales" key="{79228b2f-3bcc-41db-b9b2-7a63236519b9}">
            <rule filter=" $length >0.01" scalemindenom="5000" checkstate="0" symbol="5" label="0 - 5000" key="{557f2669-c040-4245-b628-e29d512012e9}"/>
          </rule>
        </rule>
        <rule filter="ELSE" key="{766e1a38-f6d0-4e9e-9f69-8e4b0e647dbd}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02')" symbol="6" label="Eaux usées" key="{056c6700-936d-4dc5-94bb-444be6ac21c1}">
            <rule filter=" $length >0.01" scalemindenom="5000" checkstate="0" symbol="7" label="0 - 5000" key="{e16e7031-5f55-4999-9a28-5147490d9c50}"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="8" label="Unitaire" key="{d02aedf7-0a96-43e6-b6e4-05de94c29c01}">
            <rule filter=" $length >0.01" scalemindenom="5000" checkstate="0" symbol="9" label="0 - 5000" key="{05870733-4af5-4c67-9521-0638e39097b8}"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03')" symbol="10" label="Eaux pluviales" key="{e5d88765-3a5e-45c9-9d40-4f4ccb76f3d1}">
            <rule filter=" $length >0.01" scalemindenom="5000" checkstate="0" symbol="11" label="0 - 5000" key="{59da33b5-8378-418d-8d13-e3d77b53db3b}"/>
          </rule>
        </rule>
      </rule>
      <rule filter=" &quot;branchement&quot; = 0" label="Branchement" key="{06826450-6078-4741-8f6d-022aaa3d991c}">
        <rule filter=" &quot;lid_descriptionsystem_1&quot;  IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL" key="{88663e10-e0fc-4596-9b17-73b72cdd6b17}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02')" symbol="12" label="Eaux usées" key="{1a389d12-0d10-440b-bc98-99359171cecd}">
            <rule filter=" $length >0.01" checkstate="0" symbol="13" label="0 - 5000" key="{7ea2414d-2527-4219-bd96-abcaebd05d23}" scalemaxdenom="5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="14" label="Unitaire" key="{68b407af-ccdc-4174-9cf3-b76afd97b02a}">
            <rule filter=" $length >0.01" checkstate="0" symbol="15" label="0 - 5000" key="{a3bf1739-5ac1-4b64-b6bc-d90c27195dff}" scalemaxdenom="5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03')" symbol="16" label="Eaux pluviales" key="{63296647-4e1b-4afe-b24e-22e8e31ff386}">
            <rule filter=" $length >0.01" checkstate="0" symbol="17" label="0 - 5000" key="{ac2c4c84-b8b9-4622-9ad9-2f34d7a3a2d5}" scalemaxdenom="5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('USE','02') and &quot;fonctionCannAss&quot;  =   '02' " symbol="18" label="Refoulement eaux usées" key="{3f65b50e-0bf2-40c6-a77b-07ef1672c36e}"/>
        </rule>
        <rule filter="ELSE" key="{33f84cfd-6977-4c2a-9cb5-fc1b120f5186}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02') and &quot;fonctionCannAss&quot;  =   '01'" symbol="19" label="Eaux usées" key="{d06eff82-6570-49e6-a3db-2f57ba6f18f1}">
            <rule filter=" $length >0.01" checkstate="0" symbol="20" label="0 - 5000" key="{9da33136-3b87-432c-acbd-8f6df6ab8b99}" scalemaxdenom="5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="21" label="Unitaire" key="{a3ec9bfa-cfb2-481e-bc88-423fe89f7a96}">
            <rule filter=" $length >0.01" checkstate="0" symbol="22" label="0 - 5000" key="{582a22e5-bd4f-47aa-a7fd-95ffaeac2744}" scalemaxdenom="5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03') and &quot;fonctionCannAss&quot;  =   '01'" symbol="23" label="Eaux pluviales" key="{0120d564-3526-4085-b40c-57703191a0c7}">
            <rule filter=" $length >0.01" checkstate="0" symbol="24" label="0 - 5000" key="{bd85613e-74eb-4a63-93b8-65e0b1a9c295}" scalemaxdenom="5000"/>
          </rule>
          <rule filter=" &quot;typeReseau&quot; IN ('PLU','03') and  &quot;fonctionCannAss&quot; = '02'" symbol="25" label="Refoulement eaux pluviales " key="{95b411e6-2b95-4638-810c-cebf2f9a9a05}"/>
        </rule>
      </rule>
      <rule filter="ELSE" symbol="26" key="{146b5a78-5b72-4838-8cb1-ae306bc010b5}">
        <rule checkstate="0" symbol="27" label="0 - 5000" key="{d337d640-72b2-476f-9aeb-813fdd0a2e58}" scalemaxdenom="5000"/>
      </rule>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" type="line" name="0" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="1" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@1@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="10" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="11" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@11@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="12" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="13" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@13@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="14" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="15" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@15@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="16" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="17" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@17@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="18" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="19" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="2" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="20" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@20@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="21" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="22" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@22@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="23" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="24" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@24@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="25" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="26" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="27" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@27@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="3" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@3@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="4" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="5" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@5@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="6" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="7" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@7@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="8" alpha="1" force_rhr="0">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
      <symbol clip_to_extent="1" type="line" name="9" alpha="1" force_rhr="0">
        <layer class="MarkerLine" pass="0" enabled="1" locked="0">
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
          <symbol clip_to_extent="1" type="marker" name="@9@0" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
      <text-style namedStyle="Normal" fontKerning="1" blendMode="0" fontSizeUnit="Point" textOpacity="1" fontLetterSpacing="0" previewBkgrdColor="255,255,255,255" fontUnderline="0" isExpression="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontSize="8.25" fontCapitals="0" fontItalic="0" textColor="0,0,0,255" fontWeight="50" fieldName=" &quot;diametreNominal&quot; *1000" fontStrikeout="0" textOrientation="horizontal" multilineHeight="1" useSubstitutions="0" fontWordSpacing="0" fontFamily="MS Shell Dlg 2">
        <text-buffer bufferColor="255,255,255,255" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferOpacity="1" bufferJoinStyle="128" bufferSizeUnits="MM" bufferSize="1" bufferNoFill="0" bufferDraw="1"/>
        <background shapeRadiiUnit="MM" shapeSizeUnit="MM" shapeDraw="0" shapeBorderWidthUnit="MM" shapeSVGFile="" shapeSizeType="0" shapeRadiiX="0" shapeOpacity="1" shapeBorderColor="128,128,128,255" shapeSizeY="0" shapeRotationType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeBorderWidth="0" shapeRotation="0" shapeType="0" shapeOffsetUnit="MM" shapeOffsetY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeJoinStyle="64" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeBlendMode="0">
          <symbol clip_to_extent="1" type="marker" name="markerSymbol" alpha="1" force_rhr="0">
            <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
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
        <shadow shadowOpacity="0.7" shadowColor="0,0,0,255" shadowRadiusAlphaOnly="0" shadowBlendMode="6" shadowRadius="1.5" shadowScale="100" shadowOffsetAngle="135" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowDraw="0" shadowOffsetDist="1" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" addDirectionSymbol="0" wrapChar="" decimals="3" multilineAlign="4294967295" formatNumbers="0" autoWrapLength="0" rightDirectionSymbol=">" plussign="0" placeDirectionSymbol="0" reverseDirectionSymbol="0"/>
      <placement geometryGeneratorType="PointGeometry" repeatDistance="0" distUnits="MM" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistanceUnits="MM" centroidWhole="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-25" dist="0.5" geometryGeneratorEnabled="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" fitInPolygonOnly="0" distMapUnitScale="3x:0,0,0,0,0,0" placementFlags="2" rotationAngle="0" yOffset="0" xOffset="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" offsetUnits="MapUnit" overrunDistance="0" layerType="LineGeometry" placement="3" quadOffset="4" priority="5" geometryGenerator="" overrunDistanceUnit="MM" centroidInside="0" offsetType="0" maxCurvedCharAngleIn="25"/>
      <rendering displayAll="0" mergeLines="1" obstacleFactor="1" limitNumLabels="0" obstacleType="0" fontMaxPixelSize="10000" scaleMax="5000" zIndex="0" scaleMin="1" scaleVisibility="1" obstacle="1" minFeatureSize="2" maxNumLabels="2000" upsidedownLabels="0" drawLabels="1" fontLimitPixelSize="0" fontMinPixelSize="3" labelPerPart="0"/>
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
          <Option type="QString" name="lineSymbol" value="&lt;symbol clip_to_extent=&quot;1&quot; type=&quot;line&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; pass=&quot;0&quot; enabled=&quot;1&quot; locked=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
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
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory backgroundColor="#ffffff" lineSizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" maxScaleDenominator="1e+08" minScaleDenominator="0" opacity="1" penColor="#000000" penAlpha="255" backgroundAlpha="255" lineSizeType="MM" sizeScale="3x:0,0,0,0,0,0" enabled="0" width="15" barWidth="5" scaleBasedVisibility="0" labelPlacementMethod="XHeight" height="15" rotationOffset="270" penWidth="0" scaleDependency="Area" sizeType="MM" minimumSize="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" dist="0" priority="0" showAll="1" linePlacementFlags="2" placement="2" obstacle="0">
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
    <field name="pk_infralineaire">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_infralineaire">
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
    <field name="lid_ressource_1">
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
    <field name="materiau">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="diametreNominal">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="formecanalisation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="hauteur">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="branchement">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="modeCirculation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="typeReseau">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="fonctionCannAss">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="altAmont">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="altAval">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="profamont">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="profaval">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="domaine">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="implantation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="visitable">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="litdepose">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="typesol">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="etatsol">
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
    <field name="lpk_objet">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="importancestrat">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="etatfonct">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="qualitegeolocXY">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="qualiteGeolocZ">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dateGeoloc">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sourceGeoloc">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="enservice">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="annee_debut_pose">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="annee_fin_pose">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="precision_pose">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="date_miseHorsService">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="parametres">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="listeparametres">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rue_libelle">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rue_libdebut">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rue_libfin">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rue_complement">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="intervenant_1">
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
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="pk_infralineaire" name=""/>
    <alias index="1" field="id_infralineaire" name=""/>
    <alias index="2" field="lpk_descriptionsystem" name=""/>
    <alias index="3" field="lid_ressource_1" name=""/>
    <alias index="4" field="lid_descriptionsystem_1" name=""/>
    <alias index="5" field="lid_descriptionsystem_2" name=""/>
    <alias index="6" field="materiau" name=""/>
    <alias index="7" field="diametreNominal" name=""/>
    <alias index="8" field="formecanalisation" name=""/>
    <alias index="9" field="hauteur" name="Hauteur de l'aqueduc / bâti"/>
    <alias index="10" field="branchement" name=""/>
    <alias index="11" field="modeCirculation" name=""/>
    <alias index="12" field="typeReseau" name=""/>
    <alias index="13" field="fonctionCannAss" name=""/>
    <alias index="14" field="altAmont" name=""/>
    <alias index="15" field="altAval" name=""/>
    <alias index="16" field="profamont" name=""/>
    <alias index="17" field="profaval" name=""/>
    <alias index="18" field="domaine" name=""/>
    <alias index="19" field="implantation" name=""/>
    <alias index="20" field="visitable" name=""/>
    <alias index="21" field="litdepose" name=""/>
    <alias index="22" field="typesol" name=""/>
    <alias index="23" field="etatsol" name=""/>
    <alias index="24" field="pk_descriptionsystem" name=""/>
    <alias index="25" field="id_descriptionsystem" name=""/>
    <alias index="26" field="lpk_objet" name=""/>
    <alias index="27" field="importancestrat" name=""/>
    <alias index="28" field="etatfonct" name=""/>
    <alias index="29" field="qualitegeolocXY" name=""/>
    <alias index="30" field="qualiteGeolocZ" name=""/>
    <alias index="31" field="dateGeoloc" name=""/>
    <alias index="32" field="sourceGeoloc" name=""/>
    <alias index="33" field="enservice" name=""/>
    <alias index="34" field="annee_debut_pose" name=""/>
    <alias index="35" field="annee_fin_pose" name=""/>
    <alias index="36" field="precision_pose" name=""/>
    <alias index="37" field="date_miseHorsService" name=""/>
    <alias index="38" field="parametres" name=""/>
    <alias index="39" field="listeparametres" name=""/>
    <alias index="40" field="rue_libelle" name=""/>
    <alias index="41" field="rue_libdebut" name=""/>
    <alias index="42" field="rue_libfin" name=""/>
    <alias index="43" field="rue_complement" name=""/>
    <alias index="44" field="intervenant_1" name=""/>
    <alias index="45" field="pk_objet" name=""/>
    <alias index="46" field="id_objet" name=""/>
    <alias index="47" field="lpk_revision_begin" name=""/>
    <alias index="48" field="lpk_revision_end" name=""/>
    <alias index="49" field="datetimecreation" name=""/>
    <alias index="50" field="datetimemodification" name=""/>
    <alias index="51" field="datetimedestruction" name=""/>
    <alias index="52" field="commentaire" name=""/>
    <alias index="53" field="libelle" name=""/>
    <alias index="54" field="importid" name=""/>
    <alias index="55" field="importtable" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="pk_infralineaire" expression=""/>
    <default applyOnUpdate="0" field="id_infralineaire" expression=""/>
    <default applyOnUpdate="0" field="lpk_descriptionsystem" expression=""/>
    <default applyOnUpdate="0" field="lid_ressource_1" expression=""/>
    <default applyOnUpdate="0" field="lid_descriptionsystem_1" expression=""/>
    <default applyOnUpdate="0" field="lid_descriptionsystem_2" expression=""/>
    <default applyOnUpdate="0" field="materiau" expression=""/>
    <default applyOnUpdate="0" field="diametreNominal" expression=""/>
    <default applyOnUpdate="0" field="formecanalisation" expression=""/>
    <default applyOnUpdate="0" field="hauteur" expression=""/>
    <default applyOnUpdate="0" field="branchement" expression=""/>
    <default applyOnUpdate="0" field="modeCirculation" expression=""/>
    <default applyOnUpdate="0" field="typeReseau" expression=""/>
    <default applyOnUpdate="0" field="fonctionCannAss" expression=""/>
    <default applyOnUpdate="0" field="altAmont" expression=""/>
    <default applyOnUpdate="0" field="altAval" expression=""/>
    <default applyOnUpdate="0" field="profamont" expression=""/>
    <default applyOnUpdate="0" field="profaval" expression=""/>
    <default applyOnUpdate="0" field="domaine" expression=""/>
    <default applyOnUpdate="0" field="implantation" expression=""/>
    <default applyOnUpdate="0" field="visitable" expression=""/>
    <default applyOnUpdate="0" field="litdepose" expression=""/>
    <default applyOnUpdate="0" field="typesol" expression=""/>
    <default applyOnUpdate="0" field="etatsol" expression=""/>
    <default applyOnUpdate="0" field="pk_descriptionsystem" expression=""/>
    <default applyOnUpdate="0" field="id_descriptionsystem" expression=""/>
    <default applyOnUpdate="0" field="lpk_objet" expression=""/>
    <default applyOnUpdate="0" field="importancestrat" expression=""/>
    <default applyOnUpdate="0" field="etatfonct" expression=""/>
    <default applyOnUpdate="0" field="qualitegeolocXY" expression=""/>
    <default applyOnUpdate="0" field="qualiteGeolocZ" expression=""/>
    <default applyOnUpdate="0" field="dateGeoloc" expression=""/>
    <default applyOnUpdate="0" field="sourceGeoloc" expression=""/>
    <default applyOnUpdate="0" field="enservice" expression=""/>
    <default applyOnUpdate="0" field="annee_debut_pose" expression=""/>
    <default applyOnUpdate="0" field="annee_fin_pose" expression=""/>
    <default applyOnUpdate="0" field="precision_pose" expression=""/>
    <default applyOnUpdate="0" field="date_miseHorsService" expression=""/>
    <default applyOnUpdate="0" field="parametres" expression=""/>
    <default applyOnUpdate="0" field="listeparametres" expression=""/>
    <default applyOnUpdate="0" field="rue_libelle" expression=""/>
    <default applyOnUpdate="0" field="rue_libdebut" expression=""/>
    <default applyOnUpdate="0" field="rue_libfin" expression=""/>
    <default applyOnUpdate="0" field="rue_complement" expression=""/>
    <default applyOnUpdate="0" field="intervenant_1" expression=""/>
    <default applyOnUpdate="0" field="pk_objet" expression=""/>
    <default applyOnUpdate="0" field="id_objet" expression=""/>
    <default applyOnUpdate="0" field="lpk_revision_begin" expression=""/>
    <default applyOnUpdate="0" field="lpk_revision_end" expression=""/>
    <default applyOnUpdate="0" field="datetimecreation" expression=""/>
    <default applyOnUpdate="0" field="datetimemodification" expression=""/>
    <default applyOnUpdate="0" field="datetimedestruction" expression=""/>
    <default applyOnUpdate="0" field="commentaire" expression=""/>
    <default applyOnUpdate="0" field="libelle" expression=""/>
    <default applyOnUpdate="0" field="importid" expression=""/>
    <default applyOnUpdate="0" field="importtable" expression=""/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" field="pk_infralineaire" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="id_infralineaire" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="lpk_descriptionsystem" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="lid_ressource_1" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="lid_descriptionsystem_1" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="lid_descriptionsystem_2" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="materiau" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="diametreNominal" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="formecanalisation" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="hauteur" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="branchement" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="modeCirculation" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="typeReseau" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="fonctionCannAss" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="altAmont" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="altAval" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="profamont" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="profaval" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="domaine" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="implantation" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="visitable" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="litdepose" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="typesol" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="etatsol" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="pk_descriptionsystem" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="id_descriptionsystem" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="lpk_objet" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="importancestrat" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="etatfonct" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="qualitegeolocXY" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="qualiteGeolocZ" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="dateGeoloc" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="sourceGeoloc" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="enservice" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="annee_debut_pose" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="annee_fin_pose" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="precision_pose" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="date_miseHorsService" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="parametres" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="listeparametres" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="rue_libelle" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="rue_libdebut" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="rue_libfin" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="rue_complement" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="intervenant_1" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="pk_objet" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="id_objet" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="lpk_revision_begin" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="lpk_revision_end" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="datetimecreation" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="datetimemodification" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="datetimedestruction" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="commentaire" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="libelle" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="importid" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="importtable" notnull_strength="0" unique_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="pk_infralineaire" exp=""/>
    <constraint desc="" field="id_infralineaire" exp=""/>
    <constraint desc="" field="lpk_descriptionsystem" exp=""/>
    <constraint desc="" field="lid_ressource_1" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_1" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_2" exp=""/>
    <constraint desc="" field="materiau" exp=""/>
    <constraint desc="" field="diametreNominal" exp=""/>
    <constraint desc="" field="formecanalisation" exp=""/>
    <constraint desc="" field="hauteur" exp=""/>
    <constraint desc="" field="branchement" exp=""/>
    <constraint desc="" field="modeCirculation" exp=""/>
    <constraint desc="" field="typeReseau" exp=""/>
    <constraint desc="" field="fonctionCannAss" exp=""/>
    <constraint desc="" field="altAmont" exp=""/>
    <constraint desc="" field="altAval" exp=""/>
    <constraint desc="" field="profamont" exp=""/>
    <constraint desc="" field="profaval" exp=""/>
    <constraint desc="" field="domaine" exp=""/>
    <constraint desc="" field="implantation" exp=""/>
    <constraint desc="" field="visitable" exp=""/>
    <constraint desc="" field="litdepose" exp=""/>
    <constraint desc="" field="typesol" exp=""/>
    <constraint desc="" field="etatsol" exp=""/>
    <constraint desc="" field="pk_descriptionsystem" exp=""/>
    <constraint desc="" field="id_descriptionsystem" exp=""/>
    <constraint desc="" field="lpk_objet" exp=""/>
    <constraint desc="" field="importancestrat" exp=""/>
    <constraint desc="" field="etatfonct" exp=""/>
    <constraint desc="" field="qualitegeolocXY" exp=""/>
    <constraint desc="" field="qualiteGeolocZ" exp=""/>
    <constraint desc="" field="dateGeoloc" exp=""/>
    <constraint desc="" field="sourceGeoloc" exp=""/>
    <constraint desc="" field="enservice" exp=""/>
    <constraint desc="" field="annee_debut_pose" exp=""/>
    <constraint desc="" field="annee_fin_pose" exp=""/>
    <constraint desc="" field="precision_pose" exp=""/>
    <constraint desc="" field="date_miseHorsService" exp=""/>
    <constraint desc="" field="parametres" exp=""/>
    <constraint desc="" field="listeparametres" exp=""/>
    <constraint desc="" field="rue_libelle" exp=""/>
    <constraint desc="" field="rue_libdebut" exp=""/>
    <constraint desc="" field="rue_libfin" exp=""/>
    <constraint desc="" field="rue_complement" exp=""/>
    <constraint desc="" field="intervenant_1" exp=""/>
    <constraint desc="" field="pk_objet" exp=""/>
    <constraint desc="" field="id_objet" exp=""/>
    <constraint desc="" field="lpk_revision_begin" exp=""/>
    <constraint desc="" field="lpk_revision_end" exp=""/>
    <constraint desc="" field="datetimecreation" exp=""/>
    <constraint desc="" field="datetimemodification" exp=""/>
    <constraint desc="" field="datetimedestruction" exp=""/>
    <constraint desc="" field="commentaire" exp=""/>
    <constraint desc="" field="libelle" exp=""/>
    <constraint desc="" field="importid" exp=""/>
    <constraint desc="" field="importtable" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" type="field" name="id_infralineaire" hidden="0"/>
      <column width="-1" type="field" name="id_objet" hidden="0"/>
      <column width="-1" type="field" name="id_descriptionsystem" hidden="0"/>
      <column width="-1" type="field" name="materiau" hidden="0"/>
      <column width="-1" type="field" name="diametreNominal" hidden="0"/>
      <column width="-1" type="field" name="formecanalisation" hidden="0"/>
      <column width="-1" type="field" name="hauteur" hidden="0"/>
      <column width="-1" type="field" name="branchement" hidden="0"/>
      <column width="-1" type="field" name="modeCirculation" hidden="0"/>
      <column width="-1" type="field" name="typeReseau" hidden="0"/>
      <column width="-1" type="field" name="fonctionCannAss" hidden="0"/>
      <column width="-1" type="field" name="altAmont" hidden="0"/>
      <column width="-1" type="field" name="altAval" hidden="0"/>
      <column width="-1" type="field" name="profamont" hidden="0"/>
      <column width="-1" type="field" name="profaval" hidden="0"/>
      <column width="-1" type="field" name="pk_infralineaire" hidden="0"/>
      <column width="-1" type="field" name="lpk_descriptionsystem" hidden="0"/>
      <column width="-1" type="field" name="lid_ressource_1" hidden="0"/>
      <column width="-1" type="field" name="lid_descriptionsystem_1" hidden="0"/>
      <column width="-1" type="field" name="lid_descriptionsystem_2" hidden="0"/>
      <column width="-1" type="field" name="domaine" hidden="0"/>
      <column width="-1" type="field" name="implantation" hidden="0"/>
      <column width="-1" type="field" name="visitable" hidden="0"/>
      <column width="-1" type="field" name="litdepose" hidden="0"/>
      <column width="-1" type="field" name="typesol" hidden="0"/>
      <column width="-1" type="field" name="etatsol" hidden="0"/>
      <column width="-1" type="field" name="pk_descriptionsystem" hidden="0"/>
      <column width="-1" type="field" name="lpk_objet" hidden="0"/>
      <column width="-1" type="field" name="importancestrat" hidden="0"/>
      <column width="-1" type="field" name="etatfonct" hidden="0"/>
      <column width="-1" type="field" name="qualitegeolocXY" hidden="0"/>
      <column width="-1" type="field" name="qualiteGeolocZ" hidden="0"/>
      <column width="-1" type="field" name="dateGeoloc" hidden="0"/>
      <column width="-1" type="field" name="sourceGeoloc" hidden="0"/>
      <column width="-1" type="field" name="enservice" hidden="0"/>
      <column width="-1" type="field" name="annee_debut_pose" hidden="0"/>
      <column width="-1" type="field" name="annee_fin_pose" hidden="0"/>
      <column width="-1" type="field" name="precision_pose" hidden="0"/>
      <column width="-1" type="field" name="date_miseHorsService" hidden="0"/>
      <column width="-1" type="field" name="parametres" hidden="0"/>
      <column width="-1" type="field" name="listeparametres" hidden="0"/>
      <column width="-1" type="field" name="rue_libelle" hidden="0"/>
      <column width="-1" type="field" name="rue_libdebut" hidden="0"/>
      <column width="-1" type="field" name="rue_libfin" hidden="0"/>
      <column width="-1" type="field" name="rue_complement" hidden="0"/>
      <column width="-1" type="field" name="intervenant_1" hidden="0"/>
      <column width="-1" type="field" name="pk_objet" hidden="0"/>
      <column width="-1" type="field" name="lpk_revision_begin" hidden="0"/>
      <column width="-1" type="field" name="lpk_revision_end" hidden="0"/>
      <column width="-1" type="field" name="datetimecreation" hidden="0"/>
      <column width="-1" type="field" name="datetimemodification" hidden="0"/>
      <column width="-1" type="field" name="datetimedestruction" hidden="0"/>
      <column width="-1" type="field" name="commentaire" hidden="0"/>
      <column width="-1" type="field" name="libelle" hidden="0"/>
      <column width="-1" type="field" name="importid" hidden="0"/>
      <column width="-1" type="field" name="importtable" hidden="0"/>
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
    <attributeEditorContainer visibilityExpressionEnabled="0" columnCount="1" name="Réseaux" visibilityExpression="" showLabel="1" groupBox="0">
      <attributeEditorField index="-1" name="TYP_RESEAU" showLabel="1"/>
      <attributeEditorField index="-1" name="NAT_RESEAU" showLabel="1"/>
      <attributeEditorField index="-1" name="TYP_ECOUL" showLabel="1"/>
      <attributeEditorField index="-1" name="FORME_CANA" showLabel="1"/>
      <attributeEditorField index="-1" name="DIAMETRE" showLabel="1"/>
      <attributeEditorField index="-1" name="MATERIAUX" showLabel="1"/>
      <attributeEditorField index="9" name="HAUTEUR" showLabel="1"/>
      <attributeEditorField index="-1" name="LARGEUR" showLabel="1"/>
      <attributeEditorField index="-1" name="ANNEEPOSE" showLabel="1"/>
      <attributeEditorField index="-1" name="OBSERVATIO" showLabel="1"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="altAmont"/>
    <field editable="1" name="altAval"/>
    <field editable="1" name="annee_debut_pose"/>
    <field editable="1" name="annee_fin_pose"/>
    <field editable="1" name="branchement"/>
    <field editable="1" name="commentaire"/>
    <field editable="1" name="dateGeoloc"/>
    <field editable="1" name="date_miseHorsService"/>
    <field editable="1" name="datetimecreation"/>
    <field editable="1" name="datetimedestruction"/>
    <field editable="1" name="datetimemodification"/>
    <field editable="1" name="diametreNominal"/>
    <field editable="1" name="domaine"/>
    <field editable="1" name="enservice"/>
    <field editable="1" name="etatfonct"/>
    <field editable="1" name="etatsol"/>
    <field editable="1" name="fonctionCannAss"/>
    <field editable="1" name="formecanalisation"/>
    <field editable="1" name="hauteur"/>
    <field editable="1" name="id_descriptionsystem"/>
    <field editable="1" name="id_infralineaire"/>
    <field editable="1" name="id_objet"/>
    <field editable="1" name="implantation"/>
    <field editable="1" name="importancestrat"/>
    <field editable="1" name="importid"/>
    <field editable="1" name="importtable"/>
    <field editable="1" name="intervenant_1"/>
    <field editable="1" name="libelle"/>
    <field editable="1" name="lid_descriptionsystem_1"/>
    <field editable="1" name="lid_descriptionsystem_2"/>
    <field editable="1" name="lid_ressource_1"/>
    <field editable="1" name="listeparametres"/>
    <field editable="1" name="litdepose"/>
    <field editable="1" name="lpk_descriptionsystem"/>
    <field editable="1" name="lpk_objet"/>
    <field editable="1" name="lpk_revision_begin"/>
    <field editable="1" name="lpk_revision_end"/>
    <field editable="1" name="materiau"/>
    <field editable="1" name="modeCirculation"/>
    <field editable="1" name="parametres"/>
    <field editable="1" name="pk_descriptionsystem"/>
    <field editable="1" name="pk_infralineaire"/>
    <field editable="1" name="pk_objet"/>
    <field editable="1" name="precision_pose"/>
    <field editable="1" name="profamont"/>
    <field editable="1" name="profaval"/>
    <field editable="1" name="qualiteGeolocZ"/>
    <field editable="1" name="qualitegeolocXY"/>
    <field editable="1" name="rue_complement"/>
    <field editable="1" name="rue_libdebut"/>
    <field editable="1" name="rue_libelle"/>
    <field editable="1" name="rue_libfin"/>
    <field editable="1" name="sourceGeoloc"/>
    <field editable="1" name="typeReseau"/>
    <field editable="1" name="typesol"/>
    <field editable="1" name="visitable"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="altAmont"/>
    <field labelOnTop="0" name="altAval"/>
    <field labelOnTop="0" name="annee_debut_pose"/>
    <field labelOnTop="0" name="annee_fin_pose"/>
    <field labelOnTop="0" name="branchement"/>
    <field labelOnTop="0" name="commentaire"/>
    <field labelOnTop="0" name="dateGeoloc"/>
    <field labelOnTop="0" name="date_miseHorsService"/>
    <field labelOnTop="0" name="datetimecreation"/>
    <field labelOnTop="0" name="datetimedestruction"/>
    <field labelOnTop="0" name="datetimemodification"/>
    <field labelOnTop="0" name="diametreNominal"/>
    <field labelOnTop="0" name="domaine"/>
    <field labelOnTop="0" name="enservice"/>
    <field labelOnTop="0" name="etatfonct"/>
    <field labelOnTop="0" name="etatsol"/>
    <field labelOnTop="0" name="fonctionCannAss"/>
    <field labelOnTop="0" name="formecanalisation"/>
    <field labelOnTop="0" name="hauteur"/>
    <field labelOnTop="0" name="id_descriptionsystem"/>
    <field labelOnTop="0" name="id_infralineaire"/>
    <field labelOnTop="0" name="id_objet"/>
    <field labelOnTop="0" name="implantation"/>
    <field labelOnTop="0" name="importancestrat"/>
    <field labelOnTop="0" name="importid"/>
    <field labelOnTop="0" name="importtable"/>
    <field labelOnTop="0" name="intervenant_1"/>
    <field labelOnTop="0" name="libelle"/>
    <field labelOnTop="0" name="lid_descriptionsystem_1"/>
    <field labelOnTop="0" name="lid_descriptionsystem_2"/>
    <field labelOnTop="0" name="lid_ressource_1"/>
    <field labelOnTop="0" name="listeparametres"/>
    <field labelOnTop="0" name="litdepose"/>
    <field labelOnTop="0" name="lpk_descriptionsystem"/>
    <field labelOnTop="0" name="lpk_objet"/>
    <field labelOnTop="0" name="lpk_revision_begin"/>
    <field labelOnTop="0" name="lpk_revision_end"/>
    <field labelOnTop="0" name="materiau"/>
    <field labelOnTop="0" name="modeCirculation"/>
    <field labelOnTop="0" name="parametres"/>
    <field labelOnTop="0" name="pk_descriptionsystem"/>
    <field labelOnTop="0" name="pk_infralineaire"/>
    <field labelOnTop="0" name="pk_objet"/>
    <field labelOnTop="0" name="precision_pose"/>
    <field labelOnTop="0" name="profamont"/>
    <field labelOnTop="0" name="profaval"/>
    <field labelOnTop="0" name="qualiteGeolocZ"/>
    <field labelOnTop="0" name="qualitegeolocXY"/>
    <field labelOnTop="0" name="rue_complement"/>
    <field labelOnTop="0" name="rue_libdebut"/>
    <field labelOnTop="0" name="rue_libelle"/>
    <field labelOnTop="0" name="rue_libfin"/>
    <field labelOnTop="0" name="sourceGeoloc"/>
    <field labelOnTop="0" name="typeReseau"/>
    <field labelOnTop="0" name="typesol"/>
    <field labelOnTop="0" name="visitable"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE( "TYP_RESEAU", '&lt;NULL>' )</previewExpression>
  <mapTip>TYP_RESEAU</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
