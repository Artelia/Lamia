<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" simplifyDrawingTol="1" readOnly="0" styleCategories="AllStyleCategories" simplifyDrawingHints="0" version="3.10.6-A Coruña" minScale="1e+08" maxScale="0" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" simplifyAlgorithm="0" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="RuleRenderer" forceraster="0" symbollevels="0" enableorderby="0">
    <rules key="{8d79bb70-3d56-44a7-9b09-ed3642611a95}">
      <rule label="Regard" symbol="0" key="{1dbda66e-9a74-48f9-931e-359c3ca31688}" filter=" &quot;nodetype&quot;  = '60' ">
        <rule label="Eaux pluviales" symbol="1" key="{2f18122b-dd99-49f4-9f49-5c1ba68999f1}" filter="&quot;networktype&quot; = 'PLU' "/>
        <rule label="Eaux Usées" symbol="2" key="{33ab6e33-05b3-4826-a9fe-446f501c5585}" filter="&quot;networktype&quot; = 'USE' "/>
        <rule label="Unitaire" symbol="3" key="{bb702745-da57-47af-9f8a-e0b0ee7b54ff}" filter="&quot;networktype&quot; = 'UNI' "/>
        <rule label="Industriel" symbol="4" key="{ee98eb47-0dd6-4716-8f4f-8a966360e411}" filter="&quot;networktype&quot; = 'IND' "/>
      </rule>
      <rule label="Branchement" symbol="5" key="{da89f3f5-899c-4070-bbb0-0d08ed5e159b}" filter=" &quot;nodetype&quot;  = '61' ">
        <rule label="Eaux usées" symbol="6" key="{784d2d51-4a31-4b8d-be70-5cd59a64570e}" filter="&quot;networktype&quot; = 'USE' "/>
        <rule label="Unitaire" symbol="7" key="{ac6f9fb3-11f6-457b-a295-ded6e65ecbad}" filter="&quot;networktype&quot; = 'UNI' "/>
        <rule label="Pluviale" symbol="8" key="{9a43a2a7-1ee2-4e2d-be41-f7e57678b539}" filter="&quot;networktype&quot; = 'PLU' "/>
      </rule>
      <rule label="Grille" symbol="9" key="{3b51b7a1-92a7-4db2-bf4e-f59ad1cabed0}" filter=" &quot;nodetype&quot;  = '71' ">
        <rule label="Eaux pluviales" symbol="10" key="{164298cf-da20-4dfa-9a92-96370a7dfa40}" filter="&quot;networktype&quot; = 'PLU' "/>
        <rule label="Eaux Usées" symbol="11" key="{d16e050e-659a-46e2-b793-58c43235df41}" filter="&quot;networktype&quot; = 'USE' "/>
        <rule label="Unitaire" symbol="12" key="{25bb33ea-b695-4d4b-b588-975511f08ba4}" filter="&quot;networktype&quot; = 'UNI' "/>
        <rule label="Industriel" symbol="13" key="{226af3ae-83c3-484a-9459-d204a6afb940}" filter="&quot;networktype&quot; = 'IND' "/>
      </rule>
      <rule label="Avaloir" symbol="14" key="{25f9f3c2-695e-4992-ab82-9f7b79884c7c}" filter=" &quot;nodetype&quot;  = '70' "/>
      <rule label="Avaloir grille" symbol="15" key="{6bbcb618-908e-47cb-a66a-8da7b2a45872}" filter=" &quot;nodetype&quot;  = '72' "/>
      <rule label="Poste de refoulement" symbol="16" key="{16f48c4a-184f-494e-ae72-6bb1346cc7eb}" filter=" &quot;nodetype&quot;  = '10' ">
        <rule label="Eaux pluviales" symbol="17" key="{5493c27f-99aa-4ee7-a978-50f23a04394d}" filter="&quot;networktype&quot; = 'PLU' "/>
        <rule label="Eaux Usées" symbol="18" key="{82c85b46-3db9-4533-8379-52e478563566}" filter="&quot;networktype&quot; = 'USE' "/>
        <rule label="Unitaire" symbol="19" key="{b20cfa0c-e78c-47f2-b3ca-1390ad05cb7c}" filter="&quot;networktype&quot; = 'UNI' "/>
        <rule label="Industriel" symbol="20" key="{c3c17dd9-bdde-4564-838c-a47ef8eaff80}" filter="&quot;networktype&quot; = 'IND' "/>
      </rule>
      <rule label="DSH" symbol="21" key="{7bf88f42-c44e-495f-b6c2-54268a333549}" filter=" &quot;nodetype&quot;  = '21' ">
        <rule label="Eaux pluviales" symbol="22" key="{2aac6cc9-91da-461c-8ecd-b4c0081d3a61}" filter="&quot;networktype&quot; = 'PLU' "/>
        <rule label="Eaux Usées" symbol="23" key="{c34f6ae4-5562-4008-97a5-e494691ac84a}" filter="&quot;networktype&quot; = 'USE' "/>
        <rule label="Unitaire" symbol="24" key="{fa20e50a-81dc-40f0-a50c-8999f2d8da2a}" filter="&quot;networktype&quot; = 'UNI' "/>
        <rule label="Industriel" symbol="25" key="{ff69acb3-f534-4b83-9352-0d50ee4322a9}" filter="&quot;networktype&quot; = 'IND' "/>
      </rule>
      <rule label="Gouttière" symbol="26" key="{4e19d1fe-ded8-4220-b5b1-119481512103}" filter=" &quot;nodetype&quot;  = '74' ">
        <rule label="Eaux pluviales" symbol="27" key="{7abf00d5-013b-44d5-987f-42fb0978366f}" filter="&quot;networktype&quot; = 'PLU' "/>
        <rule label="Eaux Usées" symbol="28" key="{c100c3de-24c5-4e82-b7ba-750f4d740c54}" filter="&quot;networktype&quot; = 'USE' "/>
        <rule label="Unitaire" symbol="29" key="{dec7a18f-8e04-450a-b835-c1fc66088619}" filter="&quot;networktype&quot; = 'UNI' "/>
      </rule>
      <rule label="Ouvrage spécial" key="{db7fdf51-a1b2-4384-b3eb-c69746b04a12}" filter=" &quot;TYP_POINTS&quot; = 'Ouvrage spécial'">
        <rule label="Chasse d'eau" symbol="30" key="{11b0c499-186f-404a-a99a-07af955247d1}" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Chasse deau'"/>
        <rule label="Déssableur" symbol="31" key="{e15a51c6-7ab9-450c-a196-6b6b3465d8f3}" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Déssableur'"/>
        <rule label="Siphon" symbol="32" key="{9f9ee3e5-9b17-49a0-8a53-7a2adf6a0a8a}" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Siphon'"/>
        <rule label="Déversoir d'orage" symbol="33" key="{c7c51d7e-12d7-49aa-9992-16765f8f849f}" filter="&quot;TYP_POINTS&quot; = 'Ouvrage spécial' and  &quot;TYP_OUV_SP&quot; = 'Déversoir'"/>
        <rule label="Débitmètre" symbol="34" key="{a5dafd06-7aa5-4bc3-889b-10e697c6be3d}" filter=" &quot;TYP_POINTS&quot; ='Ouvrage speciale' and  &quot;TYP_OUV_SP&quot; ='Débitmètre'"/>
      </rule>
      <rule symbol="35" key="{82d65fa5-5e1e-479c-9535-ec144a68392f}" filter="Else"/>
    </rules>
    <symbols>
      <symbol type="marker" name="0" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.4" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="1" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.4" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="10" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="cross_fill" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
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
      <symbol type="marker" name="11" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="170,108,16,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="cross_fill" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
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
      <symbol type="marker" name="12" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="239,213,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="239,213,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="cross_fill" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="239,213,0,255" k="outline_color"/>
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
      <symbol type="marker" name="13" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="cross_fill" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,0,255" k="outline_color"/>
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
      <symbol type="marker" name="14" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
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
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="semi_circle" k="name"/>
          <prop v="0,1.30000000000000004" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.95" k="size"/>
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
      <symbol type="marker" name="15" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="semi_circle" k="name"/>
          <prop v="0,1.30000000000000004" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.9" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="cross_fill" k="name"/>
          <prop v="0,-0.39000000000000001" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.8" k="size"/>
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
      <symbol type="marker" name="16" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="17" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,255,255" k="outline_color"/>
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
      <symbol type="marker" name="18" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
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
      <symbol type="marker" name="19" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="239,213,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="239,213,0,255" k="outline_color"/>
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
      <symbol type="marker" name="2" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.4" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="20" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,0,255" k="outline_color"/>
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
      <symbol type="marker" name="21" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="132,132,132,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="pentagon" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="area" k="scale_method"/>
          <prop v="3" k="size"/>
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
      <symbol type="marker" name="22" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="pentagon" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="area" k="scale_method"/>
          <prop v="3" k="size"/>
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
      <symbol type="marker" name="23" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="170,108,16,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="170,108,16,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="triangle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="170,108,16,255" k="outline_color"/>
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
      <symbol type="marker" name="24" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="239,213,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="pentagon" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="area" k="scale_method"/>
          <prop v="3" k="size"/>
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
      <symbol type="marker" name="25" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="pentagon" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="area" k="scale_method"/>
          <prop v="3" k="size"/>
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
      <symbol type="marker" name="26" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="27" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="28" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="170,108,16,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="29" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="239,213,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="3" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="239,213,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.4" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="239,213,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="30" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="9,2,2,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="3" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.5" k="size"/>
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
      <symbol type="marker" name="31" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="half_square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.5" k="size"/>
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
      <symbol type="marker" name="32" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="182,182,183,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="3" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.5" k="size"/>
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
      <symbol type="marker" name="33" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="45" k="angle"/>
          <prop v="9,2,2,255" k="color"/>
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
          <prop v="4" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="225" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="filled_arrowhead" k="name"/>
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
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="fillColor">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="case &#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux pluviales' then  color_rgba( 0, 45, 207, 255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Unitaire' then  color_rgba( 0,250 ,0 ,255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux usées' then  color_rgba( 250, 0, 0, 255)&#xd;&#xa;&#x9;end"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="45" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="filled_arrowhead" k="name"/>
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
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="fillColor">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="case &#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux pluviales' then  color_rgba( 0, 45, 207, 255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Unitaire' then  color_rgba( 0,250 ,0 ,255)&#xd;&#xa;&#x9;when  &quot;TYP_RESEAU&quot; = 'Eaux usées' then  color_rgba( 250, 0, 0, 255)&#xd;&#xa;&#x9;end"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="34" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="FontMarker">
          <prop v="220" k="angle"/>
          <prop v="" k="chr"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="Dingbats" k="font"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="miter" k="joinstyle"/>
          <prop v="0,3" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,255,255,255" k="outline_color"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="220" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="line" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="60" k="angle"/>
          <prop v="255,0,0,0" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="35" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="112,112,112,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="diamond" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="area" k="scale_method"/>
          <prop v="3" k="size"/>
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
      <symbol type="marker" name="4" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="square" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2.4" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.4" k="outline_width"/>
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
      <symbol type="marker" name="5" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="9,2,2,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.2" k="size"/>
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
      <symbol type="marker" name="6" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.2" k="size"/>
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
      <symbol type="marker" name="7" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="51,160,44,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.2" k="size"/>
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
      <symbol type="marker" name="8" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
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
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="0,0,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="9,2,2,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="1.2" k="size"/>
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
      <symbol type="marker" name="9" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
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
          <prop v="2.6" k="size"/>
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
        <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
          <prop v="0" k="angle"/>
          <prop v="14,14,29,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="cross_fill" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="14,14,26,255" k="outline_color"/>
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
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style useSubstitutions="0" fontCapitals="0" blendMode="0" namedStyle="Normal" fontUnderline="0" textOpacity="1" isExpression="0" fontWordSpacing="0" fontKerning="1" fontLetterSpacing="0" multilineHeight="1" fieldName="name" fontSizeMapUnitScale="3x:0,0,0,0,0,0" previewBkgrdColor="255,255,255,255" textOrientation="horizontal" fontSize="8.25" fontSizeUnit="Point" fontFamily="MS Shell Dlg 2" fontStrikeout="0" fontItalic="0" fontWeight="50" textColor="0,0,0,255">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferJoinStyle="128" bufferNoFill="0" bufferColor="255,255,255,255"/>
        <background shapeOffsetY="0" shapeOpacity="1" shapeDraw="0" shapeBorderWidthUnit="MM" shapeBlendMode="0" shapeSVGFile="" shapeType="0" shapeOffsetX="0" shapeSizeX="0" shapeSizeUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeSizeY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeSizeType="0" shapeJoinStyle="64" shapeRotation="0" shapeRadiiX="0" shapeRadiiUnit="MM" shapeOffsetUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0">
          <symbol type="marker" name="markerSymbol" force_rhr="0" clip_to_extent="1" alpha="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="190,207,80,255" k="color"/>
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
        <shadow shadowOffsetGlobal="1" shadowDraw="0" shadowBlendMode="6" shadowOffsetUnit="MM" shadowOffsetAngle="135" shadowRadius="1.5" shadowScale="100" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowOffsetDist="1" shadowUnder="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowRadiusAlphaOnly="0"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format placeDirectionSymbol="0" decimals="3" plussign="0" wrapChar="" multilineAlign="3" addDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" autoWrapLength="0" formatNumbers="0" rightDirectionSymbol=">"/>
      <placement overrunDistanceUnit="MM" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" offsetUnits="MapUnit" maxCurvedCharAngleIn="25" yOffset="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" geometryGenerator="" placement="0" preserveRotation="1" fitInPolygonOnly="0" rotationAngle="0" placementFlags="10" repeatDistanceUnits="MM" quadOffset="4" centroidWhole="0" distUnits="MM" xOffset="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" dist="0" geometryGeneratorEnabled="0" layerType="PointGeometry" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" distMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-25" overrunDistance="0" repeatDistance="0" centroidInside="0" priority="5" offsetType="0"/>
      <rendering displayAll="0" upsidedownLabels="0" drawLabels="1" scaleMin="1" fontMaxPixelSize="10000" obstacle="1" scaleMax="10000000" scaleVisibility="0" fontLimitPixelSize="0" mergeLines="0" obstacleFactor="1" minFeatureSize="0" labelPerPart="0" limitNumLabels="0" obstacleType="0" maxNumLabels="2000" fontMinPixelSize="3" zIndex="0"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" name="name" value=""/>
          <Option type="Map" name="properties">
            <Option type="Map" name="Color">
              <Option type="bool" name="active" value="false"/>
              <Option type="QString" name="expression" value="@symbol_color"/>
              <Option type="int" name="type" value="3"/>
            </Option>
          </Option>
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
          <Option type="QString" name="lineSymbol" value="&lt;symbol type=&quot;line&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
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
    <property key="dualview/previewExpressions" value="COALESCE(&quot;IDNUM&quot;, '&lt;NULL>')"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory backgroundAlpha="255" scaleBasedVisibility="0" penWidth="0" penAlpha="255" minScaleDenominator="0" penColor="#000000" backgroundColor="#ffffff" enabled="0" width="15" rotationOffset="270" lineSizeScale="3x:0,0,0,0,0,0" sizeType="MM" sizeScale="3x:0,0,0,0,0,0" maxScaleDenominator="1e+08" height="15" barWidth="5" minimumSize="0" labelPlacementMethod="XHeight" diagramOrientation="Up" lineSizeType="MM" scaleDependency="Area" opacity="1">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" showAll="1" placement="0" linePlacementFlags="2" priority="0" zIndex="0" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Regard" value="60"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Branchement" value="61"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Regard mixte EP EU" value="62"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Avaloir" value="70"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Grille" value="71"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Grille avaloir" value="72"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tete de buse" value="73"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Gouttière" value="74"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Poste de refoulement" value="10"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Station d epuration" value="20"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Débourbeur/déshuileur" value="21"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Dessableur" value="22"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Depierreur" value="23"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Fosse septique" value="24"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Bassin de stockage" value="30"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puit" value="31"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Cuve" value="32"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Deversoir d orage" value="40"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Régulateur de débit" value="41"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Rejet" value="50"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puisard" value="51"/>
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
    <field name="nodesubtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Carré" value="6001"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Rond" value="6002"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Passage direct" value="6101"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Passage siphoïde" value="6102"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Trop-plein de poste" value="4001"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Déversoir d'orage" value="4002"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Délestage" value="4003"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Ouvrage de reprise de temps sec" value="4004"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Aspiration" value="1001"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Refoulement" value="1002"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Relèvement" value="1003"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Simple" value="7001"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="A grille" value="7002"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Tampon" value="7003"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Autre" value="00"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Indetermine" value="99"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Cuve infiltrante" value="3201"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Cuve stockante" value="3202"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puits comblé stockant" value="3101"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puits composé stockant" value="3102"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puits préfabriqué stockant" value="3103"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puits préfabriqué à double vidange" value="3104"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puits comblé à double vidange" value="3105"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Puits composé à double vidange" value="3106"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Ouvrable" value="OUV"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Ouvrable non visitable" value="OUN"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="En privé" value="PRI"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Non ouvrable" value="NOU"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Non vu" value="NVU"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Recouvert" value="REC"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Route carrossable" value="RCA"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Herbe/TN" value="HER"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Trottoir" value="TRO"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Parking" value="PAR"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Bâtiment" value="BAT"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Chemin piéton" value="CHE"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Voie ferrées" value="VFE"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Voirie" value="VOI"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Accotement" value="COT"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Carre" value="CAR"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Circulaire" value="CIR"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Béton préfabriqué" value="01"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="PE" value="02"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Chemisage" value="03"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Autre" value="00"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Inconnu" value="99"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Carre" value="CAR"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Circulaire" value="CIR"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="presencehandle">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="presencelowflowchannel">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="presencesiphoidpartition">
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
    <field name="presencelid">
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
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="psstormwaterinlet">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="pslocked">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="psh2streatment">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="pseleccabinet">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="pseleccabinetlocked">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="psremotemonitoring">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="pspumpswitchingcontrollertype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sonde de niveau" value="SNV"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sonde Piezo" value="PIE"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sonde ultrason" value="SOS"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Autre" value="AUT"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Non" value="NON"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sonde de niveau" value="SNV"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sonde Piezo" value="PIE"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Sonde ultrason" value="SOS"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Autre" value="AUT"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Béton" value="BET"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Béton revêtu" value="BER"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="Polyester" value="POL"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="psoverflow">
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
    <field name="psinletscreen">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="pspumpliftingchain">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="pscheckvalve">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="psgatevalve">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="pspressureport">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
                <Option type="QString" name="/" value=""/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="dommestique" value="DOM"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="industriel" value="IND"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="collectif" value="COL"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="agricole" value="AGR"/>
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
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="presencecontroller">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <field name="sedimenttrap">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="/" value=""/>
              </Option>
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
    <alias name="" field="pk_node" index="0"/>
    <alias name="" field="id_node" index="1"/>
    <alias name="" field="lpk_descriptionsystem" index="2"/>
    <alias name="" field="lid_descriptionsystem_1" index="3"/>
    <alias name="" field="elevationinvert" index="4"/>
    <alias name="" field="elevationcover" index="5"/>
    <alias name="" field="depthinvert" index="6"/>
    <alias name="" field="altitude1" index="7"/>
    <alias name="" field="depth1" index="8"/>
    <alias name="" field="nodetype" index="9"/>
    <alias name="" field="nodesubtype" index="10"/>
    <alias name="" field="accessibility" index="11"/>
    <alias name="" field="domain" index="12"/>
    <alias name="" field="location" index="13"/>
    <alias name="" field="width" index="14"/>
    <alias name="" field="lenght" index="15"/>
    <alias name="" field="lid_resource_1" index="16"/>
    <alias name="" field="lid_resource_2" index="17"/>
    <alias name="" field="lid_resource_3" index="18"/>
    <alias name="" field="lid_resource_4" index="19"/>
    <alias name="" field="lid_resource_5" index="20"/>
    <alias name="" field="lid_resource_6" index="21"/>
    <alias name="" field="manholecovershape" index="22"/>
    <alias name="" field="manholecovertype" index="23"/>
    <alias name="" field="manholecoverdiameter" index="24"/>
    <alias name="" field="manholematerial" index="25"/>
    <alias name="" field="manholeshape" index="26"/>
    <alias name="" field="presencesteps" index="27"/>
    <alias name="" field="presencehandle" index="28"/>
    <alias name="" field="presencelowflowchannel" index="29"/>
    <alias name="" field="presencesiphoidpartition" index="30"/>
    <alias name="" field="presencelid" index="31"/>
    <alias name="" field="psnominalcapacity" index="32"/>
    <alias name="" field="psfence" index="33"/>
    <alias name="" field="psstormwaterinlet" index="34"/>
    <alias name="" field="pslocked" index="35"/>
    <alias name="" field="psh2streatment" index="36"/>
    <alias name="" field="pseleccabinet" index="37"/>
    <alias name="" field="pseleccabinetlocked" index="38"/>
    <alias name="" field="psremotemonitoring" index="39"/>
    <alias name="" field="psremotemonitoringcomment" index="40"/>
    <alias name="" field="pspumpswitchingcontroller" index="41"/>
    <alias name="" field="pspumpswitchingcontrollertype" index="42"/>
    <alias name="" field="psfloatnumber" index="43"/>
    <alias name="" field="psfailurecontrollertype" index="44"/>
    <alias name="" field="psmaterial" index="45"/>
    <alias name="" field="psfallprotectiongratings" index="46"/>
    <alias name="" field="psoverflow" index="47"/>
    <alias name="" field="psinletscreen" index="48"/>
    <alias name="" field="pspumpnumber" index="49"/>
    <alias name="" field="psguiderail" index="50"/>
    <alias name="" field="pspumpliftingchain" index="51"/>
    <alias name="" field="pscheckvalve" index="52"/>
    <alias name="" field="psgatevalve" index="53"/>
    <alias name="" field="pspressureport" index="54"/>
    <alias name="" field="DSHroleouvrage" index="55"/>
    <alias name="" field="lateralusercategory" index="56"/>
    <alias name="" field="presencealarm" index="57"/>
    <alias name="" field="presencecontroller" index="58"/>
    <alias name="" field="sedimenttrap" index="59"/>
    <alias name="" field="x" index="60"/>
    <alias name="" field="dx" index="61"/>
    <alias name="" field="y" index="62"/>
    <alias name="" field="dy" index="63"/>
    <alias name="" field="z" index="64"/>
    <alias name="" field="dz" index="65"/>
    <alias name="" field="pk_descriptionsystem" index="66"/>
    <alias name="" field="id_descriptionsystem" index="67"/>
    <alias name="" field="lpk_object" index="68"/>
    <alias name="" field="strategicvalue" index="69"/>
    <alias name="" field="operational" index="70"/>
    <alias name="" field="structuralstate" index="71"/>
    <alias name="" field="operationalstate" index="72"/>
    <alias name="" field="dateoperationalcreation" index="73"/>
    <alias name="" field="dateoperationalcreationupper" index="74"/>
    <alias name="" field="operationaldatecreationaccuracy" index="75"/>
    <alias name="" field="datetimeoperationaldestruction" index="76"/>
    <alias name="" field="geotrackingxyquality" index="77"/>
    <alias name="" field="geotrackingzquality" index="78"/>
    <alias name="" field="geotrackingdate" index="79"/>
    <alias name="" field="geotrackingsource" index="80"/>
    <alias name="" field="parameters" index="81"/>
    <alias name="" field="parameterslist" index="82"/>
    <alias name="" field="city" index="83"/>
    <alias name="" field="streetname" index="84"/>
    <alias name="" field="streetupname" index="85"/>
    <alias name="" field="streetdownname" index="86"/>
    <alias name="" field="streetcomment" index="87"/>
    <alias name="" field="lid_actor_1" index="88"/>
    <alias name="" field="lid_actor_2" index="89"/>
    <alias name="" field="lid_actor_3" index="90"/>
    <alias name="" field="lid_facility" index="91"/>
    <alias name="" field="float_1" index="92"/>
    <alias name="" field="float_2" index="93"/>
    <alias name="" field="float_3" index="94"/>
    <alias name="" field="float_4" index="95"/>
    <alias name="" field="float_5" index="96"/>
    <alias name="" field="float_6" index="97"/>
    <alias name="" field="float_7" index="98"/>
    <alias name="" field="float_8" index="99"/>
    <alias name="" field="float_9" index="100"/>
    <alias name="" field="float_10" index="101"/>
    <alias name="" field="string_1" index="102"/>
    <alias name="" field="string_2" index="103"/>
    <alias name="" field="string_3" index="104"/>
    <alias name="" field="string_4" index="105"/>
    <alias name="" field="string_5" index="106"/>
    <alias name="" field="string_6" index="107"/>
    <alias name="" field="string_7" index="108"/>
    <alias name="" field="string_8" index="109"/>
    <alias name="" field="string_9" index="110"/>
    <alias name="" field="string_10" index="111"/>
    <alias name="" field="networktype" index="112"/>
    <alias name="" field="flowconditionupstream" index="113"/>
    <alias name="" field="flowconditiondownstream" index="114"/>
    <alias name="" field="systemfunction" index="115"/>
    <alias name="" field="pk_object" index="116"/>
    <alias name="" field="id_object" index="117"/>
    <alias name="" field="lpk_revision_begin" index="118"/>
    <alias name="" field="lpk_revision_end" index="119"/>
    <alias name="" field="datetimecreation" index="120"/>
    <alias name="" field="datetimemodification" index="121"/>
    <alias name="" field="datetimedestruction" index="122"/>
    <alias name="" field="comment" index="123"/>
    <alias name="" field="name" index="124"/>
    <alias name="" field="importid" index="125"/>
    <alias name="" field="importtable" index="126"/>
    <alias name="" field="lid_actor_creator" index="127"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="pk_node" applyOnUpdate="0"/>
    <default expression="" field="id_node" applyOnUpdate="0"/>
    <default expression="" field="lpk_descriptionsystem" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_1" applyOnUpdate="0"/>
    <default expression="" field="elevationinvert" applyOnUpdate="0"/>
    <default expression="" field="elevationcover" applyOnUpdate="0"/>
    <default expression="" field="depthinvert" applyOnUpdate="0"/>
    <default expression="" field="altitude1" applyOnUpdate="0"/>
    <default expression="" field="depth1" applyOnUpdate="0"/>
    <default expression="" field="nodetype" applyOnUpdate="0"/>
    <default expression="" field="nodesubtype" applyOnUpdate="0"/>
    <default expression="" field="accessibility" applyOnUpdate="0"/>
    <default expression="" field="domain" applyOnUpdate="0"/>
    <default expression="" field="location" applyOnUpdate="0"/>
    <default expression="" field="width" applyOnUpdate="0"/>
    <default expression="" field="lenght" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_1" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_2" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_3" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_4" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_5" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_6" applyOnUpdate="0"/>
    <default expression="" field="manholecovershape" applyOnUpdate="0"/>
    <default expression="" field="manholecovertype" applyOnUpdate="0"/>
    <default expression="" field="manholecoverdiameter" applyOnUpdate="0"/>
    <default expression="" field="manholematerial" applyOnUpdate="0"/>
    <default expression="" field="manholeshape" applyOnUpdate="0"/>
    <default expression="" field="presencesteps" applyOnUpdate="0"/>
    <default expression="" field="presencehandle" applyOnUpdate="0"/>
    <default expression="" field="presencelowflowchannel" applyOnUpdate="0"/>
    <default expression="" field="presencesiphoidpartition" applyOnUpdate="0"/>
    <default expression="" field="presencelid" applyOnUpdate="0"/>
    <default expression="" field="psnominalcapacity" applyOnUpdate="0"/>
    <default expression="" field="psfence" applyOnUpdate="0"/>
    <default expression="" field="psstormwaterinlet" applyOnUpdate="0"/>
    <default expression="" field="pslocked" applyOnUpdate="0"/>
    <default expression="" field="psh2streatment" applyOnUpdate="0"/>
    <default expression="" field="pseleccabinet" applyOnUpdate="0"/>
    <default expression="" field="pseleccabinetlocked" applyOnUpdate="0"/>
    <default expression="" field="psremotemonitoring" applyOnUpdate="0"/>
    <default expression="" field="psremotemonitoringcomment" applyOnUpdate="0"/>
    <default expression="" field="pspumpswitchingcontroller" applyOnUpdate="0"/>
    <default expression="" field="pspumpswitchingcontrollertype" applyOnUpdate="0"/>
    <default expression="" field="psfloatnumber" applyOnUpdate="0"/>
    <default expression="" field="psfailurecontrollertype" applyOnUpdate="0"/>
    <default expression="" field="psmaterial" applyOnUpdate="0"/>
    <default expression="" field="psfallprotectiongratings" applyOnUpdate="0"/>
    <default expression="" field="psoverflow" applyOnUpdate="0"/>
    <default expression="" field="psinletscreen" applyOnUpdate="0"/>
    <default expression="" field="pspumpnumber" applyOnUpdate="0"/>
    <default expression="" field="psguiderail" applyOnUpdate="0"/>
    <default expression="" field="pspumpliftingchain" applyOnUpdate="0"/>
    <default expression="" field="pscheckvalve" applyOnUpdate="0"/>
    <default expression="" field="psgatevalve" applyOnUpdate="0"/>
    <default expression="" field="pspressureport" applyOnUpdate="0"/>
    <default expression="" field="DSHroleouvrage" applyOnUpdate="0"/>
    <default expression="" field="lateralusercategory" applyOnUpdate="0"/>
    <default expression="" field="presencealarm" applyOnUpdate="0"/>
    <default expression="" field="presencecontroller" applyOnUpdate="0"/>
    <default expression="" field="sedimenttrap" applyOnUpdate="0"/>
    <default expression="" field="x" applyOnUpdate="0"/>
    <default expression="" field="dx" applyOnUpdate="0"/>
    <default expression="" field="y" applyOnUpdate="0"/>
    <default expression="" field="dy" applyOnUpdate="0"/>
    <default expression="" field="z" applyOnUpdate="0"/>
    <default expression="" field="dz" applyOnUpdate="0"/>
    <default expression="" field="pk_descriptionsystem" applyOnUpdate="0"/>
    <default expression="" field="id_descriptionsystem" applyOnUpdate="0"/>
    <default expression="" field="lpk_object" applyOnUpdate="0"/>
    <default expression="" field="strategicvalue" applyOnUpdate="0"/>
    <default expression="" field="operational" applyOnUpdate="0"/>
    <default expression="" field="structuralstate" applyOnUpdate="0"/>
    <default expression="" field="operationalstate" applyOnUpdate="0"/>
    <default expression="" field="dateoperationalcreation" applyOnUpdate="0"/>
    <default expression="" field="dateoperationalcreationupper" applyOnUpdate="0"/>
    <default expression="" field="operationaldatecreationaccuracy" applyOnUpdate="0"/>
    <default expression="" field="datetimeoperationaldestruction" applyOnUpdate="0"/>
    <default expression="" field="geotrackingxyquality" applyOnUpdate="0"/>
    <default expression="" field="geotrackingzquality" applyOnUpdate="0"/>
    <default expression="" field="geotrackingdate" applyOnUpdate="0"/>
    <default expression="" field="geotrackingsource" applyOnUpdate="0"/>
    <default expression="" field="parameters" applyOnUpdate="0"/>
    <default expression="" field="parameterslist" applyOnUpdate="0"/>
    <default expression="" field="city" applyOnUpdate="0"/>
    <default expression="" field="streetname" applyOnUpdate="0"/>
    <default expression="" field="streetupname" applyOnUpdate="0"/>
    <default expression="" field="streetdownname" applyOnUpdate="0"/>
    <default expression="" field="streetcomment" applyOnUpdate="0"/>
    <default expression="" field="lid_actor_1" applyOnUpdate="0"/>
    <default expression="" field="lid_actor_2" applyOnUpdate="0"/>
    <default expression="" field="lid_actor_3" applyOnUpdate="0"/>
    <default expression="" field="lid_facility" applyOnUpdate="0"/>
    <default expression="" field="float_1" applyOnUpdate="0"/>
    <default expression="" field="float_2" applyOnUpdate="0"/>
    <default expression="" field="float_3" applyOnUpdate="0"/>
    <default expression="" field="float_4" applyOnUpdate="0"/>
    <default expression="" field="float_5" applyOnUpdate="0"/>
    <default expression="" field="float_6" applyOnUpdate="0"/>
    <default expression="" field="float_7" applyOnUpdate="0"/>
    <default expression="" field="float_8" applyOnUpdate="0"/>
    <default expression="" field="float_9" applyOnUpdate="0"/>
    <default expression="" field="float_10" applyOnUpdate="0"/>
    <default expression="" field="string_1" applyOnUpdate="0"/>
    <default expression="" field="string_2" applyOnUpdate="0"/>
    <default expression="" field="string_3" applyOnUpdate="0"/>
    <default expression="" field="string_4" applyOnUpdate="0"/>
    <default expression="" field="string_5" applyOnUpdate="0"/>
    <default expression="" field="string_6" applyOnUpdate="0"/>
    <default expression="" field="string_7" applyOnUpdate="0"/>
    <default expression="" field="string_8" applyOnUpdate="0"/>
    <default expression="" field="string_9" applyOnUpdate="0"/>
    <default expression="" field="string_10" applyOnUpdate="0"/>
    <default expression="" field="networktype" applyOnUpdate="0"/>
    <default expression="" field="flowconditionupstream" applyOnUpdate="0"/>
    <default expression="" field="flowconditiondownstream" applyOnUpdate="0"/>
    <default expression="" field="systemfunction" applyOnUpdate="0"/>
    <default expression="" field="pk_object" applyOnUpdate="0"/>
    <default expression="" field="id_object" applyOnUpdate="0"/>
    <default expression="" field="lpk_revision_begin" applyOnUpdate="0"/>
    <default expression="" field="lpk_revision_end" applyOnUpdate="0"/>
    <default expression="" field="datetimecreation" applyOnUpdate="0"/>
    <default expression="" field="datetimemodification" applyOnUpdate="0"/>
    <default expression="" field="datetimedestruction" applyOnUpdate="0"/>
    <default expression="" field="comment" applyOnUpdate="0"/>
    <default expression="" field="name" applyOnUpdate="0"/>
    <default expression="" field="importid" applyOnUpdate="0"/>
    <default expression="" field="importtable" applyOnUpdate="0"/>
    <default expression="" field="lid_actor_creator" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="pk_node" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="id_node" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lpk_descriptionsystem" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_descriptionsystem_1" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="elevationinvert" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="elevationcover" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="depthinvert" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="altitude1" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="depth1" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="nodetype" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="nodesubtype" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="accessibility" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="domain" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="location" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="width" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lenght" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_resource_1" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_resource_2" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_resource_3" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_resource_4" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_resource_5" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_resource_6" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="manholecovershape" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="manholecovertype" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="manholecoverdiameter" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="manholematerial" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="manholeshape" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="presencesteps" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="presencehandle" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="presencelowflowchannel" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="presencesiphoidpartition" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="presencelid" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psnominalcapacity" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psfence" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psstormwaterinlet" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pslocked" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psh2streatment" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pseleccabinet" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pseleccabinetlocked" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psremotemonitoring" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psremotemonitoringcomment" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pspumpswitchingcontroller" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pspumpswitchingcontrollertype" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psfloatnumber" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psfailurecontrollertype" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psmaterial" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psfallprotectiongratings" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psoverflow" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psinletscreen" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pspumpnumber" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psguiderail" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pspumpliftingchain" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pscheckvalve" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psgatevalve" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pspressureport" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="DSHroleouvrage" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lateralusercategory" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="presencealarm" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="presencecontroller" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="sedimenttrap" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="x" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="dx" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="y" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="dy" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="z" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="dz" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pk_descriptionsystem" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="id_descriptionsystem" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lpk_object" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="strategicvalue" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="operational" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="structuralstate" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="operationalstate" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="dateoperationalcreation" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="dateoperationalcreationupper" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="operationaldatecreationaccuracy" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="datetimeoperationaldestruction" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="geotrackingxyquality" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="geotrackingzquality" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="geotrackingdate" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="geotrackingsource" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="parameters" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="parameterslist" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="city" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="streetname" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="streetupname" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="streetdownname" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="streetcomment" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_actor_1" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_actor_2" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_actor_3" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_facility" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_1" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_2" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_3" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_4" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_5" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_6" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_7" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_8" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_9" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="float_10" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_1" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_2" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_3" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_4" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_5" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_6" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_7" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_8" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_9" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="string_10" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="networktype" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="flowconditionupstream" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="flowconditiondownstream" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="systemfunction" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="pk_object" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="id_object" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lpk_revision_begin" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lpk_revision_end" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="datetimecreation" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="datetimemodification" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="datetimedestruction" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="comment" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="name" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="importid" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="importtable" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="lid_actor_creator" notnull_strength="0" exp_strength="0" constraints="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="pk_node" exp=""/>
    <constraint desc="" field="id_node" exp=""/>
    <constraint desc="" field="lpk_descriptionsystem" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_1" exp=""/>
    <constraint desc="" field="elevationinvert" exp=""/>
    <constraint desc="" field="elevationcover" exp=""/>
    <constraint desc="" field="depthinvert" exp=""/>
    <constraint desc="" field="altitude1" exp=""/>
    <constraint desc="" field="depth1" exp=""/>
    <constraint desc="" field="nodetype" exp=""/>
    <constraint desc="" field="nodesubtype" exp=""/>
    <constraint desc="" field="accessibility" exp=""/>
    <constraint desc="" field="domain" exp=""/>
    <constraint desc="" field="location" exp=""/>
    <constraint desc="" field="width" exp=""/>
    <constraint desc="" field="lenght" exp=""/>
    <constraint desc="" field="lid_resource_1" exp=""/>
    <constraint desc="" field="lid_resource_2" exp=""/>
    <constraint desc="" field="lid_resource_3" exp=""/>
    <constraint desc="" field="lid_resource_4" exp=""/>
    <constraint desc="" field="lid_resource_5" exp=""/>
    <constraint desc="" field="lid_resource_6" exp=""/>
    <constraint desc="" field="manholecovershape" exp=""/>
    <constraint desc="" field="manholecovertype" exp=""/>
    <constraint desc="" field="manholecoverdiameter" exp=""/>
    <constraint desc="" field="manholematerial" exp=""/>
    <constraint desc="" field="manholeshape" exp=""/>
    <constraint desc="" field="presencesteps" exp=""/>
    <constraint desc="" field="presencehandle" exp=""/>
    <constraint desc="" field="presencelowflowchannel" exp=""/>
    <constraint desc="" field="presencesiphoidpartition" exp=""/>
    <constraint desc="" field="presencelid" exp=""/>
    <constraint desc="" field="psnominalcapacity" exp=""/>
    <constraint desc="" field="psfence" exp=""/>
    <constraint desc="" field="psstormwaterinlet" exp=""/>
    <constraint desc="" field="pslocked" exp=""/>
    <constraint desc="" field="psh2streatment" exp=""/>
    <constraint desc="" field="pseleccabinet" exp=""/>
    <constraint desc="" field="pseleccabinetlocked" exp=""/>
    <constraint desc="" field="psremotemonitoring" exp=""/>
    <constraint desc="" field="psremotemonitoringcomment" exp=""/>
    <constraint desc="" field="pspumpswitchingcontroller" exp=""/>
    <constraint desc="" field="pspumpswitchingcontrollertype" exp=""/>
    <constraint desc="" field="psfloatnumber" exp=""/>
    <constraint desc="" field="psfailurecontrollertype" exp=""/>
    <constraint desc="" field="psmaterial" exp=""/>
    <constraint desc="" field="psfallprotectiongratings" exp=""/>
    <constraint desc="" field="psoverflow" exp=""/>
    <constraint desc="" field="psinletscreen" exp=""/>
    <constraint desc="" field="pspumpnumber" exp=""/>
    <constraint desc="" field="psguiderail" exp=""/>
    <constraint desc="" field="pspumpliftingchain" exp=""/>
    <constraint desc="" field="pscheckvalve" exp=""/>
    <constraint desc="" field="psgatevalve" exp=""/>
    <constraint desc="" field="pspressureport" exp=""/>
    <constraint desc="" field="DSHroleouvrage" exp=""/>
    <constraint desc="" field="lateralusercategory" exp=""/>
    <constraint desc="" field="presencealarm" exp=""/>
    <constraint desc="" field="presencecontroller" exp=""/>
    <constraint desc="" field="sedimenttrap" exp=""/>
    <constraint desc="" field="x" exp=""/>
    <constraint desc="" field="dx" exp=""/>
    <constraint desc="" field="y" exp=""/>
    <constraint desc="" field="dy" exp=""/>
    <constraint desc="" field="z" exp=""/>
    <constraint desc="" field="dz" exp=""/>
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
    <constraint desc="" field="networktype" exp=""/>
    <constraint desc="" field="flowconditionupstream" exp=""/>
    <constraint desc="" field="flowconditiondownstream" exp=""/>
    <constraint desc="" field="systemfunction" exp=""/>
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
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="1" actionWidgetStyle="dropDown" sortExpression="&quot;typeOuvrageAss&quot;">
    <columns>
      <column type="actions" width="-1" hidden="1"/>
      <column type="field" name="id_descriptionsystem" width="-1" hidden="0"/>
      <column type="field" name="lpk_descriptionsystem" width="-1" hidden="0"/>
      <column type="field" name="DSHroleouvrage" width="-1" hidden="0"/>
      <column type="field" name="pk_descriptionsystem" width="-1" hidden="0"/>
      <column type="field" name="lpk_revision_begin" width="-1" hidden="0"/>
      <column type="field" name="lpk_revision_end" width="-1" hidden="0"/>
      <column type="field" name="datetimecreation" width="-1" hidden="0"/>
      <column type="field" name="datetimemodification" width="-1" hidden="0"/>
      <column type="field" name="datetimedestruction" width="-1" hidden="0"/>
      <column type="field" name="importid" width="-1" hidden="0"/>
      <column type="field" name="importtable" width="-1" hidden="0"/>
      <column type="field" name="pk_node" width="-1" hidden="0"/>
      <column type="field" name="id_node" width="-1" hidden="0"/>
      <column type="field" name="lid_descriptionsystem_1" width="-1" hidden="0"/>
      <column type="field" name="elevationinvert" width="-1" hidden="0"/>
      <column type="field" name="elevationcover" width="-1" hidden="0"/>
      <column type="field" name="depthinvert" width="-1" hidden="0"/>
      <column type="field" name="altitude1" width="-1" hidden="0"/>
      <column type="field" name="depth1" width="-1" hidden="0"/>
      <column type="field" name="nodetype" width="-1" hidden="0"/>
      <column type="field" name="nodesubtype" width="-1" hidden="0"/>
      <column type="field" name="accessibility" width="-1" hidden="0"/>
      <column type="field" name="domain" width="-1" hidden="0"/>
      <column type="field" name="location" width="-1" hidden="0"/>
      <column type="field" name="width" width="-1" hidden="0"/>
      <column type="field" name="lenght" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_1" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_2" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_3" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_4" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_5" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_6" width="-1" hidden="0"/>
      <column type="field" name="manholecovershape" width="-1" hidden="0"/>
      <column type="field" name="manholecovertype" width="-1" hidden="0"/>
      <column type="field" name="manholecoverdiameter" width="-1" hidden="0"/>
      <column type="field" name="manholematerial" width="-1" hidden="0"/>
      <column type="field" name="manholeshape" width="-1" hidden="0"/>
      <column type="field" name="presencesteps" width="-1" hidden="0"/>
      <column type="field" name="presencehandle" width="-1" hidden="0"/>
      <column type="field" name="presencelowflowchannel" width="-1" hidden="0"/>
      <column type="field" name="presencesiphoidpartition" width="-1" hidden="0"/>
      <column type="field" name="presencelid" width="-1" hidden="0"/>
      <column type="field" name="psnominalcapacity" width="-1" hidden="0"/>
      <column type="field" name="psfence" width="-1" hidden="0"/>
      <column type="field" name="psstormwaterinlet" width="-1" hidden="0"/>
      <column type="field" name="pslocked" width="-1" hidden="0"/>
      <column type="field" name="psh2streatment" width="-1" hidden="0"/>
      <column type="field" name="pseleccabinet" width="-1" hidden="0"/>
      <column type="field" name="pseleccabinetlocked" width="-1" hidden="0"/>
      <column type="field" name="psremotemonitoring" width="-1" hidden="0"/>
      <column type="field" name="psremotemonitoringcomment" width="-1" hidden="0"/>
      <column type="field" name="pspumpswitchingcontroller" width="-1" hidden="0"/>
      <column type="field" name="pspumpswitchingcontrollertype" width="-1" hidden="0"/>
      <column type="field" name="psfloatnumber" width="-1" hidden="0"/>
      <column type="field" name="psfailurecontrollertype" width="-1" hidden="0"/>
      <column type="field" name="psmaterial" width="-1" hidden="0"/>
      <column type="field" name="psfallprotectiongratings" width="-1" hidden="0"/>
      <column type="field" name="psoverflow" width="-1" hidden="0"/>
      <column type="field" name="psinletscreen" width="-1" hidden="0"/>
      <column type="field" name="pspumpnumber" width="-1" hidden="0"/>
      <column type="field" name="psguiderail" width="-1" hidden="0"/>
      <column type="field" name="pspumpliftingchain" width="-1" hidden="0"/>
      <column type="field" name="pscheckvalve" width="-1" hidden="0"/>
      <column type="field" name="psgatevalve" width="-1" hidden="0"/>
      <column type="field" name="pspressureport" width="-1" hidden="0"/>
      <column type="field" name="lateralusercategory" width="-1" hidden="0"/>
      <column type="field" name="presencealarm" width="-1" hidden="0"/>
      <column type="field" name="presencecontroller" width="-1" hidden="0"/>
      <column type="field" name="sedimenttrap" width="-1" hidden="0"/>
      <column type="field" name="x" width="-1" hidden="0"/>
      <column type="field" name="dx" width="-1" hidden="0"/>
      <column type="field" name="y" width="-1" hidden="0"/>
      <column type="field" name="dy" width="-1" hidden="0"/>
      <column type="field" name="z" width="-1" hidden="0"/>
      <column type="field" name="dz" width="-1" hidden="0"/>
      <column type="field" name="lpk_object" width="-1" hidden="0"/>
      <column type="field" name="strategicvalue" width="-1" hidden="0"/>
      <column type="field" name="operational" width="-1" hidden="0"/>
      <column type="field" name="structuralstate" width="-1" hidden="0"/>
      <column type="field" name="operationalstate" width="-1" hidden="0"/>
      <column type="field" name="dateoperationalcreation" width="-1" hidden="0"/>
      <column type="field" name="dateoperationalcreationupper" width="-1" hidden="0"/>
      <column type="field" name="operationaldatecreationaccuracy" width="-1" hidden="0"/>
      <column type="field" name="datetimeoperationaldestruction" width="-1" hidden="0"/>
      <column type="field" name="geotrackingxyquality" width="-1" hidden="0"/>
      <column type="field" name="geotrackingzquality" width="-1" hidden="0"/>
      <column type="field" name="geotrackingdate" width="-1" hidden="0"/>
      <column type="field" name="geotrackingsource" width="-1" hidden="0"/>
      <column type="field" name="parameters" width="-1" hidden="0"/>
      <column type="field" name="parameterslist" width="-1" hidden="0"/>
      <column type="field" name="city" width="-1" hidden="0"/>
      <column type="field" name="streetname" width="-1" hidden="0"/>
      <column type="field" name="streetupname" width="-1" hidden="0"/>
      <column type="field" name="streetdownname" width="-1" hidden="0"/>
      <column type="field" name="streetcomment" width="-1" hidden="0"/>
      <column type="field" name="lid_actor_1" width="-1" hidden="0"/>
      <column type="field" name="lid_actor_2" width="-1" hidden="0"/>
      <column type="field" name="lid_actor_3" width="-1" hidden="0"/>
      <column type="field" name="lid_facility" width="-1" hidden="0"/>
      <column type="field" name="float_1" width="-1" hidden="0"/>
      <column type="field" name="float_2" width="-1" hidden="0"/>
      <column type="field" name="float_3" width="-1" hidden="0"/>
      <column type="field" name="float_4" width="-1" hidden="0"/>
      <column type="field" name="float_5" width="-1" hidden="0"/>
      <column type="field" name="float_6" width="-1" hidden="0"/>
      <column type="field" name="float_7" width="-1" hidden="0"/>
      <column type="field" name="float_8" width="-1" hidden="0"/>
      <column type="field" name="float_9" width="-1" hidden="0"/>
      <column type="field" name="float_10" width="-1" hidden="0"/>
      <column type="field" name="string_1" width="-1" hidden="0"/>
      <column type="field" name="string_2" width="-1" hidden="0"/>
      <column type="field" name="string_3" width="-1" hidden="0"/>
      <column type="field" name="string_4" width="-1" hidden="0"/>
      <column type="field" name="string_5" width="-1" hidden="0"/>
      <column type="field" name="string_6" width="-1" hidden="0"/>
      <column type="field" name="string_7" width="-1" hidden="0"/>
      <column type="field" name="string_8" width="-1" hidden="0"/>
      <column type="field" name="string_9" width="-1" hidden="0"/>
      <column type="field" name="string_10" width="-1" hidden="0"/>
      <column type="field" name="networktype" width="-1" hidden="0"/>
      <column type="field" name="flowconditionupstream" width="-1" hidden="0"/>
      <column type="field" name="flowconditiondownstream" width="-1" hidden="0"/>
      <column type="field" name="systemfunction" width="-1" hidden="0"/>
      <column type="field" name="pk_object" width="-1" hidden="0"/>
      <column type="field" name="id_object" width="-1" hidden="0"/>
      <column type="field" name="comment" width="-1" hidden="0"/>
      <column type="field" name="name" width="-1" hidden="0"/>
      <column type="field" name="lid_actor_creator" width="-1" hidden="0"/>
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
    <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Général" visibilityExpression="" groupBox="0" columnCount="1">
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Type d'ouvrage" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="TYP_POINTS" index="-1"/>
        <attributeEditorField showLabel="1" name="TYP_RESEAU" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Identification de l'ouvrage" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ART_ID_ART" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Données générales" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="COMMUNE" index="-1"/>
        <attributeEditorField showLabel="1" name="INSEE" index="-1"/>
        <attributeEditorField showLabel="1" name="DATEMAJ" index="-1"/>
        <attributeEditorField showLabel="1" name="SYSTCOLLEC" index="-1"/>
        <attributeEditorField showLabel="1" name="SOURCEMAJ" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Topographie du point" visibilityExpression="" groupBox="1" columnCount="3">
        <attributeEditorField showLabel="1" name="Topo_X" index="-1"/>
        <attributeEditorField showLabel="1" name="Topo_Y" index="-1"/>
        <attributeEditorField showLabel="1" name="Topo_Z_TN" index="-1"/>
        <attributeEditorField showLabel="1" name="Topo_Xp" index="-1"/>
        <attributeEditorField showLabel="1" name="Topo_Yp" index="-1"/>
        <attributeEditorField showLabel="1" name="Topo_Zp" index="-1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Regard" visibilityExpression="" groupBox="0" columnCount="1">
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Photo" visibilityExpression="" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" name="ART_PHOTOS" index="-1"/>
        <attributeEditorField showLabel="1" name="ART_PHOTO2" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Arrivées" visibilityExpression="" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" name="ART_NB_ARR" index="-1"/>
        <attributeEditorField showLabel="1" name="ART_NB_BRT" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Profondeurs et chutes" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="0" name="Profondeurs" visibilityExpression="" groupBox="1" columnCount="2">
          <attributeEditorField showLabel="1" name="ART_PROF_A" index="-1"/>
          <attributeEditorField showLabel="1" name="PRO_FE_REU" index="-1"/>
        </attributeEditorContainer>
        <attributeEditorField showLabel="1" name="CHUTE_REU" index="-1"/>
        <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="0" name="Chutes" visibilityExpression="" groupBox="1" columnCount="3">
          <attributeEditorField showLabel="1" name="FE_CHUTE1" index="-1"/>
          <attributeEditorField showLabel="1" name="FE_CHUTE2" index="-1"/>
          <attributeEditorField showLabel="1" name="FE_CHUTE3" index="-1"/>
          <attributeEditorField showLabel="1" name="Heure1_REU" index="-1"/>
          <attributeEditorField showLabel="1" name="Heure2_REU" index="-1"/>
          <attributeEditorField showLabel="1" name="Heure3_REU" index="-1"/>
        </attributeEditorContainer>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Accessibilité" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ART_ACCESS" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Dépôts" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ART_DEPOTS" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Anomalies" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="NB_ANO_REU" index="-1"/>
        <attributeEditorField showLabel="1" name="ANOM_EU1" index="-1"/>
        <attributeEditorField showLabel="1" name="ANOM_EU2" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Travaux" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ART_TRAVAU" index="-1"/>
        <attributeEditorField showLabel="1" name="ART_PRIORI" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Observations" visibilityExpression="" groupBox="1" columnCount="3">
        <attributeEditorField showLabel="1" name="ES_REU" index="-1"/>
        <attributeEditorField showLabel="1" name="Tete_REU" index="-1"/>
        <attributeEditorField showLabel="1" name="Sec_REU" index="-1"/>
        <attributeEditorField showLabel="1" name="REGARD_PE" index="-1"/>
        <attributeEditorField showLabel="1" name="REGARD_NV" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="0" name="Remarques" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ART_OBSERV" index="-1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Branchement" visibilityExpression="" groupBox="0" columnCount="1">
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Profondeur" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="PROF_BRT" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Cotes" visibilityExpression="" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" name="COTE_TN" index="-1"/>
        <attributeEditorField showLabel="1" name="COTE_FE_BR" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Dépôts" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="DEPOTS_BRT" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Anomalies" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ANOM_BRT1" index="-1"/>
        <attributeEditorField showLabel="1" name="ANOM_BRT2" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Observations" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="CLOISO_BRT" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Accessibilité" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ACCES_BRT" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Remarques" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="OBSERV_BRT" index="-1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Ouvrages EP" visibilityExpression="" groupBox="0" columnCount="1">
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Ouvrage EP" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="TYP_OUV_EP" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Profondeur" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="PRO_OUV_EP" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Cotes" visibilityExpression="" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" name="COT_TN_OUV" index="-1"/>
        <attributeEditorField showLabel="1" name="COT_FE_OUV" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Dépôts" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="DEPOTS_OUV" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Anomalies" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ANOM_OUV1" index="-1"/>
        <attributeEditorField showLabel="1" name="ANOM_OUV2" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Accessbilité" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="ACCES_OUV" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Remarques" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="OBSERV_OUV" index="-1"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Ouvrage spécial" visibilityExpression="" groupBox="0" columnCount="1">
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Type d'ouvrage spécial" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="TYP_OUV_SP" index="-1"/>
      </attributeEditorContainer>
      <attributeEditorContainer visibilityExpressionEnabled="0" showLabel="1" name="Remarques" visibilityExpression="" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" name="OBS_OUVSP" index="-1"/>
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
