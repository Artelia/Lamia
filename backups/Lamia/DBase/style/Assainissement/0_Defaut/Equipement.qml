<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.18.19" simplifyAlgorithm="0" minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="0" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" readOnly="0" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
  <edittypes>
    <edittype widgetv2type="TextEdit" name="id_equipement">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="id_objet">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="id_descriptionsystem">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="anMESSup">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="anMESInf">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="maitreOuvrage">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="exploitant">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="metaREAPA">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="altNoeud">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="typeReseau">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="typeAppAss">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="lk_cana1">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="lk_cana2">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="lk_descriptionsystem">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="commentaireequipement">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="datecreation">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="datedestruction">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
  </edittypes>
  <renderer-v2 forceraster="0" symbollevels="0" type="RuleRenderer" enableorderby="0">
    <rules key="{8d79bb70-3d56-44a7-9b09-ed3642611a95}">
      <rule filter=" &quot;typeAppAss&quot; = 5" key="{f000d11b-d68f-4bf7-a63c-499d2af98ee4}" symbol="0" label="Chasse d'eau"/>
      <rule filter=" &quot;typeAppAss&quot; = 6" key="{bdef30db-cbe0-47fb-b85a-f6212ab64259}" symbol="1" label="Déssableur"/>
      <rule filter=" &quot;typeAppAss&quot; = 8" key="{a664c46d-41d5-414e-92ba-43cb555a04e1}" symbol="2" label="Siphon"/>
      <rule filter=" &quot;typeAppAss&quot; = 7" key="{79f5c2c6-8ca7-4a08-8f23-bd460b74cb05}" symbol="3" label="Déversoir d'orage"/>
      <rule filter=" &quot;typeAppAss&quot; = 4" key="{e95d31fe-ae53-4f44-8ce1-dd32771db99d}" symbol="4" label="Débitmètre"/>
    </rules>
    <symbols>
      <symbol alpha="1" clip_to_extent="1" type="marker" name="0">
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="9,2,2,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.5"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="marker" name="1">
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="half_square"/>
          <prop k="offset" v="3.40000000000000036,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.8"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="marker" name="2">
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="182,182,183,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="4,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3.2"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="line"/>
          <prop k="offset" v="3.80000000000000027,-0.59999999999999998"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.6"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.4"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="marker" name="3">
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="9,2,2,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="half_square"/>
          <prop k="offset" v="3.60000000000000053,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="90"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="line"/>
          <prop k="offset" v="0,-4"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.6"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3.4"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="filled_arrowhead"/>
          <prop k="offset" v="6.20000000000000018,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.8"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
      <symbol alpha="1" clip_to_extent="1" type="marker" name="4">
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="315"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="name" v="filled_arrowhead"/>
          <prop k="offset" v="6.20000000000000284,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,255,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5.4"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="221.5"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="line"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="7.6"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="60"/>
          <prop k="color" v="255,0,0,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple"/>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="labeling" value="pal"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="true"/>
    <property key="labeling/bufferJoinStyle" value="128"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="1"/>
    <property key="labeling/bufferSizeInMapUnits" value="false"/>
    <property key="labeling/bufferSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/bufferTransp" value="0"/>
    <property key="labeling/centroidInside" value="false"/>
    <property key="labeling/centroidWhole" value="false"/>
    <property key="labeling/decimals" value="3"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="2"/>
    <property key="labeling/distInMapUnits" value="false"/>
    <property key="labeling/distMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/drawLabels" value="false"/>
    <property key="labeling/enabled" value="false"/>
    <property key="labeling/fieldName" value="ART_ID_ART"/>
    <property key="labeling/fitInPolygonOnly" value="false"/>
    <property key="labeling/fontCapitals" value="0"/>
    <property key="labeling/fontFamily" value="Arial"/>
    <property key="labeling/fontItalic" value="false"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="8.25"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="50"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="true"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="25"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-25"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="3"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Normal"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/obstacleFactor" value="1"/>
    <property key="labeling/obstacleType" value="0"/>
    <property key="labeling/offsetType" value="0"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="1"/>
    <property key="labeling/placementFlags" value="10"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/predefinedPositionOrder" value="TR,TL,BR,BL,R,L,TSR,BSR"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="2"/>
    <property key="labeling/repeatDistance" value="0"/>
    <property key="labeling/repeatDistanceMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/repeatDistanceUnit" value="1"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="10000000"/>
    <property key="labeling/scaleMin" value="1"/>
    <property key="labeling/scaleVisibility" value="false"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="false"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/substitutions" value="&lt;substitutions/>"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="28"/>
    <property key="labeling/textColorG" value="26"/>
    <property key="labeling/textColorR" value="227"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/useSubstitutions" value="false"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0.8"/>
    <property key="labeling/yOffset" value="0.8"/>
    <property key="labeling/zIndex" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerTransparency>0</layerTransparency>
  <displayfield>IDNUM</displayfield>
  <label>0</label>
  <labelattributes>
    <label fieldname="" text="Étiquette"/>
    <family fieldname="" name="MS Shell Dlg 2"/>
    <size fieldname="" units="pt" value="12"/>
    <bold fieldname="" on="0"/>
    <italic fieldname="" on="0"/>
    <underline fieldname="" on="0"/>
    <strikeout fieldname="" on="0"/>
    <color fieldname="" red="0" blue="0" green="0"/>
    <x fieldname=""/>
    <y fieldname=""/>
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
    <angle fieldname="" value="0" auto="0"/>
    <alignment fieldname="" value="center"/>
    <buffercolor fieldname="" red="255" blue="255" green="255"/>
    <buffersize fieldname="" units="pt" value="1"/>
    <bufferenabled fieldname="" on=""/>
    <multilineenabled fieldname="" on=""/>
    <selectedonly on=""/>
  </labelattributes>
  <SingleCategoryDiagramRenderer diagramType="Histogram" sizeLegend="0" attributeLegend="1">
    <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" sizeScale="0,0,0,0,0,0" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" lineSizeScale="0,0,0,0,0,0" sizeType="MM" lineSizeType="MM" minScaleDenominator="inf">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
    <symbol alpha="1" clip_to_extent="1" type="marker" name="sizeSymbol">
      <layer pass="0" class="SimpleMarker" locked="0">
        <prop k="angle" v="0"/>
        <prop k="color" v="255,0,0,255"/>
        <prop k="horizontal_anchor_point" v="1"/>
        <prop k="joinstyle" v="bevel"/>
        <prop k="name" v="circle"/>
        <prop k="offset" v="0,0"/>
        <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="offset_unit" v="MM"/>
        <prop k="outline_color" v="0,0,0,255"/>
        <prop k="outline_style" v="solid"/>
        <prop k="outline_width" v="0"/>
        <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="outline_width_unit" v="MM"/>
        <prop k="scale_method" v="diameter"/>
        <prop k="size" v="2"/>
        <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="size_unit" v="MM"/>
        <prop k="vertical_anchor_point" v="1"/>
      </layer>
    </symbol>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings yPosColumn="-1" showColumn="-1" linePlacementFlags="10" placement="0" dist="0" xPosColumn="-1" priority="0" obstacle="0" zIndex="0" showAll="1"/>
  <annotationform>U:/00_QGis/30_Urbain/Regards EU</annotationform>
  <aliases>
    <alias field="id_equipement" index="0" name=""/>
    <alias field="id_objet" index="1" name=""/>
    <alias field="id_descriptionsystem" index="2" name=""/>
    <alias field="anMESSup" index="3" name=""/>
    <alias field="anMESInf" index="4" name=""/>
    <alias field="maitreOuvrage" index="5" name=""/>
    <alias field="exploitant" index="6" name=""/>
    <alias field="metaREAPA" index="7" name=""/>
    <alias field="altNoeud" index="8" name=""/>
    <alias field="typeReseau" index="9" name=""/>
    <alias field="typeAppAss" index="10" name=""/>
    <alias field="lk_cana1" index="11" name=""/>
    <alias field="lk_cana2" index="12" name=""/>
    <alias field="lk_descriptionsystem" index="13" name=""/>
    <alias field="commentaireequipement" index="14" name=""/>
    <alias field="datecreation" index="15" name=""/>
    <alias field="datedestruction" index="16" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <attributeactions default="-1"/>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="&quot;ART_PHOTOS&quot;" sortOrder="0">
    <columns>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" hidden="0" type="field" name="id_equipement"/>
      <column width="-1" hidden="0" type="field" name="id_objet"/>
      <column width="-1" hidden="0" type="field" name="id_descriptionsystem"/>
      <column width="-1" hidden="0" type="field" name="anMESSup"/>
      <column width="-1" hidden="0" type="field" name="anMESInf"/>
      <column width="-1" hidden="0" type="field" name="maitreOuvrage"/>
      <column width="-1" hidden="0" type="field" name="exploitant"/>
      <column width="-1" hidden="0" type="field" name="metaREAPA"/>
      <column width="-1" hidden="0" type="field" name="altNoeud"/>
      <column width="-1" hidden="0" type="field" name="typeReseau"/>
      <column width="-1" hidden="0" type="field" name="typeAppAss"/>
      <column width="-1" hidden="0" type="field" name="lk_cana1"/>
      <column width="-1" hidden="0" type="field" name="lk_cana2"/>
      <column width="-1" hidden="0" type="field" name="lk_descriptionsystem"/>
      <column width="-1" hidden="0" type="field" name="commentaireequipement"/>
      <column width="-1" hidden="0" type="field" name="datecreation"/>
      <column width="-1" hidden="0" type="field" name="datedestruction"/>
    </columns>
  </attributetableconfig>
  <editform>U:/00_QGis/30_Urbain/Regards EU</editform>
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
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Général" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Type d'ouvrage" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="TYP_POINTS"/>
        <attributeEditorField showLabel="1" index="-1" name="TYP_RESEAU"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Identification de l'ouvrage" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ART_ID_ART"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Données générales" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="COMMUNE"/>
        <attributeEditorField showLabel="1" index="-1" name="INSEE"/>
        <attributeEditorField showLabel="1" index="-1" name="DATEMAJ"/>
        <attributeEditorField showLabel="1" index="-1" name="SYSTCOLLEC"/>
        <attributeEditorField showLabel="1" index="-1" name="SOURCEMAJ"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Topographie du point" groupBox="1" columnCount="3">
        <attributeEditorField showLabel="1" index="-1" name="Topo_X"/>
        <attributeEditorField showLabel="1" index="-1" name="Topo_Y"/>
        <attributeEditorField showLabel="1" index="-1" name="Topo_Z_TN"/>
        <attributeEditorField showLabel="1" index="-1" name="Topo_Xp"/>
        <attributeEditorField showLabel="1" index="-1" name="Topo_Yp"/>
        <attributeEditorField showLabel="1" index="-1" name="Topo_Zp"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Regard" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Photo" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" index="-1" name="ART_PHOTOS"/>
        <attributeEditorField showLabel="1" index="-1" name="ART_PHOTO2"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Arrivées" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" index="-1" name="ART_NB_ARR"/>
        <attributeEditorField showLabel="1" index="-1" name="ART_NB_BRT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Profondeurs et chutes" groupBox="1" columnCount="1">
        <attributeEditorContainer showLabel="0" visibilityExpressionEnabled="0" visibilityExpression="" name="Profondeurs" groupBox="1" columnCount="2">
          <attributeEditorField showLabel="1" index="-1" name="ART_PROF_A"/>
          <attributeEditorField showLabel="1" index="-1" name="PRO_FE_REU"/>
        </attributeEditorContainer>
        <attributeEditorField showLabel="1" index="-1" name="CHUTE_REU"/>
        <attributeEditorContainer showLabel="0" visibilityExpressionEnabled="0" visibilityExpression="" name="Chutes" groupBox="1" columnCount="3">
          <attributeEditorField showLabel="1" index="-1" name="FE_CHUTE1"/>
          <attributeEditorField showLabel="1" index="-1" name="FE_CHUTE2"/>
          <attributeEditorField showLabel="1" index="-1" name="FE_CHUTE3"/>
          <attributeEditorField showLabel="1" index="-1" name="Heure1_REU"/>
          <attributeEditorField showLabel="1" index="-1" name="Heure2_REU"/>
          <attributeEditorField showLabel="1" index="-1" name="Heure3_REU"/>
        </attributeEditorContainer>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Accessibilité" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ART_ACCESS"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Dépôts" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ART_DEPOTS"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Anomalies" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="NB_ANO_REU"/>
        <attributeEditorField showLabel="1" index="-1" name="ANOM_EU1"/>
        <attributeEditorField showLabel="1" index="-1" name="ANOM_EU2"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Travaux" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ART_TRAVAU"/>
        <attributeEditorField showLabel="1" index="-1" name="ART_PRIORI"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Observations" groupBox="1" columnCount="3">
        <attributeEditorField showLabel="1" index="-1" name="ES_REU"/>
        <attributeEditorField showLabel="1" index="-1" name="Tete_REU"/>
        <attributeEditorField showLabel="1" index="-1" name="Sec_REU"/>
        <attributeEditorField showLabel="1" index="-1" name="REGARD_PE"/>
        <attributeEditorField showLabel="1" index="-1" name="REGARD_NV"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="0" visibilityExpressionEnabled="0" visibilityExpression="" name="Remarques" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ART_OBSERV"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Branchement" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Profondeur" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="PROF_BRT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Cotes" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" index="-1" name="COTE_TN"/>
        <attributeEditorField showLabel="1" index="-1" name="COTE_FE_BR"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Dépôts" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="DEPOTS_BRT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Anomalies" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ANOM_BRT1"/>
        <attributeEditorField showLabel="1" index="-1" name="ANOM_BRT2"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Observations" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="CLOISO_BRT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Accessibilité" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ACCES_BRT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Remarques" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="OBSERV_BRT"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Ouvrages EP" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Ouvrage EP" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="TYP_OUV_EP"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Profondeur" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="PRO_OUV_EP"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Cotes" groupBox="1" columnCount="2">
        <attributeEditorField showLabel="1" index="-1" name="COT_TN_OUV"/>
        <attributeEditorField showLabel="1" index="-1" name="COT_FE_OUV"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Dépôts" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="DEPOTS_OUV"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Anomalies" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ANOM_OUV1"/>
        <attributeEditorField showLabel="1" index="-1" name="ANOM_OUV2"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Accessbilité" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="ACCES_OUV"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Remarques" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="OBSERV_OUV"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Ouvrage spécial" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Type d'ouvrage spécial" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="TYP_OUV_SP"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Remarques" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="-1" name="OBS_OUVSP"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <widgets>
    <widget name="ART_ID_ART">
      <config>
        <option key="IsMultiline" value="false"/>
        <option key="UseHtml" value="false"/>
      </config>
    </widget>
  </widgets>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <defaults>
    <default field="id_equipement" expression=""/>
    <default field="id_objet" expression=""/>
    <default field="id_descriptionsystem" expression=""/>
    <default field="anMESSup" expression=""/>
    <default field="anMESInf" expression=""/>
    <default field="maitreOuvrage" expression=""/>
    <default field="exploitant" expression=""/>
    <default field="metaREAPA" expression=""/>
    <default field="altNoeud" expression=""/>
    <default field="typeReseau" expression=""/>
    <default field="typeAppAss" expression=""/>
    <default field="lk_cana1" expression=""/>
    <default field="lk_cana2" expression=""/>
    <default field="lk_descriptionsystem" expression=""/>
    <default field="commentaireequipement" expression=""/>
    <default field="datecreation" expression=""/>
    <default field="datedestruction" expression=""/>
  </defaults>
  <previewExpression>COALESCE("IDNUM", '&lt;NULL>')</previewExpression>
  <layerGeometryType>0</layerGeometryType>
</qgis>
