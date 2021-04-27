<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingHints="1" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" readOnly="0" styleCategories="AllStyleCategories" simplifyAlgorithm="0" labelsEnabled="0" simplifyDrawingTol="1" minScale="0" version="3.10.6-A Coruña" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="RuleRenderer">
    <rules key="{5e78f11d-4178-4ed7-8af6-f80178c4ba25}">
      <rule key="{221c65f2-4316-4674-9cdd-43cfb1e49457}" filter=" &quot;edgecategory&quot;  =  'HAB' ">
        <rule key="{a2565bbe-a09c-4371-b9a8-992380c9601a}" symbol="0" filter=" distance(start_point( $geometry) ,  end_point( $geometry))&lt; 0.01"/>
        <rule key="{e170a888-6ec6-432d-9dc7-98756b30abcc}" symbol="1" filter="ELSE"/>
      </rule>
      <rule key="{b14c7500-1664-4f11-9a34-dcba657b9e96}" filter=" &quot;edgecategory&quot;  =  'PRO' ">
        <rule key="{53cff050-4d86-4fed-bbd2-59afeb6b5daf}" symbol="2" filter=" $length &lt; 0.01"/>
        <rule key="{f1b60d11-bfe9-47f5-b586-4a88ec792bcc}" symbol="3" filter="ELSE"/>
      </rule>
      <rule key="{1cbe3cbd-c1b7-4bc0-8f98-c82a875d39f3}" symbol="4" filter="ELSE"/>
    </rules>
    <symbols>
      <symbol force_rhr="0" name="0" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" class="GeometryGenerator" pass="0" locked="0">
          <prop v="Fill" k="SymbolType"/>
          <prop v=" make_polygon( $geometry)" k="geometryModifier"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" name="@0@0" clip_to_extent="1" type="fill" alpha="1">
            <layer enabled="1" class="SimpleFill" pass="0" locked="0">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="51,255,44,76" k="color"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="51,255,44,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.46" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
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
      <symbol force_rhr="0" name="1" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" class="SimpleLine" pass="0" locked="0">
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="2" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" class="MarkerLine" pass="0" locked="0">
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" name="@2@0" clip_to_extent="1" type="marker" alpha="1">
            <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
              <prop v="0" k="angle"/>
              <prop v="31,120,180,255" k="color"/>
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
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="3" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" class="SimpleLine" pass="0" locked="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="31,120,180,255" k="line_color"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" name="4" clip_to_extent="1" type="line" alpha="1">
        <layer enabled="1" class="SimpleLine" pass="0" locked="0">
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontSize="8" textOrientation="horizontal" fontWeight="75" isExpression="1" textOpacity="1" previewBkgrdColor="255,255,255,255" fontFamily="MS Shell Dlg 2" blendMode="0" fontLetterSpacing="0" useSubstitutions="0" fontUnderline="0" fontWordSpacing="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textColor="51,255,44,255" multilineHeight="1" fontItalic="0" namedStyle="Bold" fontStrikeout="0" fontSizeUnit="Point" fontCapitals="0" fontKerning="1" fieldName="coalesce(&quot;habitatcode&quot;,'')  || 'x' || coalesce( &quot;habitat2code&quot;, '')">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="0" bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferBlendMode="0" bufferJoinStyle="128" bufferColor="255,255,255,255"/>
        <background shapeRadiiX="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeSizeType="0" shapeRadiiY="0" shapeOpacity="1" shapeBorderWidth="0" shapeRotationType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeSizeY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeJoinStyle="64" shapeOffsetUnit="MM" shapeOffsetY="0" shapeBorderWidthUnit="MM" shapeBlendMode="0" shapeRotation="0" shapeSVGFile="" shapeDraw="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0">
          <symbol force_rhr="0" name="markerSymbol" clip_to_extent="1" type="marker" alpha="1">
            <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
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
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetGlobal="1" shadowRadius="1.5" shadowColor="0,0,0,255" shadowBlendMode="6" shadowOffsetAngle="135" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowScale="100" shadowOpacity="0.7" shadowOffsetUnit="MM" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" autoWrapLength="0" addDirectionSymbol="0" leftDirectionSymbol="&lt;" formatNumbers="0" multilineAlign="0" placeDirectionSymbol="0" rightDirectionSymbol=">" decimals="3" plussign="0" wrapChar="" reverseDirectionSymbol="0"/>
      <placement priority="5" quadOffset="4" geometryGenerator=" make_polygon( $geometry)" offsetType="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistanceUnits="MM" fitInPolygonOnly="0" maxCurvedCharAngleIn="25" rotationAngle="0" layerType="LineGeometry" maxCurvedCharAngleOut="-25" xOffset="0" placementFlags="2" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PolygonGeometry" offsetUnits="MapUnit" placement="1" centroidInside="0" distMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceUnit="MM" dist="0.5" distUnits="MM" preserveRotation="1" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0" repeatDistance="0" yOffset="0" overrunDistance="100" geometryGeneratorEnabled="1"/>
      <rendering fontMinPixelSize="3" fontMaxPixelSize="10000" minFeatureSize="2" obstacleFactor="1" upsidedownLabels="0" scaleMax="5000" drawLabels="1" scaleVisibility="1" obstacleType="0" scaleMin="1" limitNumLabels="0" fontLimitPixelSize="0" zIndex="0" obstacle="1" labelPerPart="0" maxNumLabels="2000" mergeLines="1" displayAll="0"/>
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
          <Option name="lineSymbol" value="&lt;symbol force_rhr=&quot;0&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot; locked=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
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
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory opacity="1" penColor="#000000" rotationOffset="270" height="15" barWidth="5" minScaleDenominator="0" minimumSize="0" backgroundColor="#ffffff" scaleBasedVisibility="0" sizeType="MM" penAlpha="255" enabled="0" penWidth="0" sizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" width="15" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" backgroundAlpha="255" maxScaleDenominator="0" lineSizeType="MM" diagramOrientation="Up">
      <fontProperties style="" description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" zIndex="0" dist="0" linePlacementFlags="18" placement="2" priority="0" showAll="1">
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
                <Option name="Protocole" value="PRO" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Habitat" value="HAB" type="QString"/>
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
                <Option name="IPA" value="IPA" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Transect oiseaux nicheurs" value="TON" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Transect oiseaux hivernants" value="TOH" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Point oiseaux migrateurs" value="POM" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Plaque reptile" value="PRE" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Transects entomologie" value="TEN" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Repasse nocturne" value="RNO" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Enregistreurs chiroptères" value="ECH" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Nasse amphibiens" value="NAM" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Piège photo" value="PPH" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Relevé de végétation" value="VEG" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Sondage pédologique" value="PED" type="QString"/>
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
                <Option name="Humide" value="HUM" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Non humide" value="NHU" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Non interprétable" value="NIN" type="QString"/>
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
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Oui" value="1" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Non" value="0" type="QString"/>
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
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="A" value="A" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="B" value="B" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="C" value="C" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="NC" value="NC" type="QString"/>
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
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe A" value="1" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe B" value="2" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe C" value="3" type="QString"/>
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
                <Option name="/" value="" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe A" value="1" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe B" value="2" type="QString"/>
              </Option>
              <Option type="Map">
                <Option name="Classe C" value="3" type="QString"/>
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
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="pk_edge"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="id_edge"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_descriptionsystem"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_resource_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_descriptionsystem_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="edgecategory"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="edgetype"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="edgesubtype"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="edgenumber"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitatwetland"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitatrepository"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitatname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitatcode"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitat2wetland"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitat2repository"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitat2name"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="habitat2code"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="pk_descriptionsystem"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="id_descriptionsystem"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_object"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="strategicvalue"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="operational"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="structuralstate"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="operationalstate"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="dateoperationalcreation"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="dateoperationalcreationupper"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="operationaldatecreationaccuracy"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimeoperationaldestruction"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingxyquality"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingzquality"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingdate"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="geotrackingsource"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="parameters"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="parameterslist"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="city"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetupname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetdownname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="streetcomment"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor_3"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_facility"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_3"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_4"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_5"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_6"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_7"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_8"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_9"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="float_10"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_1"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_2"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_3"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_4"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_5"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_6"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_7"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_8"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_9"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="string_10"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="commonname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="scientificname"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="orderclass"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="pk_object"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="id_object"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_revision_begin"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lpk_revision_end"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimecreation"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimemodification"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="datetimedestruction"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="comment"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="name"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="importid"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="importtable"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" constraints="0" field="lid_actor"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="pk_edge" exp=""/>
    <constraint desc="" field="id_edge" exp=""/>
    <constraint desc="" field="lpk_descriptionsystem" exp=""/>
    <constraint desc="" field="lid_resource_1" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_1" exp=""/>
    <constraint desc="" field="lid_descriptionsystem_2" exp=""/>
    <constraint desc="" field="edgecategory" exp=""/>
    <constraint desc="" field="edgetype" exp=""/>
    <constraint desc="" field="edgesubtype" exp=""/>
    <constraint desc="" field="edgenumber" exp=""/>
    <constraint desc="" field="habitatwetland" exp=""/>
    <constraint desc="" field="habitatrepository" exp=""/>
    <constraint desc="" field="habitatname" exp=""/>
    <constraint desc="" field="habitatcode" exp=""/>
    <constraint desc="" field="habitat2wetland" exp=""/>
    <constraint desc="" field="habitat2repository" exp=""/>
    <constraint desc="" field="habitat2name" exp=""/>
    <constraint desc="" field="habitat2code" exp=""/>
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
    <constraint desc="" field="commonname" exp=""/>
    <constraint desc="" field="scientificname" exp=""/>
    <constraint desc="" field="orderclass" exp=""/>
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
    <constraint desc="" field="lid_actor" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column width="-1" hidden="0" name="pk_edge" type="field"/>
      <column width="-1" hidden="0" name="id_edge" type="field"/>
      <column width="-1" hidden="0" name="lpk_descriptionsystem" type="field"/>
      <column width="-1" hidden="0" name="lid_resource_1" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_1" type="field"/>
      <column width="-1" hidden="0" name="lid_descriptionsystem_2" type="field"/>
      <column width="-1" hidden="0" name="edgecategory" type="field"/>
      <column width="-1" hidden="0" name="edgetype" type="field"/>
      <column width="-1" hidden="0" name="edgesubtype" type="field"/>
      <column width="-1" hidden="0" name="edgenumber" type="field"/>
      <column width="-1" hidden="0" name="habitatwetland" type="field"/>
      <column width="-1" hidden="0" name="habitatrepository" type="field"/>
      <column width="-1" hidden="0" name="habitatname" type="field"/>
      <column width="-1" hidden="0" name="habitatcode" type="field"/>
      <column width="-1" hidden="0" name="habitat2wetland" type="field"/>
      <column width="-1" hidden="0" name="habitat2repository" type="field"/>
      <column width="-1" hidden="0" name="habitat2name" type="field"/>
      <column width="-1" hidden="0" name="habitat2code" type="field"/>
      <column width="-1" hidden="0" name="pk_descriptionsystem" type="field"/>
      <column width="-1" hidden="0" name="id_descriptionsystem" type="field"/>
      <column width="-1" hidden="0" name="lpk_object" type="field"/>
      <column width="-1" hidden="0" name="strategicvalue" type="field"/>
      <column width="-1" hidden="0" name="operational" type="field"/>
      <column width="-1" hidden="0" name="structuralstate" type="field"/>
      <column width="-1" hidden="0" name="operationalstate" type="field"/>
      <column width="-1" hidden="0" name="dateoperationalcreation" type="field"/>
      <column width="-1" hidden="0" name="dateoperationalcreationupper" type="field"/>
      <column width="-1" hidden="0" name="operationaldatecreationaccuracy" type="field"/>
      <column width="-1" hidden="0" name="datetimeoperationaldestruction" type="field"/>
      <column width="-1" hidden="0" name="geotrackingxyquality" type="field"/>
      <column width="-1" hidden="0" name="geotrackingzquality" type="field"/>
      <column width="-1" hidden="0" name="geotrackingdate" type="field"/>
      <column width="-1" hidden="0" name="geotrackingsource" type="field"/>
      <column width="-1" hidden="0" name="parameters" type="field"/>
      <column width="-1" hidden="0" name="parameterslist" type="field"/>
      <column width="-1" hidden="0" name="city" type="field"/>
      <column width="-1" hidden="0" name="streetname" type="field"/>
      <column width="-1" hidden="0" name="streetupname" type="field"/>
      <column width="-1" hidden="0" name="streetdownname" type="field"/>
      <column width="-1" hidden="0" name="streetcomment" type="field"/>
      <column width="-1" hidden="0" name="lid_actor_1" type="field"/>
      <column width="-1" hidden="0" name="lid_actor_2" type="field"/>
      <column width="-1" hidden="0" name="lid_actor_3" type="field"/>
      <column width="-1" hidden="0" name="lid_facility" type="field"/>
      <column width="-1" hidden="0" name="float_1" type="field"/>
      <column width="-1" hidden="0" name="float_2" type="field"/>
      <column width="-1" hidden="0" name="float_3" type="field"/>
      <column width="-1" hidden="0" name="float_4" type="field"/>
      <column width="-1" hidden="0" name="float_5" type="field"/>
      <column width="-1" hidden="0" name="float_6" type="field"/>
      <column width="-1" hidden="0" name="float_7" type="field"/>
      <column width="-1" hidden="0" name="float_8" type="field"/>
      <column width="-1" hidden="0" name="float_9" type="field"/>
      <column width="-1" hidden="0" name="float_10" type="field"/>
      <column width="-1" hidden="0" name="string_1" type="field"/>
      <column width="-1" hidden="0" name="string_2" type="field"/>
      <column width="-1" hidden="0" name="string_3" type="field"/>
      <column width="-1" hidden="0" name="string_4" type="field"/>
      <column width="-1" hidden="0" name="string_5" type="field"/>
      <column width="-1" hidden="0" name="string_6" type="field"/>
      <column width="-1" hidden="0" name="string_7" type="field"/>
      <column width="-1" hidden="0" name="string_8" type="field"/>
      <column width="-1" hidden="0" name="string_9" type="field"/>
      <column width="-1" hidden="0" name="string_10" type="field"/>
      <column width="-1" hidden="0" name="commonname" type="field"/>
      <column width="-1" hidden="0" name="scientificname" type="field"/>
      <column width="-1" hidden="0" name="orderclass" type="field"/>
      <column width="-1" hidden="0" name="pk_object" type="field"/>
      <column width="-1" hidden="0" name="id_object" type="field"/>
      <column width="-1" hidden="0" name="lpk_revision_begin" type="field"/>
      <column width="-1" hidden="0" name="lpk_revision_end" type="field"/>
      <column width="-1" hidden="0" name="datetimecreation" type="field"/>
      <column width="-1" hidden="0" name="datetimemodification" type="field"/>
      <column width="-1" hidden="0" name="datetimedestruction" type="field"/>
      <column width="-1" hidden="0" name="comment" type="field"/>
      <column width="-1" hidden="0" name="name" type="field"/>
      <column width="-1" hidden="0" name="importid" type="field"/>
      <column width="-1" hidden="0" name="importtable" type="field"/>
      <column width="-1" hidden="0" name="lid_actor" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
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
