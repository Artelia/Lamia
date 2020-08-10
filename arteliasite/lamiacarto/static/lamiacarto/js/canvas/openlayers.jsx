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
import TileWMS from 'ol/source/TileWMS'
import Vector from 'ol/layer/Vector'
import OSM from 'ol/source/OSM'
// import Select from 'ol/interaction/Select';
// import {click, pointerMove, altKeyOnly} from 'ol/events/condition';
// import {defaults as defaultInteractions, DragRotateAndZoom} from 'ol/interaction';
import { defaults as defaultControls } from 'ol/control';
import ScaleLine from 'ol/control/ScaleLine';
// import Draw from 'ol/control/Draw';
import $ from 'jquery';


// import DbaseCommunication from '../dbase/dbasecommunicate'
// https://taylor.callsen.me/using-reactflux-with-openlayers-3-and-other-third-party-libraries/

class OLCanvasReact extends React.Component {

  static workclasses = {
    'infralineaire': 'InfralineaireWdg',
    'photo': 'PhotoWdg',
    'equipement': 'EquipementWdg',
  }

  constructor(props) {
    super(props);
    this.mainiface = this.props.mainiface
    // this.dbase = new DbaseCommunication()
  }



  componentDidMount() {
    console.log('DidMount ', this.constructor.name, this.props.qgisserverurl)

    // create feature layer and vector source
    // var qgislayer = new Vector({
    //   source: new VectorSource({
    //     features: []
    //   })
    // });

    var qgislayer = new TileLayer();

    // console.log(this.mainiface.mainwidgetdom.type.toolwdgclass.workclasses)
    // console.log(OLCanvasReact.workclasses)
    // let layers = []
    // // let workclasses = this.mainiface.mainwidgetdom.type.toolwdgclass.workclasses
    // Object.keys(OLCanvasReact.workclasses).forEach((tablename) => layers.push(tablename.charAt(0).toUpperCase()
    //   + tablename.substr(1).toLowerCase()
    //   + '_qgis')
    // )
    // console.log(layers)
    // console.log('**', this.props.qgisserverurl)
    // if ([null, false].includes(this.props.qgisserverurl)) {
    //   console.log('not inc')
    // } else {
    //   console.log('okok')
    // }
    // var qgislayer = new TileLayer({
    //   // extent: [-13884991, 2870341, -7455066, 6338219],
    //   source: new TileWMS({
    //     url: 'http://localhost:8380/',
    //     params: {
    //       'LAYERS': layers,
    //       'TRANSPARENT': true,
    //     },
    //     serverType: 'qgis'
    //   })
    // });


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
      ],
      controls: defaultControls({
        zoom: true,
        attribution: true,
        rotate: false
      })
        .extend([
          new ScaleLine()
        ])
      // .extend([
      //   new Draw({
      //     source: source,
      //     type: 'Point'
      //   })
      // ])
      ,
      view: new View({
        center: [-61015.32359086573, 5594194.573559809], //Boulder
        zoom: 15,
        // interactions: defaultInteractions(),
      })
    });
    // let scaleline = new ScaleLine()
    // map.addInteraction(scaleline);

    // map.on('click', this.handleMapClick.bind(this));

    // var updateLegend = function (resolution) {
    //   var graphicUrl = qgislayer.getSource().getLegendUrl(resolution);
    //   console.log('rr', graphicUrl)
    //   // var img = $('#legend')
    //   // img.src = graphicUrl;
    // };

    // // Initial legend
    // var resolution = map.getView().getResolution();
    // updateLegend(resolution);

    // map.getView().on('change:resolution', function (event) {
    //   var resolution = event.target.getResolution();
    //   updateLegend(resolution);
    // });
    map.on('singleclick', function (evt) {
      console.log(evt.coordinate);
    });

    // var selectClick = new Select({
    //   condition: click
    // });
    // map.addInteraction(selectClick);
    // selectClick.on('select', this.handleMapClick(e));

    // save map and layer references to local state
    this.setState({
      map: map,
      // featuresLayer: featuresLayer,
      qgislayer: qgislayer,
    });

  }

  shouldComponentUpdate_(nextProps, nextState) {
    console.log('shouldComponentUpdate ', this.constructor.name, this.props.qgisserverurl)

    console.log('**', this.props.qgisserverurl)
    if ([null, false].includes(this.props.qgisserverurl)) {
      console.log('not inc')
    } else {
      console.log('okok')
    }
    let layers = []
    // let workclasses = this.mainiface.mainwidgetdom.type.toolwdgclass.workclasses
    Object.keys(OLCanvasReact.workclasses).forEach((tablename) => layers.push(tablename.charAt(0).toUpperCase()
      + tablename.substr(1).toLowerCase()
      + '_qgis')
    )
    var qgislayer = new TileLayer({
      // extent: [-13884991, 2870341, -7455066, 6338219],
      source: new TileWMS({
        url: 'http://localhost:8380/',
        params: {
          'LAYERS': layers,
          'TRANSPARENT': true,
        },
        serverType: 'qgis'
      })
    });

    this.setState({ qgislayer: qgislayer })


  }

  // pass new features from props into the OpenLayers layer object
  componentDidUpdate(prevProps, prevState) {
    console.log('DidUpdate ', this.constructor.name, this.props.qgisserverurl)




    // this.state.featuresLayer.setSource(
    //   new VectorSource({
    //     features: this.props.routes
    //   })
    // );
  }

  componentWillReceiveProps(nextProps) {
    console.log('componentWillReceiveProps ', this.constructor.name, this.props.qgisserverurl, nextProps)

    console.log('**', nextProps.qgisserverurl)
    if ([null, false].includes(nextProps.qgisserverurl)) {
      console.log('not inc')
    } else {

      console.log('okok')

      let layers = []
      // let workclasses = this.mainiface.mainwidgetdom.type.toolwdgclass.workclasses
      Object.keys(OLCanvasReact.workclasses).forEach((tablename) => layers.push(tablename.charAt(0).toUpperCase()
        + tablename.substr(1).toLowerCase()
        + '_qgis')
      )
      var qgislayer = new TileLayer({
        // extent: [-13884991, 2870341, -7455066, 6338219],
        source: new TileWMS({
          url: nextProps.qgisserverurl,
          params: {
            'LAYERS': layers,
            'TRANSPARENT': true,
          },
          serverType: 'qgis'
        })
      });

      // this.setState({ qgislayer: qgislayer })

      this.state.qgislayer.setSource(
        new TileWMS({
          url: nextProps.qgisserverurl,
          params: {
            'LAYERS': layers,
            'TRANSPARENT': true,
          },
          serverType: 'qgis'
        })
      );

    }

  }

  render() {
    console.log('render ', this.constructor.name, this.props.qgisserverurl)

    // this.addQgsLayer()

    const debug = false;
    let mainol = <p></p>;
    if (debug) {
      mainol = <p style={{ backgroundColor: 'red' }} >{this.constructor.name}</p>
    }
    let qgisserverstate = null;
    if (this.props.qgisserverurl === null) {
      qgisserverstate = <p>Loading qgisserver ... </p>
    } else if (this.props.qgisserverurl === false) {
      qgisserverstate = <p>Qgisserver no found - contact admin </p>
    };

    return (

      < div ref="mapContainer" style={{ width: '100%', height: '100%', backgroundColor: 'transparent' }
      }>
        {qgisserverstate}
        {mainol}
      </div >
    );
  }
}


export default OLCanvasReact;