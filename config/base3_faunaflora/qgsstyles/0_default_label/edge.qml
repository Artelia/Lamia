<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" styleCategories="AllStyleCategories" simplifyDrawingHints="1" minScale="1e+08" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" simplifyLocal="1" version="3.10.6-A Coruña" labelsEnabled="1" maxScale="0" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" symbollevels="0" type="RuleRenderer">
    <rules key="{5e78f11d-4178-4ed7-8af6-f80178c4ba25}">
      <rule key="{221c65f2-4316-4674-9cdd-43cfb1e49457}" filter=" &quot;edgecategory&quot;  =  'HAB' " symbol="0">
        <rule key="{a2565bbe-a09c-4371-b9a8-992380c9601a}" filter=" distance(start_point( $geometry) ,  end_point( $geometry))&lt; 0.01" symbol="1"/>
        <rule key="{e170a888-6ec6-432d-9dc7-98756b30abcc}" filter="ELSE" symbol="2"/>
      </rule>
      <rule key="{b14c7500-1664-4f11-9a34-dcba657b9e96}" filter=" &quot;edgecategory&quot;  =  'PRO' " symbol="3"/>
      <rule key="{1cbe3cbd-c1b7-4bc0-8f98-c82a875d39f3}" filter="ELSE" symbol="4"/>
    </rules>
    <symbols>
      <symbol name="0" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="72,123,182,255" k="line_color"/>
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
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="GeometryGenerator">
          <prop v="Fill" k="SymbolType"/>
          <prop v=" make_polygon( $geometry)" k="geometryModifier"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@1@0" force_rhr="0" type="fill" clip_to_extent="1" alpha="1">
            <layer enabled="1" pass="0" locked="0" class="ShapeburstFill">
              <prop v="0" k="blur_radius"/>
              <prop v="51,160,44,255" k="color"/>
              <prop v="0,0,255,255" k="color1"/>
              <prop v="0,255,0,255" k="color2"/>
              <prop v="0" k="color_type"/>
              <prop v="0" k="discrete"/>
              <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
              <prop v="MM" k="distance_unit"/>
              <prop v="255,255,255,255" k="gradient_color2"/>
              <prop v="0" k="ignore_rings"/>
              <prop v="5" k="max_distance"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="gradient" k="rampType"/>
              <prop v="1" k="use_whole_shape"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="2" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="51,160,44,255" k="line_color"/>
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
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="3" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="72,123,182,255" k="line_color"/>
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
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="4" force_rhr="0" type="line" clip_to_extent="1" alpha="1">
        <layer enabled="1" pass="0" locked="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="183,72,75,255" k="line_color"/>
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
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" isExpression="1" useSubstitutions="0" fontLetterSpacing="0" fontKerning="1" fontCapitals="0" fontFamily="MS Shell Dlg 2" textColor="0,0,0,255" multilineHeight="1" fontItalic="0" fontSizeUnit="Point" fieldName=" &quot;diametreNominal&quot; *1000" fontWordSpacing="0" blendMode="0" fontUnderline="0" fontSize="8.25" fontWeight="50" fontStrikeout="0" namedStyle="Normal" textOrientation="horizontal">
        <text-buffer bufferColor="255,255,255,255" bufferDraw="1" bufferSizeUnits="MM" bufferNoFill="0" bufferOpacity="1" bufferJoinStyle="128" bufferSize="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0"/>
        <background shapeBorderColor="128,128,128,255" shapeType="0" shapeSizeType="0" shapeOffsetX="0" shapeBorderWidth="0" shapeOffsetY="0" shapeRotation="0" shapeBlendMode="0" shapeSizeUnit="MM" shapeOffsetUnit="MM" shapeJoinStyle="64" shapeSizeX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeFillColor="255,255,255,255" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeRadiiUnit="MM" shapeSVGFile="" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeOpacity="1" shapeRadiiX="0" shapeBorderWidthUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0">
          <symbol name="markerSymbol" force_rhr="0" type="marker" clip_to_extent="1" alpha="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetGlobal="1" shadowOpacity="0.7" shadowOffsetDist="1" shadowDraw="0" shadowScale="100" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowRadiusUnit="MM" shadowColor="0,0,0,255" shadowUnder="0" shadowOffsetAngle="135" shadowBlendMode="6" shadowRadius="1.5"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format rightDirectionSymbol=">" plussign="0" autoWrapLength="0" wrapChar="" multilineAlign="4294967295" formatNumbers="0" leftDirectionSymbol="&lt;" useMaxLineLengthForAutoWrap="1" reverseDirectionSymbol="0" decimals="3" placeDirectionSymbol="0" addDirectionSymbol="0"/>
      <placement preserveRotation="1" overrunDistance="0" yOffset="0" geometryGeneratorEnabled="0" offsetType="0" centroidWhole="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" centroidInside="0" layerType="LineGeometry" maxCurvedCharAngleOut="-25" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" xOffset="0" placement="3" rotationAngle="0" distUnits="MM" offsetUnits="MapUnit" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" repeatDistanceUnits="MM" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="2" distMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceUnit="MM" quadOffset="4" geometryGenerator="" dist="0.5" maxCurvedCharAngleIn="25" priority="5" repeatDistance="0"/>
      <rendering obstacleFactor="1" maxNumLabels="2000" zIndex="0" upsidedownLabels="0" obstacleType="0" limitNumLabels="0" mergeLines="1" labelPerPart="0" fontMaxPixelSize="10000" scaleMax="5000" fontMinPixelSize="3" scaleVisibility="1" scaleMin="1" fontLimitPixelSize="0" drawLabels="1" obstacle="1" displayAll="0" minFeatureSize="2"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties"/>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
          <Option name="ddProperties" type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
          <Option name="drawToAllParts" type="bool" value="false"/>
          <Option name="enabled" type="QString" value="0"/>
          <Option name="lineSymbol" type="QString" value="&lt;symbol name=&quot;symbol&quot; force_rhr=&quot;0&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
          <Option name="minLength" type="double" value="0"/>
          <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="minLengthUnit" type="QString" value="MM"/>
          <Option name="offsetFromAnchor" type="double" value="0"/>
          <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
          <Option name="offsetFromLabel" type="double" value="0"/>
          <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
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
    <DiagramCategory scaleBasedVisibility="0" enabled="0" minScaleDenominator="0" minimumSize="0" penWidth="0" lineSizeType="MM" barWidth="5" diagramOrientation="Up" backgroundAlpha="255" labelPlacementMethod="XHeight" sizeScale="3x:0,0,0,0,0,0" maxScaleDenominator="1e+08" penAlpha="255" rotationOffset="270" width="15" lineSizeScale="3x:0,0,0,0,0,0" penColor="#000000" scaleDependency="Area" backgroundColor="#ffffff" opacity="1" sizeType="MM" height="15">
      <fontProperties style="" description="MS Shell Dlg 2,9.75,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" obstacle="0" zIndex="0" placement="2" showAll="1" dist="0" priority="0">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
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
    <field name="edgecategory">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="Protocole" type="QString" value="PRO"/>
              </Option>
              <Option type="Map">
                <Option name="Habitat" type="QString" value="HAB"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="edgetype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="IPA" type="QString" value="IPA"/>
              </Option>
              <Option type="Map">
                <Option name="Transect oiseaux nicheurs" type="QString" value="TON"/>
              </Option>
              <Option type="Map">
                <Option name="Transect oiseaux hivernants" type="QString" value="TOH"/>
              </Option>
              <Option type="Map">
                <Option name="Point oiseaux migrateurs" type="QString" value="POM"/>
              </Option>
              <Option type="Map">
                <Option name="Plaque reptile" type="QString" value="PRE"/>
              </Option>
              <Option type="Map">
                <Option name="Transects entomologie" type="QString" value="TEN"/>
              </Option>
              <Option type="Map">
                <Option name="Repasse nocturne" type="QString" value="RNO"/>
              </Option>
              <Option type="Map">
                <Option name="Enregistreurs chiroptères" type="QString" value="ECH"/>
              </Option>
              <Option type="Map">
                <Option name="Nasse amphibiens" type="QString" value="NAM"/>
              </Option>
              <Option type="Map">
                <Option name="Piège photo" type="QString" value="PPH"/>
              </Option>
              <Option type="Map">
                <Option name="Relevé de végétation" type="QString" value="VEG"/>
              </Option>
              <Option type="Map">
                <Option name="Sondage pédologique" type="QString" value="PED"/>
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
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="Humide" type="QString" value="HUM"/>
              </Option>
              <Option type="Map">
                <Option name="Non humide" type="QString" value="NHU"/>
              </Option>
              <Option type="Map">
                <Option name="Non interprétable" type="QString" value="NIN"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="edgenumber">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitatwetland">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitatrepository">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitatname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitatcode">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitat2wetland">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitat2repository">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitat2name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="habitat2code">
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
            <Option name="map" type="List">
              <Option type="Map">
                <Option name="/" type="QString" value=""/>
              </Option>
              <Option type="Map">
                <Option name="Oui" type="QString" value="1"/>
              </Option>
              <Option type="Map">
                <Option name="Non" type="QString" value="0"/>
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
                <Option name="/" type="QString" value=""/>
              </Option>
              <Option type="Map">
                <Option name="A" type="QString" value="A"/>
              </Option>
              <Option type="Map">
                <Option name="B" type="QString" value="B"/>
              </Option>
              <Option type="Map">
                <Option name="C" type="QString" value="C"/>
              </Option>
              <Option type="Map">
                <Option name="NC" type="QString" value="NC"/>
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
                <Option name="/" type="QString" value=""/>
              </Option>
              <Option type="Map">
                <Option name="Classe A" type="QString" value="1"/>
              </Option>
              <Option type="Map">
                <Option name="Classe B" type="QString" value="2"/>
              </Option>
              <Option type="Map">
                <Option name="Classe C" type="QString" value="3"/>
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
                <Option name="/" type="QString" value=""/>
              </Option>
              <Option type="Map">
                <Option name="Classe A" type="QString" value="1"/>
              </Option>
              <Option type="Map">
                <Option name="Classe B" type="QString" value="2"/>
              </Option>
              <Option type="Map">
                <Option name="Classe C" type="QString" value="3"/>
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
    <field name="commonname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="scientificname">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="orderclass">
      <editWidget type="TextEdit">
        <config>
          <Option/>
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
    <field name="lid_actor">
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
    <alias name="" field="edgecategory" index="6"/>
    <alias name="" field="edgetype" index="7"/>
    <alias name="" field="edgesubtype" index="8"/>
    <alias name="" field="edgenumber" index="9"/>
    <alias name="" field="habitatwetland" index="10"/>
    <alias name="" field="habitatrepository" index="11"/>
    <alias name="" field="habitatname" index="12"/>
    <alias name="" field="habitatcode" index="13"/>
    <alias name="" field="habitat2wetland" index="14"/>
    <alias name="" field="habitat2repository" index="15"/>
    <alias name="" field="habitat2name" index="16"/>
    <alias name="" field="habitat2code" index="17"/>
    <alias name="" field="pk_descriptionsystem" index="18"/>
    <alias name="" field="id_descriptionsystem" index="19"/>
    <alias name="" field="lpk_object" index="20"/>
    <alias name="" field="strategicvalue" index="21"/>
    <alias name="" field="operational" index="22"/>
    <alias name="" field="structuralstate" index="23"/>
    <alias name="" field="operationalstate" index="24"/>
    <alias name="" field="dateoperationalcreation" index="25"/>
    <alias name="" field="dateoperationalcreationupper" index="26"/>
    <alias name="" field="operationaldatecreationaccuracy" index="27"/>
    <alias name="" field="datetimeoperationaldestruction" index="28"/>
    <alias name="" field="geotrackingxyquality" index="29"/>
    <alias name="" field="geotrackingzquality" index="30"/>
    <alias name="" field="geotrackingdate" index="31"/>
    <alias name="" field="geotrackingsource" index="32"/>
    <alias name="" field="parameters" index="33"/>
    <alias name="" field="parameterslist" index="34"/>
    <alias name="" field="city" index="35"/>
    <alias name="" field="streetname" index="36"/>
    <alias name="" field="streetupname" index="37"/>
    <alias name="" field="streetdownname" index="38"/>
    <alias name="" field="streetcomment" index="39"/>
    <alias name="" field="lid_actor_1" index="40"/>
    <alias name="" field="lid_actor_2" index="41"/>
    <alias name="" field="lid_actor_3" index="42"/>
    <alias name="" field="lid_facility" index="43"/>
    <alias name="" field="float_1" index="44"/>
    <alias name="" field="float_2" index="45"/>
    <alias name="" field="float_3" index="46"/>
    <alias name="" field="float_4" index="47"/>
    <alias name="" field="float_5" index="48"/>
    <alias name="" field="float_6" index="49"/>
    <alias name="" field="float_7" index="50"/>
    <alias name="" field="float_8" index="51"/>
    <alias name="" field="float_9" index="52"/>
    <alias name="" field="float_10" index="53"/>
    <alias name="" field="string_1" index="54"/>
    <alias name="" field="string_2" index="55"/>
    <alias name="" field="string_3" index="56"/>
    <alias name="" field="string_4" index="57"/>
    <alias name="" field="string_5" index="58"/>
    <alias name="" field="string_6" index="59"/>
    <alias name="" field="string_7" index="60"/>
    <alias name="" field="string_8" index="61"/>
    <alias name="" field="string_9" index="62"/>
    <alias name="" field="string_10" index="63"/>
    <alias name="" field="commonname" index="64"/>
    <alias name="" field="scientificname" index="65"/>
    <alias name="" field="orderclass" index="66"/>
    <alias name="" field="pk_object" index="67"/>
    <alias name="" field="id_object" index="68"/>
    <alias name="" field="lpk_revision_begin" index="69"/>
    <alias name="" field="lpk_revision_end" index="70"/>
    <alias name="" field="datetimecreation" index="71"/>
    <alias name="" field="datetimemodification" index="72"/>
    <alias name="" field="datetimedestruction" index="73"/>
    <alias name="" field="comment" index="74"/>
    <alias name="" field="name" index="75"/>
    <alias name="" field="importid" index="76"/>
    <alias name="" field="importtable" index="77"/>
    <alias name="" field="lid_actor" index="78"/>
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
    <default expression="" field="edgecategory" applyOnUpdate="0"/>
    <default expression="" field="edgetype" applyOnUpdate="0"/>
    <default expression="" field="edgesubtype" applyOnUpdate="0"/>
    <default expression="" field="edgenumber" applyOnUpdate="0"/>
    <default expression="" field="habitatwetland" applyOnUpdate="0"/>
    <default expression="" field="habitatrepository" applyOnUpdate="0"/>
    <default expression="" field="habitatname" applyOnUpdate="0"/>
    <default expression="" field="habitatcode" applyOnUpdate="0"/>
    <default expression="" field="habitat2wetland" applyOnUpdate="0"/>
    <default expression="" field="habitat2repository" applyOnUpdate="0"/>
    <default expression="" field="habitat2name" applyOnUpdate="0"/>
    <default expression="" field="habitat2code" applyOnUpdate="0"/>
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
    <default expression="" field="commonname" applyOnUpdate="0"/>
    <default expression="" field="scientificname" applyOnUpdate="0"/>
    <default expression="" field="orderclass" applyOnUpdate="0"/>
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
    <default expression="" field="lid_actor" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="pk_edge"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="id_edge"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lpk_descriptionsystem"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_resource_1"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_descriptionsystem_1"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_descriptionsystem_2"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="edgecategory"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="edgetype"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="edgesubtype"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="edgenumber"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitatwetland"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitatrepository"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitatname"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitatcode"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitat2wetland"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitat2repository"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitat2name"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="habitat2code"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="pk_descriptionsystem"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="id_descriptionsystem"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lpk_object"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="strategicvalue"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="operational"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="structuralstate"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="operationalstate"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="dateoperationalcreation"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="dateoperationalcreationupper"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="operationaldatecreationaccuracy"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="datetimeoperationaldestruction"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="geotrackingxyquality"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="geotrackingzquality"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="geotrackingdate"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="geotrackingsource"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="parameters"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="parameterslist"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="city"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="streetname"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="streetupname"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="streetdownname"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="streetcomment"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_actor_1"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_actor_2"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_actor_3"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_facility"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_1"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_2"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_3"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_4"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_5"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_6"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_7"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_8"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_9"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="float_10"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_1"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_2"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_3"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_4"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_5"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_6"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_7"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_8"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_9"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="string_10"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="commonname"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="scientificname"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="orderclass"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="pk_object"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="id_object"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lpk_revision_begin"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lpk_revision_end"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="datetimecreation"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="datetimemodification"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="datetimedestruction"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="comment"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="name"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="importid"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="importtable"/>
    <constraint constraints="0" notnull_strength="0" unique_strength="0" exp_strength="0" field="lid_actor"/>
  </constraints>
  <constraintExpressions>
    <constraint field="pk_edge" exp="" desc=""/>
    <constraint field="id_edge" exp="" desc=""/>
    <constraint field="lpk_descriptionsystem" exp="" desc=""/>
    <constraint field="lid_resource_1" exp="" desc=""/>
    <constraint field="lid_descriptionsystem_1" exp="" desc=""/>
    <constraint field="lid_descriptionsystem_2" exp="" desc=""/>
    <constraint field="edgecategory" exp="" desc=""/>
    <constraint field="edgetype" exp="" desc=""/>
    <constraint field="edgesubtype" exp="" desc=""/>
    <constraint field="edgenumber" exp="" desc=""/>
    <constraint field="habitatwetland" exp="" desc=""/>
    <constraint field="habitatrepository" exp="" desc=""/>
    <constraint field="habitatname" exp="" desc=""/>
    <constraint field="habitatcode" exp="" desc=""/>
    <constraint field="habitat2wetland" exp="" desc=""/>
    <constraint field="habitat2repository" exp="" desc=""/>
    <constraint field="habitat2name" exp="" desc=""/>
    <constraint field="habitat2code" exp="" desc=""/>
    <constraint field="pk_descriptionsystem" exp="" desc=""/>
    <constraint field="id_descriptionsystem" exp="" desc=""/>
    <constraint field="lpk_object" exp="" desc=""/>
    <constraint field="strategicvalue" exp="" desc=""/>
    <constraint field="operational" exp="" desc=""/>
    <constraint field="structuralstate" exp="" desc=""/>
    <constraint field="operationalstate" exp="" desc=""/>
    <constraint field="dateoperationalcreation" exp="" desc=""/>
    <constraint field="dateoperationalcreationupper" exp="" desc=""/>
    <constraint field="operationaldatecreationaccuracy" exp="" desc=""/>
    <constraint field="datetimeoperationaldestruction" exp="" desc=""/>
    <constraint field="geotrackingxyquality" exp="" desc=""/>
    <constraint field="geotrackingzquality" exp="" desc=""/>
    <constraint field="geotrackingdate" exp="" desc=""/>
    <constraint field="geotrackingsource" exp="" desc=""/>
    <constraint field="parameters" exp="" desc=""/>
    <constraint field="parameterslist" exp="" desc=""/>
    <constraint field="city" exp="" desc=""/>
    <constraint field="streetname" exp="" desc=""/>
    <constraint field="streetupname" exp="" desc=""/>
    <constraint field="streetdownname" exp="" desc=""/>
    <constraint field="streetcomment" exp="" desc=""/>
    <constraint field="lid_actor_1" exp="" desc=""/>
    <constraint field="lid_actor_2" exp="" desc=""/>
    <constraint field="lid_actor_3" exp="" desc=""/>
    <constraint field="lid_facility" exp="" desc=""/>
    <constraint field="float_1" exp="" desc=""/>
    <constraint field="float_2" exp="" desc=""/>
    <constraint field="float_3" exp="" desc=""/>
    <constraint field="float_4" exp="" desc=""/>
    <constraint field="float_5" exp="" desc=""/>
    <constraint field="float_6" exp="" desc=""/>
    <constraint field="float_7" exp="" desc=""/>
    <constraint field="float_8" exp="" desc=""/>
    <constraint field="float_9" exp="" desc=""/>
    <constraint field="float_10" exp="" desc=""/>
    <constraint field="string_1" exp="" desc=""/>
    <constraint field="string_2" exp="" desc=""/>
    <constraint field="string_3" exp="" desc=""/>
    <constraint field="string_4" exp="" desc=""/>
    <constraint field="string_5" exp="" desc=""/>
    <constraint field="string_6" exp="" desc=""/>
    <constraint field="string_7" exp="" desc=""/>
    <constraint field="string_8" exp="" desc=""/>
    <constraint field="string_9" exp="" desc=""/>
    <constraint field="string_10" exp="" desc=""/>
    <constraint field="commonname" exp="" desc=""/>
    <constraint field="scientificname" exp="" desc=""/>
    <constraint field="orderclass" exp="" desc=""/>
    <constraint field="pk_object" exp="" desc=""/>
    <constraint field="id_object" exp="" desc=""/>
    <constraint field="lpk_revision_begin" exp="" desc=""/>
    <constraint field="lpk_revision_end" exp="" desc=""/>
    <constraint field="datetimecreation" exp="" desc=""/>
    <constraint field="datetimemodification" exp="" desc=""/>
    <constraint field="datetimedestruction" exp="" desc=""/>
    <constraint field="comment" exp="" desc=""/>
    <constraint field="name" exp="" desc=""/>
    <constraint field="importid" exp="" desc=""/>
    <constraint field="importtable" exp="" desc=""/>
    <constraint field="lid_actor" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column name="pk_edge" hidden="0" type="field" width="-1"/>
      <column name="id_edge" hidden="0" type="field" width="-1"/>
      <column name="lpk_descriptionsystem" hidden="0" type="field" width="-1"/>
      <column name="lid_resource_1" hidden="0" type="field" width="-1"/>
      <column name="lid_descriptionsystem_1" hidden="0" type="field" width="-1"/>
      <column name="lid_descriptionsystem_2" hidden="0" type="field" width="-1"/>
      <column name="edgecategory" hidden="0" type="field" width="-1"/>
      <column name="edgetype" hidden="0" type="field" width="-1"/>
      <column name="edgesubtype" hidden="0" type="field" width="-1"/>
      <column name="edgenumber" hidden="0" type="field" width="-1"/>
      <column name="habitatwetland" hidden="0" type="field" width="-1"/>
      <column name="habitatrepository" hidden="0" type="field" width="-1"/>
      <column name="habitatname" hidden="0" type="field" width="-1"/>
      <column name="habitatcode" hidden="0" type="field" width="-1"/>
      <column name="habitat2wetland" hidden="0" type="field" width="-1"/>
      <column name="habitat2repository" hidden="0" type="field" width="-1"/>
      <column name="habitat2name" hidden="0" type="field" width="-1"/>
      <column name="habitat2code" hidden="0" type="field" width="-1"/>
      <column name="pk_descriptionsystem" hidden="0" type="field" width="-1"/>
      <column name="id_descriptionsystem" hidden="0" type="field" width="-1"/>
      <column name="lpk_object" hidden="0" type="field" width="-1"/>
      <column name="strategicvalue" hidden="0" type="field" width="-1"/>
      <column name="operational" hidden="0" type="field" width="-1"/>
      <column name="structuralstate" hidden="0" type="field" width="-1"/>
      <column name="operationalstate" hidden="0" type="field" width="-1"/>
      <column name="dateoperationalcreation" hidden="0" type="field" width="-1"/>
      <column name="dateoperationalcreationupper" hidden="0" type="field" width="-1"/>
      <column name="operationaldatecreationaccuracy" hidden="0" type="field" width="-1"/>
      <column name="datetimeoperationaldestruction" hidden="0" type="field" width="-1"/>
      <column name="geotrackingxyquality" hidden="0" type="field" width="-1"/>
      <column name="geotrackingzquality" hidden="0" type="field" width="-1"/>
      <column name="geotrackingdate" hidden="0" type="field" width="-1"/>
      <column name="geotrackingsource" hidden="0" type="field" width="-1"/>
      <column name="parameters" hidden="0" type="field" width="-1"/>
      <column name="parameterslist" hidden="0" type="field" width="-1"/>
      <column name="city" hidden="0" type="field" width="-1"/>
      <column name="streetname" hidden="0" type="field" width="-1"/>
      <column name="streetupname" hidden="0" type="field" width="-1"/>
      <column name="streetdownname" hidden="0" type="field" width="-1"/>
      <column name="streetcomment" hidden="0" type="field" width="-1"/>
      <column name="lid_actor_1" hidden="0" type="field" width="-1"/>
      <column name="lid_actor_2" hidden="0" type="field" width="-1"/>
      <column name="lid_actor_3" hidden="0" type="field" width="-1"/>
      <column name="lid_facility" hidden="0" type="field" width="-1"/>
      <column name="float_1" hidden="0" type="field" width="-1"/>
      <column name="float_2" hidden="0" type="field" width="-1"/>
      <column name="float_3" hidden="0" type="field" width="-1"/>
      <column name="float_4" hidden="0" type="field" width="-1"/>
      <column name="float_5" hidden="0" type="field" width="-1"/>
      <column name="float_6" hidden="0" type="field" width="-1"/>
      <column name="float_7" hidden="0" type="field" width="-1"/>
      <column name="float_8" hidden="0" type="field" width="-1"/>
      <column name="float_9" hidden="0" type="field" width="-1"/>
      <column name="float_10" hidden="0" type="field" width="-1"/>
      <column name="string_1" hidden="0" type="field" width="-1"/>
      <column name="string_2" hidden="0" type="field" width="-1"/>
      <column name="string_3" hidden="0" type="field" width="-1"/>
      <column name="string_4" hidden="0" type="field" width="-1"/>
      <column name="string_5" hidden="0" type="field" width="-1"/>
      <column name="string_6" hidden="0" type="field" width="-1"/>
      <column name="string_7" hidden="0" type="field" width="-1"/>
      <column name="string_8" hidden="0" type="field" width="-1"/>
      <column name="string_9" hidden="0" type="field" width="-1"/>
      <column name="string_10" hidden="0" type="field" width="-1"/>
      <column name="commonname" hidden="0" type="field" width="-1"/>
      <column name="scientificname" hidden="0" type="field" width="-1"/>
      <column name="orderclass" hidden="0" type="field" width="-1"/>
      <column name="pk_object" hidden="0" type="field" width="-1"/>
      <column name="id_object" hidden="0" type="field" width="-1"/>
      <column name="lpk_revision_begin" hidden="0" type="field" width="-1"/>
      <column name="lpk_revision_end" hidden="0" type="field" width="-1"/>
      <column name="datetimecreation" hidden="0" type="field" width="-1"/>
      <column name="datetimemodification" hidden="0" type="field" width="-1"/>
      <column name="datetimedestruction" hidden="0" type="field" width="-1"/>
      <column name="comment" hidden="0" type="field" width="-1"/>
      <column name="name" hidden="0" type="field" width="-1"/>
      <column name="importid" hidden="0" type="field" width="-1"/>
      <column name="importtable" hidden="0" type="field" width="-1"/>
      <column name="lid_actor" hidden="0" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
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
    <field name="city" editable="1"/>
    <field name="comment" editable="1"/>
    <field name="commonname" editable="1"/>
    <field name="dateoperationalcreation" editable="1"/>
    <field name="dateoperationalcreationupper" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimemodification" editable="1"/>
    <field name="datetimeoperationaldestruction" editable="1"/>
    <field name="edgecategory" editable="1"/>
    <field name="edgenumber" editable="1"/>
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
    <field name="geotrackingdate" editable="1"/>
    <field name="geotrackingsource" editable="1"/>
    <field name="geotrackingxyquality" editable="1"/>
    <field name="geotrackingzquality" editable="1"/>
    <field name="habitat2code" editable="1"/>
    <field name="habitat2name" editable="1"/>
    <field name="habitat2repository" editable="1"/>
    <field name="habitat2wetland" editable="1"/>
    <field name="habitatcode" editable="1"/>
    <field name="habitatname" editable="1"/>
    <field name="habitatrepository" editable="1"/>
    <field name="habitatwetland" editable="1"/>
    <field name="id_descriptionsystem" editable="1"/>
    <field name="id_edge" editable="1"/>
    <field name="id_object" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="lid_actor" editable="1"/>
    <field name="lid_actor_1" editable="1"/>
    <field name="lid_actor_2" editable="1"/>
    <field name="lid_actor_3" editable="1"/>
    <field name="lid_descriptionsystem_1" editable="1"/>
    <field name="lid_descriptionsystem_2" editable="1"/>
    <field name="lid_facility" editable="1"/>
    <field name="lid_resource_1" editable="1"/>
    <field name="lpk_descriptionsystem" editable="1"/>
    <field name="lpk_object" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="name" editable="1"/>
    <field name="operational" editable="1"/>
    <field name="operationaldatecreationaccuracy" editable="1"/>
    <field name="operationalstate" editable="1"/>
    <field name="orderclass" editable="1"/>
    <field name="parameters" editable="1"/>
    <field name="parameterslist" editable="1"/>
    <field name="pk_descriptionsystem" editable="1"/>
    <field name="pk_edge" editable="1"/>
    <field name="pk_object" editable="1"/>
    <field name="scientificname" editable="1"/>
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
    <field name="commonname" labelOnTop="0"/>
    <field name="dateoperationalcreation" labelOnTop="0"/>
    <field name="dateoperationalcreationupper" labelOnTop="0"/>
    <field name="datetimecreation" labelOnTop="0"/>
    <field name="datetimedestruction" labelOnTop="0"/>
    <field name="datetimemodification" labelOnTop="0"/>
    <field name="datetimeoperationaldestruction" labelOnTop="0"/>
    <field name="edgecategory" labelOnTop="0"/>
    <field name="edgenumber" labelOnTop="0"/>
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
    <field name="geotrackingdate" labelOnTop="0"/>
    <field name="geotrackingsource" labelOnTop="0"/>
    <field name="geotrackingxyquality" labelOnTop="0"/>
    <field name="geotrackingzquality" labelOnTop="0"/>
    <field name="habitat2code" labelOnTop="0"/>
    <field name="habitat2name" labelOnTop="0"/>
    <field name="habitat2repository" labelOnTop="0"/>
    <field name="habitat2wetland" labelOnTop="0"/>
    <field name="habitatcode" labelOnTop="0"/>
    <field name="habitatname" labelOnTop="0"/>
    <field name="habitatrepository" labelOnTop="0"/>
    <field name="habitatwetland" labelOnTop="0"/>
    <field name="id_descriptionsystem" labelOnTop="0"/>
    <field name="id_edge" labelOnTop="0"/>
    <field name="id_object" labelOnTop="0"/>
    <field name="importid" labelOnTop="0"/>
    <field name="importtable" labelOnTop="0"/>
    <field name="lid_actor" labelOnTop="0"/>
    <field name="lid_actor_1" labelOnTop="0"/>
    <field name="lid_actor_2" labelOnTop="0"/>
    <field name="lid_actor_3" labelOnTop="0"/>
    <field name="lid_descriptionsystem_1" labelOnTop="0"/>
    <field name="lid_descriptionsystem_2" labelOnTop="0"/>
    <field name="lid_facility" labelOnTop="0"/>
    <field name="lid_resource_1" labelOnTop="0"/>
    <field name="lpk_descriptionsystem" labelOnTop="0"/>
    <field name="lpk_object" labelOnTop="0"/>
    <field name="lpk_revision_begin" labelOnTop="0"/>
    <field name="lpk_revision_end" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="operational" labelOnTop="0"/>
    <field name="operationaldatecreationaccuracy" labelOnTop="0"/>
    <field name="operationalstate" labelOnTop="0"/>
    <field name="orderclass" labelOnTop="0"/>
    <field name="parameters" labelOnTop="0"/>
    <field name="parameterslist" labelOnTop="0"/>
    <field name="pk_descriptionsystem" labelOnTop="0"/>
    <field name="pk_edge" labelOnTop="0"/>
    <field name="pk_object" labelOnTop="0"/>
    <field name="scientificname" labelOnTop="0"/>
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
  <previewExpression>habitatname</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
