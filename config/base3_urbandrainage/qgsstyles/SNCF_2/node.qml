<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" labelsEnabled="1" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" simplifyLocal="1" simplifyDrawingHints="0" styleCategories="AllStyleCategories" simplifyAlgorithm="0" readOnly="0" version="3.10.6-A Coruña" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" type="RuleRenderer" forceraster="0" symbollevels="0">
    <rules key="{8d79bb70-3d56-44a7-9b09-ed3642611a95}">
      <rule label="Regard" symbol="0" filter=" &quot;nodetype&quot;  = '60' " key="{1dbda66e-9a74-48f9-931e-359c3ca31688}">
        <rule label="Eaux pluviales" symbol="1" filter="&quot;networktype&quot; = 'PLU' " key="{2f18122b-dd99-49f4-9f49-5c1ba68999f1}"/>
        <rule label="Eaux Usées" symbol="2" filter="&quot;networktype&quot; = 'USE' " key="{33ab6e33-05b3-4826-a9fe-446f501c5585}"/>
        <rule label="Unitaire" symbol="3" filter="&quot;networktype&quot; = 'UNI' " key="{bb702745-da57-47af-9f8a-e0b0ee7b54ff}"/>
        <rule label="Industriel" symbol="4" filter="&quot;networktype&quot; = 'IND' " key="{ee98eb47-0dd6-4716-8f4f-8a966360e411}"/>
      </rule>
      <rule label="Branchement" symbol="5" filter=" &quot;nodetype&quot;  = '61' " key="{da89f3f5-899c-4070-bbb0-0d08ed5e159b}">
        <rule label="Eaux usées" symbol="6" filter="&quot;networktype&quot; = 'USE' " key="{784d2d51-4a31-4b8d-be70-5cd59a64570e}"/>
        <rule label="Unitaire" symbol="7" filter="&quot;networktype&quot; = 'UNI' " key="{ac6f9fb3-11f6-457b-a295-ded6e65ecbad}"/>
        <rule label="Pluviale" symbol="8" filter="&quot;networktype&quot; = 'PLU' " key="{9a43a2a7-1ee2-4e2d-be41-f7e57678b539}"/>
      </rule>
      <rule label="Grille" symbol="9" filter=" &quot;nodetype&quot;  = '71' " key="{3b51b7a1-92a7-4db2-bf4e-f59ad1cabed0}">
        <rule label="Eaux pluviales" symbol="10" filter="&quot;networktype&quot; = 'PLU' " key="{164298cf-da20-4dfa-9a92-96370a7dfa40}"/>
        <rule label="Eaux Usées" symbol="11" filter="&quot;networktype&quot; = 'USE' " key="{d16e050e-659a-46e2-b793-58c43235df41}"/>
        <rule label="Unitaire" symbol="12" filter="&quot;networktype&quot; = 'UNI' " key="{25bb33ea-b695-4d4b-b588-975511f08ba4}"/>
        <rule label="Industriel" symbol="13" filter="&quot;networktype&quot; = 'IND' " key="{226af3ae-83c3-484a-9459-d204a6afb940}"/>
      </rule>
      <rule label="Avaloir" symbol="14" filter=" &quot;nodetype&quot;  = '70' " key="{25f9f3c2-695e-4992-ab82-9f7b79884c7c}"/>
      <rule label="Avaloir grille" symbol="15" filter=" &quot;nodetype&quot;  = '72' " key="{6bbcb618-908e-47cb-a66a-8da7b2a45872}"/>
      <rule label="Poste de refoulement" symbol="16" filter=" &quot;nodetype&quot;  = '10' " key="{16f48c4a-184f-494e-ae72-6bb1346cc7eb}">
        <rule label="Eaux pluviales" symbol="17" filter="&quot;networktype&quot; = 'PLU' " key="{5493c27f-99aa-4ee7-a978-50f23a04394d}"/>
        <rule label="Eaux Usées" symbol="18" filter="&quot;networktype&quot; = 'USE' " key="{82c85b46-3db9-4533-8379-52e478563566}"/>
        <rule label="Unitaire" symbol="19" filter="&quot;networktype&quot; = 'UNI' " key="{b20cfa0c-e78c-47f2-b3ca-1390ad05cb7c}"/>
        <rule label="Industriel" symbol="20" filter="&quot;networktype&quot; = 'IND' " key="{c3c17dd9-bdde-4564-838c-a47ef8eaff80}"/>
      </rule>
      <rule label="DSH" symbol="21" filter=" &quot;nodetype&quot;  = '21' " key="{7bf88f42-c44e-495f-b6c2-54268a333549}">
        <rule label="Eaux pluviales" symbol="22" filter="&quot;networktype&quot; = 'PLU' " key="{2aac6cc9-91da-461c-8ecd-b4c0081d3a61}"/>
        <rule label="Eaux Usées" symbol="23" filter="&quot;networktype&quot; = 'USE' " key="{c34f6ae4-5562-4008-97a5-e494691ac84a}"/>
        <rule label="Unitaire" symbol="24" filter="&quot;networktype&quot; = 'UNI' " key="{fa20e50a-81dc-40f0-a50c-8999f2d8da2a}"/>
        <rule label="Industriel" symbol="25" filter="&quot;networktype&quot; = 'IND' " key="{ff69acb3-f534-4b83-9352-0d50ee4322a9}"/>
      </rule>
      <rule label="Gouttière" symbol="26" filter=" &quot;nodetype&quot;  = '74' " key="{4e19d1fe-ded8-4220-b5b1-119481512103}">
        <rule label="Eaux pluviales" symbol="27" filter="&quot;networktype&quot; = 'PLU' " key="{7abf00d5-013b-44d5-987f-42fb0978366f}"/>
        <rule label="Eaux Usées" symbol="28" filter="&quot;networktype&quot; = 'USE' " key="{c100c3de-24c5-4e82-b7ba-750f4d740c54}"/>
        <rule label="Unitaire" symbol="29" filter="&quot;networktype&quot; = 'UNI' " key="{dec7a18f-8e04-450a-b835-c1fc66088619}"/>
      </rule>
      <rule label="Ouvrage spécial" filter=" &quot;TYP_POINTS&quot; = 'Ouvrage spécial'" key="{db7fdf51-a1b2-4384-b3eb-c69746b04a12}">
        <rule label="Chasse d'eau" symbol="30" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Chasse deau'" key="{11b0c499-186f-404a-a99a-07af955247d1}"/>
        <rule label="Déssableur" symbol="31" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Déssableur'" key="{e15a51c6-7ab9-450c-a196-6b6b3465d8f3}"/>
        <rule label="Siphon" symbol="32" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Siphon'" key="{9f9ee3e5-9b17-49a0-8a53-7a2adf6a0a8a}"/>
        <rule label="Déversoir d'orage" symbol="33" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Déversoir'" key="{c7c51d7e-12d7-49aa-9992-16765f8f849f}"/>
        <rule label="Débitmètre" symbol="34" filter=" &quot;TYP_POINTS&quot; ='Ouvrage speciale' and  &quot;TYP_OUV_SP&quot; ='Débitmètre'" key="{a5dafd06-7aa5-4bc3-889b-10e697c6be3d}"/>
      </rule>
      <rule symbol="35" filter="Else" key="{82d65fa5-5e1e-479c-9535-ec144a68392f}"/>
    </rules>
    <symbols>
      <symbol alpha="1" type="marker" name="0" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.4"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="1" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.4"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="10" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="cross_fill"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
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
      <symbol alpha="1" type="marker" name="11" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="170,108,16,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="cross_fill"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
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
      <symbol alpha="1" type="marker" name="12" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="239,213,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="239,213,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="cross_fill"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="239,213,0,255"/>
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
      <symbol alpha="1" type="marker" name="13" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="cross_fill"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,0,0,255"/>
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
      <symbol alpha="1" type="marker" name="14" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="semi_circle"/>
          <prop k="offset" v="0,1.30000000000000004"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.95"/>
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
      <symbol alpha="1" type="marker" name="15" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="semi_circle"/>
          <prop k="offset" v="0,1.30000000000000004"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.9"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="cross_fill"/>
          <prop k="offset" v="0,-0.39000000000000001"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.8"/>
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
      <symbol alpha="1" type="marker" name="16" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
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
      <symbol alpha="1" type="marker" name="17" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,255,255"/>
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
      <symbol alpha="1" type="marker" name="18" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
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
      <symbol alpha="1" type="marker" name="19" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="239,213,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="239,213,0,255"/>
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
      <symbol alpha="1" type="marker" name="2" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.4"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="20" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,0,0,255"/>
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
      <symbol alpha="1" type="marker" name="21" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="132,132,132,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="pentagon"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="3"/>
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
      <symbol alpha="1" type="marker" name="22" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="pentagon"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="3"/>
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
      <symbol alpha="1" type="marker" name="23" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="170,108,16,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="170,108,16,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="170,108,16,255"/>
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
      <symbol alpha="1" type="marker" name="24" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="239,213,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="pentagon"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="3"/>
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
      <symbol alpha="1" type="marker" name="25" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="pentagon"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="3"/>
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
      <symbol alpha="1" type="marker" name="26" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="27" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="28" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="170,108,16,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="29" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="239,213,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="3" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="239,213,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.4"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="239,213,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="30" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="9,2,2,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.5"/>
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
      <symbol alpha="1" type="marker" name="31" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="half_square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.5"/>
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
      <symbol alpha="1" type="marker" name="32" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="182,182,183,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.5"/>
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
      <symbol alpha="1" type="marker" name="33" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="45"/>
          <prop k="color" v="9,2,2,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="4"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="225"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="filled_arrowhead"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="4"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="fillColor">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="case &#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux pluviales' then  color_rgba( 0, 45, 207, 255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Unitaire' then  color_rgba( 0,250 ,0 ,255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux usées' then  color_rgba( 250, 0, 0, 255)&#xd;&#xa;&#x9;end" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="45"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="filled_arrowhead"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="4"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="fillColor">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="case &#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux pluviales' then  color_rgba( 0, 45, 207, 255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Unitaire' then  color_rgba( 0,250 ,0 ,255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux usées' then  color_rgba( 250, 0, 0, 255)&#xd;&#xa;&#x9;end" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" name="34" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="FontMarker" enabled="1" pass="0">
          <prop k="angle" v="220"/>
          <prop k="chr" v=""/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="font" v="Dingbats"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="offset" v="0,3"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,255,255,255"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="size" v="6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="220"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="line"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="60"/>
          <prop k="color" v="255,0,0,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="4"/>
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
      <symbol alpha="1" type="marker" name="35" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="112,112,112,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="diamond"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="3"/>
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
      <symbol alpha="1" type="marker" name="4" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.4"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
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
      <symbol alpha="1" type="marker" name="5" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="9,2,2,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.2"/>
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
      <symbol alpha="1" type="marker" name="6" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.2"/>
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
      <symbol alpha="1" type="marker" name="7" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="51,160,44,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.2"/>
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
      <symbol alpha="1" type="marker" name="8" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="9,2,2,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.2"/>
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
      <symbol alpha="1" type="marker" name="9" clip_to_extent="1" force_rhr="0">
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.6"/>
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
        <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="14,14,29,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="cross_fill"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="14,14,26,255"/>
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
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontSizeUnit="Point" fontStrikeout="0" blendMode="0" fieldName="if( &quot;nodetype&quot; = 74,'', &quot;name&quot; )" previewBkgrdColor="255,255,255,255" fontCapitals="0" fontKerning="1" fontItalic="0" fontSize="8.25" namedStyle="Normal" multilineHeight="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" fontLetterSpacing="0" fontUnderline="0" isExpression="1" useSubstitutions="0" fontFamily="MS Shell Dlg 2" textOrientation="horizontal" fontWeight="50" fontWordSpacing="0" textColor="0,0,0,255">
        <text-buffer bufferBlendMode="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferNoFill="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferSizeUnits="MM" bufferDraw="1" bufferOpacity="1"/>
        <background shapeRadiiUnit="MM" shapeOffsetX="0" shapeOffsetY="0" shapeOpacity="1" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeRadiiY="0" shapeBlendMode="0" shapeRotation="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeSizeY="0" shapeType="0" shapeSizeUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeBorderColor="128,128,128,255" shapeSizeType="0" shapeJoinStyle="64" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeSVGFile="" shapeRotationType="0">
          <symbol alpha="1" type="marker" name="markerSymbol" clip_to_extent="1" force_rhr="0">
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="164,113,88,255"/>
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
      <text-format useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" formatNumbers="0" reverseDirectionSymbol="0" placeDirectionSymbol="0" multilineAlign="3" rightDirectionSymbol=">" decimals="3" leftDirectionSymbol="&lt;" wrapChar="" plussign="0" autoWrapLength="0"/>
      <placement dist="2.2" maxCurvedCharAngleOut="-25" maxCurvedCharAngleIn="25" layerType="PointGeometry" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" quadOffset="4" placementFlags="10" yOffset="0" overrunDistanceUnit="MM" offsetUnits="MapUnit" centroidInside="0" xOffset="0" geometryGeneratorType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistance="0" priority="5" geometryGeneratorEnabled="0" placement="6" geometryGenerator="" preserveRotation="1" fitInPolygonOnly="0" centroidWhole="0" offsetType="0" rotationAngle="0" distUnits="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" distMapUnitScale="3x:0,0,0,0,0,0"/>
      <rendering obstacle="1" scaleMin="1" drawLabels="1" displayAll="1" minFeatureSize="0" fontMaxPixelSize="10000" fontLimitPixelSize="0" maxNumLabels="2000" obstacleFactor="1" obstacleType="0" scaleVisibility="0" fontMinPixelSize="3" labelPerPart="0" zIndex="0" limitNumLabels="0" scaleMax="10000000" mergeLines="0" upsidedownLabels="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option type="Map" name="properties">
            <Option type="Map" name="Color">
              <Option value="false" type="bool" name="active"/>
              <Option value="@symbol_color" type="QString" name="expression"/>
              <Option value="3" type="int" name="type"/>
            </Option>
          </Option>
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
    <property key="dualview/previewExpressions">
      <value>COALESCE("IDNUM", '&lt;NULL>')</value>
    </property>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory scaleBasedVisibility="0" scaleDependency="Area" minimumSize="0" maxScaleDenominator="1e+08" barWidth="5" height="15" width="15" labelPlacementMethod="XHeight" rotationOffset="270" sizeType="MM" penColor="#000000" minScaleDenominator="-2.14748e+09" penAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" penWidth="0" lineSizeType="MM" sizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" opacity="1" enabled="0" backgroundAlpha="255">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" color="#000000" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" showAll="1" placement="0" zIndex="0" dist="0" obstacle="0" linePlacementFlags="2">
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
    <field name="pk_node">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_node">
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
    <field name="lid_descriptionsystem_1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="elevationinvert">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="elevationcover">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="depthinvert">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="altitude1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="depth1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nodetype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="60" type="QString" name="Regard"/>
              </Option>
              <Option type="Map">
                <Option value="61" type="QString" name="Branchement"/>
              </Option>
              <Option type="Map">
                <Option value="62" type="QString" name="Regard mixte EP EU"/>
              </Option>
              <Option type="Map">
                <Option value="70" type="QString" name="Avaloir"/>
              </Option>
              <Option type="Map">
                <Option value="71" type="QString" name="Grille"/>
              </Option>
              <Option type="Map">
                <Option value="72" type="QString" name="Grille avaloir"/>
              </Option>
              <Option type="Map">
                <Option value="73" type="QString" name="Tete de buse"/>
              </Option>
              <Option type="Map">
                <Option value="74" type="QString" name="Gouttière"/>
              </Option>
              <Option type="Map">
                <Option value="10" type="QString" name="Poste de refoulement"/>
              </Option>
              <Option type="Map">
                <Option value="20" type="QString" name="Station d epuration"/>
              </Option>
              <Option type="Map">
                <Option value="21" type="QString" name="Débourbeur/déshuileur"/>
              </Option>
              <Option type="Map">
                <Option value="22" type="QString" name="Dessableur"/>
              </Option>
              <Option type="Map">
                <Option value="23" type="QString" name="Depierreur"/>
              </Option>
              <Option type="Map">
                <Option value="24" type="QString" name="Fosse septique"/>
              </Option>
              <Option type="Map">
                <Option value="30" type="QString" name="Bassin de stockage"/>
              </Option>
              <Option type="Map">
                <Option value="31" type="QString" name="Puit"/>
              </Option>
              <Option type="Map">
                <Option value="32" type="QString" name="Cuve"/>
              </Option>
              <Option type="Map">
                <Option value="40" type="QString" name="Deversoir d orage"/>
              </Option>
              <Option type="Map">
                <Option value="41" type="QString" name="Régulateur de débit"/>
              </Option>
              <Option type="Map">
                <Option value="50" type="QString" name="Rejet"/>
              </Option>
              <Option type="Map">
                <Option value="51" type="QString" name="Puisard"/>
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
    <field name="nodesubtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="6001" type="QString" name="Carré"/>
              </Option>
              <Option type="Map">
                <Option value="6002" type="QString" name="Rond"/>
              </Option>
              <Option type="Map">
                <Option value="6101" type="QString" name="Passage direct"/>
              </Option>
              <Option type="Map">
                <Option value="6102" type="QString" name="Passage siphoïde"/>
              </Option>
              <Option type="Map">
                <Option value="4001" type="QString" name="Trop-plein de poste"/>
              </Option>
              <Option type="Map">
                <Option value="4002" type="QString" name="Déversoir d'orage"/>
              </Option>
              <Option type="Map">
                <Option value="4003" type="QString" name="Délestage"/>
              </Option>
              <Option type="Map">
                <Option value="4004" type="QString" name="Ouvrage de reprise de temps sec"/>
              </Option>
              <Option type="Map">
                <Option value="1001" type="QString" name="Aspiration"/>
              </Option>
              <Option type="Map">
                <Option value="1002" type="QString" name="Refoulement"/>
              </Option>
              <Option type="Map">
                <Option value="1003" type="QString" name="Relèvement"/>
              </Option>
              <Option type="Map">
                <Option value="7001" type="QString" name="Simple"/>
              </Option>
              <Option type="Map">
                <Option value="7002" type="QString" name="A grille"/>
              </Option>
              <Option type="Map">
                <Option value="7003" type="QString" name="Tampon"/>
              </Option>
              <Option type="Map">
                <Option value="00" type="QString" name="Autre"/>
              </Option>
              <Option type="Map">
                <Option value="99" type="QString" name="Indetermine"/>
              </Option>
              <Option type="Map">
                <Option value="3201" type="QString" name="Cuve infiltrante"/>
              </Option>
              <Option type="Map">
                <Option value="3202" type="QString" name="Cuve stockante"/>
              </Option>
              <Option type="Map">
                <Option value="3101" type="QString" name="Puits comblé stockant"/>
              </Option>
              <Option type="Map">
                <Option value="3102" type="QString" name="Puits composé stockant"/>
              </Option>
              <Option type="Map">
                <Option value="3103" type="QString" name="Puits préfabriqué stockant"/>
              </Option>
              <Option type="Map">
                <Option value="3104" type="QString" name="Puits préfabriqué à double vidange"/>
              </Option>
              <Option type="Map">
                <Option value="3105" type="QString" name="Puits comblé à double vidange"/>
              </Option>
              <Option type="Map">
                <Option value="3106" type="QString" name="Puits composé à double vidange"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="accessibility">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="OUV" type="QString" name="Ouvrable"/>
              </Option>
              <Option type="Map">
                <Option value="OUN" type="QString" name="Ouvrable non visitable"/>
              </Option>
              <Option type="Map">
                <Option value="PRI" type="QString" name="En privé"/>
              </Option>
              <Option type="Map">
                <Option value="NOU" type="QString" name="Non ouvrable"/>
              </Option>
              <Option type="Map">
                <Option value="NVU" type="QString" name="Non vu"/>
              </Option>
              <Option type="Map">
                <Option value="REC" type="QString" name="Recouvert"/>
              </Option>
            </Option>
          </Option>
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
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="RCA" type="QString" name="Route carrossable"/>
              </Option>
              <Option type="Map">
                <Option value="HER" type="QString" name="Herbe/TN"/>
              </Option>
              <Option type="Map">
                <Option value="TRO" type="QString" name="Trottoir"/>
              </Option>
              <Option type="Map">
                <Option value="PAR" type="QString" name="Parking"/>
              </Option>
              <Option type="Map">
                <Option value="BAT" type="QString" name="Bâtiment"/>
              </Option>
              <Option type="Map">
                <Option value="CHE" type="QString" name="Chemin piéton"/>
              </Option>
              <Option type="Map">
                <Option value="VFE" type="QString" name="Voie ferrées"/>
              </Option>
              <Option type="Map">
                <Option value="VOI" type="QString" name="Voirie"/>
              </Option>
              <Option type="Map">
                <Option value="COT" type="QString" name="Accotement"/>
              </Option>
            </Option>
          </Option>
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
    <field name="lenght">
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
    <field name="lid_resource_2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_resource_3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_resource_4">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_resource_5">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_resource_6">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="manholecovershape">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="CAR" type="QString" name="Carre"/>
              </Option>
              <Option type="Map">
                <Option value="CIR" type="QString" name="Circulaire"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="manholecovertype">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="manholecoverdiameter">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="manholematerial">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="01" type="QString" name="Béton préfabriqué"/>
              </Option>
              <Option type="Map">
                <Option value="02" type="QString" name="PE"/>
              </Option>
              <Option type="Map">
                <Option value="03" type="QString" name="Chemisage"/>
              </Option>
              <Option type="Map">
                <Option value="00" type="QString" name="Autre"/>
              </Option>
              <Option type="Map">
                <Option value="99" type="QString" name="Inconnu"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="manholeshape">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="CAR" type="QString" name="Carre"/>
              </Option>
              <Option type="Map">
                <Option value="CIR" type="QString" name="Circulaire"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="presencesteps">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="presencehandle">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="presencelowflowchannel">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="presencesiphoidpartition">
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
    <field name="presencelid">
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
    <field name="psnominalcapacity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="psfence">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="psstormwaterinlet">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pslocked">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="psh2streatment">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pseleccabinet">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pseleccabinetlocked">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="psremotemonitoring">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="psremotemonitoringcomment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pspumpswitchingcontroller">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pspumpswitchingcontrollertype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="SNV" type="QString" name="Sonde de niveau"/>
              </Option>
              <Option type="Map">
                <Option value="PIE" type="QString" name="Sonde Piezo"/>
              </Option>
              <Option type="Map">
                <Option value="SOS" type="QString" name="Sonde ultrason"/>
              </Option>
              <Option type="Map">
                <Option value="AUT" type="QString" name="Autre"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="psfloatnumber">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="psfailurecontrollertype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="NON" type="QString" name="Non"/>
              </Option>
              <Option type="Map">
                <Option value="SNV" type="QString" name="Sonde de niveau"/>
              </Option>
              <Option type="Map">
                <Option value="PIE" type="QString" name="Sonde Piezo"/>
              </Option>
              <Option type="Map">
                <Option value="SOS" type="QString" name="Sonde ultrason"/>
              </Option>
              <Option type="Map">
                <Option value="AUT" type="QString" name="Autre"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="psmaterial">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="BET" type="QString" name="Béton"/>
              </Option>
              <Option type="Map">
                <Option value="BER" type="QString" name="Béton revêtu"/>
              </Option>
              <Option type="Map">
                <Option value="POL" type="QString" name="Polyester"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="psfallprotectiongratings">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="psoverflow">
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
    <field name="psinletscreen">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pspumpnumber">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="psguiderail">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pspumpliftingchain">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pscheckvalve">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="psgatevalve">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="pspressureport">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="DSHroleouvrage">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lateralusercategory">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
              <Option type="Map">
                <Option value="DOM" type="QString" name="dommestique"/>
              </Option>
              <Option type="Map">
                <Option value="IND" type="QString" name="industriel"/>
              </Option>
              <Option type="Map">
                <Option value="COL" type="QString" name="collectif"/>
              </Option>
              <Option type="Map">
                <Option value="AGR" type="QString" name="agricole"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="presencealarm">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="presencecontroller">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="sedimenttrap">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option value="" type="QString" name="/"/>
              </Option>
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
    <field name="x">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dx">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="y">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dy">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="z">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dz">
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
    <alias name="" index="0" field="pk_node"/>
    <alias name="" index="1" field="id_node"/>
    <alias name="" index="2" field="lpk_descriptionsystem"/>
    <alias name="" index="3" field="lid_descriptionsystem_1"/>
    <alias name="" index="4" field="elevationinvert"/>
    <alias name="" index="5" field="elevationcover"/>
    <alias name="" index="6" field="depthinvert"/>
    <alias name="" index="7" field="altitude1"/>
    <alias name="" index="8" field="depth1"/>
    <alias name="" index="9" field="nodetype"/>
    <alias name="" index="10" field="nodesubtype"/>
    <alias name="" index="11" field="accessibility"/>
    <alias name="" index="12" field="domain"/>
    <alias name="" index="13" field="location"/>
    <alias name="" index="14" field="width"/>
    <alias name="" index="15" field="lenght"/>
    <alias name="" index="16" field="lid_resource_1"/>
    <alias name="" index="17" field="lid_resource_2"/>
    <alias name="" index="18" field="lid_resource_3"/>
    <alias name="" index="19" field="lid_resource_4"/>
    <alias name="" index="20" field="lid_resource_5"/>
    <alias name="" index="21" field="lid_resource_6"/>
    <alias name="" index="22" field="manholecovershape"/>
    <alias name="" index="23" field="manholecovertype"/>
    <alias name="" index="24" field="manholecoverdiameter"/>
    <alias name="" index="25" field="manholematerial"/>
    <alias name="" index="26" field="manholeshape"/>
    <alias name="" index="27" field="presencesteps"/>
    <alias name="" index="28" field="presencehandle"/>
    <alias name="" index="29" field="presencelowflowchannel"/>
    <alias name="" index="30" field="presencesiphoidpartition"/>
    <alias name="" index="31" field="presencelid"/>
    <alias name="" index="32" field="psnominalcapacity"/>
    <alias name="" index="33" field="psfence"/>
    <alias name="" index="34" field="psstormwaterinlet"/>
    <alias name="" index="35" field="pslocked"/>
    <alias name="" index="36" field="psh2streatment"/>
    <alias name="" index="37" field="pseleccabinet"/>
    <alias name="" index="38" field="pseleccabinetlocked"/>
    <alias name="" index="39" field="psremotemonitoring"/>
    <alias name="" index="40" field="psremotemonitoringcomment"/>
    <alias name="" index="41" field="pspumpswitchingcontroller"/>
    <alias name="" index="42" field="pspumpswitchingcontrollertype"/>
    <alias name="" index="43" field="psfloatnumber"/>
    <alias name="" index="44" field="psfailurecontrollertype"/>
    <alias name="" index="45" field="psmaterial"/>
    <alias name="" index="46" field="psfallprotectiongratings"/>
    <alias name="" index="47" field="psoverflow"/>
    <alias name="" index="48" field="psinletscreen"/>
    <alias name="" index="49" field="pspumpnumber"/>
    <alias name="" index="50" field="psguiderail"/>
    <alias name="" index="51" field="pspumpliftingchain"/>
    <alias name="" index="52" field="pscheckvalve"/>
    <alias name="" index="53" field="psgatevalve"/>
    <alias name="" index="54" field="pspressureport"/>
    <alias name="" index="55" field="DSHroleouvrage"/>
    <alias name="" index="56" field="lateralusercategory"/>
    <alias name="" index="57" field="presencealarm"/>
    <alias name="" index="58" field="presencecontroller"/>
    <alias name="" index="59" field="sedimenttrap"/>
    <alias name="" index="60" field="x"/>
    <alias name="" index="61" field="dx"/>
    <alias name="" index="62" field="y"/>
    <alias name="" index="63" field="dy"/>
    <alias name="" index="64" field="z"/>
    <alias name="" index="65" field="dz"/>
    <alias name="" index="66" field="pk_descriptionsystem"/>
    <alias name="" index="67" field="id_descriptionsystem"/>
    <alias name="" index="68" field="lpk_object"/>
    <alias name="" index="69" field="strategicvalue"/>
    <alias name="" index="70" field="operational"/>
    <alias name="" index="71" field="structuralstate"/>
    <alias name="" index="72" field="operationalstate"/>
    <alias name="" index="73" field="dateoperationalcreation"/>
    <alias name="" index="74" field="dateoperationalcreationupper"/>
    <alias name="" index="75" field="operationaldatecreationaccuracy"/>
    <alias name="" index="76" field="datetimeoperationaldestruction"/>
    <alias name="" index="77" field="geotrackingxyquality"/>
    <alias name="" index="78" field="geotrackingzquality"/>
    <alias name="" index="79" field="geotrackingdate"/>
    <alias name="" index="80" field="geotrackingsource"/>
    <alias name="" index="81" field="parameters"/>
    <alias name="" index="82" field="parameterslist"/>
    <alias name="" index="83" field="city"/>
    <alias name="" index="84" field="streetname"/>
    <alias name="" index="85" field="streetupname"/>
    <alias name="" index="86" field="streetdownname"/>
    <alias name="" index="87" field="streetcomment"/>
    <alias name="" index="88" field="lid_actor_1"/>
    <alias name="" index="89" field="lid_actor_2"/>
    <alias name="" index="90" field="lid_actor_3"/>
    <alias name="" index="91" field="lid_facility"/>
    <alias name="" index="92" field="float_1"/>
    <alias name="" index="93" field="float_2"/>
    <alias name="" index="94" field="float_3"/>
    <alias name="" index="95" field="float_4"/>
    <alias name="" index="96" field="float_5"/>
    <alias name="" index="97" field="float_6"/>
    <alias name="" index="98" field="float_7"/>
    <alias name="" index="99" field="float_8"/>
    <alias name="" index="100" field="float_9"/>
    <alias name="" index="101" field="float_10"/>
    <alias name="" index="102" field="string_1"/>
    <alias name="" index="103" field="string_2"/>
    <alias name="" index="104" field="string_3"/>
    <alias name="" index="105" field="string_4"/>
    <alias name="" index="106" field="string_5"/>
    <alias name="" index="107" field="string_6"/>
    <alias name="" index="108" field="string_7"/>
    <alias name="" index="109" field="string_8"/>
    <alias name="" index="110" field="string_9"/>
    <alias name="" index="111" field="string_10"/>
    <alias name="" index="112" field="networktype"/>
    <alias name="" index="113" field="flowconditionupstream"/>
    <alias name="" index="114" field="flowconditiondownstream"/>
    <alias name="" index="115" field="systemfunction"/>
    <alias name="" index="116" field="pk_object"/>
    <alias name="" index="117" field="id_object"/>
    <alias name="" index="118" field="lpk_revision_begin"/>
    <alias name="" index="119" field="lpk_revision_end"/>
    <alias name="" index="120" field="datetimecreation"/>
    <alias name="" index="121" field="datetimemodification"/>
    <alias name="" index="122" field="datetimedestruction"/>
    <alias name="" index="123" field="comment"/>
    <alias name="" index="124" field="name"/>
    <alias name="" index="125" field="importid"/>
    <alias name="" index="126" field="importtable"/>
    <alias name="" index="127" field="lid_actor_creator"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="pk_node"/>
    <default expression="" applyOnUpdate="0" field="id_node"/>
    <default expression="" applyOnUpdate="0" field="lpk_descriptionsystem"/>
    <default expression="" applyOnUpdate="0" field="lid_descriptionsystem_1"/>
    <default expression="" applyOnUpdate="0" field="elevationinvert"/>
    <default expression="" applyOnUpdate="0" field="elevationcover"/>
    <default expression="" applyOnUpdate="0" field="depthinvert"/>
    <default expression="" applyOnUpdate="0" field="altitude1"/>
    <default expression="" applyOnUpdate="0" field="depth1"/>
    <default expression="" applyOnUpdate="0" field="nodetype"/>
    <default expression="" applyOnUpdate="0" field="nodesubtype"/>
    <default expression="" applyOnUpdate="0" field="accessibility"/>
    <default expression="" applyOnUpdate="0" field="domain"/>
    <default expression="" applyOnUpdate="0" field="location"/>
    <default expression="" applyOnUpdate="0" field="width"/>
    <default expression="" applyOnUpdate="0" field="lenght"/>
    <default expression="" applyOnUpdate="0" field="lid_resource_1"/>
    <default expression="" applyOnUpdate="0" field="lid_resource_2"/>
    <default expression="" applyOnUpdate="0" field="lid_resource_3"/>
    <default expression="" applyOnUpdate="0" field="lid_resource_4"/>
    <default expression="" applyOnUpdate="0" field="lid_resource_5"/>
    <default expression="" applyOnUpdate="0" field="lid_resource_6"/>
    <default expression="" applyOnUpdate="0" field="manholecovershape"/>
    <default expression="" applyOnUpdate="0" field="manholecovertype"/>
    <default expression="" applyOnUpdate="0" field="manholecoverdiameter"/>
    <default expression="" applyOnUpdate="0" field="manholematerial"/>
    <default expression="" applyOnUpdate="0" field="manholeshape"/>
    <default expression="" applyOnUpdate="0" field="presencesteps"/>
    <default expression="" applyOnUpdate="0" field="presencehandle"/>
    <default expression="" applyOnUpdate="0" field="presencelowflowchannel"/>
    <default expression="" applyOnUpdate="0" field="presencesiphoidpartition"/>
    <default expression="" applyOnUpdate="0" field="presencelid"/>
    <default expression="" applyOnUpdate="0" field="psnominalcapacity"/>
    <default expression="" applyOnUpdate="0" field="psfence"/>
    <default expression="" applyOnUpdate="0" field="psstormwaterinlet"/>
    <default expression="" applyOnUpdate="0" field="pslocked"/>
    <default expression="" applyOnUpdate="0" field="psh2streatment"/>
    <default expression="" applyOnUpdate="0" field="pseleccabinet"/>
    <default expression="" applyOnUpdate="0" field="pseleccabinetlocked"/>
    <default expression="" applyOnUpdate="0" field="psremotemonitoring"/>
    <default expression="" applyOnUpdate="0" field="psremotemonitoringcomment"/>
    <default expression="" applyOnUpdate="0" field="pspumpswitchingcontroller"/>
    <default expression="" applyOnUpdate="0" field="pspumpswitchingcontrollertype"/>
    <default expression="" applyOnUpdate="0" field="psfloatnumber"/>
    <default expression="" applyOnUpdate="0" field="psfailurecontrollertype"/>
    <default expression="" applyOnUpdate="0" field="psmaterial"/>
    <default expression="" applyOnUpdate="0" field="psfallprotectiongratings"/>
    <default expression="" applyOnUpdate="0" field="psoverflow"/>
    <default expression="" applyOnUpdate="0" field="psinletscreen"/>
    <default expression="" applyOnUpdate="0" field="pspumpnumber"/>
    <default expression="" applyOnUpdate="0" field="psguiderail"/>
    <default expression="" applyOnUpdate="0" field="pspumpliftingchain"/>
    <default expression="" applyOnUpdate="0" field="pscheckvalve"/>
    <default expression="" applyOnUpdate="0" field="psgatevalve"/>
    <default expression="" applyOnUpdate="0" field="pspressureport"/>
    <default expression="" applyOnUpdate="0" field="DSHroleouvrage"/>
    <default expression="" applyOnUpdate="0" field="lateralusercategory"/>
    <default expression="" applyOnUpdate="0" field="presencealarm"/>
    <default expression="" applyOnUpdate="0" field="presencecontroller"/>
    <default expression="" applyOnUpdate="0" field="sedimenttrap"/>
    <default expression="" applyOnUpdate="0" field="x"/>
    <default expression="" applyOnUpdate="0" field="dx"/>
    <default expression="" applyOnUpdate="0" field="y"/>
    <default expression="" applyOnUpdate="0" field="dy"/>
    <default expression="" applyOnUpdate="0" field="z"/>
    <default expression="" applyOnUpdate="0" field="dz"/>
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
    <constraint unique_strength="0" exp_strength="0" field="pk_node" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="id_node" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lpk_descriptionsystem" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_descriptionsystem_1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="elevationinvert" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="elevationcover" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="depthinvert" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="altitude1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="depth1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="nodetype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="nodesubtype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="accessibility" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="domain" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="location" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="width" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lenght" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_resource_1" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_resource_2" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_resource_3" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_resource_4" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_resource_5" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lid_resource_6" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="manholecovershape" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="manholecovertype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="manholecoverdiameter" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="manholematerial" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="manholeshape" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="presencesteps" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="presencehandle" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="presencelowflowchannel" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="presencesiphoidpartition" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="presencelid" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psnominalcapacity" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psfence" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psstormwaterinlet" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pslocked" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psh2streatment" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pseleccabinet" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pseleccabinetlocked" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psremotemonitoring" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psremotemonitoringcomment" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pspumpswitchingcontroller" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pspumpswitchingcontrollertype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psfloatnumber" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psfailurecontrollertype" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psmaterial" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psfallprotectiongratings" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psoverflow" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psinletscreen" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pspumpnumber" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psguiderail" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pspumpliftingchain" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pscheckvalve" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="psgatevalve" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="pspressureport" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="DSHroleouvrage" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="lateralusercategory" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="presencealarm" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="presencecontroller" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="sedimenttrap" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="x" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="dx" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="y" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="dy" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="z" constraints="0" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" field="dz" constraints="0" notnull_strength="0"/>
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
    <constraint exp="" field="pk_node" desc=""/>
    <constraint exp="" field="id_node" desc=""/>
    <constraint exp="" field="lpk_descriptionsystem" desc=""/>
    <constraint exp="" field="lid_descriptionsystem_1" desc=""/>
    <constraint exp="" field="elevationinvert" desc=""/>
    <constraint exp="" field="elevationcover" desc=""/>
    <constraint exp="" field="depthinvert" desc=""/>
    <constraint exp="" field="altitude1" desc=""/>
    <constraint exp="" field="depth1" desc=""/>
    <constraint exp="" field="nodetype" desc=""/>
    <constraint exp="" field="nodesubtype" desc=""/>
    <constraint exp="" field="accessibility" desc=""/>
    <constraint exp="" field="domain" desc=""/>
    <constraint exp="" field="location" desc=""/>
    <constraint exp="" field="width" desc=""/>
    <constraint exp="" field="lenght" desc=""/>
    <constraint exp="" field="lid_resource_1" desc=""/>
    <constraint exp="" field="lid_resource_2" desc=""/>
    <constraint exp="" field="lid_resource_3" desc=""/>
    <constraint exp="" field="lid_resource_4" desc=""/>
    <constraint exp="" field="lid_resource_5" desc=""/>
    <constraint exp="" field="lid_resource_6" desc=""/>
    <constraint exp="" field="manholecovershape" desc=""/>
    <constraint exp="" field="manholecovertype" desc=""/>
    <constraint exp="" field="manholecoverdiameter" desc=""/>
    <constraint exp="" field="manholematerial" desc=""/>
    <constraint exp="" field="manholeshape" desc=""/>
    <constraint exp="" field="presencesteps" desc=""/>
    <constraint exp="" field="presencehandle" desc=""/>
    <constraint exp="" field="presencelowflowchannel" desc=""/>
    <constraint exp="" field="presencesiphoidpartition" desc=""/>
    <constraint exp="" field="presencelid" desc=""/>
    <constraint exp="" field="psnominalcapacity" desc=""/>
    <constraint exp="" field="psfence" desc=""/>
    <constraint exp="" field="psstormwaterinlet" desc=""/>
    <constraint exp="" field="pslocked" desc=""/>
    <constraint exp="" field="psh2streatment" desc=""/>
    <constraint exp="" field="pseleccabinet" desc=""/>
    <constraint exp="" field="pseleccabinetlocked" desc=""/>
    <constraint exp="" field="psremotemonitoring" desc=""/>
    <constraint exp="" field="psremotemonitoringcomment" desc=""/>
    <constraint exp="" field="pspumpswitchingcontroller" desc=""/>
    <constraint exp="" field="pspumpswitchingcontrollertype" desc=""/>
    <constraint exp="" field="psfloatnumber" desc=""/>
    <constraint exp="" field="psfailurecontrollertype" desc=""/>
    <constraint exp="" field="psmaterial" desc=""/>
    <constraint exp="" field="psfallprotectiongratings" desc=""/>
    <constraint exp="" field="psoverflow" desc=""/>
    <constraint exp="" field="psinletscreen" desc=""/>
    <constraint exp="" field="pspumpnumber" desc=""/>
    <constraint exp="" field="psguiderail" desc=""/>
    <constraint exp="" field="pspumpliftingchain" desc=""/>
    <constraint exp="" field="pscheckvalve" desc=""/>
    <constraint exp="" field="psgatevalve" desc=""/>
    <constraint exp="" field="pspressureport" desc=""/>
    <constraint exp="" field="DSHroleouvrage" desc=""/>
    <constraint exp="" field="lateralusercategory" desc=""/>
    <constraint exp="" field="presencealarm" desc=""/>
    <constraint exp="" field="presencecontroller" desc=""/>
    <constraint exp="" field="sedimenttrap" desc=""/>
    <constraint exp="" field="x" desc=""/>
    <constraint exp="" field="dx" desc=""/>
    <constraint exp="" field="y" desc=""/>
    <constraint exp="" field="dy" desc=""/>
    <constraint exp="" field="z" desc=""/>
    <constraint exp="" field="dz" desc=""/>
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
  <attributetableconfig sortExpression="&quot;typeOuvrageAss&quot;" sortOrder="1" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="1" type="actions" width="-1"/>
      <column hidden="0" type="field" name="id_descriptionsystem" width="-1"/>
      <column hidden="0" type="field" name="lpk_descriptionsystem" width="-1"/>
      <column hidden="0" type="field" name="DSHroleouvrage" width="-1"/>
      <column hidden="0" type="field" name="pk_descriptionsystem" width="-1"/>
      <column hidden="0" type="field" name="lpk_revision_begin" width="-1"/>
      <column hidden="0" type="field" name="lpk_revision_end" width="-1"/>
      <column hidden="0" type="field" name="datetimecreation" width="-1"/>
      <column hidden="0" type="field" name="datetimemodification" width="-1"/>
      <column hidden="0" type="field" name="datetimedestruction" width="-1"/>
      <column hidden="0" type="field" name="importid" width="-1"/>
      <column hidden="0" type="field" name="importtable" width="-1"/>
      <column hidden="0" type="field" name="pk_node" width="-1"/>
      <column hidden="0" type="field" name="id_node" width="-1"/>
      <column hidden="0" type="field" name="lid_descriptionsystem_1" width="-1"/>
      <column hidden="0" type="field" name="elevationinvert" width="-1"/>
      <column hidden="0" type="field" name="elevationcover" width="-1"/>
      <column hidden="0" type="field" name="depthinvert" width="-1"/>
      <column hidden="0" type="field" name="altitude1" width="-1"/>
      <column hidden="0" type="field" name="depth1" width="-1"/>
      <column hidden="0" type="field" name="nodetype" width="-1"/>
      <column hidden="0" type="field" name="nodesubtype" width="-1"/>
      <column hidden="0" type="field" name="accessibility" width="-1"/>
      <column hidden="0" type="field" name="domain" width="-1"/>
      <column hidden="0" type="field" name="location" width="-1"/>
      <column hidden="0" type="field" name="width" width="-1"/>
      <column hidden="0" type="field" name="lenght" width="-1"/>
      <column hidden="0" type="field" name="lid_resource_1" width="-1"/>
      <column hidden="0" type="field" name="lid_resource_2" width="-1"/>
      <column hidden="0" type="field" name="lid_resource_3" width="-1"/>
      <column hidden="0" type="field" name="lid_resource_4" width="-1"/>
      <column hidden="0" type="field" name="lid_resource_5" width="-1"/>
      <column hidden="0" type="field" name="lid_resource_6" width="-1"/>
      <column hidden="0" type="field" name="manholecovershape" width="-1"/>
      <column hidden="0" type="field" name="manholecovertype" width="-1"/>
      <column hidden="0" type="field" name="manholecoverdiameter" width="-1"/>
      <column hidden="0" type="field" name="manholematerial" width="-1"/>
      <column hidden="0" type="field" name="manholeshape" width="-1"/>
      <column hidden="0" type="field" name="presencesteps" width="-1"/>
      <column hidden="0" type="field" name="presencehandle" width="-1"/>
      <column hidden="0" type="field" name="presencelowflowchannel" width="-1"/>
      <column hidden="0" type="field" name="presencesiphoidpartition" width="-1"/>
      <column hidden="0" type="field" name="presencelid" width="-1"/>
      <column hidden="0" type="field" name="psnominalcapacity" width="-1"/>
      <column hidden="0" type="field" name="psfence" width="-1"/>
      <column hidden="0" type="field" name="psstormwaterinlet" width="-1"/>
      <column hidden="0" type="field" name="pslocked" width="-1"/>
      <column hidden="0" type="field" name="psh2streatment" width="-1"/>
      <column hidden="0" type="field" name="pseleccabinet" width="-1"/>
      <column hidden="0" type="field" name="pseleccabinetlocked" width="-1"/>
      <column hidden="0" type="field" name="psremotemonitoring" width="-1"/>
      <column hidden="0" type="field" name="psremotemonitoringcomment" width="-1"/>
      <column hidden="0" type="field" name="pspumpswitchingcontroller" width="-1"/>
      <column hidden="0" type="field" name="pspumpswitchingcontrollertype" width="-1"/>
      <column hidden="0" type="field" name="psfloatnumber" width="-1"/>
      <column hidden="0" type="field" name="psfailurecontrollertype" width="-1"/>
      <column hidden="0" type="field" name="psmaterial" width="-1"/>
      <column hidden="0" type="field" name="psfallprotectiongratings" width="-1"/>
      <column hidden="0" type="field" name="psoverflow" width="-1"/>
      <column hidden="0" type="field" name="psinletscreen" width="-1"/>
      <column hidden="0" type="field" name="pspumpnumber" width="-1"/>
      <column hidden="0" type="field" name="psguiderail" width="-1"/>
      <column hidden="0" type="field" name="pspumpliftingchain" width="-1"/>
      <column hidden="0" type="field" name="pscheckvalve" width="-1"/>
      <column hidden="0" type="field" name="psgatevalve" width="-1"/>
      <column hidden="0" type="field" name="pspressureport" width="-1"/>
      <column hidden="0" type="field" name="lateralusercategory" width="-1"/>
      <column hidden="0" type="field" name="presencealarm" width="-1"/>
      <column hidden="0" type="field" name="presencecontroller" width="-1"/>
      <column hidden="0" type="field" name="sedimenttrap" width="-1"/>
      <column hidden="0" type="field" name="x" width="-1"/>
      <column hidden="0" type="field" name="dx" width="-1"/>
      <column hidden="0" type="field" name="y" width="-1"/>
      <column hidden="0" type="field" name="dy" width="-1"/>
      <column hidden="0" type="field" name="z" width="-1"/>
      <column hidden="0" type="field" name="dz" width="-1"/>
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
  <editforminitfilepath>U:/00_QGis/30_Urbain/Regards EU</editforminitfilepath>
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
    <attributeEditorContainer visibilityExpression="" columnCount="1" name="Général" showLabel="1" visibilityExpressionEnabled="0" groupBox="0">
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Type d'ouvrage" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="TYP_POINTS" index="-1" showLabel="1"/>
        <attributeEditorField name="TYP_RESEAU" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Identification de l'ouvrage" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ART_ID_ART" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Données générales" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="COMMUNE" index="-1" showLabel="1"/>
        <attributeEditorField name="INSEE" index="-1" showLabel="1"/>
        <attributeEditorField name="DATEMAJ" index="-1" showLabel="1"/>
        <attributeEditorField name="SYSTCOLLEC" index="-1" showLabel="1"/>
        <attributeEditorField name="SOURCEMAJ" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="3" name="Topographie du point" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="Topo_X" index="-1" showLabel="1"/>
        <attributeEditorField name="Topo_Y" index="-1" showLabel="1"/>
        <attributeEditorField name="Topo_Z_TN" index="-1" showLabel="1"/>
        <attributeEditorField name="Topo_Xp" index="-1" showLabel="1"/>
        <attributeEditorField name="Topo_Yp" index="-1" showLabel="1"/>
        <attributeEditorField name="Topo_Zp" index="-1" showLabel="1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpression="" columnCount="1" name="Regard" showLabel="1" visibilityExpressionEnabled="0" groupBox="0">
      <attributeEditorContainer visibilityExpression="" columnCount="2" name="Photo" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ART_PHOTOS" index="-1" showLabel="1"/>
        <attributeEditorField name="ART_PHOTO2" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="2" name="Arrivées" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ART_NB_ARR" index="-1" showLabel="1"/>
        <attributeEditorField name="ART_NB_BRT" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Profondeurs et chutes" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorContainer visibilityExpression="" columnCount="2" name="Profondeurs" showLabel="0" visibilityExpressionEnabled="0" groupBox="1">
          <attributeEditorField name="ART_PROF_A" index="-1" showLabel="1"/>
          <attributeEditorField name="PRO_FE_REU" index="-1" showLabel="1"/>
        </attributeEditorContainer>
        <attributeEditorField name="CHUTE_REU" index="-1" showLabel="1"/>
        <attributeEditorContainer visibilityExpression="" columnCount="3" name="Chutes" showLabel="0" visibilityExpressionEnabled="0" groupBox="1">
          <attributeEditorField name="FE_CHUTE1" index="-1" showLabel="1"/>
          <attributeEditorField name="FE_CHUTE2" index="-1" showLabel="1"/>
          <attributeEditorField name="FE_CHUTE3" index="-1" showLabel="1"/>
          <attributeEditorField name="Heure1_REU" index="-1" showLabel="1"/>
          <attributeEditorField name="Heure2_REU" index="-1" showLabel="1"/>
          <attributeEditorField name="Heure3_REU" index="-1" showLabel="1"/>
        </attributeEditorContainer>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Accessibilité" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ART_ACCESS" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Dépôts" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ART_DEPOTS" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Anomalies" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="NB_ANO_REU" index="-1" showLabel="1"/>
        <attributeEditorField name="ANOM_EU1" index="-1" showLabel="1"/>
        <attributeEditorField name="ANOM_EU2" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Travaux" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ART_TRAVAU" index="-1" showLabel="1"/>
        <attributeEditorField name="ART_PRIORI" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="3" name="Observations" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ES_REU" index="-1" showLabel="1"/>
        <attributeEditorField name="Tete_REU" index="-1" showLabel="1"/>
        <attributeEditorField name="Sec_REU" index="-1" showLabel="1"/>
        <attributeEditorField name="REGARD_PE" index="-1" showLabel="1"/>
        <attributeEditorField name="REGARD_NV" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Remarques" showLabel="0" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ART_OBSERV" index="-1" showLabel="1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpression="" columnCount="1" name="Branchement" showLabel="1" visibilityExpressionEnabled="0" groupBox="0">
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Profondeur" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="PROF_BRT" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="2" name="Cotes" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="COTE_TN" index="-1" showLabel="1"/>
        <attributeEditorField name="COTE_FE_BR" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Dépôts" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="DEPOTS_BRT" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Anomalies" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ANOM_BRT1" index="-1" showLabel="1"/>
        <attributeEditorField name="ANOM_BRT2" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Observations" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="CLOISO_BRT" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Accessibilité" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ACCES_BRT" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Remarques" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="OBSERV_BRT" index="-1" showLabel="1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpression="" columnCount="1" name="Ouvrages EP" showLabel="1" visibilityExpressionEnabled="0" groupBox="0">
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Ouvrage EP" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="TYP_OUV_EP" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Profondeur" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="PRO_OUV_EP" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="2" name="Cotes" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="COT_TN_OUV" index="-1" showLabel="1"/>
        <attributeEditorField name="COT_FE_OUV" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Dépôts" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="DEPOTS_OUV" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Anomalies" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ANOM_OUV1" index="-1" showLabel="1"/>
        <attributeEditorField name="ANOM_OUV2" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Accessbilité" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="ACCES_OUV" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Remarques" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="OBSERV_OUV" index="-1" showLabel="1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpression="" columnCount="1" name="Ouvrage spécial" showLabel="1" visibilityExpressionEnabled="0" groupBox="0">
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Type d'ouvrage spécial" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="TYP_OUV_SP" index="-1" showLabel="1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpression="" columnCount="1" name="Remarques" showLabel="1" visibilityExpressionEnabled="0" groupBox="1">
        <attributeEditorField name="OBS_OUVSP" index="-1" showLabel="1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field name="DSHroleouvrage" editable="1"/>
    <field name="accessibility" editable="1"/>
    <field name="altitude1" editable="1"/>
    <field name="city" editable="1"/>
    <field name="comment" editable="1"/>
    <field name="dateoperationalcreation" editable="1"/>
    <field name="dateoperationalcreationupper" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimemodification" editable="1"/>
    <field name="datetimeoperationaldestruction" editable="1"/>
    <field name="depth1" editable="1"/>
    <field name="depthinvert" editable="1"/>
    <field name="domain" editable="1"/>
    <field name="dx" editable="1"/>
    <field name="dy" editable="1"/>
    <field name="dz" editable="1"/>
    <field name="elevationcover" editable="1"/>
    <field name="elevationinvert" editable="1"/>
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
    <field name="geotrackingdate" editable="1"/>
    <field name="geotrackingsource" editable="1"/>
    <field name="geotrackingxyquality" editable="1"/>
    <field name="geotrackingzquality" editable="1"/>
    <field name="id_descriptionsystem" editable="1"/>
    <field name="id_node" editable="1"/>
    <field name="id_object" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="lateralusercategory" editable="1"/>
    <field name="lenght" editable="1"/>
    <field name="lid_actor_1" editable="1"/>
    <field name="lid_actor_2" editable="1"/>
    <field name="lid_actor_3" editable="1"/>
    <field name="lid_actor_creator" editable="1"/>
    <field name="lid_descriptionsystem_1" editable="1"/>
    <field name="lid_facility" editable="1"/>
    <field name="lid_resource_1" editable="1"/>
    <field name="lid_resource_2" editable="1"/>
    <field name="lid_resource_3" editable="1"/>
    <field name="lid_resource_4" editable="1"/>
    <field name="lid_resource_5" editable="1"/>
    <field name="lid_resource_6" editable="1"/>
    <field name="location" editable="1"/>
    <field name="lpk_descriptionsystem" editable="1"/>
    <field name="lpk_object" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="manholecoverdiameter" editable="1"/>
    <field name="manholecovershape" editable="1"/>
    <field name="manholecovertype" editable="1"/>
    <field name="manholematerial" editable="1"/>
    <field name="manholeshape" editable="1"/>
    <field name="name" editable="1"/>
    <field name="networktype" editable="1"/>
    <field name="nodesubtype" editable="1"/>
    <field name="nodetype" editable="1"/>
    <field name="operational" editable="1"/>
    <field name="operationaldatecreationaccuracy" editable="1"/>
    <field name="operationalstate" editable="1"/>
    <field name="parameters" editable="1"/>
    <field name="parameterslist" editable="1"/>
    <field name="pk_descriptionsystem" editable="1"/>
    <field name="pk_node" editable="1"/>
    <field name="pk_object" editable="1"/>
    <field name="presencealarm" editable="1"/>
    <field name="presencecontroller" editable="1"/>
    <field name="presencehandle" editable="1"/>
    <field name="presencelid" editable="1"/>
    <field name="presencelowflowchannel" editable="1"/>
    <field name="presencesiphoidpartition" editable="1"/>
    <field name="presencesteps" editable="1"/>
    <field name="pscheckvalve" editable="1"/>
    <field name="pseleccabinet" editable="1"/>
    <field name="pseleccabinetlocked" editable="1"/>
    <field name="psfailurecontrollertype" editable="1"/>
    <field name="psfallprotectiongratings" editable="1"/>
    <field name="psfence" editable="1"/>
    <field name="psfloatnumber" editable="1"/>
    <field name="psgatevalve" editable="1"/>
    <field name="psguiderail" editable="1"/>
    <field name="psh2streatment" editable="1"/>
    <field name="psinletscreen" editable="1"/>
    <field name="pslocked" editable="1"/>
    <field name="psmaterial" editable="1"/>
    <field name="psnominalcapacity" editable="1"/>
    <field name="psoverflow" editable="1"/>
    <field name="pspressureport" editable="1"/>
    <field name="pspumpliftingchain" editable="1"/>
    <field name="pspumpnumber" editable="1"/>
    <field name="pspumpswitchingcontroller" editable="1"/>
    <field name="pspumpswitchingcontrollertype" editable="1"/>
    <field name="psremotemonitoring" editable="1"/>
    <field name="psremotemonitoringcomment" editable="1"/>
    <field name="psstormwaterinlet" editable="1"/>
    <field name="sedimenttrap" editable="1"/>
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
    <field name="width" editable="1"/>
    <field name="x" editable="1"/>
    <field name="y" editable="1"/>
    <field name="z" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="DSHroleouvrage" labelOnTop="0"/>
    <field name="accessibility" labelOnTop="0"/>
    <field name="altitude1" labelOnTop="0"/>
    <field name="city" labelOnTop="0"/>
    <field name="comment" labelOnTop="0"/>
    <field name="dateoperationalcreation" labelOnTop="0"/>
    <field name="dateoperationalcreationupper" labelOnTop="0"/>
    <field name="datetimecreation" labelOnTop="0"/>
    <field name="datetimedestruction" labelOnTop="0"/>
    <field name="datetimemodification" labelOnTop="0"/>
    <field name="datetimeoperationaldestruction" labelOnTop="0"/>
    <field name="depth1" labelOnTop="0"/>
    <field name="depthinvert" labelOnTop="0"/>
    <field name="domain" labelOnTop="0"/>
    <field name="dx" labelOnTop="0"/>
    <field name="dy" labelOnTop="0"/>
    <field name="dz" labelOnTop="0"/>
    <field name="elevationcover" labelOnTop="0"/>
    <field name="elevationinvert" labelOnTop="0"/>
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
    <field name="geotrackingdate" labelOnTop="0"/>
    <field name="geotrackingsource" labelOnTop="0"/>
    <field name="geotrackingxyquality" labelOnTop="0"/>
    <field name="geotrackingzquality" labelOnTop="0"/>
    <field name="id_descriptionsystem" labelOnTop="0"/>
    <field name="id_node" labelOnTop="0"/>
    <field name="id_object" labelOnTop="0"/>
    <field name="importid" labelOnTop="0"/>
    <field name="importtable" labelOnTop="0"/>
    <field name="lateralusercategory" labelOnTop="0"/>
    <field name="lenght" labelOnTop="0"/>
    <field name="lid_actor_1" labelOnTop="0"/>
    <field name="lid_actor_2" labelOnTop="0"/>
    <field name="lid_actor_3" labelOnTop="0"/>
    <field name="lid_actor_creator" labelOnTop="0"/>
    <field name="lid_descriptionsystem_1" labelOnTop="0"/>
    <field name="lid_facility" labelOnTop="0"/>
    <field name="lid_resource_1" labelOnTop="0"/>
    <field name="lid_resource_2" labelOnTop="0"/>
    <field name="lid_resource_3" labelOnTop="0"/>
    <field name="lid_resource_4" labelOnTop="0"/>
    <field name="lid_resource_5" labelOnTop="0"/>
    <field name="lid_resource_6" labelOnTop="0"/>
    <field name="location" labelOnTop="0"/>
    <field name="lpk_descriptionsystem" labelOnTop="0"/>
    <field name="lpk_object" labelOnTop="0"/>
    <field name="lpk_revision_begin" labelOnTop="0"/>
    <field name="lpk_revision_end" labelOnTop="0"/>
    <field name="manholecoverdiameter" labelOnTop="0"/>
    <field name="manholecovershape" labelOnTop="0"/>
    <field name="manholecovertype" labelOnTop="0"/>
    <field name="manholematerial" labelOnTop="0"/>
    <field name="manholeshape" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="networktype" labelOnTop="0"/>
    <field name="nodesubtype" labelOnTop="0"/>
    <field name="nodetype" labelOnTop="0"/>
    <field name="operational" labelOnTop="0"/>
    <field name="operationaldatecreationaccuracy" labelOnTop="0"/>
    <field name="operationalstate" labelOnTop="0"/>
    <field name="parameters" labelOnTop="0"/>
    <field name="parameterslist" labelOnTop="0"/>
    <field name="pk_descriptionsystem" labelOnTop="0"/>
    <field name="pk_node" labelOnTop="0"/>
    <field name="pk_object" labelOnTop="0"/>
    <field name="presencealarm" labelOnTop="0"/>
    <field name="presencecontroller" labelOnTop="0"/>
    <field name="presencehandle" labelOnTop="0"/>
    <field name="presencelid" labelOnTop="0"/>
    <field name="presencelowflowchannel" labelOnTop="0"/>
    <field name="presencesiphoidpartition" labelOnTop="0"/>
    <field name="presencesteps" labelOnTop="0"/>
    <field name="pscheckvalve" labelOnTop="0"/>
    <field name="pseleccabinet" labelOnTop="0"/>
    <field name="pseleccabinetlocked" labelOnTop="0"/>
    <field name="psfailurecontrollertype" labelOnTop="0"/>
    <field name="psfallprotectiongratings" labelOnTop="0"/>
    <field name="psfence" labelOnTop="0"/>
    <field name="psfloatnumber" labelOnTop="0"/>
    <field name="psgatevalve" labelOnTop="0"/>
    <field name="psguiderail" labelOnTop="0"/>
    <field name="psh2streatment" labelOnTop="0"/>
    <field name="psinletscreen" labelOnTop="0"/>
    <field name="pslocked" labelOnTop="0"/>
    <field name="psmaterial" labelOnTop="0"/>
    <field name="psnominalcapacity" labelOnTop="0"/>
    <field name="psoverflow" labelOnTop="0"/>
    <field name="pspressureport" labelOnTop="0"/>
    <field name="pspumpliftingchain" labelOnTop="0"/>
    <field name="pspumpnumber" labelOnTop="0"/>
    <field name="pspumpswitchingcontroller" labelOnTop="0"/>
    <field name="pspumpswitchingcontrollertype" labelOnTop="0"/>
    <field name="psremotemonitoring" labelOnTop="0"/>
    <field name="psremotemonitoringcomment" labelOnTop="0"/>
    <field name="psstormwaterinlet" labelOnTop="0"/>
    <field name="sedimenttrap" labelOnTop="0"/>
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
    <field name="width" labelOnTop="0"/>
    <field name="x" labelOnTop="0"/>
    <field name="y" labelOnTop="0"/>
    <field name="z" labelOnTop="0"/>
  </labelOnTop>
  <widgets>
    <widget name="ART_ID_ART">
      <config/>
    </widget>
  </widgets>
  <previewExpression>COALESCE("IDNUM", '&lt;NULL>')</previewExpression>
  <mapTip>IDNUM</mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
