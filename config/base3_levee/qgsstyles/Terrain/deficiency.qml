<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingHints="1" readOnly="0" simplifyAlgorithm="0" minScale="10000" simplifyDrawingTol="1" styleCategories="AllStyleCategories" labelsEnabled="0" maxScale="0" simplifyLocal="1" version="3.10.6-A Coruña" hasScaleBasedVisibilityFlag="1" simplifyMaxScale="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="1" forceraster="0" enableorderby="0" type="RuleRenderer">
    <rules key="{814f4a1d-ecf8-4ab4-af4f-b8f84c22d0bd}">
      <rule filter="&quot;lid_delivery&quot; IS NULL" key="{6652c99c-0248-4546-88d6-1bb35ef40c04}">
        <rule symbol="0" label="Désordre lineaire" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) !=  &#xa;geom_to_wkt( start_point(  $geometry ))" key="{747333ae-2688-406a-89f4-39747d717133}"/>
        <rule symbol="1" label="Fiche ouvrage" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) =  &#xa;geom_to_wkt( start_point(  $geometry )) AND  &quot;deficiencycategory&quot; = 'EQP'" key="{efcb44ac-3d5a-46cf-82f4-1a8e37d88cb4}"/>
        <rule symbol="2" label="Désordre ponctuel" filter="&#xa;geom_to_wkt( end_point(  $geometry ) ) =  &#xa;geom_to_wkt( start_point(  $geometry )) AND  &quot;deficiencycategory&quot; = 'INF'" key="{0ab42a12-fbde-44ed-8e8b-4e734c36fa3d}"/>
      </rule>
    </rules>
    <symbols>
      <symbol name="0" alpha="1" clip_to_extent="1" force_rhr="0" type="line">
        <layer locked="0" enabled="1" pass="0" class="SimpleLine">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,138,99,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.56" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer locked="1" enabled="1" pass="0" class="SimpleLine">
          <prop v="round" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="round" k="joinstyle"/>
          <prop v="255,1,1,255" k="line_color"/>
          <prop v="dot" k="line_style"/>
          <prop v="1.36" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" alpha="1" clip_to_extent="1" force_rhr="0" type="line">
        <layer locked="0" enabled="1" pass="6" class="MarkerLine">
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol name="@1@0" alpha="1" clip_to_extent="1" force_rhr="0" type="marker">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="31,120,180,255" k="color"/>
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
              <prop v="4" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
      <symbol name="2" alpha="1" clip_to_extent="1" force_rhr="0" type="line">
        <layer locked="0" enabled="1" pass="6" class="MarkerLine">
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol name="@2@0" alpha="1" clip_to_extent="1" force_rhr="0" type="marker">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,0,0,255" k="color"/>
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
              <prop v="4" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
    </symbols>
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
    <DiagramCategory labelPlacementMethod="XHeight" backgroundAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" opacity="1" penColor="#000000" maxScaleDenominator="1e+08" lineSizeType="MM" minimumSize="0" scaleBasedVisibility="0" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0" height="15" barWidth="5" penAlpha="255" diagramOrientation="Up" backgroundColor="#ffffff" scaleDependency="Area" minScaleDenominator="0" sizeType="MM" width="15" penWidth="0" enabled="0">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" field="" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" zIndex="0" placement="2" dist="0" linePlacementFlags="2" priority="0" obstacle="0">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="pk_deficiency">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id_deficiency">
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
    <field name="deficiencycategory">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="INF" name="Infralineaire" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="EQP" name="Equipement" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="impact">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="priority">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="risks">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sector1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sector2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sector3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lid_descriptionsystem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="side">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RIV" name="Eau" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TER" name="Terre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ETG" name="Etang" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MER" name="Océan" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DEU" name="Deux cotés" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CRE" name="Crête" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indefini" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="position">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CRE" name="Crête" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BRM" name="Berme supérieure" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="COU" name="Ouvrage de couronnement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TAD" name="Talus digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SOR" name="Sommet risberme" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TAR" name="Talus risberme" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TRP" name="Talus risberme - pied" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PDI" name="Pied de digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FRB" name="Franc-bord" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BER" name="Berge" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="HOR" name="Hors digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PLU" name="Plusieurs parties" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indefini" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="deficiencytype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ERX" name="Erosion externe" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ERI" name="Erosion interne" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DAF" name="Affectant la structure" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ENT" name="Lié à l'entretien de la digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BRE" name="Brèche" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="AUT" name="Autre" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="deficiencysubtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ERF" name="Erosion long. due au fleuve" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ERD" name="Erosion long. autre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SUD" name="Surverse directe" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SUR" name="Surverse par retour" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ARR" name="Arrachement lié a une chute d'arbre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PIE" name="Piétinements d'animaux" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PIT" name="Piétinements anthropiques" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ESS" name="Escaliers sauvages" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RAV" name="Indice de Ravinement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="AVG" name="Absence de végétaion" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IFU" name="Indice de fuite" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RUP" name="Rupture de réseaux" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SDG" name="Sondage en cours de visite" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="RDH" name="Renard hydraulique" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FON" name="Fontis" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CHS" name="Canalisation HS" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FOS" name="Fossé en pied de digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CAT" name="Canalisation traversante" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CAL" name="Canalisation londitudinale" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SOU" name="Souches" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="TER" name="Terrier d animaux fouisseurs" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="VED" name="Végétation dangereuse" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DEP" name="Dépression hors digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PZO" name="Tête de piezomètre" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DSA" name="Dépôt sauvage" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PAS" name="Passage d'engins a moteur" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="VAN" name="Vandalisme sur voirie" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BMQ" name="Borne manquante" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BDT" name="Borne déteriorée" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CLO" name="Clôture sauvage" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BAT" name="Batiment encastré dans la digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="LAB" name="Labour" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="REM" name="Remblai non autorisé contre digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="VEG" name="Végétation gênante" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MUR" name="Mur de soutenement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="CEB" name="Crête bombée" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PTB" name="Point bas" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ALT" name="Altération (pierre,béton,corrosion)" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DEC" name="Mauvais contact entre deux éléments" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DEJ" name="Déjointement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="DES" name="Déstructuration ouvrage" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PRV" name="Prélèvement de matériau de digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="FIS" name="Fissure (terrain, structure rigide)" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="COR" name="Corps étranger dangereux" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="MVT" name="Glissement, affaissement, tassement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="VID" name="Vide important (enrochement, maçonné)" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="NID" name="Nid de poule" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ESC" name="Escalier maçonné dans la digue" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BRD" name="Brèche par Renard Direct" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BRR" name="Brèche par Renard en Retour" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BSD" name="Brèche par Surverse Directe" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="SUR" name="Brèche par SUrverse par Retour" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BRE" name="Brèche par cause indeterminee" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BPR" name="Brèche provoquee" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="BAF" name="Brèche par affouillement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="ELS" name="En limite de surverse" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="INR" name="Inondation par refoulement" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="IND" name="Indéfini" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="deficiencysubsubtype">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option name="map" type="List">
              <Option type="Map">
                <Option value="" name="/" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="AAP" name="Aciers apparents" type="QString"/>
              </Option>
              <Option type="Map">
                <Option value="PPE" name="Palplanche percée" type="QString"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="lid_delivery">
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
    <alias name="" index="0" field="pk_deficiency"/>
    <alias name="" index="1" field="id_deficiency"/>
    <alias name="" index="2" field="lpk_object"/>
    <alias name="" index="3" field="deficiencycategory"/>
    <alias name="" index="4" field="impact"/>
    <alias name="" index="5" field="priority"/>
    <alias name="" index="6" field="risks"/>
    <alias name="" index="7" field="sector1"/>
    <alias name="" index="8" field="sector2"/>
    <alias name="" index="9" field="sector3"/>
    <alias name="" index="10" field="lid_descriptionsystem"/>
    <alias name="" index="11" field="side"/>
    <alias name="" index="12" field="position"/>
    <alias name="" index="13" field="deficiencytype"/>
    <alias name="" index="14" field="deficiencysubtype"/>
    <alias name="" index="15" field="deficiencysubsubtype"/>
    <alias name="" index="16" field="lid_delivery"/>
    <alias name="" index="17" field="pk_object"/>
    <alias name="" index="18" field="id_object"/>
    <alias name="" index="19" field="lpk_revision_begin"/>
    <alias name="" index="20" field="lpk_revision_end"/>
    <alias name="" index="21" field="datetimecreation"/>
    <alias name="" index="22" field="datetimemodification"/>
    <alias name="" index="23" field="datetimedestruction"/>
    <alias name="" index="24" field="comment"/>
    <alias name="" index="25" field="name"/>
    <alias name="" index="26" field="importid"/>
    <alias name="" index="27" field="importtable"/>
    <alias name="" index="28" field="lid_actor_creator"/>
    <alias name="" index="29" field="sirsid"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="pk_deficiency" expression="" applyOnUpdate="0"/>
    <default field="id_deficiency" expression="" applyOnUpdate="0"/>
    <default field="lpk_object" expression="" applyOnUpdate="0"/>
    <default field="deficiencycategory" expression="" applyOnUpdate="0"/>
    <default field="impact" expression="" applyOnUpdate="0"/>
    <default field="priority" expression="" applyOnUpdate="0"/>
    <default field="risks" expression="" applyOnUpdate="0"/>
    <default field="sector1" expression="" applyOnUpdate="0"/>
    <default field="sector2" expression="" applyOnUpdate="0"/>
    <default field="sector3" expression="" applyOnUpdate="0"/>
    <default field="lid_descriptionsystem" expression="" applyOnUpdate="0"/>
    <default field="side" expression="" applyOnUpdate="0"/>
    <default field="position" expression="" applyOnUpdate="0"/>
    <default field="deficiencytype" expression="" applyOnUpdate="0"/>
    <default field="deficiencysubtype" expression="" applyOnUpdate="0"/>
    <default field="deficiencysubsubtype" expression="" applyOnUpdate="0"/>
    <default field="lid_delivery" expression="" applyOnUpdate="0"/>
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
    <default field="lid_actor_creator" expression="" applyOnUpdate="0"/>
    <default field="sirsid" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" field="pk_deficiency" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="id_deficiency" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="lpk_object" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="deficiencycategory" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="impact" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="priority" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="risks" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="sector1" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="sector2" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="sector3" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="lid_descriptionsystem" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="side" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="position" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="deficiencytype" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="deficiencysubtype" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="deficiencysubsubtype" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="lid_delivery" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="pk_object" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="id_object" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="lpk_revision_begin" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="lpk_revision_end" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="datetimecreation" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="datetimemodification" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="datetimedestruction" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="comment" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="name" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="importid" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="importtable" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="lid_actor_creator" constraints="0" unique_strength="0" exp_strength="0"/>
    <constraint notnull_strength="0" field="sirsid" constraints="0" unique_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="pk_deficiency" exp=""/>
    <constraint desc="" field="id_deficiency" exp=""/>
    <constraint desc="" field="lpk_object" exp=""/>
    <constraint desc="" field="deficiencycategory" exp=""/>
    <constraint desc="" field="impact" exp=""/>
    <constraint desc="" field="priority" exp=""/>
    <constraint desc="" field="risks" exp=""/>
    <constraint desc="" field="sector1" exp=""/>
    <constraint desc="" field="sector2" exp=""/>
    <constraint desc="" field="sector3" exp=""/>
    <constraint desc="" field="lid_descriptionsystem" exp=""/>
    <constraint desc="" field="side" exp=""/>
    <constraint desc="" field="position" exp=""/>
    <constraint desc="" field="deficiencytype" exp=""/>
    <constraint desc="" field="deficiencysubtype" exp=""/>
    <constraint desc="" field="deficiencysubsubtype" exp=""/>
    <constraint desc="" field="lid_delivery" exp=""/>
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
    <constraint desc="" field="sirsid" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" type="actions" hidden="1"/>
      <column name="position" width="-1" type="field" hidden="0"/>
      <column name="impact" width="-1" type="field" hidden="0"/>
      <column name="lid_descriptionsystem" width="-1" type="field" hidden="0"/>
      <column name="lpk_revision_begin" width="-1" type="field" hidden="0"/>
      <column name="lpk_revision_end" width="-1" type="field" hidden="0"/>
      <column name="datetimecreation" width="-1" type="field" hidden="0"/>
      <column name="datetimemodification" width="-1" type="field" hidden="0"/>
      <column name="datetimedestruction" width="-1" type="field" hidden="0"/>
      <column name="importid" width="-1" type="field" hidden="0"/>
      <column name="importtable" width="-1" type="field" hidden="0"/>
      <column name="pk_deficiency" width="-1" type="field" hidden="0"/>
      <column name="id_deficiency" width="-1" type="field" hidden="0"/>
      <column name="lpk_object" width="-1" type="field" hidden="0"/>
      <column name="deficiencycategory" width="-1" type="field" hidden="0"/>
      <column name="priority" width="-1" type="field" hidden="0"/>
      <column name="risks" width="-1" type="field" hidden="0"/>
      <column name="sector1" width="-1" type="field" hidden="0"/>
      <column name="sector2" width="-1" type="field" hidden="0"/>
      <column name="sector3" width="-1" type="field" hidden="0"/>
      <column name="side" width="-1" type="field" hidden="0"/>
      <column name="deficiencytype" width="-1" type="field" hidden="0"/>
      <column name="deficiencysubtype" width="-1" type="field" hidden="0"/>
      <column name="deficiencysubsubtype" width="-1" type="field" hidden="0"/>
      <column name="lid_delivery" width="-1" type="field" hidden="0"/>
      <column name="pk_object" width="-1" type="field" hidden="0"/>
      <column name="id_object" width="-1" type="field" hidden="0"/>
      <column name="comment" width="-1" type="field" hidden="0"/>
      <column name="name" width="-1" type="field" hidden="0"/>
      <column name="lid_actor_creator" width="-1" type="field" hidden="0"/>
      <column name="sirsid" width="-1" type="field" hidden="0"/>
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
    <field name="comment" editable="1"/>
    <field name="datetimecreation" editable="1"/>
    <field name="datetimedestruction" editable="1"/>
    <field name="datetimemodification" editable="1"/>
    <field name="deficiencycategory" editable="1"/>
    <field name="deficiencysubsubtype" editable="1"/>
    <field name="deficiencysubtype" editable="1"/>
    <field name="deficiencytype" editable="1"/>
    <field name="id_deficiency" editable="1"/>
    <field name="id_object" editable="1"/>
    <field name="impact" editable="1"/>
    <field name="importid" editable="1"/>
    <field name="importtable" editable="1"/>
    <field name="lid_actor_creator" editable="1"/>
    <field name="lid_delivery" editable="1"/>
    <field name="lid_descriptionsystem" editable="1"/>
    <field name="lpk_object" editable="1"/>
    <field name="lpk_revision_begin" editable="1"/>
    <field name="lpk_revision_end" editable="1"/>
    <field name="name" editable="1"/>
    <field name="pk_deficiency" editable="1"/>
    <field name="pk_object" editable="1"/>
    <field name="position" editable="1"/>
    <field name="priority" editable="1"/>
    <field name="risks" editable="1"/>
    <field name="sector1" editable="1"/>
    <field name="sector2" editable="1"/>
    <field name="sector3" editable="1"/>
    <field name="side" editable="1"/>
    <field name="sirsid" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="comment" labelOnTop="0"/>
    <field name="datetimecreation" labelOnTop="0"/>
    <field name="datetimedestruction" labelOnTop="0"/>
    <field name="datetimemodification" labelOnTop="0"/>
    <field name="deficiencycategory" labelOnTop="0"/>
    <field name="deficiencysubsubtype" labelOnTop="0"/>
    <field name="deficiencysubtype" labelOnTop="0"/>
    <field name="deficiencytype" labelOnTop="0"/>
    <field name="id_deficiency" labelOnTop="0"/>
    <field name="id_object" labelOnTop="0"/>
    <field name="impact" labelOnTop="0"/>
    <field name="importid" labelOnTop="0"/>
    <field name="importtable" labelOnTop="0"/>
    <field name="lid_actor_creator" labelOnTop="0"/>
    <field name="lid_delivery" labelOnTop="0"/>
    <field name="lid_descriptionsystem" labelOnTop="0"/>
    <field name="lpk_object" labelOnTop="0"/>
    <field name="lpk_revision_begin" labelOnTop="0"/>
    <field name="lpk_revision_end" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="pk_deficiency" labelOnTop="0"/>
    <field name="pk_object" labelOnTop="0"/>
    <field name="position" labelOnTop="0"/>
    <field name="priority" labelOnTop="0"/>
    <field name="risks" labelOnTop="0"/>
    <field name="sector1" labelOnTop="0"/>
    <field name="sector2" labelOnTop="0"/>
    <field name="sector3" labelOnTop="0"/>
    <field name="side" labelOnTop="0"/>
    <field name="sirsid" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>COALESCE("ID", '&lt;NULL>')</previewExpression>
  <mapTip>ID</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
