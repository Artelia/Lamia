<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" version="3.10.0-A CoruÃ±a" maxScale="0" simplifyAlgorithm="0" simplifyLocal="1" minScale="1e+08" simplifyDrawingHints="1" simplifyMaxScale="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" enableorderby="0" type="RuleRenderer">
    <rules key="{5e78f11d-4178-4ed7-8af6-f80178c4ba25}">
      <rule filter=" &quot;branchement&quot; = 1" key="{c647d32b-b632-485f-bd3c-91150bd75a8b}" label="Branchement">
        <rule filter="&quot;lid_descriptionsystem_1&quot; IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL" key="{c64b87c5-2e70-47ec-a94f-a9b46d7ca120}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02')" symbol="0" key="{9739976b-e285-47e5-a9b3-f03be0ead4d2}" label="Eaux usées">
            <rule symbol="1" key="{33fbb348-5c57-44e8-b6fc-be6c61d5397f}" scalemindenom="5000" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="2" key="{b58611c9-3fed-43bb-b53c-b9e470bd0e7a}" label="Unitaire">
            <rule symbol="3" key="{aadc49a6-4a5f-49a6-b31e-fb53caa7da29}" scalemindenom="5000" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03')" symbol="4" key="{79228b2f-3bcc-41db-b9b2-7a63236519b9}" label="Eaux pluviales">
            <rule symbol="5" key="{557f2669-c040-4245-b628-e29d512012e9}" scalemindenom="5000" label="0 - 5000"/>
          </rule>
        </rule>
        <rule filter="ELSE" key="{766e1a38-f6d0-4e9e-9f69-8e4b0e647dbd}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02')" symbol="6" key="{056c6700-936d-4dc5-94bb-444be6ac21c1}" label="Eaux usées">
            <rule symbol="7" key="{e16e7031-5f55-4999-9a28-5147490d9c50}" scalemindenom="5000" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="8" key="{d02aedf7-0a96-43e6-b6e4-05de94c29c01}" label="Unitaire">
            <rule symbol="9" key="{05870733-4af5-4c67-9521-0638e39097b8}" scalemindenom="5000" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03')" symbol="10" key="{e5d88765-3a5e-45c9-9d40-4f4ccb76f3d1}" label="Eaux pluviales">
            <rule symbol="11" key="{59da33b5-8378-418d-8d13-e3d77b53db3b}" scalemindenom="5000" label="0 - 5000"/>
          </rule>
        </rule>
      </rule>
      <rule filter=" &quot;branchement&quot; = 0" key="{06826450-6078-4741-8f6d-022aaa3d991c}" label="Branchement">
        <rule filter=" &quot;lid_descriptionsystem_1&quot;  IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL" key="{88663e10-e0fc-4596-9b17-73b72cdd6b17}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02')" symbol="12" key="{1a389d12-0d10-440b-bc98-99359171cecd}" label="Eaux usées">
            <rule scalemaxdenom="5000" symbol="13" key="{7ea2414d-2527-4219-bd96-abcaebd05d23}" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="14" key="{68b407af-ccdc-4174-9cf3-b76afd97b02a}" label="Unitaire">
            <rule scalemaxdenom="5000" symbol="15" key="{a3bf1739-5ac1-4b64-b6bc-d90c27195dff}" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03')" symbol="16" key="{63296647-4e1b-4afe-b24e-22e8e31ff386}" label="Eaux pluviales">
            <rule scalemaxdenom="5000" symbol="17" key="{ac2c4c84-b8b9-4622-9ad9-2f34d7a3a2d5}" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('USE','02') and &quot;fonctionCannAss&quot;  =   '02' " symbol="18" key="{3f65b50e-0bf2-40c6-a77b-07ef1672c36e}" label="Refoulement eaux usées"/>
        </rule>
        <rule filter="ELSE" key="{33f84cfd-6977-4c2a-9cb5-fc1b120f5186}">
          <rule filter="&quot;typeReseau&quot; IN ('USE','02') and &quot;fonctionCannAss&quot;  =   '01'" symbol="19" key="{d06eff82-6570-49e6-a3db-2f57ba6f18f1}" label="Eaux usées">
            <rule scalemaxdenom="5000" symbol="20" key="{9da33136-3b87-432c-acbd-8f6df6ab8b99}" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('UNI','01')" symbol="21" key="{a3ec9bfa-cfb2-481e-bc88-423fe89f7a96}" label="Unitaire">
            <rule scalemaxdenom="5000" symbol="22" key="{582a22e5-bd4f-47aa-a7fd-95ffaeac2744}" label="0 - 5000"/>
          </rule>
          <rule filter="&quot;typeReseau&quot; IN ('PLU','03') and &quot;fonctionCannAss&quot;  =   '01'" symbol="23" key="{0120d564-3526-4085-b40c-57703191a0c7}" label="Eaux pluviales">
            <rule scalemaxdenom="5000" symbol="24" key="{bd85613e-74eb-4a63-93b8-65e0b1a9c295}" label="0 - 5000"/>
          </rule>
          <rule filter=" &quot;typeReseau&quot; IN ('PLU','03') and  &quot;fonctionCannAss&quot; = '02'" symbol="25" key="{95b411e6-2b95-4638-810c-cebf2f9a9a05}" label="Refoulement eaux pluviales "/>
        </rule>
      </rule>
      <rule filter="ELSE" symbol="26" key="{146b5a78-5b72-4838-8cb1-ae306bc010b5}">
        <rule scalemaxdenom="5000" symbol="27" key="{d337d640-72b2-476f-9aeb-813fdd0a2e58}" label="0 - 5000"/>
      </rule>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" force_rhr="0" name="0" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,1,1,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.4"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="1" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@1@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,1,1,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,0,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="10" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,255,255"/>
          <prop k="line_style" v="dash"/>
          <prop k="line_width" v="0.4"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="11" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@11@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,255,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="0,0,255,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="12" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,1,1,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="13" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@13@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,1,1,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,0,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="3.2"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="14" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,127,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="15" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@15@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,127,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,127,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="3.2"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="16" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,255,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="17" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@17@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,255,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="0,0,255,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="3.2"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="18" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="213,116,255,255"/>
          <prop k="line_style" v="dot"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="19" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,1,1,255"/>
          <prop k="line_style" v="dash"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="2" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,127,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.4"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="20" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@20@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,1,1,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,0,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="3.2"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="21" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,127,0,255"/>
          <prop k="line_style" v="dash"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="22" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@22@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,127,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,127,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="3.2"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="23" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,255,255"/>
          <prop k="line_style" v="dash"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="24" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@24@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,255,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="0,0,255,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="3.2"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="25" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="11,202,255,255"/>
          <prop k="line_style" v="dot"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="26" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="112,112,112,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="27" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@27@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="112,112,112,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="112,112,112,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="3.2"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="3" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@3@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,127,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,127,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="4" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,255,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.4"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="5" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@5@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,255,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="0,0,255,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="6" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,1,1,255"/>
          <prop k="line_style" v="dash"/>
          <prop k="line_width" v="0.4"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="7" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@7@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,1,1,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,0,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2.8"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="8" type="line" alpha="1">
        <layer class="SimpleLine" locked="0" enabled="1" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="255,127,0,255"/>
          <prop k="line_style" v="dash"/>
          <prop k="line_width" v="0.4"/>
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
      <symbol clip_to_extent="1" force_rhr="0" name="9" type="line" alpha="1">
        <layer class="MarkerLine" locked="0" enabled="1" pass="0">
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
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@9@0" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,127,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="filled_arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="255,127,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2.8"/>
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
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style textOrientation="horizontal" fieldName=" &quot;diametreNominal&quot; *1000" fontStrikeout="0" fontSizeUnit="Point" fontWordSpacing="0" useSubstitutions="0" fontKerning="1" fontUnderline="0" textOpacity="1" fontLetterSpacing="0" fontCapitals="0" fontSize="8.25" blendMode="0" fontItalic="0" fontWeight="50" fontSizeMapUnitScale="3x:0,0,0,0,0,0" namedStyle="Normal" previewBkgrdColor="255,255,255,255" fontFamily="MS Shell Dlg 2" multilineHeight="1" isExpression="1" textColor="0,0,0,255">
        <text-buffer bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferColor="255,255,255,255" bufferDraw="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferJoinStyle="128" bufferNoFill="0"/>
        <background shapeSVGFile="" shapeRadiiX="0" shapeRotation="0" shapeOffsetUnit="MM" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeRotationType="0" shapeBlendMode="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeOpacity="1" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeType="0" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeJoinStyle="64" shapeSizeType="0" shapeRadiiUnit="MM" shapeSizeX="0" shapeDraw="0" shapeOffsetX="0">
          <symbol clip_to_extent="1" force_rhr="0" name="markerSymbol" type="marker" alpha="1">
            <layer class="SimpleMarker" locked="0" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="133,182,111,255"/>
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
        <shadow shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowOffsetGlobal="1" shadowRadius="1.5" shadowColor="0,0,0,255" shadowOpacity="0.7" shadowRadiusUnit="MM" shadowDraw="0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetAngle="135" shadowBlendMode="6"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" placeDirectionSymbol="0" wrapChar="" multilineAlign="4294967295" addDirectionSymbol="0" rightDirectionSymbol=">" formatNumbers="0" decimals="3" reverseDirectionSymbol="0" plussign="0" autoWrapLength="0" leftDirectionSymbol="&lt;"/>
      <placement repeatDistanceUnits="MM" preserveRotation="1" offsetUnits="MapUnit" overrunDistance="0" geometryGeneratorEnabled="0" dist="0.5" distMapUnitScale="3x:0,0,0,0,0,0" quadOffset="4" centroidWhole="0" layerType="LineGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" placementFlags="2" placement="3" distUnits="MM" xOffset="0" geometryGeneratorType="PointGeometry" offsetType="0" rotationAngle="0" centroidInside="0" repeatDistance="0" maxCurvedCharAngleOut="-25" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" priority="5" geometryGenerator="" yOffset="0" overrunDistanceUnit="MM" fitInPolygonOnly="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" maxCurvedCharAngleIn="25"/>
      <rendering zIndex="0" fontMinPixelSize="3" displayAll="0" maxNumLabels="2000" fontMaxPixelSize="10000" minFeatureSize="2" upsidedownLabels="0" fontLimitPixelSize="0" scaleMin="1" limitNumLabels="0" mergeLines="1" drawLabels="1" obstacle="1" scaleVisibility="1" obstacleType="0" obstacleFactor="1" scaleMax="5000" labelPerPart="0"/>
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
          <Option name="lineSymbol" value="&lt;symbol clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;layer class=&quot;SimpleLine&quot; locked=&quot;0&quot; enabled=&quot;1&quot; pass=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
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
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory lineSizeType="MM" labelPlacementMethod="XHeight" barWidth="5" opacity="1" backgroundColor="#ffffff" enabled="0" sizeType="MM" scaleDependency="Area" minimumSize="0" penColor="#000000" minScaleDenominator="0" maxScaleDenominator="1e+08" diagramOrientation="Up" rotationOffset="270" backgroundAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" sizeScale="3x:0,0,0,0,0,0" penWidth="0" penAlpha="255" height="15" width="15">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" label="" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" obstacle="0" placement="2" dist="0" priority="0" showAll="1" linePlacementFlags="2">
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
    <alias name="" index="0" field="pk_infralineaire"/>
    <alias name="" index="1" field="id_infralineaire"/>
    <alias name="" index="2" field="lpk_descriptionsystem"/>
    <alias name="" index="3" field="lid_ressource_1"/>
    <alias name="" index="4" field="lid_descriptionsystem_1"/>
    <alias name="" index="5" field="lid_descriptionsystem_2"/>
    <alias name="" index="6" field="materiau"/>
    <alias name="" index="7" field="diametreNominal"/>
    <alias name="" index="8" field="formecanalisation"/>
    <alias name="Hauteur de l'aqueduc / bâti" index="9" field="hauteur"/>
    <alias name="" index="10" field="branchement"/>
    <alias name="" index="11" field="modeCirculation"/>
    <alias name="" index="12" field="typeReseau"/>
    <alias name="" index="13" field="fonctionCannAss"/>
    <alias name="" index="14" field="altAmont"/>
    <alias name="" index="15" field="altAval"/>
    <alias name="" index="16" field="profamont"/>
    <alias name="" index="17" field="profaval"/>
    <alias name="" index="18" field="domaine"/>
    <alias name="" index="19" field="implantation"/>
    <alias name="" index="20" field="visitable"/>
    <alias name="" index="21" field="litdepose"/>
    <alias name="" index="22" field="typesol"/>
    <alias name="" index="23" field="etatsol"/>
    <alias name="" index="24" field="pk_descriptionsystem"/>
    <alias name="" index="25" field="id_descriptionsystem"/>
    <alias name="" index="26" field="lpk_objet"/>
    <alias name="" index="27" field="importancestrat"/>
    <alias name="" index="28" field="etatfonct"/>
    <alias name="" index="29" field="qualitegeolocXY"/>
    <alias name="" index="30" field="qualiteGeolocZ"/>
    <alias name="" index="31" field="dateGeoloc"/>
    <alias name="" index="32" field="sourceGeoloc"/>
    <alias name="" index="33" field="enservice"/>
    <alias name="" index="34" field="annee_debut_pose"/>
    <alias name="" index="35" field="annee_fin_pose"/>
    <alias name="" index="36" field="precision_pose"/>
    <alias name="" index="37" field="date_miseHorsService"/>
    <alias name="" index="38" field="parametres"/>
    <alias name="" index="39" field="listeparametres"/>
    <alias name="" index="40" field="rue_libelle"/>
    <alias name="" index="41" field="rue_libdebut"/>
    <alias name="" index="42" field="rue_libfin"/>
    <alias name="" index="43" field="rue_complement"/>
    <alias name="" index="44" field="intervenant_1"/>
    <alias name="" index="45" field="pk_objet"/>
    <alias name="" index="46" field="id_objet"/>
    <alias name="" index="47" field="lpk_revision_begin"/>
    <alias name="" index="48" field="lpk_revision_end"/>
    <alias name="" index="49" field="datetimecreation"/>
    <alias name="" index="50" field="datetimemodification"/>
    <alias name="" index="51" field="datetimedestruction"/>
    <alias name="" index="52" field="commentaire"/>
    <alias name="" index="53" field="libelle"/>
    <alias name="" index="54" field="importid"/>
    <alias name="" index="55" field="importtable"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="pk_infralineaire"/>
    <default expression="" applyOnUpdate="0" field="id_infralineaire"/>
    <default expression="" applyOnUpdate="0" field="lpk_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="lid_ressource_1"/>
    <default expression="" applyOnUpdate="0" field="lid_descriptionsystem_1"/>
    <default expression="" applyOnUpdate="0" field="lid_descriptionsystem_2"/>
    <default expression="" applyOnUpdate="0" field="materiau"/>
    <default expression="" applyOnUpdate="0" field="diametreNominal"/>
    <default expression="" applyOnUpdate="0" field="formecanalisation"/>
    <default expression="" applyOnUpdate="0" field="hauteur"/>
    <default expression="" applyOnUpdate="0" field="branchement"/>
    <default expression="" applyOnUpdate="0" field="modeCirculation"/>
    <default expression="" applyOnUpdate="0" field="typeReseau"/>
    <default expression="" applyOnUpdate="0" field="fonctionCannAss"/>
    <default expression="" applyOnUpdate="0" field="altAmont"/>
    <default expression="" applyOnUpdate="0" field="altAval"/>
    <default expression="" applyOnUpdate="0" field="profamont"/>
    <default expression="" applyOnUpdate="0" field="profaval"/>
    <default expression="" applyOnUpdate="0" field="domaine"/>
    <default expression="" applyOnUpdate="0" field="implantation"/>
    <default expression="" applyOnUpdate="0" field="visitable"/>
    <default expression="" applyOnUpdate="0" field="litdepose"/>
    <default expression="" applyOnUpdate="0" field="typesol"/>
    <default expression="" applyOnUpdate="0" field="etatsol"/>
    <default expression="" applyOnUpdate="0" field="pk_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="id_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="lpk_objet"/>
    <default expression="" applyOnUpdate="0" field="importancestrat"/>
    <default expression="" applyOnUpdate="0" field="etatfonct"/>
    <default expression="" applyOnUpdate="0" field="qualitegeolocXY"/>
    <default expression="" applyOnUpdate="0" field="qualiteGeolocZ"/>
    <default expression="" applyOnUpdate="0" field="dateGeoloc"/>
    <default expression="" applyOnUpdate="0" field="sourceGeoloc"/>
    <default expression="" applyOnUpdate="0" field="enservice"/>
    <default expression="" applyOnUpdate="0" field="annee_debut_pose"/>
    <default expression="" applyOnUpdate="0" field="annee_fin_pose"/>
    <default expression="" applyOnUpdate="0" field="precision_pose"/>
    <default expression="" applyOnUpdate="0" field="date_miseHorsService"/>
    <default expression="" applyOnUpdate="0" field="parametres"/>
    <default expression="" applyOnUpdate="0" field="listeparametres"/>
    <default expression="" applyOnUpdate="0" field="rue_libelle"/>
    <default expression="" applyOnUpdate="0" field="rue_libdebut"/>
    <default expression="" applyOnUpdate="0" field="rue_libfin"/>
    <default expression="" applyOnUpdate="0" field="rue_complement"/>
    <default expression="" applyOnUpdate="0" field="intervenant_1"/>
    <default expression="" applyOnUpdate="0" field="pk_objet"/>
    <default expression="" applyOnUpdate="0" field="id_objet"/>
    <default expression="" applyOnUpdate="0" field="lpk_revision_begin"/>
    <default expression="" applyOnUpdate="0" field="lpk_revision_end"/>
    <default expression="" applyOnUpdate="0" field="datetimecreation"/>
    <default expression="" applyOnUpdate="0" field="datetimemodification"/>
    <default expression="" applyOnUpdate="0" field="datetimedestruction"/>
    <default expression="" applyOnUpdate="0" field="commentaire"/>
    <default expression="" applyOnUpdate="0" field="libelle"/>
    <default expression="" applyOnUpdate="0" field="importid"/>
    <default expression="" applyOnUpdate="0" field="importtable"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="pk_infralineaire"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="id_infralineaire"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="lpk_descriptionsystem"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="lid_ressource_1"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="lid_descriptionsystem_1"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="lid_descriptionsystem_2"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="materiau"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="diametreNominal"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="formecanalisation"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="hauteur"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="branchement"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="modeCirculation"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="typeReseau"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="fonctionCannAss"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="altAmont"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="altAval"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="profamont"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="profaval"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="domaine"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="implantation"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="visitable"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="litdepose"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="typesol"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="etatsol"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="pk_descriptionsystem"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="id_descriptionsystem"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="lpk_objet"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="importancestrat"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="etatfonct"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="qualitegeolocXY"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="qualiteGeolocZ"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="dateGeoloc"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="sourceGeoloc"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="enservice"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="annee_debut_pose"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="annee_fin_pose"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="precision_pose"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="date_miseHorsService"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="parametres"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="listeparametres"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="rue_libelle"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="rue_libdebut"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="rue_libfin"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="rue_complement"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="intervenant_1"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="pk_objet"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="id_objet"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="lpk_revision_begin"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="lpk_revision_end"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="datetimecreation"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="datetimemodification"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="datetimedestruction"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="commentaire"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="libelle"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="importid"/>
    <constraint unique_strength="0" notnull_strength="0" exp_strength="0" constraints="0" field="importtable"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="pk_infralineaire"/>
    <constraint exp="" desc="" field="id_infralineaire"/>
    <constraint exp="" desc="" field="lpk_descriptionsystem"/>
    <constraint exp="" desc="" field="lid_ressource_1"/>
    <constraint exp="" desc="" field="lid_descriptionsystem_1"/>
    <constraint exp="" desc="" field="lid_descriptionsystem_2"/>
    <constraint exp="" desc="" field="materiau"/>
    <constraint exp="" desc="" field="diametreNominal"/>
    <constraint exp="" desc="" field="formecanalisation"/>
    <constraint exp="" desc="" field="hauteur"/>
    <constraint exp="" desc="" field="branchement"/>
    <constraint exp="" desc="" field="modeCirculation"/>
    <constraint exp="" desc="" field="typeReseau"/>
    <constraint exp="" desc="" field="fonctionCannAss"/>
    <constraint exp="" desc="" field="altAmont"/>
    <constraint exp="" desc="" field="altAval"/>
    <constraint exp="" desc="" field="profamont"/>
    <constraint exp="" desc="" field="profaval"/>
    <constraint exp="" desc="" field="domaine"/>
    <constraint exp="" desc="" field="implantation"/>
    <constraint exp="" desc="" field="visitable"/>
    <constraint exp="" desc="" field="litdepose"/>
    <constraint exp="" desc="" field="typesol"/>
    <constraint exp="" desc="" field="etatsol"/>
    <constraint exp="" desc="" field="pk_descriptionsystem"/>
    <constraint exp="" desc="" field="id_descriptionsystem"/>
    <constraint exp="" desc="" field="lpk_objet"/>
    <constraint exp="" desc="" field="importancestrat"/>
    <constraint exp="" desc="" field="etatfonct"/>
    <constraint exp="" desc="" field="qualitegeolocXY"/>
    <constraint exp="" desc="" field="qualiteGeolocZ"/>
    <constraint exp="" desc="" field="dateGeoloc"/>
    <constraint exp="" desc="" field="sourceGeoloc"/>
    <constraint exp="" desc="" field="enservice"/>
    <constraint exp="" desc="" field="annee_debut_pose"/>
    <constraint exp="" desc="" field="annee_fin_pose"/>
    <constraint exp="" desc="" field="precision_pose"/>
    <constraint exp="" desc="" field="date_miseHorsService"/>
    <constraint exp="" desc="" field="parametres"/>
    <constraint exp="" desc="" field="listeparametres"/>
    <constraint exp="" desc="" field="rue_libelle"/>
    <constraint exp="" desc="" field="rue_libdebut"/>
    <constraint exp="" desc="" field="rue_libfin"/>
    <constraint exp="" desc="" field="rue_complement"/>
    <constraint exp="" desc="" field="intervenant_1"/>
    <constraint exp="" desc="" field="pk_objet"/>
    <constraint exp="" desc="" field="id_objet"/>
    <constraint exp="" desc="" field="lpk_revision_begin"/>
    <constraint exp="" desc="" field="lpk_revision_end"/>
    <constraint exp="" desc="" field="datetimecreation"/>
    <constraint exp="" desc="" field="datetimemodification"/>
    <constraint exp="" desc="" field="datetimedestruction"/>
    <constraint exp="" desc="" field="commentaire"/>
    <constraint exp="" desc="" field="libelle"/>
    <constraint exp="" desc="" field="importid"/>
    <constraint exp="" desc="" field="importtable"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column hidden="1" width="-1" type="actions"/>
      <column hidden="0" name="id_infralineaire" width="-1" type="field"/>
      <column hidden="0" name="id_objet" width="-1" type="field"/>
      <column hidden="0" name="id_descriptionsystem" width="-1" type="field"/>
      <column hidden="0" name="materiau" width="-1" type="field"/>
      <column hidden="0" name="diametreNominal" width="-1" type="field"/>
      <column hidden="0" name="formecanalisation" width="-1" type="field"/>
      <column hidden="0" name="hauteur" width="-1" type="field"/>
      <column hidden="0" name="branchement" width="-1" type="field"/>
      <column hidden="0" name="modeCirculation" width="-1" type="field"/>
      <column hidden="0" name="typeReseau" width="-1" type="field"/>
      <column hidden="0" name="fonctionCannAss" width="-1" type="field"/>
      <column hidden="0" name="altAmont" width="-1" type="field"/>
      <column hidden="0" name="altAval" width="-1" type="field"/>
      <column hidden="0" name="profamont" width="-1" type="field"/>
      <column hidden="0" name="profaval" width="-1" type="field"/>
      <column hidden="0" name="pk_infralineaire" width="-1" type="field"/>
      <column hidden="0" name="lpk_descriptionsystem" width="-1" type="field"/>
      <column hidden="0" name="lid_ressource_1" width="-1" type="field"/>
      <column hidden="0" name="lid_descriptionsystem_1" width="-1" type="field"/>
      <column hidden="0" name="lid_descriptionsystem_2" width="-1" type="field"/>
      <column hidden="0" name="domaine" width="-1" type="field"/>
      <column hidden="0" name="implantation" width="-1" type="field"/>
      <column hidden="0" name="visitable" width="-1" type="field"/>
      <column hidden="0" name="litdepose" width="-1" type="field"/>
      <column hidden="0" name="typesol" width="-1" type="field"/>
      <column hidden="0" name="etatsol" width="-1" type="field"/>
      <column hidden="0" name="pk_descriptionsystem" width="-1" type="field"/>
      <column hidden="0" name="lpk_objet" width="-1" type="field"/>
      <column hidden="0" name="importancestrat" width="-1" type="field"/>
      <column hidden="0" name="etatfonct" width="-1" type="field"/>
      <column hidden="0" name="qualitegeolocXY" width="-1" type="field"/>
      <column hidden="0" name="qualiteGeolocZ" width="-1" type="field"/>
      <column hidden="0" name="dateGeoloc" width="-1" type="field"/>
      <column hidden="0" name="sourceGeoloc" width="-1" type="field"/>
      <column hidden="0" name="enservice" width="-1" type="field"/>
      <column hidden="0" name="annee_debut_pose" width="-1" type="field"/>
      <column hidden="0" name="annee_fin_pose" width="-1" type="field"/>
      <column hidden="0" name="precision_pose" width="-1" type="field"/>
      <column hidden="0" name="date_miseHorsService" width="-1" type="field"/>
      <column hidden="0" name="parametres" width="-1" type="field"/>
      <column hidden="0" name="listeparametres" width="-1" type="field"/>
      <column hidden="0" name="rue_libelle" width="-1" type="field"/>
      <column hidden="0" name="rue_libdebut" width="-1" type="field"/>
      <column hidden="0" name="rue_libfin" width="-1" type="field"/>
      <column hidden="0" name="rue_complement" width="-1" type="field"/>
      <column hidden="0" name="intervenant_1" width="-1" type="field"/>
      <column hidden="0" name="pk_objet" width="-1" type="field"/>
      <column hidden="0" name="lpk_revision_begin" width="-1" type="field"/>
      <column hidden="0" name="lpk_revision_end" width="-1" type="field"/>
      <column hidden="0" name="datetimecreation" width="-1" type="field"/>
      <column hidden="0" name="datetimemodification" width="-1" type="field"/>
      <column hidden="0" name="datetimedestruction" width="-1" type="field"/>
      <column hidden="0" name="commentaire" width="-1" type="field"/>
      <column hidden="0" name="libelle" width="-1" type="field"/>
      <column hidden="0" name="importid" width="-1" type="field"/>
      <column hidden="0" name="importtable" width="-1" type="field"/>
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
    <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Réseaux" groupBox="0" columnCount="1" visibilityExpression="">
      <attributeEditorField showLabel="1" name="TYP_RESEAU" index="-1"/>
      <attributeEditorField showLabel="1" name="NAT_RESEAU" index="-1"/>
      <attributeEditorField showLabel="1" name="TYP_ECOUL" index="-1"/>
      <attributeEditorField showLabel="1" name="FORME_CANA" index="-1"/>
      <attributeEditorField showLabel="1" name="DIAMETRE" index="-1"/>
      <attributeEditorField showLabel="1" name="MATERIAUX" index="-1"/>
      <attributeEditorField showLabel="1" name="HAUTEUR" index="9"/>
      <attributeEditorField showLabel="1" name="LARGEUR" index="-1"/>
      <attributeEditorField showLabel="1" name="ANNEEPOSE" index="-1"/>
      <attributeEditorField showLabel="1" name="OBSERVATIO" index="-1"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field name="altAmont" editable="1"/>
    <field name="altAval" editable="1"/>
    <field name="annee_debut_pose" editable="1"/>
    <field name="annee_fin_pose" editable="1"/>
    <field name="branchement" editable="1"/>
    <field name="commentaire" editable="1"/>
    <field name="dateGeoloc" editable="1"/>
    <field name="date_miseHorsService" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimemodification" editable="1"/>
    <field name="diametreNominal" editable="1"/>
    <field name="domaine" editable="1"/>
    <field name="enservice" editable="1"/>
    <field name="etatfonct" editable="1"/>
    <field name="etatsol" editable="1"/>
    <field name="fonctionCannAss" editable="1"/>
    <field name="formecanalisation" editable="1"/>
    <field name="hauteur" editable="1"/>
    <field name="id_descriptionsystem" editable="1"/>
    <field name="id_infralineaire" editable="1"/>
    <field name="id_objet" editable="1"/>
    <field name="implantation" editable="1"/>
    <field name="importancestrat" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="intervenant_1" editable="1"/>
    <field name="libelle" editable="1"/>
    <field name="lid_descriptionsystem_1" editable="1"/>
    <field name="lid_descriptionsystem_2" editable="1"/>
    <field name="lid_ressource_1" editable="1"/>
    <field name="listeparametres" editable="1"/>
    <field name="litdepose" editable="1"/>
    <field name="lpk_descriptionsystem" editable="1"/>
    <field name="lpk_objet" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="materiau" editable="1"/>
    <field name="modeCirculation" editable="1"/>
    <field name="parametres" editable="1"/>
    <field name="pk_descriptionsystem" editable="1"/>
    <field name="pk_infralineaire" editable="1"/>
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
    <field name="sourceGeoloc" editable="1"/>
    <field name="typeReseau" editable="1"/>
    <field name="typesol" editable="1"/>
    <field name="visitable" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="altAmont" labelOnTop="0"/>
    <field name="altAval" labelOnTop="0"/>
    <field name="annee_debut_pose" labelOnTop="0"/>
    <field name="annee_fin_pose" labelOnTop="0"/>
    <field name="branchement" labelOnTop="0"/>
    <field name="commentaire" labelOnTop="0"/>
    <field name="dateGeoloc" labelOnTop="0"/>
    <field name="date_miseHorsService" labelOnTop="0"/>
    <field name="datetimecreation" labelOnTop="0"/>
    <field name="datetimedestruction" labelOnTop="0"/>
    <field name="datetimemodification" labelOnTop="0"/>
    <field name="diametreNominal" labelOnTop="0"/>
    <field name="domaine" labelOnTop="0"/>
    <field name="enservice" labelOnTop="0"/>
    <field name="etatfonct" labelOnTop="0"/>
    <field name="etatsol" labelOnTop="0"/>
    <field name="fonctionCannAss" labelOnTop="0"/>
    <field name="formecanalisation" labelOnTop="0"/>
    <field name="hauteur" labelOnTop="0"/>
    <field name="id_descriptionsystem" labelOnTop="0"/>
    <field name="id_infralineaire" labelOnTop="0"/>
    <field name="id_objet" labelOnTop="0"/>
    <field name="implantation" labelOnTop="0"/>
    <field name="importancestrat" labelOnTop="0"/>
    <field name="importid" labelOnTop="0"/>
    <field name="importtable" labelOnTop="0"/>
    <field name="intervenant_1" labelOnTop="0"/>
    <field name="libelle" labelOnTop="0"/>
    <field name="lid_descriptionsystem_1" labelOnTop="0"/>
    <field name="lid_descriptionsystem_2" labelOnTop="0"/>
    <field name="lid_ressource_1" labelOnTop="0"/>
    <field name="listeparametres" labelOnTop="0"/>
    <field name="litdepose" labelOnTop="0"/>
    <field name="lpk_descriptionsystem" labelOnTop="0"/>
    <field name="lpk_objet" labelOnTop="0"/>
    <field name="lpk_revision_begin" labelOnTop="0"/>
    <field name="lpk_revision_end" labelOnTop="0"/>
    <field name="materiau" labelOnTop="0"/>
    <field name="modeCirculation" labelOnTop="0"/>
    <field name="parametres" labelOnTop="0"/>
    <field name="pk_descriptionsystem" labelOnTop="0"/>
    <field name="pk_infralineaire" labelOnTop="0"/>
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
    <field name="sourceGeoloc" labelOnTop="0"/>
    <field name="typeReseau" labelOnTop="0"/>
    <field name="typesol" labelOnTop="0"/>
    <field name="visitable" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE( "TYP_RESEAU", '&lt;NULL>' )</previewExpression>
  <mapTip>TYP_RESEAU</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
