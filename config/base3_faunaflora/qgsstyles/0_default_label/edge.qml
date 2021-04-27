<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" version="3.16.3-Hannover" styleCategories="Symbology|Labeling">
  <renderer-v2 enableorderby="0" forceraster="0" symbollevels="0" type="RuleRenderer">
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
      <symbol clip_to_extent="1" force_rhr="0" name="0" alpha="1" type="line">
        <layer pass="0" locked="0" enabled="1" class="GeometryGenerator">
          <prop k="SymbolType" v="Fill"/>
          <prop k="geometryModifier" v=" make_polygon( $geometry)"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@0@0" alpha="1" type="fill">
            <layer pass="0" locked="0" enabled="1" class="SimpleFill">
              <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="51,255,44,76"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="51,255,44,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.46"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="style" v="solid"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="1" alpha="1" type="line">
        <layer pass="0" locked="0" enabled="1" class="SimpleLine">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
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
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="2" alpha="1" type="line">
        <layer pass="0" locked="0" enabled="1" class="MarkerLine">
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@2@0" alpha="1" type="marker">
            <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="3" alpha="1" type="line">
        <layer pass="0" locked="0" enabled="1" class="SimpleLine">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
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
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="4" alpha="1" type="line">
        <layer pass="0" locked="0" enabled="1" class="SimpleLine">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
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
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontItalic="0" capitalization="0" fontLetterSpacing="0" textOrientation="horizontal" fontWeight="75" fontFamily="MS Shell Dlg 2" multilineHeight="1" allowHtml="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" blendMode="0" fontSizeUnit="Point" fontStrikeout="0" fontUnderline="0" fontSize="8" textColor="51,255,44,255" isExpression="1" fieldName="coalesce(&quot;habitatcode&quot;,'')  || 'x' || coalesce( &quot;habitat2code&quot;, '')" namedStyle="Bold" previewBkgrdColor="255,255,255,255" fontWordSpacing="0" useSubstitutions="0" fontKerning="1" textOpacity="1">
        <text-buffer bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferNoFill="0" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferDraw="1" bufferJoinStyle="128"/>
        <text-mask maskedSymbolLayers="" maskType="0" maskSizeUnits="MM" maskSize="0" maskJoinStyle="128" maskEnabled="0" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskOpacity="1"/>
        <background shapeRotationType="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeSizeType="0" shapeType="0" shapeRotation="0" shapeBorderWidth="0" shapeOpacity="1" shapeOffsetX="0" shapeOffsetY="0" shapeSizeUnit="MM" shapeSizeY="0" shapeRadiiY="0" shapeSizeX="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeSVGFile="" shapeRadiiUnit="MM" shapeDraw="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeBlendMode="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0">
          <symbol clip_to_extent="1" force_rhr="0" name="markerSymbol" alpha="1" type="marker">
            <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowDraw="0" shadowOffsetDist="1" shadowOpacity="0.7" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowUnder="0" shadowRadiusAlphaOnly="0" shadowScale="100" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" autoWrapLength="0" reverseDirectionSymbol="0" placeDirectionSymbol="0" multilineAlign="0" formatNumbers="0" decimals="3" wrapChar="" rightDirectionSymbol=">" addDirectionSymbol="0" plussign="0"/>
      <placement placement="1" centroidInside="0" geometryGeneratorEnabled="1" polygonPlacementFlags="2" repeatDistance="0" centroidWhole="0" offsetUnits="MapUnit" quadOffset="4" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="100" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator=" make_polygon( $geometry)" distMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" lineAnchorPercent="0.5" xOffset="0" priority="5" dist="0.5" fitInPolygonOnly="0" geometryGeneratorType="PolygonGeometry" preserveRotation="1" lineAnchorType="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" maxCurvedCharAngleIn="25" repeatDistanceUnits="MM" distUnits="MM" offsetType="0" overrunDistanceUnit="MM" yOffset="0" maxCurvedCharAngleOut="-25" placementFlags="2" layerType="LineGeometry"/>
      <rendering obstacle="1" scaleVisibility="1" fontLimitPixelSize="0" upsidedownLabels="0" fontMaxPixelSize="10000" maxNumLabels="2000" limitNumLabels="0" labelPerPart="0" displayAll="0" obstacleFactor="1" minFeatureSize="2" fontMinPixelSize="3" scaleMax="5000" mergeLines="1" drawLabels="1" scaleMin="1" zIndex="0" obstacleType="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" name="anchorPoint" type="QString"/>
          <Option name="ddProperties" type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
          <Option value="false" name="drawToAllParts" type="bool"/>
          <Option value="0" name="enabled" type="QString"/>
          <Option value="point_on_exterior" name="labelAnchorPoint" type="QString"/>
          <Option value="&lt;symbol clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; type=&quot;line&quot;>&lt;layer pass=&quot;0&quot; locked=&quot;0&quot; enabled=&quot;1&quot; class=&quot;SimpleLine&quot;>&lt;prop k=&quot;align_dash_pattern&quot; v=&quot;0&quot;/>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;dash_pattern_offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;dash_pattern_offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;dash_pattern_offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;tweak_dash_pattern_on_corners&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
          <Option value="0" name="minLength" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale" type="QString"/>
          <Option value="MM" name="minLengthUnit" type="QString"/>
          <Option value="0" name="offsetFromAnchor" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromAnchorUnit" type="QString"/>
          <Option value="0" name="offsetFromLabel" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromLabelUnit" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerGeometryType>1</layerGeometryType>
</qgis>
