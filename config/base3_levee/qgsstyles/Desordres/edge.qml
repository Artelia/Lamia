<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingHints="1" simplifyAlgorithm="0" simplifyLocal="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" version="3.10.6-A Coruña" labelsEnabled="0" simplifyMaxScale="1" minScale="1e+08" simplifyDrawingTol="1" readOnly="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" enableorderby="0" forceraster="0" symbollevels="0">
    <symbols>
      <symbol type="line" clip_to_extent="1" alpha="1" force_rhr="0" name="0">
        <layer enabled="1" locked="0" class="SimpleLine" pass="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="0,0,0,255"/>
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
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory penColor="#000000" minScaleDenominator="0" labelPlacementMethod="XHeight" opacity="1" barWidth="5" backgroundColor="#ffffff" sizeType="MM" scaleBasedVisibility="0" lineSizeType="MM" maxScaleDenominator="1e+08" diagramOrientation="Up" minimumSize="0" backgroundAlpha="255" width="15" penAlpha="255" height="15" scaleDependency="Area" rotationOffset="270" enabled="0" lineSizeScale="3x:0,0,0,0,0,0" penWidth="0" sizeScale="3x:0,0,0,0,0,0">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" priority="0" showAll="1" placement="2" zIndex="0" linePlacementFlags="18" dist="0">
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
    <field name="edgetype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="DIG" name="Digue"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="TNA" name="Terrain naturel"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="REM" name="Remblai"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="CDU" name="Cordon dunaire"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="CRO" name="Cote Rocheuse"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="REB" name="Remblai routier"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="EPI" name="Epi"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="BLA" name="Brise-lame"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="BAT" name="Batardeau"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="DEV" name="Deversoir"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="NDE" name="Non defini"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="edgesubtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="TER" name="Terre"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="TEN" name="Terre - enrochement"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="PAL" name="Palplanche"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="GCI" name="Genie-civil"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="PMA" name="Perré maçonné"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="VOI" name="Voirie"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="GAL" name="Cordon de galet"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="AUT" name="Autre"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="regulatorycategory">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="A" name="A"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="B" name="B"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="C" name="C"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="NC" name="NC"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="setbackwidth">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="0" name="nulle"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="0-5m" name="0-5 m"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="5-10m" name="5-10 m"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value=">10m" name=">10 m"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="setbackvegetationherbaceous">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="0" name="absente"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="1" name="clairsemée"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="2" name="moyenne"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="3" name="dense"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="setbackvegetationshrub">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="0" name="absente"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="1" name="clairsemée"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="2" name="moyenne"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="3" name="dense"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="setbackvegetationtree">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="0" name="absente"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="1" name="clairsemée"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="2" name="moyenne"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="3" name="dense"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="setbackcomment">
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
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="1" name="Oui"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="0" name="Non"/>
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
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="A" name="A"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="B" name="B"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="C" name="C"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="NC" name="NC"/>
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
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="1" name="Classe A"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="2" name="Classe B"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="3" name="Classe C"/>
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
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="1" name="Classe A"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="2" name="Classe B"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="3" name="Classe C"/>
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
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" value="" name="/"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="0" name="Hors service"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="1" name="Mauvais"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="2" name="Moyen"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="3" name="Bon"/>
              </Option>
              <Option type="Map">
                <Option type="QString" value="4" name="Excellent"/>
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
    <alias name="" field="pk_edge" index="0"/>
    <alias name="" field="id_edge" index="1"/>
    <alias name="" field="lpk_descriptionsystem" index="2"/>
    <alias name="" field="lid_resource_1" index="3"/>
    <alias name="" field="lid_descriptionsystem_1" index="4"/>
    <alias name="" field="lid_descriptionsystem_2" index="5"/>
    <alias name="" field="edgetype" index="6"/>
    <alias name="" field="edgesubtype" index="7"/>
    <alias name="" field="regulatorycategory" index="8"/>
    <alias name="" field="setbackwidth" index="9"/>
    <alias name="" field="setbackvegetationherbaceous" index="10"/>
    <alias name="" field="setbackvegetationshrub" index="11"/>
    <alias name="" field="setbackvegetationtree" index="12"/>
    <alias name="" field="setbackcomment" index="13"/>
    <alias name="" field="lid_resource_2" index="14"/>
    <alias name="" field="lid_resource_3" index="15"/>
    <alias name="" field="lid_resource_4" index="16"/>
    <alias name="" field="pk_descriptionsystem" index="17"/>
    <alias name="" field="id_descriptionsystem" index="18"/>
    <alias name="" field="lpk_object" index="19"/>
    <alias name="" field="strategicvalue" index="20"/>
    <alias name="" field="operational" index="21"/>
    <alias name="" field="structuralstate" index="22"/>
    <alias name="" field="operationalstate" index="23"/>
    <alias name="" field="dateoperationalcreation" index="24"/>
    <alias name="" field="dateoperationalcreationupper" index="25"/>
    <alias name="" field="operationaldatecreationaccuracy" index="26"/>
    <alias name="" field="datetimeoperationaldestruction" index="27"/>
    <alias name="" field="geotrackingxyquality" index="28"/>
    <alias name="" field="geotrackingzquality" index="29"/>
    <alias name="" field="geotrackingdate" index="30"/>
    <alias name="" field="geotrackingsource" index="31"/>
    <alias name="" field="parameters" index="32"/>
    <alias name="" field="parameterslist" index="33"/>
    <alias name="" field="city" index="34"/>
    <alias name="" field="streetname" index="35"/>
    <alias name="" field="streetupname" index="36"/>
    <alias name="" field="streetdownname" index="37"/>
    <alias name="" field="streetcomment" index="38"/>
    <alias name="" field="lid_actor_1" index="39"/>
    <alias name="" field="lid_actor_2" index="40"/>
    <alias name="" field="lid_actor_3" index="41"/>
    <alias name="" field="lid_facility" index="42"/>
    <alias name="" field="float_1" index="43"/>
    <alias name="" field="float_2" index="44"/>
    <alias name="" field="float_3" index="45"/>
    <alias name="" field="float_4" index="46"/>
    <alias name="" field="float_5" index="47"/>
    <alias name="" field="float_6" index="48"/>
    <alias name="" field="float_7" index="49"/>
    <alias name="" field="float_8" index="50"/>
    <alias name="" field="float_9" index="51"/>
    <alias name="" field="float_10" index="52"/>
    <alias name="" field="string_1" index="53"/>
    <alias name="" field="string_2" index="54"/>
    <alias name="" field="string_3" index="55"/>
    <alias name="" field="string_4" index="56"/>
    <alias name="" field="string_5" index="57"/>
    <alias name="" field="string_6" index="58"/>
    <alias name="" field="string_7" index="59"/>
    <alias name="" field="string_8" index="60"/>
    <alias name="" field="string_9" index="61"/>
    <alias name="" field="string_10" index="62"/>
    <alias name="" field="fonctionnalcondition" index="63"/>
    <alias name="" field="pk_object" index="64"/>
    <alias name="" field="id_object" index="65"/>
    <alias name="" field="lpk_revision_begin" index="66"/>
    <alias name="" field="lpk_revision_end" index="67"/>
    <alias name="" field="datetimecreation" index="68"/>
    <alias name="" field="datetimemodification" index="69"/>
    <alias name="" field="datetimedestruction" index="70"/>
    <alias name="" field="comment" index="71"/>
    <alias name="" field="name" index="72"/>
    <alias name="" field="importid" index="73"/>
    <alias name="" field="importtable" index="74"/>
    <alias name="" field="lid_actor_creator" index="75"/>
    <alias name="" field="sirsid" index="76"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="pk_edge" applyOnUpdate="0"/>
    <default expression="" field="id_edge" applyOnUpdate="0"/>
    <default expression="" field="lpk_descriptionsystem" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_1" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_1" applyOnUpdate="0"/>
    <default expression="" field="lid_descriptionsystem_2" applyOnUpdate="0"/>
    <default expression="" field="edgetype" applyOnUpdate="0"/>
    <default expression="" field="edgesubtype" applyOnUpdate="0"/>
    <default expression="" field="regulatorycategory" applyOnUpdate="0"/>
    <default expression="" field="setbackwidth" applyOnUpdate="0"/>
    <default expression="" field="setbackvegetationherbaceous" applyOnUpdate="0"/>
    <default expression="" field="setbackvegetationshrub" applyOnUpdate="0"/>
    <default expression="" field="setbackvegetationtree" applyOnUpdate="0"/>
    <default expression="" field="setbackcomment" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_2" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_3" applyOnUpdate="0"/>
    <default expression="" field="lid_resource_4" applyOnUpdate="0"/>
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
    <default expression="" field="fonctionnalcondition" applyOnUpdate="0"/>
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
    <default expression="" field="sirsid" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="pk_edge"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="id_edge"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lpk_descriptionsystem"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_resource_1"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_descriptionsystem_1"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_descriptionsystem_2"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="edgetype"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="edgesubtype"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="regulatorycategory"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="setbackwidth"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="setbackvegetationherbaceous"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="setbackvegetationshrub"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="setbackvegetationtree"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="setbackcomment"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_resource_2"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_resource_3"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_resource_4"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="pk_descriptionsystem"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="id_descriptionsystem"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lpk_object"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="strategicvalue"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="operational"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="structuralstate"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="operationalstate"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="dateoperationalcreation"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="dateoperationalcreationupper"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="operationaldatecreationaccuracy"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="datetimeoperationaldestruction"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="geotrackingxyquality"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="geotrackingzquality"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="geotrackingdate"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="geotrackingsource"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="parameters"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="parameterslist"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="city"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="streetname"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="streetupname"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="streetdownname"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="streetcomment"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_actor_1"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_actor_2"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_actor_3"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_facility"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_1"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_2"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_3"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_4"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_5"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_6"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_7"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_8"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_9"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="float_10"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_1"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_2"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_3"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_4"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_5"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_6"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_7"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_8"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_9"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="string_10"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="fonctionnalcondition"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="pk_object"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="id_object"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lpk_revision_begin"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lpk_revision_end"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="datetimecreation"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="datetimemodification"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="datetimedestruction"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="comment"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="name"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="importid"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="importtable"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="lid_actor_creator"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0" field="sirsid"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="pk_edge"/>
    <constraint exp="" desc="" field="id_edge"/>
    <constraint exp="" desc="" field="lpk_descriptionsystem"/>
    <constraint exp="" desc="" field="lid_resource_1"/>
    <constraint exp="" desc="" field="lid_descriptionsystem_1"/>
    <constraint exp="" desc="" field="lid_descriptionsystem_2"/>
    <constraint exp="" desc="" field="edgetype"/>
    <constraint exp="" desc="" field="edgesubtype"/>
    <constraint exp="" desc="" field="regulatorycategory"/>
    <constraint exp="" desc="" field="setbackwidth"/>
    <constraint exp="" desc="" field="setbackvegetationherbaceous"/>
    <constraint exp="" desc="" field="setbackvegetationshrub"/>
    <constraint exp="" desc="" field="setbackvegetationtree"/>
    <constraint exp="" desc="" field="setbackcomment"/>
    <constraint exp="" desc="" field="lid_resource_2"/>
    <constraint exp="" desc="" field="lid_resource_3"/>
    <constraint exp="" desc="" field="lid_resource_4"/>
    <constraint exp="" desc="" field="pk_descriptionsystem"/>
    <constraint exp="" desc="" field="id_descriptionsystem"/>
    <constraint exp="" desc="" field="lpk_object"/>
    <constraint exp="" desc="" field="strategicvalue"/>
    <constraint exp="" desc="" field="operational"/>
    <constraint exp="" desc="" field="structuralstate"/>
    <constraint exp="" desc="" field="operationalstate"/>
    <constraint exp="" desc="" field="dateoperationalcreation"/>
    <constraint exp="" desc="" field="dateoperationalcreationupper"/>
    <constraint exp="" desc="" field="operationaldatecreationaccuracy"/>
    <constraint exp="" desc="" field="datetimeoperationaldestruction"/>
    <constraint exp="" desc="" field="geotrackingxyquality"/>
    <constraint exp="" desc="" field="geotrackingzquality"/>
    <constraint exp="" desc="" field="geotrackingdate"/>
    <constraint exp="" desc="" field="geotrackingsource"/>
    <constraint exp="" desc="" field="parameters"/>
    <constraint exp="" desc="" field="parameterslist"/>
    <constraint exp="" desc="" field="city"/>
    <constraint exp="" desc="" field="streetname"/>
    <constraint exp="" desc="" field="streetupname"/>
    <constraint exp="" desc="" field="streetdownname"/>
    <constraint exp="" desc="" field="streetcomment"/>
    <constraint exp="" desc="" field="lid_actor_1"/>
    <constraint exp="" desc="" field="lid_actor_2"/>
    <constraint exp="" desc="" field="lid_actor_3"/>
    <constraint exp="" desc="" field="lid_facility"/>
    <constraint exp="" desc="" field="float_1"/>
    <constraint exp="" desc="" field="float_2"/>
    <constraint exp="" desc="" field="float_3"/>
    <constraint exp="" desc="" field="float_4"/>
    <constraint exp="" desc="" field="float_5"/>
    <constraint exp="" desc="" field="float_6"/>
    <constraint exp="" desc="" field="float_7"/>
    <constraint exp="" desc="" field="float_8"/>
    <constraint exp="" desc="" field="float_9"/>
    <constraint exp="" desc="" field="float_10"/>
    <constraint exp="" desc="" field="string_1"/>
    <constraint exp="" desc="" field="string_2"/>
    <constraint exp="" desc="" field="string_3"/>
    <constraint exp="" desc="" field="string_4"/>
    <constraint exp="" desc="" field="string_5"/>
    <constraint exp="" desc="" field="string_6"/>
    <constraint exp="" desc="" field="string_7"/>
    <constraint exp="" desc="" field="string_8"/>
    <constraint exp="" desc="" field="string_9"/>
    <constraint exp="" desc="" field="string_10"/>
    <constraint exp="" desc="" field="fonctionnalcondition"/>
    <constraint exp="" desc="" field="pk_object"/>
    <constraint exp="" desc="" field="id_object"/>
    <constraint exp="" desc="" field="lpk_revision_begin"/>
    <constraint exp="" desc="" field="lpk_revision_end"/>
    <constraint exp="" desc="" field="datetimecreation"/>
    <constraint exp="" desc="" field="datetimemodification"/>
    <constraint exp="" desc="" field="datetimedestruction"/>
    <constraint exp="" desc="" field="comment"/>
    <constraint exp="" desc="" field="name"/>
    <constraint exp="" desc="" field="importid"/>
    <constraint exp="" desc="" field="importtable"/>
    <constraint exp="" desc="" field="lid_actor_creator"/>
    <constraint exp="" desc="" field="sirsid"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column type="actions" width="-1" hidden="1"/>
      <column type="field" name="id_descriptionsystem" width="-1" hidden="0"/>
      <column type="field" name="pk_edge" width="-1" hidden="0"/>
      <column type="field" name="id_edge" width="-1" hidden="0"/>
      <column type="field" name="lpk_descriptionsystem" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_1" width="-1" hidden="0"/>
      <column type="field" name="lid_descriptionsystem_1" width="-1" hidden="0"/>
      <column type="field" name="lid_descriptionsystem_2" width="-1" hidden="0"/>
      <column type="field" name="edgetype" width="-1" hidden="0"/>
      <column type="field" name="edgesubtype" width="-1" hidden="0"/>
      <column type="field" name="regulatorycategory" width="-1" hidden="0"/>
      <column type="field" name="setbackwidth" width="-1" hidden="0"/>
      <column type="field" name="setbackvegetationherbaceous" width="-1" hidden="0"/>
      <column type="field" name="setbackvegetationshrub" width="-1" hidden="0"/>
      <column type="field" name="setbackvegetationtree" width="-1" hidden="0"/>
      <column type="field" name="setbackcomment" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_2" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_3" width="-1" hidden="0"/>
      <column type="field" name="lid_resource_4" width="-1" hidden="0"/>
      <column type="field" name="pk_descriptionsystem" width="-1" hidden="0"/>
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
      <column type="field" name="fonctionnalcondition" width="-1" hidden="0"/>
      <column type="field" name="pk_object" width="-1" hidden="0"/>
      <column type="field" name="id_object" width="-1" hidden="0"/>
      <column type="field" name="lpk_revision_begin" width="-1" hidden="0"/>
      <column type="field" name="lpk_revision_end" width="-1" hidden="0"/>
      <column type="field" name="datetimecreation" width="-1" hidden="0"/>
      <column type="field" name="datetimemodification" width="-1" hidden="0"/>
      <column type="field" name="datetimedestruction" width="-1" hidden="0"/>
      <column type="field" name="comment" width="-1" hidden="0"/>
      <column type="field" name="name" width="-1" hidden="0"/>
      <column type="field" name="importid" width="-1" hidden="0"/>
      <column type="field" name="importtable" width="-1" hidden="0"/>
      <column type="field" name="lid_actor_creator" width="-1" hidden="0"/>
      <column type="field" name="sirsid" width="-1" hidden="0"/>
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
    <field name="edgesubtype" editable="1"/>
    <field name="edgetype" editable="1"/>
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
    <field name="fonctionnalcondition" editable="1"/>
    <field name="geotrackingdate" editable="1"/>
    <field name="geotrackingsource" editable="1"/>
    <field name="geotrackingxyquality" editable="1"/>
    <field name="geotrackingzquality" editable="1"/>
    <field name="id_descriptionsystem" editable="1"/>
    <field name="id_edge" editable="1"/>
    <field name="id_object" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="lid_actor_1" editable="1"/>
    <field name="lid_actor_2" editable="1"/>
    <field name="lid_actor_3" editable="1"/>
    <field name="lid_actor_creator" editable="1"/>
    <field name="lid_descriptionsystem_1" editable="1"/>
    <field name="lid_descriptionsystem_2" editable="1"/>
    <field name="lid_facility" editable="1"/>
    <field name="lid_resource_1" editable="1"/>
    <field name="lid_resource_2" editable="1"/>
    <field name="lid_resource_3" editable="1"/>
    <field name="lid_resource_4" editable="1"/>
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
    <field name="pk_edge" editable="1"/>
    <field name="pk_object" editable="1"/>
    <field name="regulatorycategory" editable="1"/>
    <field name="setbackcomment" editable="1"/>
    <field name="setbackvegetationherbaceous" editable="1"/>
    <field name="setbackvegetationshrub" editable="1"/>
    <field name="setbackvegetationtree" editable="1"/>
    <field name="setbackwidth" editable="1"/>
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
  </editable>
  <labelOnTop>
    <field name="city" labelOnTop="0"/>
    <field name="comment" labelOnTop="0"/>
    <field name="dateoperationalcreation" labelOnTop="0"/>
    <field name="dateoperationalcreationupper" labelOnTop="0"/>
    <field name="datetimecreation" labelOnTop="0"/>
    <field name="datetimedestruction" labelOnTop="0"/>
    <field name="datetimemodification" labelOnTop="0"/>
    <field name="datetimeoperationaldestruction" labelOnTop="0"/>
    <field name="edgesubtype" labelOnTop="0"/>
    <field name="edgetype" labelOnTop="0"/>
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
    <field name="fonctionnalcondition" labelOnTop="0"/>
    <field name="geotrackingdate" labelOnTop="0"/>
    <field name="geotrackingsource" labelOnTop="0"/>
    <field name="geotrackingxyquality" labelOnTop="0"/>
    <field name="geotrackingzquality" labelOnTop="0"/>
    <field name="id_descriptionsystem" labelOnTop="0"/>
    <field name="id_edge" labelOnTop="0"/>
    <field name="id_object" labelOnTop="0"/>
    <field name="importid" labelOnTop="0"/>
    <field name="importtable" labelOnTop="0"/>
    <field name="lid_actor_1" labelOnTop="0"/>
    <field name="lid_actor_2" labelOnTop="0"/>
    <field name="lid_actor_3" labelOnTop="0"/>
    <field name="lid_actor_creator" labelOnTop="0"/>
    <field name="lid_descriptionsystem_1" labelOnTop="0"/>
    <field name="lid_descriptionsystem_2" labelOnTop="0"/>
    <field name="lid_facility" labelOnTop="0"/>
    <field name="lid_resource_1" labelOnTop="0"/>
    <field name="lid_resource_2" labelOnTop="0"/>
    <field name="lid_resource_3" labelOnTop="0"/>
    <field name="lid_resource_4" labelOnTop="0"/>
    <field name="lpk_descriptionsystem" labelOnTop="0"/>
    <field name="lpk_object" labelOnTop="0"/>
    <field name="lpk_revision_begin" labelOnTop="0"/>
    <field name="lpk_revision_end" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="operational" labelOnTop="0"/>
    <field name="operationaldatecreationaccuracy" labelOnTop="0"/>
    <field name="operationalstate" labelOnTop="0"/>
    <field name="parameters" labelOnTop="0"/>
    <field name="parameterslist" labelOnTop="0"/>
    <field name="pk_descriptionsystem" labelOnTop="0"/>
    <field name="pk_edge" labelOnTop="0"/>
    <field name="pk_object" labelOnTop="0"/>
    <field name="regulatorycategory" labelOnTop="0"/>
    <field name="setbackcomment" labelOnTop="0"/>
    <field name="setbackvegetationherbaceous" labelOnTop="0"/>
    <field name="setbackvegetationshrub" labelOnTop="0"/>
    <field name="setbackvegetationtree" labelOnTop="0"/>
    <field name="setbackwidth" labelOnTop="0"/>
    <field name="sirsid" labelOnTop="0"/>
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
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE("ID", '&lt;NULL>')</previewExpression>
  <mapTip>ID</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
