<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" labelsEnabled="1" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" simplifyLocal="1" simplifyDrawingHints="1" styleCategories="AllStyleCategories" simplifyAlgorithm="0" readOnly="0" version="3.10.6-A Coruña" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" type="RuleRenderer" forceraster="0" symbollevels="0">
    <rules key="{5e78f11d-4178-4ed7-8af6-f80178c4ba25}">
      <rule label="Branchement" filter=" &quot;laterals&quot; = 1" key="{c647d32b-b632-485f-bd3c-91150bd75a8b}">
        <rule filter="&quot;lid_descriptionsystem_1&quot; IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL" key="{c64b87c5-2e70-47ec-a94f-a9b46d7ca120}">
          <rule label="Eaux usées" symbol="0" filter="&quot;networktype&quot; IN ('USE','02')" key="{9739976b-e285-47e5-a9b3-f03be0ead4d2}">
            <rule label="0 - 5000" symbol="1" scalemindenom="5000" key="{33fbb348-5c57-44e8-b6fc-be6c61d5397f}"/>
          </rule>
          <rule label="Unitaire" symbol="2" filter="&quot;networktype&quot; IN ('UNI','01')" key="{b58611c9-3fed-43bb-b53c-b9e470bd0e7a}">
            <rule label="0 - 5000" symbol="3" scalemindenom="5000" key="{aadc49a6-4a5f-49a6-b31e-fb53caa7da29}"/>
          </rule>
          <rule label="Eaux pluviales" symbol="4" filter="&quot;networktype&quot; IN ('PLU','03')" key="{79228b2f-3bcc-41db-b9b2-7a63236519b9}">
            <rule label="0 - 5000" symbol="5" scalemindenom="5000" key="{557f2669-c040-4245-b628-e29d512012e9}"/>
          </rule>
        </rule>
        <rule filter="ELSE" key="{766e1a38-f6d0-4e9e-9f69-8e4b0e647dbd}">
          <rule label="Eaux usées" symbol="6" filter="&quot;networktype&quot; IN ('USE','02')" key="{056c6700-936d-4dc5-94bb-444be6ac21c1}">
            <rule label="0 - 5000" symbol="7" scalemindenom="5000" key="{e16e7031-5f55-4999-9a28-5147490d9c50}"/>
          </rule>
          <rule label="Unitaire" symbol="8" filter="&quot;networktype&quot; IN ('UNI','01')" key="{d02aedf7-0a96-43e6-b6e4-05de94c29c01}">
            <rule label="0 - 5000" symbol="9" scalemindenom="5000" key="{05870733-4af5-4c67-9521-0638e39097b8}"/>
          </rule>
          <rule label="Eaux pluviales" symbol="10" filter="&quot;networktype&quot; IN ('PLU','03')" key="{e5d88765-3a5e-45c9-9d40-4f4ccb76f3d1}">
            <rule label="0 - 5000" symbol="11" scalemindenom="5000" key="{59da33b5-8378-418d-8d13-e3d77b53db3b}"/>
          </rule>
        </rule>
      </rule>
      <rule label="Branchement" filter=" &quot;laterals&quot; = 0" key="{06826450-6078-4741-8f6d-022aaa3d991c}">
        <rule filter=" &quot;lid_descriptionsystem_1&quot;  IS NOT NULL AND &quot;lid_descriptionsystem_2&quot; IS NOT NULL" key="{88663e10-e0fc-4596-9b17-73b72cdd6b17}">
          <rule label="Eaux usées" symbol="12" filter="&quot;networktype&quot; IN ('USE','02')" key="{1a389d12-0d10-440b-bc98-99359171cecd}">
            <rule label="0 - 5000" symbol="13" key="{7ea2414d-2527-4219-bd96-abcaebd05d23}" scalemaxdenom="5000"/>
          </rule>
          <rule label="Unitaire" symbol="14" filter="&quot;networktype&quot; IN ('UNI','01')" key="{68b407af-ccdc-4174-9cf3-b76afd97b02a}">
            <rule label="0 - 5000" symbol="15" key="{a3bf1739-5ac1-4b64-b6bc-d90c27195dff}" scalemaxdenom="5000"/>
          </rule>
          <rule label="Eaux pluviales" symbol="16" filter="&quot;networktype&quot; IN ('PLU','03')" key="{63296647-4e1b-4afe-b24e-22e8e31ff386}">
            <rule label="0 - 5000" symbol="17" key="{ac2c4c84-b8b9-4622-9ad9-2f34d7a3a2d5}" scalemaxdenom="5000"/>
          </rule>
          <rule label="Refoulement eaux usées" symbol="18" filter="&quot;networktype&quot; IN ('USE','02') and &quot;fonctionCannAss&quot;  =   '02' " key="{3f65b50e-0bf2-40c6-a77b-07ef1672c36e}"/>
        </rule>
        <rule filter="ELSE" key="{33f84cfd-6977-4c2a-9cb5-fc1b120f5186}">
          <rule label="Eaux usées" symbol="19" filter="&quot;networktype&quot; IN ('USE','02') and &quot;fonctionCannAss&quot;  =   '01'" key="{d06eff82-6570-49e6-a3db-2f57ba6f18f1}">
            <rule label="0 - 5000" symbol="20" key="{9da33136-3b87-432c-acbd-8f6df6ab8b99}" scalemaxdenom="5000"/>
          </rule>
          <rule label="Unitaire" symbol="21" filter="&quot;networktype&quot; IN ('UNI','01')" key="{a3ec9bfa-cfb2-481e-bc88-423fe89f7a96}">
            <rule label="0 - 5000" symbol="22" key="{582a22e5-bd4f-47aa-a7fd-95ffaeac2744}" scalemaxdenom="5000"/>
          </rule>
          <rule label="Eaux pluviales" symbol="23" filter="&quot;networktype&quot; IN ('PLU','03') and &quot;fonctionCannAss&quot;  =   '01'" key="{0120d564-3526-4085-b40c-57703191a0c7}">
            <rule label="0 - 5000" symbol="24" key="{bd85613e-74eb-4a63-93b8-65e0b1a9c295}" scalemaxdenom="5000"/>
          </rule>
          <rule label="Refoulement eaux pluviales " symbol="25" filter=" &quot;networktype&quot; IN ('PLU','03') and  &quot;fonctionCannAss&quot; = '02'" key="{95b411e6-2b95-4638-810c-cebf2f9a9a05}"/>
        </rule>
      </rule>
      <rule symbol="26" filter="ELSE" key="{146b5a78-5b72-4838-8cb1-ae306bc010b5}">
        <rule label="0 - 5000" symbol="27" key="{d337d640-72b2-476f-9aeb-813fdd0a2e58}" scalemaxdenom="5000"/>
      </rule>
    </rules>
    <symbols>
      <symbol alpha="1" type="line" name="0" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="1" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@1@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="10" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="11" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@11@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="12" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="13" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@13@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="14" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="15" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@15@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="16" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="17" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@17@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="18" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="19" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="2" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="20" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@20@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="21" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="22" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@22@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="23" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="24" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@24@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="25" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="26" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="27" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@27@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="3" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@3@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="4" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="5" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@5@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="6" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="7" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@7@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="8" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="line" name="9" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="MarkerLine" enabled="1" pass="0">
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
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" type="marker" name="@9@0" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
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
      <text-style fontSizeUnit="Point" fontStrikeout="0" blendMode="0" fieldName=" &quot;nominaldiameter&quot; *1000" previewBkgrdColor="255,255,255,255" fontCapitals="0" fontKerning="1" fontItalic="0" fontSize="8.25" namedStyle="Normal" multilineHeight="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" fontLetterSpacing="0" fontUnderline="0" isExpression="1" useSubstitutions="0" fontFamily="MS Shell Dlg 2" textOrientation="horizontal" fontWeight="50" fontWordSpacing="0" textColor="0,0,0,255">
        <text-buffer bufferBlendMode="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferNoFill="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferSizeUnits="MM" bufferDraw="1" bufferOpacity="1"/>
        <background shapeRadiiUnit="MM" shapeOffsetX="0" shapeOffsetY="0" shapeOpacity="1" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeRadiiY="0" shapeBlendMode="0" shapeRotation="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeSizeY="0" shapeType="0" shapeSizeUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeBorderColor="128,128,128,255" shapeSizeType="0" shapeJoinStyle="64" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeSVGFile="" shapeRotationType="0">
          <symbol alpha="1" type="marker" name="markerSymbol" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
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
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadius="1.5" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowScale="100" shadowOffsetUnit="MM" shadowBlendMode="6" shadowOffsetGlobal="1" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowColor="0,0,0,255" shadowDraw="0" shadowOpacity="0.7" shadowRadiusUnit="MM"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" formatNumbers="0" reverseDirectionSymbol="0" placeDirectionSymbol="0" multilineAlign="4294967295" rightDirectionSymbol=">" decimals="3" leftDirectionSymbol="&lt;" wrapChar="" plussign="0" autoWrapLength="0"/>
      <placement dist="0.5" maxCurvedCharAngleOut="-25" maxCurvedCharAngleIn="25" layerType="LineGeometry" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" quadOffset="4" placementFlags="2" yOffset="0" overrunDistanceUnit="MM" offsetUnits="MapUnit" centroidInside="0" xOffset="0" geometryGeneratorType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistance="0" priority="5" geometryGeneratorEnabled="0" placement="3" geometryGenerator="" preserveRotation="1" fitInPolygonOnly="0" centroidWhole="0" offsetType="0" rotationAngle="0" distUnits="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" distMapUnitScale="3x:0,0,0,0,0,0"/>
      <rendering obstacle="1" scaleMin="1" drawLabels="1" displayAll="0" minFeatureSize="2" fontMaxPixelSize="10000" fontLimitPixelSize="0" maxNumLabels="2000" obstacleFactor="1" obstacleType="0" scaleVisibility="1" fontMinPixelSize="3" labelPerPart="0" zIndex="0" limitNumLabels="0" scaleMax="5000" mergeLines="1" upsidedownLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option name="properties"/>
          <Option value="collection" type="QString" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" type="QString" name="anchorPoint"/>
          <Option type="Map" name="ddProperties">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
          <Option value="false" type="bool" name="drawToAllParts"/>
          <Option value="0" type="QString" name="enabled"/>
          <Option value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer locked=&quot;0&quot; class=&quot;SimpleLine&quot; enabled=&quot;1&quot; pass=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; type=&quot;QString&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; type=&quot;QString&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString" name="lineSymbol"/>
          <Option value="0" type="double" name="minLength"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="minLengthMapUnitScale"/>
          <Option value="MM" type="QString" name="minLengthUnit"/>
          <Option value="0" type="double" name="offsetFromAnchor"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromAnchorMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromAnchorUnit"/>
          <Option value="0" type="double" name="offsetFromLabel"/>
          <Option value="3x:0,0,0,0,0,0" type="QString" name="offsetFromLabelMapUnitScale"/>
          <Option value="MM" type="QString" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory scaleBasedVisibility="0" scaleDependency="Area" minimumSize="0" maxScaleDenominator="1e+08" barWidth="5" height="15" width="15" labelPlacementMethod="XHeight" rotationOffset="270" sizeType="MM" penColor="#000000" minScaleDenominator="0" penAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" penWidth="0" lineSizeType="MM" sizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" opacity="1" enabled="0" backgroundAlpha="255">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" color="#000000" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" showAll="1" placement="2" zIndex="0" dist="0" obstacle="0" linePlacementFlags="2">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="01" type="QString" name="Acier"/>
              </Option>
              <Option type="Map">
                <Option value="02" type="QString" name="Amiante-ciment"/>
              </Option>
              <Option type="Map">
                <Option value="03" type="QString" name="Béton arme tole"/>
              </Option>
              <Option type="Map">
                <Option value="04" type="QString" name="Beton arme"/>
              </Option>
              <Option type="Map">
                <Option value="05" type="QString" name="Beton fibre"/>
              </Option>
              <Option type="Map">
                <Option value="06" type="QString" name="Beton non arme"/>
              </Option>
              <Option type="Map">
                <Option value="07" type="QString" name="Cuivre"/>
              </Option>
              <Option type="Map">
                <Option value="08" type="QString" name="Fibre ciment"/>
              </Option>
              <Option type="Map">
                <Option value="09" type="QString" name="Fibre de verre"/>
              </Option>
              <Option type="Map">
                <Option value="10" type="QString" name="Fibrociment"/>
              </Option>
              <Option type="Map">
                <Option value="11" type="QString" name="Fonte ductile"/>
              </Option>
              <Option type="Map">
                <Option value="12" type="QString" name="Fonte grise"/>
              </Option>
              <Option type="Map">
                <Option value="13" type="QString" name="Gres"/>
              </Option>
              <Option type="Map">
                <Option value="14" type="QString" name="Maconnerie"/>
              </Option>
              <Option type="Map">
                <Option value="15" type="QString" name="Meuliere"/>
              </Option>
              <Option type="Map">
                <Option value="16" type="QString" name="PEBD"/>
              </Option>
              <Option type="Map">
                <Option value="17" type="QString" name="PEHD annele"/>
              </Option>
              <Option type="Map">
                <Option value="18" type="QString" name="PEHD lisse"/>
              </Option>
              <Option type="Map">
                <Option value="19" type="QString" name="Plomb"/>
              </Option>
              <Option type="Map">
                <Option value="20" type="QString" name="PP annele"/>
              </Option>
              <Option type="Map">
                <Option value="21" type="QString" name="PP lisse"/>
              </Option>
              <Option type="Map">
                <Option value="22" type="QString" name="PRV A"/>
              </Option>
              <Option type="Map">
                <Option value="23" type="QString" name="PRV B"/>
              </Option>
              <Option type="Map">
                <Option value="24" type="QString" name="PVC ancien"/>
              </Option>
              <Option type="Map">
                <Option value="25" type="QString" name="PVC BO"/>
              </Option>
              <Option type="Map">
                <Option value="26" type="QString" name="PVC U annele"/>
              </Option>
              <Option type="Map">
                <Option value="27" type="QString" name="PVC U lisse"/>
              </Option>
              <Option type="Map">
                <Option value="28" type="QString" name="Tole galvanisee"/>
              </Option>
              <Option type="Map">
                <Option value="00" type="QString" name="Autre"/>
              </Option>
              <Option type="Map">
                <Option value="99" type="QString" name="Indetermine"/>
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
                <Option value="COL" type="QString" name="Collecteur enterré"/>
              </Option>
              <Option type="Map">
                <Option value="FOS" type="QString" name="Fossé"/>
              </Option>
              <Option type="Map">
                <Option value="TRA" type="QString" name="Tranchée"/>
              </Option>
              <Option type="Map">
                <Option value="CHE" type="QString" name="Chemin agricole"/>
              </Option>
              <Option type="Map">
                <Option value="NOU" type="QString" name="Noue"/>
              </Option>
              <Option type="Map">
                <Option value="CAN" type="QString" name="Caniveau"/>
              </Option>
              <Option type="Map">
                <Option value="HAI" type="QString" name="Haie"/>
              </Option>
              <Option type="Map">
                <Option value="FAS" type="QString" name="Fascine"/>
              </Option>
              <Option type="Map">
                <Option value="CHV" type="QString" name="Chevets"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="BET" type="QString" name="Bétonné"/>
              </Option>
              <Option type="Map">
                <Option value="REV" type="QString" name="Revêtu"/>
              </Option>
              <Option type="Map">
                <Option value="ENH" type="QString" name="Enherbé"/>
              </Option>
              <Option type="Map">
                <Option value="NUE" type="QString" name="Terre à nue"/>
              </Option>
              <Option type="Map">
                <Option value="TSD" type="QString" name="Tranchée simple à double vidange"/>
              </Option>
              <Option type="Map">
                <Option value="TCD" type="QString" name="Tranchée compose à double vidange"/>
              </Option>
              <Option type="Map">
                <Option value="TCS" type="QString" name="Tranchée composée stockante"/>
              </Option>
              <Option type="Map">
                <Option value="TIN" type="QString" name="Tranchée infiltrante"/>
              </Option>
              <Option type="Map">
                <Option value="TCI" type="QString" name="Tranchée composée infiltrante"/>
              </Option>
              <Option type="Map">
                <Option value="NIN" type="QString" name="Noue d'infiltration"/>
              </Option>
              <Option type="Map">
                <Option value="NST" type="QString" name="Noue stockante"/>
              </Option>
              <Option type="Map">
                <Option value="NDV" type="QString" name="Noue à double vidange"/>
              </Option>
              <Option type="Map">
                <Option value="CIR" type="QString" name="Circulaire"/>
              </Option>
              <Option type="Map">
                <Option value="AQU" type="QString" name="Aqueduc"/>
              </Option>
              <Option type="Map">
                <Option value="OVO" type="QString" name="Ovoide"/>
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
                <Option value="0" type="QString" name="Non"/>
              </Option>
              <Option type="Map">
                <Option value="1" type="QString" name="Oui"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="1" type="QString" name="Gravitaire"/>
              </Option>
              <Option type="Map">
                <Option value="2" type="QString" name="Force"/>
              </Option>
              <Option type="Map">
                <Option value="3" type="QString" name="Sous-vide"/>
              </Option>
              <Option type="Map">
                <Option value="0" type="QString" name="Autre"/>
              </Option>
              <Option type="Map">
                <Option value="99" type="QString" name="Indetermine"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="1" type="QString" name="Oui"/>
              </Option>
              <Option type="Map">
                <Option value="0" type="QString" name="Non"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="A" type="QString" name="A"/>
              </Option>
              <Option type="Map">
                <Option value="B" type="QString" name="B"/>
              </Option>
              <Option type="Map">
                <Option value="C" type="QString" name="C"/>
              </Option>
              <Option type="Map">
                <Option value="NC" type="QString" name="NC"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="1" type="QString" name="Classe A"/>
              </Option>
              <Option type="Map">
                <Option value="2" type="QString" name="Classe B"/>
              </Option>
              <Option type="Map">
                <Option value="3" type="QString" name="Classe C"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="1" type="QString" name="Classe A"/>
              </Option>
              <Option type="Map">
                <Option value="2" type="QString" name="Classe B"/>
              </Option>
              <Option type="Map">
                <Option value="3" type="QString" name="Classe C"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="PLU" type="QString" name="Pluvial"/>
              </Option>
              <Option type="Map">
                <Option value="USE" type="QString" name="Eaux usees"/>
              </Option>
              <Option type="Map">
                <Option value="UNI" type="QString" name="Unitaire"/>
              </Option>
              <Option type="Map">
                <Option value="IND" type="QString" name="Industriel"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="GRA" type="QString" name="Gravitaire"/>
              </Option>
              <Option type="Map">
                <Option value="DIF" type="QString" name="Ruissellement diffus"/>
              </Option>
              <Option type="Map">
                <Option value="CHU" type="QString" name="En chute"/>
              </Option>
              <Option type="Map">
                <Option value="REG" type="QString" name="Régulé"/>
              </Option>
              <Option type="Map">
                <Option value="PRE" type="QString" name="Sous-pression"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="GRA" type="QString" name="Gravitaire"/>
              </Option>
              <Option type="Map">
                <Option value="REG" type="QString" name="Régulé"/>
              </Option>
              <Option type="Map">
                <Option value="INF" type="QString" name="Infiltration"/>
              </Option>
              <Option type="Map">
                <Option value="PRE" type="QString" name="Sous pressions"/>
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
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="1" type="QString" name="Transport"/>
              </Option>
              <Option type="Map">
                <Option value="2" type="QString" name="Collecte"/>
              </Option>
              <Option type="Map">
                <Option value="3" type="QString" name="Stockage"/>
              </Option>
              <Option type="Map">
                <Option value="4" type="QString" name="Régulation"/>
              </Option>
              <Option type="Map">
                <Option value="5" type="QString" name="Traitement"/>
              </Option>
              <Option type="Map">
                <Option value="0" type="QString" name="Autre"/>
              </Option>
              <Option type="Map">
                <Option value="99" type="QString" name="Indetermine"/>
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
    <alias name="" index="0" field="pk_edge"/>
    <alias name="" index="1" field="id_edge"/>
    <alias name="" index="2" field="lpk_descriptionsystem"/>
    <alias name="" index="3" field="lid_resource_1"/>
    <alias name="" index="4" field="lid_descriptionsystem_1"/>
    <alias name="" index="5" field="lid_descriptionsystem_2"/>
    <alias name="" index="6" field="material"/>
    <alias name="" index="7" field="nominaldiameter"/>
    <alias name="" index="8" field="pipetype"/>
    <alias name="" index="9" field="pipesubtype"/>
    <alias name="" index="10" field="pipeshape"/>
    <alias name="" index="11" field="height"/>
    <alias name="" index="12" field="laterals"/>
    <alias name="" index="13" field="flowtype"/>
    <alias name="" index="14" field="elevationup"/>
    <alias name="" index="15" field="elevationdown"/>
    <alias name="" index="16" field="depthup"/>
    <alias name="" index="17" field="depthdown"/>
    <alias name="" index="18" field="domain"/>
    <alias name="" index="19" field="location"/>
    <alias name="" index="20" field="accessibility"/>
    <alias name="" index="21" field="beddingmaterial"/>
    <alias name="" index="22" field="soiltype"/>
    <alias name="" index="23" field="soilmoisture"/>
    <alias name="" index="24" field="pk_descriptionsystem"/>
    <alias name="" index="25" field="id_descriptionsystem"/>
    <alias name="" index="26" field="lpk_object"/>
    <alias name="" index="27" field="strategicvalue"/>
    <alias name="" index="28" field="operational"/>
    <alias name="" index="29" field="structuralstate"/>
    <alias name="" index="30" field="operationalstate"/>
    <alias name="" index="31" field="dateoperationalcreation"/>
    <alias name="" index="32" field="dateoperationalcreationupper"/>
    <alias name="" index="33" field="operationaldatecreationaccuracy"/>
    <alias name="" index="34" field="datetimeoperationaldestruction"/>
    <alias name="" index="35" field="geotrackingxyquality"/>
    <alias name="" index="36" field="geotrackingzquality"/>
    <alias name="" index="37" field="geotrackingdate"/>
    <alias name="" index="38" field="geotrackingsource"/>
    <alias name="" index="39" field="parameters"/>
    <alias name="" index="40" field="parameterslist"/>
    <alias name="" index="41" field="city"/>
    <alias name="" index="42" field="streetname"/>
    <alias name="" index="43" field="streetupname"/>
    <alias name="" index="44" field="streetdownname"/>
    <alias name="" index="45" field="streetcomment"/>
    <alias name="" index="46" field="lid_actor_1"/>
    <alias name="" index="47" field="lid_actor_2"/>
    <alias name="" index="48" field="lid_actor_3"/>
    <alias name="" index="49" field="lid_facility"/>
    <alias name="" index="50" field="float_1"/>
    <alias name="" index="51" field="float_2"/>
    <alias name="" index="52" field="float_3"/>
    <alias name="" index="53" field="float_4"/>
    <alias name="" index="54" field="float_5"/>
    <alias name="" index="55" field="float_6"/>
    <alias name="" index="56" field="float_7"/>
    <alias name="" index="57" field="float_8"/>
    <alias name="" index="58" field="float_9"/>
    <alias name="" index="59" field="float_10"/>
    <alias name="" index="60" field="string_1"/>
    <alias name="" index="61" field="string_2"/>
    <alias name="" index="62" field="string_3"/>
    <alias name="" index="63" field="string_4"/>
    <alias name="" index="64" field="string_5"/>
    <alias name="" index="65" field="string_6"/>
    <alias name="" index="66" field="string_7"/>
    <alias name="" index="67" field="string_8"/>
    <alias name="" index="68" field="string_9"/>
    <alias name="" index="69" field="string_10"/>
    <alias name="" index="70" field="networktype"/>
    <alias name="" index="71" field="flowconditionupstream"/>
    <alias name="" index="72" field="flowconditiondownstream"/>
    <alias name="" index="73" field="systemfunction"/>
    <alias name="" index="74" field="pk_object"/>
    <alias name="" index="75" field="id_object"/>
    <alias name="" index="76" field="lpk_revision_begin"/>
    <alias name="" index="77" field="lpk_revision_end"/>
    <alias name="" index="78" field="datetimecreation"/>
    <alias name="" index="79" field="datetimemodification"/>
    <alias name="" index="80" field="datetimedestruction"/>
    <alias name="" index="81" field="comment"/>
    <alias name="" index="82" field="name"/>
    <alias name="" index="83" field="importid"/>
    <alias name="" index="84" field="importtable"/>
    <alias name="" index="85" field="lid_actor_creator"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="pk_edge"/>
    <default expression="" applyOnUpdate="0" field="id_edge"/>
    <default expression="" applyOnUpdate="0" field="lpk_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="lid_resource_1"/>
    <default expression="" applyOnUpdate="0" field="lid_descriptionsystem_1"/>
    <default expression="" applyOnUpdate="0" field="lid_descriptionsystem_2"/>
    <default expression="" applyOnUpdate="0" field="material"/>
    <default expression="" applyOnUpdate="0" field="nominaldiameter"/>
    <default expression="" applyOnUpdate="0" field="pipetype"/>
    <default expression="" applyOnUpdate="0" field="pipesubtype"/>
    <default expression="" applyOnUpdate="0" field="pipeshape"/>
    <default expression="" applyOnUpdate="0" field="height"/>
    <default expression="" applyOnUpdate="0" field="laterals"/>
    <default expression="" applyOnUpdate="0" field="flowtype"/>
    <default expression="" applyOnUpdate="0" field="elevationup"/>
    <default expression="" applyOnUpdate="0" field="elevationdown"/>
    <default expression="" applyOnUpdate="0" field="depthup"/>
    <default expression="" applyOnUpdate="0" field="depthdown"/>
    <default expression="" applyOnUpdate="0" field="domain"/>
    <default expression="" applyOnUpdate="0" field="location"/>
    <default expression="" applyOnUpdate="0" field="accessibility"/>
    <default expression="" applyOnUpdate="0" field="beddingmaterial"/>
    <default expression="" applyOnUpdate="0" field="soiltype"/>
    <default expression="" applyOnUpdate="0" field="soilmoisture"/>
    <default expression="" applyOnUpdate="0" field="pk_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="id_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="lpk_object"/>
    <default expression="" applyOnUpdate="0" field="strategicvalue"/>
    <default expression="" applyOnUpdate="0" field="operational"/>
    <default expression="" applyOnUpdate="0" field="structuralstate"/>
    <default expression="" applyOnUpdate="0" field="operationalstate"/>
    <default expression="" applyOnUpdate="0" field="dateoperationalcreation"/>
    <default expression="" applyOnUpdate="0" field="dateoperationalcreationupper"/>
    <default expression="" applyOnUpdate="0" field="operationaldatecreationaccuracy"/>
    <default expression="" applyOnUpdate="0" field="datetimeoperationaldestruction"/>
    <default expression="" applyOnUpdate="0" field="geotrackingxyquality"/>
    <default expression="" applyOnUpdate="0" field="geotrackingzquality"/>
    <default expression="" applyOnUpdate="0" field="geotrackingdate"/>
    <default expression="" applyOnUpdate="0" field="geotrackingsource"/>
    <default expression="" applyOnUpdate="0" field="parameters"/>
    <default expression="" applyOnUpdate="0" field="parameterslist"/>
    <default expression="" applyOnUpdate="0" field="city"/>
    <default expression="" applyOnUpdate="0" field="streetname"/>
    <default expression="" applyOnUpdate="0" field="streetupname"/>
    <default expression="" applyOnUpdate="0" field="streetdownname"/>
    <default expression="" applyOnUpdate="0" field="streetcomment"/>
    <default expression="" applyOnUpdate="0" field="lid_actor_1"/>
    <default expression="" applyOnUpdate="0" field="lid_actor_2"/>
    <default expression="" applyOnUpdate="0" field="lid_actor_3"/>
    <default expression="" applyOnUpdate="0" field="lid_facility"/>
    <default expression="" applyOnUpdate="0" field="float_1"/>
    <default expression="" applyOnUpdate="0" field="float_2"/>
    <default expression="" applyOnUpdate="0" field="float_3"/>
    <default expression="" applyOnUpdate="0" field="float_4"/>
    <default expression="" applyOnUpdate="0" field="float_5"/>
    <default expression="" applyOnUpdate="0" field="float_6"/>
    <default expression="" applyOnUpdate="0" field="float_7"/>
    <default expression="" applyOnUpdate="0" field="float_8"/>
    <default expression="" applyOnUpdate="0" field="float_9"/>
    <default expression="" applyOnUpdate="0" field="float_10"/>
    <default expression="" applyOnUpdate="0" field="string_1"/>
    <default expression="" applyOnUpdate="0" field="string_2"/>
    <default expression="" applyOnUpdate="0" field="string_3"/>
    <default expression="" applyOnUpdate="0" field="string_4"/>
    <default expression="" applyOnUpdate="0" field="string_5"/>
    <default expression="" applyOnUpdate="0" field="string_6"/>
    <default expression="" applyOnUpdate="0" field="string_7"/>
    <default expression="" applyOnUpdate="0" field="string_8"/>
    <default expression="" applyOnUpdate="0" field="string_9"/>
    <default expression="" applyOnUpdate="0" field="string_10"/>
    <default expression="" applyOnUpdate="0" field="networktype"/>
    <default expression="" applyOnUpdate="0" field="flowconditionupstream"/>
    <default expression="" applyOnUpdate="0" field="flowconditiondownstream"/>
    <default expression="" applyOnUpdate="0" field="systemfunction"/>
    <default expression="" applyOnUpdate="0" field="pk_object"/>
    <default expression="" applyOnUpdate="0" field="id_object"/>
    <default expression="" applyOnUpdate="0" field="lpk_revision_begin"/>
    <default expression="" applyOnUpdate="0" field="lpk_revision_end"/>
    <default expression="" applyOnUpdate="0" field="datetimecreation"/>
    <default expression="" applyOnUpdate="0" field="datetimemodification"/>
    <default expression="" applyOnUpdate="0" field="datetimedestruction"/>
    <default expression="" applyOnUpdate="0" field="comment"/>
    <default expression="" applyOnUpdate="0" field="name"/>
    <default expression="" applyOnUpdate="0" field="importid"/>
    <default expression="" applyOnUpdate="0" field="importtable"/>
    <default expression="" applyOnUpdate="0" field="lid_actor_creator"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" exp_strength="0" field="pk_edge" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="id_edge" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lpk_descriptionsystem" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_resource_1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_descriptionsystem_1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_descriptionsystem_2" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="material" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="nominaldiameter" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pipetype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pipesubtype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pipeshape" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="height" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="laterals" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="flowtype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="elevationup" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="elevationdown" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="depthup" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="depthdown" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="domain" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="location" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="accessibility" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="beddingmaterial" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="soiltype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="soilmoisture" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pk_descriptionsystem" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="id_descriptionsystem" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lpk_object" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="strategicvalue" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="operational" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="structuralstate" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="operationalstate" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="dateoperationalcreation" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="dateoperationalcreationupper" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="operationaldatecreationaccuracy" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="datetimeoperationaldestruction" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="geotrackingxyquality" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="geotrackingzquality" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="geotrackingdate" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="geotrackingsource" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="parameters" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="parameterslist" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="city" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="streetname" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="streetupname" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="streetdownname" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="streetcomment" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_actor_1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_actor_2" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_actor_3" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_facility" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_2" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_3" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_4" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_5" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_6" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_7" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_8" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_9" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="float_10" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_2" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_3" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_4" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_5" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_6" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_7" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_8" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_9" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="string_10" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="networktype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="flowconditionupstream" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="flowconditiondownstream" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="systemfunction" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pk_object" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="id_object" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lpk_revision_begin" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lpk_revision_end" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="datetimecreation" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="datetimemodification" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="datetimedestruction" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="comment" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="name" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="importid" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="importtable" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_actor_creator" constraints="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="pk_edge" desc=""/>
    <constraint exp="" field="id_edge" desc=""/>
    <constraint exp="" field="lpk_descriptionsystem" desc=""/>
    <constraint exp="" field="lid_resource_1" desc=""/>
    <constraint exp="" field="lid_descriptionsystem_1" desc=""/>
    <constraint exp="" field="lid_descriptionsystem_2" desc=""/>
    <constraint exp="" field="material" desc=""/>
    <constraint exp="" field="nominaldiameter" desc=""/>
    <constraint exp="" field="pipetype" desc=""/>
    <constraint exp="" field="pipesubtype" desc=""/>
    <constraint exp="" field="pipeshape" desc=""/>
    <constraint exp="" field="height" desc=""/>
    <constraint exp="" field="laterals" desc=""/>
    <constraint exp="" field="flowtype" desc=""/>
    <constraint exp="" field="elevationup" desc=""/>
    <constraint exp="" field="elevationdown" desc=""/>
    <constraint exp="" field="depthup" desc=""/>
    <constraint exp="" field="depthdown" desc=""/>
    <constraint exp="" field="domain" desc=""/>
    <constraint exp="" field="location" desc=""/>
    <constraint exp="" field="accessibility" desc=""/>
    <constraint exp="" field="beddingmaterial" desc=""/>
    <constraint exp="" field="soiltype" desc=""/>
    <constraint exp="" field="soilmoisture" desc=""/>
    <constraint exp="" field="pk_descriptionsystem" desc=""/>
    <constraint exp="" field="id_descriptionsystem" desc=""/>
    <constraint exp="" field="lpk_object" desc=""/>
    <constraint exp="" field="strategicvalue" desc=""/>
    <constraint exp="" field="operational" desc=""/>
    <constraint exp="" field="structuralstate" desc=""/>
    <constraint exp="" field="operationalstate" desc=""/>
    <constraint exp="" field="dateoperationalcreation" desc=""/>
    <constraint exp="" field="dateoperationalcreationupper" desc=""/>
    <constraint exp="" field="operationaldatecreationaccuracy" desc=""/>
    <constraint exp="" field="datetimeoperationaldestruction" desc=""/>
    <constraint exp="" field="geotrackingxyquality" desc=""/>
    <constraint exp="" field="geotrackingzquality" desc=""/>
    <constraint exp="" field="geotrackingdate" desc=""/>
    <constraint exp="" field="geotrackingsource" desc=""/>
    <constraint exp="" field="parameters" desc=""/>
    <constraint exp="" field="parameterslist" desc=""/>
    <constraint exp="" field="city" desc=""/>
    <constraint exp="" field="streetname" desc=""/>
    <constraint exp="" field="streetupname" desc=""/>
    <constraint exp="" field="streetdownname" desc=""/>
    <constraint exp="" field="streetcomment" desc=""/>
    <constraint exp="" field="lid_actor_1" desc=""/>
    <constraint exp="" field="lid_actor_2" desc=""/>
    <constraint exp="" field="lid_actor_3" desc=""/>
    <constraint exp="" field="lid_facility" desc=""/>
    <constraint exp="" field="float_1" desc=""/>
    <constraint exp="" field="float_2" desc=""/>
    <constraint exp="" field="float_3" desc=""/>
    <constraint exp="" field="float_4" desc=""/>
    <constraint exp="" field="float_5" desc=""/>
    <constraint exp="" field="float_6" desc=""/>
    <constraint exp="" field="float_7" desc=""/>
    <constraint exp="" field="float_8" desc=""/>
    <constraint exp="" field="float_9" desc=""/>
    <constraint exp="" field="float_10" desc=""/>
    <constraint exp="" field="string_1" desc=""/>
    <constraint exp="" field="string_2" desc=""/>
    <constraint exp="" field="string_3" desc=""/>
    <constraint exp="" field="string_4" desc=""/>
    <constraint exp="" field="string_5" desc=""/>
    <constraint exp="" field="string_6" desc=""/>
    <constraint exp="" field="string_7" desc=""/>
    <constraint exp="" field="string_8" desc=""/>
    <constraint exp="" field="string_9" desc=""/>
    <constraint exp="" field="string_10" desc=""/>
    <constraint exp="" field="networktype" desc=""/>
    <constraint exp="" field="flowconditionupstream" desc=""/>
    <constraint exp="" field="flowconditiondownstream" desc=""/>
    <constraint exp="" field="systemfunction" desc=""/>
    <constraint exp="" field="pk_object" desc=""/>
    <constraint exp="" field="id_object" desc=""/>
    <constraint exp="" field="lpk_revision_begin" desc=""/>
    <constraint exp="" field="lpk_revision_end" desc=""/>
    <constraint exp="" field="datetimecreation" desc=""/>
    <constraint exp="" field="datetimemodification" desc=""/>
    <constraint exp="" field="datetimedestruction" desc=""/>
    <constraint exp="" field="comment" desc=""/>
    <constraint exp="" field="name" desc=""/>
    <constraint exp="" field="importid" desc=""/>
    <constraint exp="" field="importtable" desc=""/>
    <constraint exp="" field="lid_actor_creator" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="1" type="actions" width="-1"/>
      <column hidden="0" type="field" name="id_descriptionsystem" width="-1"/>
      <column hidden="0" type="field" name="lpk_descriptionsystem" width="-1"/>
      <column hidden="0" type="field" name="lid_descriptionsystem_1" width="-1"/>
      <column hidden="0" type="field" name="lid_descriptionsystem_2" width="-1"/>
      <column hidden="0" type="field" name="pk_descriptionsystem" width="-1"/>
      <column hidden="0" type="field" name="lpk_revision_begin" width="-1"/>
      <column hidden="0" type="field" name="lpk_revision_end" width="-1"/>
      <column hidden="0" type="field" name="datetimecreation" width="-1"/>
      <column hidden="0" type="field" name="datetimemodification" width="-1"/>
      <column hidden="0" type="field" name="datetimedestruction" width="-1"/>
      <column hidden="0" type="field" name="importid" width="-1"/>
      <column hidden="0" type="field" name="importtable" width="-1"/>
      <column hidden="0" type="field" name="pk_edge" width="-1"/>
      <column hidden="0" type="field" name="id_edge" width="-1"/>
      <column hidden="0" type="field" name="lid_resource_1" width="-1"/>
      <column hidden="0" type="field" name="material" width="-1"/>
      <column hidden="0" type="field" name="nominaldiameter" width="-1"/>
      <column hidden="0" type="field" name="pipetype" width="-1"/>
      <column hidden="0" type="field" name="pipesubtype" width="-1"/>
      <column hidden="0" type="field" name="pipeshape" width="-1"/>
      <column hidden="0" type="field" name="height" width="-1"/>
      <column hidden="0" type="field" name="laterals" width="-1"/>
      <column hidden="0" type="field" name="flowtype" width="-1"/>
      <column hidden="0" type="field" name="elevationup" width="-1"/>
      <column hidden="0" type="field" name="elevationdown" width="-1"/>
      <column hidden="0" type="field" name="depthup" width="-1"/>
      <column hidden="0" type="field" name="depthdown" width="-1"/>
      <column hidden="0" type="field" name="domain" width="-1"/>
      <column hidden="0" type="field" name="location" width="-1"/>
      <column hidden="0" type="field" name="accessibility" width="-1"/>
      <column hidden="0" type="field" name="beddingmaterial" width="-1"/>
      <column hidden="0" type="field" name="soiltype" width="-1"/>
      <column hidden="0" type="field" name="soilmoisture" width="-1"/>
      <column hidden="0" type="field" name="lpk_object" width="-1"/>
      <column hidden="0" type="field" name="strategicvalue" width="-1"/>
      <column hidden="0" type="field" name="operational" width="-1"/>
      <column hidden="0" type="field" name="structuralstate" width="-1"/>
      <column hidden="0" type="field" name="operationalstate" width="-1"/>
      <column hidden="0" type="field" name="dateoperationalcreation" width="-1"/>
      <column hidden="0" type="field" name="dateoperationalcreationupper" width="-1"/>
      <column hidden="0" type="field" name="operationaldatecreationaccuracy" width="-1"/>
      <column hidden="0" type="field" name="datetimeoperationaldestruction" width="-1"/>
      <column hidden="0" type="field" name="geotrackingxyquality" width="-1"/>
      <column hidden="0" type="field" name="geotrackingzquality" width="-1"/>
      <column hidden="0" type="field" name="geotrackingdate" width="-1"/>
      <column hidden="0" type="field" name="geotrackingsource" width="-1"/>
      <column hidden="0" type="field" name="parameters" width="-1"/>
      <column hidden="0" type="field" name="parameterslist" width="-1"/>
      <column hidden="0" type="field" name="city" width="-1"/>
      <column hidden="0" type="field" name="streetname" width="-1"/>
      <column hidden="0" type="field" name="streetupname" width="-1"/>
      <column hidden="0" type="field" name="streetdownname" width="-1"/>
      <column hidden="0" type="field" name="streetcomment" width="-1"/>
      <column hidden="0" type="field" name="lid_actor_1" width="-1"/>
      <column hidden="0" type="field" name="lid_actor_2" width="-1"/>
      <column hidden="0" type="field" name="lid_actor_3" width="-1"/>
      <column hidden="0" type="field" name="lid_facility" width="-1"/>
      <column hidden="0" type="field" name="float_1" width="-1"/>
      <column hidden="0" type="field" name="float_2" width="-1"/>
      <column hidden="0" type="field" name="float_3" width="-1"/>
      <column hidden="0" type="field" name="float_4" width="-1"/>
      <column hidden="0" type="field" name="float_5" width="-1"/>
      <column hidden="0" type="field" name="float_6" width="-1"/>
      <column hidden="0" type="field" name="float_7" width="-1"/>
      <column hidden="0" type="field" name="float_8" width="-1"/>
      <column hidden="0" type="field" name="float_9" width="-1"/>
      <column hidden="0" type="field" name="float_10" width="-1"/>
      <column hidden="0" type="field" name="string_1" width="-1"/>
      <column hidden="0" type="field" name="string_2" width="-1"/>
      <column hidden="0" type="field" name="string_3" width="-1"/>
      <column hidden="0" type="field" name="string_4" width="-1"/>
      <column hidden="0" type="field" name="string_5" width="-1"/>
      <column hidden="0" type="field" name="string_6" width="-1"/>
      <column hidden="0" type="field" name="string_7" width="-1"/>
      <column hidden="0" type="field" name="string_8" width="-1"/>
      <column hidden="0" type="field" name="string_9" width="-1"/>
      <column hidden="0" type="field" name="string_10" width="-1"/>
      <column hidden="0" type="field" name="networktype" width="-1"/>
      <column hidden="0" type="field" name="flowconditionupstream" width="-1"/>
      <column hidden="0" type="field" name="flowconditiondownstream" width="-1"/>
      <column hidden="0" type="field" name="systemfunction" width="-1"/>
      <column hidden="0" type="field" name="pk_object" width="-1"/>
      <column hidden="0" type="field" name="id_object" width="-1"/>
      <column hidden="0" type="field" name="comment" width="-1"/>
      <column hidden="0" type="field" name="name" width="-1"/>
      <column hidden="0" type="field" name="lid_actor_creator" width="-1"/>
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
    <attributeEditorContainer visibilityExpression="" columnCount="1" name="Réseaux" showLabel="1" visibilityExpressionEnabled="0" groupBox="0">
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
