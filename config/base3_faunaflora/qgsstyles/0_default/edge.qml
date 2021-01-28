<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" styleCategories="AllStyleCategories" maxScale="0" simplifyMaxScale="1" labelsEnabled="1" readOnly="0" minScale="1e+08" simplifyAlgorithm="0" version="3.10.6-A Coruña" simplifyDrawingHints="1" simplifyLocal="1" hasScaleBasedVisibilityFlag="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="RuleRenderer" forceraster="0" enableorderby="0" symbollevels="0">
    <rules key="{5e78f11d-4178-4ed7-8af6-f80178c4ba25}">
      <rule filter=" &quot;edgecategory&quot;  =  'HAB' " key="{221c65f2-4316-4674-9cdd-43cfb1e49457}">
        <rule filter=" distance(start_point( $geometry) ,  end_point( $geometry))&lt; 0.01" key="{a2565bbe-a09c-4371-b9a8-992380c9601a}" symbol="0"/>
        <rule filter="ELSE" key="{e170a888-6ec6-432d-9dc7-98756b30abcc}" symbol="1"/>
      </rule>
      <rule filter=" &quot;edgecategory&quot;  =  'PRO' " key="{b14c7500-1664-4f11-9a34-dcba657b9e96}">
        <rule filter=" $length &lt; 0.01" key="{53cff050-4d86-4fed-bbd2-59afeb6b5daf}" symbol="2"/>
        <rule filter="ELSE" key="{f1b60d11-bfe9-47f5-b586-4a88ec792bcc}" symbol="3"/>
      </rule>
      <rule filter="ELSE" key="{1cbe3cbd-c1b7-4bc0-8f98-c82a875d39f3}" symbol="4"/>
    </rules>
    <symbols>
      <symbol name="0" type="line" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" locked="0" pass="0" class="GeometryGenerator">
          <prop k="SymbolType" v="Fill"/>
          <prop k="geometryModifier" v=" make_polygon( $geometry)"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@0@0" type="fill" force_rhr="0" clip_to_extent="1" alpha="1">
            <layer enabled="1" locked="0" pass="0" class="ShapeburstFill">
              <prop k="blur_radius" v="0"/>
              <prop k="color" v="51,160,44,255"/>
              <prop k="color1" v="0,0,255,255"/>
              <prop k="color2" v="0,255,0,255"/>
              <prop k="color_type" v="0"/>
              <prop k="discrete" v="0"/>
              <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="distance_unit" v="MM"/>
              <prop k="gradient_color2" v="255,255,255,255"/>
              <prop k="ignore_rings" v="0"/>
              <prop k="max_distance" v="5"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="rampType" v="gradient"/>
              <prop k="use_whole_shape" v="1"/>
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
      <symbol name="1" type="line" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="51,160,44,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.86"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" type="line" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" locked="0" pass="0" class="MarkerLine">
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
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@2@0" type="marker" force_rhr="0" clip_to_extent="1" alpha="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="31,120,180,255"/>
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol name="3" type="line" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="31,120,180,255"/>
          <prop k="line_style" v="solid"/>
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
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="4" type="line" force_rhr="0" clip_to_extent="1" alpha="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="183,72,75,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.26"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
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
      <text-style fontSizeUnit="Point" fontItalic="0" fontStrikeout="0" fontWordSpacing="0" fontWeight="50" namedStyle="Normal" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textColor="0,0,0,255" useSubstitutions="0" fontSize="8.25" fieldName=" &quot;diametreNominal&quot; *1000" fontKerning="1" fontUnderline="0" multilineHeight="1" fontCapitals="0" blendMode="0" fontFamily="MS Shell Dlg 2" fontLetterSpacing="0" textOrientation="horizontal" previewBkgrdColor="255,255,255,255" textOpacity="1" isExpression="1">
        <text-buffer bufferNoFill="0" bufferBlendMode="0" bufferSizeUnits="MM" bufferSize="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferJoinStyle="128" bufferDraw="1" bufferOpacity="1" bufferColor="255,255,255,255"/>
        <background shapeType="0" shapeOffsetX="0" shapeSizeX="0" shapeSizeUnit="MM" shapeRotation="0" shapeSizeType="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeOffsetY="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeRotationType="0" shapeBlendMode="0" shapeRadiiUnit="MM" shapeDraw="0" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeOpacity="1" shapeFillColor="255,255,255,255" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeRadiiX="0" shapeBorderColor="128,128,128,255">
          <symbol name="markerSymbol" type="marker" force_rhr="0" clip_to_extent="1" alpha="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadiusUnit="MM" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowScale="100" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowUnder="0" shadowDraw="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowOffsetDist="1" shadowRadius="1.5" shadowOffsetAngle="135"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format reverseDirectionSymbol="0" decimals="3" autoWrapLength="0" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" formatNumbers="0" addDirectionSymbol="0" multilineAlign="4294967295" wrapChar="" plussign="0" placeDirectionSymbol="0"/>
      <placement rotationAngle="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" repeatDistance="0" quadOffset="4" yOffset="0" geometryGeneratorType="PointGeometry" xOffset="0" distUnits="MM" offsetUnits="MapUnit" priority="5" overrunDistanceUnit="MM" geometryGeneratorEnabled="0" geometryGenerator="" preserveRotation="1" centroidWhole="0" maxCurvedCharAngleOut="-25" placement="3" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="LineGeometry" offsetType="0" placementFlags="2" dist="0.5" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" distMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" overrunDistance="0" repeatDistanceUnits="MM"/>
      <rendering obstacleType="0" drawLabels="1" minFeatureSize="2" obstacle="1" fontLimitPixelSize="0" zIndex="0" fontMaxPixelSize="10000" displayAll="0" obstacleFactor="1" fontMinPixelSize="3" mergeLines="1" labelPerPart="0" scaleVisibility="1" scaleMin="1" scaleMax="5000" upsidedownLabels="0" maxNumLabels="2000" limitNumLabels="0"/>
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
          <Option name="lineSymbol" type="QString" value="&lt;symbol name=&quot;symbol&quot; type=&quot;line&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
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
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory penWidth="0" opacity="1" barWidth="5" backgroundAlpha="255" scaleBasedVisibility="0" diagramOrientation="Up" width="15" penColor="#000000" enabled="0" sizeType="MM" scaleDependency="Area" backgroundColor="#ffffff" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" penAlpha="255" maxScaleDenominator="1e+08" height="15" minimumSize="0" minScaleDenominator="0" labelPlacementMethod="XHeight" lineSizeScale="3x:0,0,0,0,0,0">
      <fontProperties description="MS Shell Dlg 2,9.75,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" showAll="1" priority="0" placement="2" dist="0" zIndex="0" obstacle="0">
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
    <default field="pk_edge" expression="" applyOnUpdate="0"/>
    <default field="id_edge" expression="" applyOnUpdate="0"/>
    <default field="lpk_descriptionsystem" expression="" applyOnUpdate="0"/>
    <default field="lid_resource_1" expression="" applyOnUpdate="0"/>
    <default field="lid_descriptionsystem_1" expression="" applyOnUpdate="0"/>
    <default field="lid_descriptionsystem_2" expression="" applyOnUpdate="0"/>
    <default field="edgecategory" expression="" applyOnUpdate="0"/>
    <default field="edgetype" expression="" applyOnUpdate="0"/>
    <default field="edgesubtype" expression="" applyOnUpdate="0"/>
    <default field="edgenumber" expression="" applyOnUpdate="0"/>
    <default field="habitatwetland" expression="" applyOnUpdate="0"/>
    <default field="habitatrepository" expression="" applyOnUpdate="0"/>
    <default field="habitatname" expression="" applyOnUpdate="0"/>
    <default field="habitatcode" expression="" applyOnUpdate="0"/>
    <default field="habitat2wetland" expression="" applyOnUpdate="0"/>
    <default field="habitat2repository" expression="" applyOnUpdate="0"/>
    <default field="habitat2name" expression="" applyOnUpdate="0"/>
    <default field="habitat2code" expression="" applyOnUpdate="0"/>
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
    <default field="commonname" expression="" applyOnUpdate="0"/>
    <default field="scientificname" expression="" applyOnUpdate="0"/>
    <default field="orderclass" expression="" applyOnUpdate="0"/>
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
    <default field="lid_actor" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="pk_edge" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="id_edge" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lpk_descriptionsystem" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_resource_1" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_descriptionsystem_1" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_descriptionsystem_2" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="edgecategory" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="edgetype" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="edgesubtype" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="edgenumber" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitatwetland" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitatrepository" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitatname" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitatcode" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitat2wetland" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitat2repository" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitat2name" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="habitat2code" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="pk_descriptionsystem" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="id_descriptionsystem" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lpk_object" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="strategicvalue" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="operational" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="structuralstate" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="operationalstate" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="dateoperationalcreation" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="dateoperationalcreationupper" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="operationaldatecreationaccuracy" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="datetimeoperationaldestruction" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="geotrackingxyquality" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="geotrackingzquality" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="geotrackingdate" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="geotrackingsource" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="parameters" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="parameterslist" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="city" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="streetname" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="streetupname" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="streetdownname" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="streetcomment" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_actor_1" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_actor_2" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_actor_3" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_facility" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_1" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_2" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_3" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_4" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_5" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_6" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_7" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_8" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_9" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="float_10" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_1" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_2" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_3" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_4" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_5" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_6" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_7" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_8" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_9" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="string_10" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="commonname" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="scientificname" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="orderclass" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="pk_object" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="id_object" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lpk_revision_begin" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lpk_revision_end" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="datetimecreation" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="datetimemodification" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="datetimedestruction" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="comment" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="name" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="importid" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="importtable" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="lid_actor" exp_strength="0" unique_strength="0" notnull_strength="0" constraints="0"/>
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
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column name="pk_edge" type="field" width="-1" hidden="0"/>
      <column name="id_edge" type="field" width="-1" hidden="0"/>
      <column name="lpk_descriptionsystem" type="field" width="-1" hidden="0"/>
      <column name="lid_resource_1" type="field" width="-1" hidden="0"/>
      <column name="lid_descriptionsystem_1" type="field" width="-1" hidden="0"/>
      <column name="lid_descriptionsystem_2" type="field" width="-1" hidden="0"/>
      <column name="edgecategory" type="field" width="-1" hidden="0"/>
      <column name="edgetype" type="field" width="-1" hidden="0"/>
      <column name="edgesubtype" type="field" width="-1" hidden="0"/>
      <column name="edgenumber" type="field" width="-1" hidden="0"/>
      <column name="habitatwetland" type="field" width="-1" hidden="0"/>
      <column name="habitatrepository" type="field" width="-1" hidden="0"/>
      <column name="habitatname" type="field" width="-1" hidden="0"/>
      <column name="habitatcode" type="field" width="-1" hidden="0"/>
      <column name="habitat2wetland" type="field" width="-1" hidden="0"/>
      <column name="habitat2repository" type="field" width="-1" hidden="0"/>
      <column name="habitat2name" type="field" width="-1" hidden="0"/>
      <column name="habitat2code" type="field" width="-1" hidden="0"/>
      <column name="pk_descriptionsystem" type="field" width="-1" hidden="0"/>
      <column name="id_descriptionsystem" type="field" width="-1" hidden="0"/>
      <column name="lpk_object" type="field" width="-1" hidden="0"/>
      <column name="strategicvalue" type="field" width="-1" hidden="0"/>
      <column name="operational" type="field" width="-1" hidden="0"/>
      <column name="structuralstate" type="field" width="-1" hidden="0"/>
      <column name="operationalstate" type="field" width="-1" hidden="0"/>
      <column name="dateoperationalcreation" type="field" width="-1" hidden="0"/>
      <column name="dateoperationalcreationupper" type="field" width="-1" hidden="0"/>
      <column name="operationaldatecreationaccuracy" type="field" width="-1" hidden="0"/>
      <column name="datetimeoperationaldestruction" type="field" width="-1" hidden="0"/>
      <column name="geotrackingxyquality" type="field" width="-1" hidden="0"/>
      <column name="geotrackingzquality" type="field" width="-1" hidden="0"/>
      <column name="geotrackingdate" type="field" width="-1" hidden="0"/>
      <column name="geotrackingsource" type="field" width="-1" hidden="0"/>
      <column name="parameters" type="field" width="-1" hidden="0"/>
      <column name="parameterslist" type="field" width="-1" hidden="0"/>
      <column name="city" type="field" width="-1" hidden="0"/>
      <column name="streetname" type="field" width="-1" hidden="0"/>
      <column name="streetupname" type="field" width="-1" hidden="0"/>
      <column name="streetdownname" type="field" width="-1" hidden="0"/>
      <column name="streetcomment" type="field" width="-1" hidden="0"/>
      <column name="lid_actor_1" type="field" width="-1" hidden="0"/>
      <column name="lid_actor_2" type="field" width="-1" hidden="0"/>
      <column name="lid_actor_3" type="field" width="-1" hidden="0"/>
      <column name="lid_facility" type="field" width="-1" hidden="0"/>
      <column name="float_1" type="field" width="-1" hidden="0"/>
      <column name="float_2" type="field" width="-1" hidden="0"/>
      <column name="float_3" type="field" width="-1" hidden="0"/>
      <column name="float_4" type="field" width="-1" hidden="0"/>
      <column name="float_5" type="field" width="-1" hidden="0"/>
      <column name="float_6" type="field" width="-1" hidden="0"/>
      <column name="float_7" type="field" width="-1" hidden="0"/>
      <column name="float_8" type="field" width="-1" hidden="0"/>
      <column name="float_9" type="field" width="-1" hidden="0"/>
      <column name="float_10" type="field" width="-1" hidden="0"/>
      <column name="string_1" type="field" width="-1" hidden="0"/>
      <column name="string_2" type="field" width="-1" hidden="0"/>
      <column name="string_3" type="field" width="-1" hidden="0"/>
      <column name="string_4" type="field" width="-1" hidden="0"/>
      <column name="string_5" type="field" width="-1" hidden="0"/>
      <column name="string_6" type="field" width="-1" hidden="0"/>
      <column name="string_7" type="field" width="-1" hidden="0"/>
      <column name="string_8" type="field" width="-1" hidden="0"/>
      <column name="string_9" type="field" width="-1" hidden="0"/>
      <column name="string_10" type="field" width="-1" hidden="0"/>
      <column name="commonname" type="field" width="-1" hidden="0"/>
      <column name="scientificname" type="field" width="-1" hidden="0"/>
      <column name="orderclass" type="field" width="-1" hidden="0"/>
      <column name="pk_object" type="field" width="-1" hidden="0"/>
      <column name="id_object" type="field" width="-1" hidden="0"/>
      <column name="lpk_revision_begin" type="field" width="-1" hidden="0"/>
      <column name="lpk_revision_end" type="field" width="-1" hidden="0"/>
      <column name="datetimecreation" type="field" width="-1" hidden="0"/>
      <column name="datetimemodification" type="field" width="-1" hidden="0"/>
      <column name="datetimedestruction" type="field" width="-1" hidden="0"/>
      <column name="comment" type="field" width="-1" hidden="0"/>
      <column name="name" type="field" width="-1" hidden="0"/>
      <column name="importid" type="field" width="-1" hidden="0"/>
      <column name="importtable" type="field" width="-1" hidden="0"/>
      <column name="lid_actor" type="field" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
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
