import React from 'react';
// import Map from "ol/map";
//open layers and styles
var ol = require('ol');
// require('ol/css/ol.css');
// import * as ol from 'ol';
import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
// import XYZ from 'ol/source/XYZ';
import VectorSource from 'ol/source/Vector'
import VectorLayer from 'ol/layer/Vector';
import TileWMS from 'ol/source/TileWMS'
import Vector from 'ol/layer/Vector'
import OSM from 'ol/source/OSM'
import { GeoJSON } from 'ol/format';
import { Circle as CircleStyle, Fill, Stroke, Style } from 'ol/style';
// import Select from 'ol/interaction/Select';
// import {click, pointerMove, altKeyOnly} from 'ol/events/condition';
// import {defaults as defaultInteractions, DragRotateAndZoom} from 'ol/interaction';
import { Draw, Modify, Snap } from 'ol/interaction';
import Select from 'ol/interaction/Select';
import { altKeyOnly, click, pointerMove } from 'ol/events/condition'
import { defaults as defaultControls, MousePosition } from 'ol/control';
import ScaleLine from 'ol/control/ScaleLine';
// import createStringXY from 'ol/coordinate';
// import Draw from 'ol/control/Draw';
import $ from 'jquery';
import MainIfaceReact from '../MainIface'

import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

// import DbaseCommunication from '../dbase/dbasecommunicate'
// https://taylor.callsen.me/using-reactflux-with-openlayers-3-and-other-third-party-libraries/



class OLCanvasReact extends React.Component {

  projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

  static workclasses = {
    'infralineaire': 'InfralineaireWdg',
    'photo': 'PhotoWdg',
    'equipement': 'EquipementWdg',
  }

  debug = false

  constructor(props) {
    // Singleton workflow
    if (OLCanvasReact.exists) {
      return OLCanvasReact.instance;
    }

    super(props);
    this.state = { 'qgisserverurl': null }

    OLCanvasReact.instance = this;
    OLCanvasReact.exists = true;
  }


  componentDidMount() {
    if (this.debug) {
      console.log('DidMount ', this.constructor.name, this.props.qgisserverurl)
    }

    // qgis tile layer
    var qgislayer = new TileLayer();

    // selection geojson layer
    var selsource = new VectorSource({
      format: new GeoJSON(),
      // projection: 'EPSG:4326' 
    });
    var sellayer = new VectorLayer({
      source: selsource,
      // projection: 'EPSG:4326',
      style: new Style({
        stroke: new Stroke({
          color: 'green',
          width: 6,
        }),
      }),
    });



    // create map object with feature layer
    var map = new Map({
      target: this.refs.mapContainer,
      layers: [
        //default OSM layer
        new TileLayer({
          source: new OSM()
        }),
        // featuresLayer,
        qgislayer,
        sellayer,
      ],
      controls: defaultControls({
        zoom: true,
        attribution: true,
        rotate: false
      })
        .extend([
          new ScaleLine()
        ])

      ,
      view: new View({
        projection: 'EPSG:3857',
        // center: [0, 0],
        // zoom: 2,
        center: [-61015.32359086573, 5594194.573559809], //Boulder
        zoom: 15,
        // projection: 'EPSG:2154',
        // interactions: defaultInteractions(),
      })
    });

    //* Interactions

    //* scaleline
    // let scaleline = new ScaleLine()
    // map.addInteraction(scaleline);

    map.on('click', this.handleMapClick.bind(this));
    // variante
    // map.on('singleclick', function (evt) {
    //   console.log(evt.coordinate);
    // });

    //* for modifying selection
    // var modify = new Modify({ source: selsource });
    // map.addInteraction(modify);

    //* for mouse position
    // var mouse_position = new MousePosition();
    // map.addControl(mouse_position);

    //* legend
    // var updateLegend = function (resolution) {
    //   var graphicUrl = qgislayer.getSource().getLegendUrl(resolution);
    //   console.log('rr', graphicUrl)
    // };
    // var resolution = map.getView().getResolution();
    // updateLegend(resolution);
    // map.getView().on('change:resolution', function (event) {
    //   var resolution = event.target.getResolution();
    //   updateLegend(resolution);
    // });


    // save map and layer references to local state
    this.setState({
      map: map,
      qgislayer: qgislayer,
      sellayer: sellayer,
    });
    // url = 

    this.loadMapAndLayers.bind(this)()

  }

  async loadMapAndLayers() {
    let success = false
    let qgisserverurl = this.projectdata.qgisserverurl

    try {
      const data = await axios.get(qgisserverurl);
      success = true;
    } catch (error) {
      success = false
      this.setState({ qgisserverurl: false })
    }

    if (success) {


      let collections = await axios.get(qgisserverurl + 'wfs3/collections.json?')

      // let workclasses = this.mainiface.mainwidgetdom.type.toolwdgclass.workclasses
      // Object.keys(OLCanvasReact.workclasses).forEach((tablename) => layers.push(tablename.charAt(0).toUpperCase()
      //   + tablename.substr(1).toLowerCase()
      //   + '_qgis')
      // )
      let layers = []
      collections.data.collections.forEach((coll) => coll.id != 'report_qgis' ? layers.push(coll.id) : null)

      let qgslayer = this.state.qgislayer
      qgslayer.setSource(
        new TileWMS({
          url: qgisserverurl,
          params: {
            'LAYERS': layers,
            'TRANSPARENT': true,
          },
          serverType: 'qgis'
        })
      );

      await axios.get('http://localhost:8000/lamiafunc/' + this.projectdata.id_project, {
        func: 'nearest',
      });

      this.setState({
        qgislayer: qgslayer,
        qgisserverurl: qgisserverurl

      });




    }

  }


  addInteractions() {
    draw = new Draw({
      source: this.state.selsource,
      type: typeSelect.value,
    });
    this.state.map.addInteraction(draw);
    snap = new Snap({ source: this.state.selsource });
    this.state.map.addInteraction(snap);
  }

  handleMapClick(event) {
    // create WKT writer
    // var wktWriter = new ol.format.WKT();

    // derive map coordinate (references map from Wrapper Component state)
    var clickedCoordinate = this.state.map.getCoordinateFromPixel(event.pixel);
    console.log('**', clickedCoordinate)

    return clickedCoordinate
  }


  render() {
    // console.log('render ', this.constructor.name, this.state)

    // loader
    let loader = (<div className="loader" ng-hide="data.length > 0"></div>)
    if (this.state.qgisserverurl === null) {
      loader = loader
    } else {
      loader = null
    }

    //message
    let qgisserverstate = null;
    if (this.state.qgisserverurl === null) {
      qgisserverstate = <p>Loading qgisserver ... </p>
    } else if (this.state.qgisserverurl === false) {
      qgisserverstate = <p>Qgisserver no found - contact admin </p>
    };

    return (

      < div ref="mapContainer" style={{ width: '100%', height: '100%', backgroundColor: 'transparent' }
      }>
        {qgisserverstate}
        {loader}
      </div >
    );
  }
}


export default OLCanvasReact;