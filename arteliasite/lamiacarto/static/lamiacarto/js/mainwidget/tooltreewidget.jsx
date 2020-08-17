import React from 'react';
// import TreeView from 'react-simple-jstree';

// import TreeView from '@material-ui/lab/TreeView';
// import TreeItem from '@material-ui/lab/TreeItem';
// import { makeStyles } from '@material-ui/core/styles';
// import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
// import ChevronRightIcon from '@material-ui/icons/ChevronRight';

// import Tree from '@naisutech/react-tree'
import TreeMenu from 'react-simple-tree-menu';
// import '../../node_modules/react-simple-tree-menu/dist/main.css';
import 'react-simple-tree-menu/dist/main.css'

// import EdgeEditingFormReact from './edgewidget'
import EdgeEditingFormReact from './forms/base3_urbandrainage/edgewidget'
import NodeEditingFormReact from './forms/base3_urbandrainage/nodewidget'
import MediaEditingFormReact from './forms/base3_urbandrainage/mediawidget'
import OLCanvasReact from '../canvas/openlayers'


import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class ToolTreeWidgetReact extends React.Component {

  workclasses = [
    EdgeEditingFormReact,
    NodeEditingFormReact,
    MediaEditingFormReact
  ]

  olcanvas = new OLCanvasReact()

  projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

  constructor(props) {
    super(props);
    this.state = { 'visualmode': 1, 'currentwdg': null }

  }

  render() {

    let dropdown = this.createToolbar.bind(this)()

    return (

      < div className="row " >
        <div className="row">
          <div className="col-md-12 mb-4">

            <div className="btn-toolbar " role="group" aria-label="Basic example">
              <div className="btn-group mr-2" role="group" aria-label="First group">
                <div className="dropdown">
                  <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Layers
                </button>
                  <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    {dropdown}
                  </div>
                </div>
              </div>
              <div className="btn-group mr-2" role="group" aria-label="First group">

                <button type="button" className="btn btn-secondary" id="canvaspick" onClick={this.onclick}>Pick</button>
                <button type="button" className="btn btn-secondary" onClick={this.onclick}>Middle</button>
                <button type="button" className="btn btn-secondary" onClick={this.onclick}>Right</button>
              </div>
            </div>

          </div>
        </div>
        < div className="row " style={{ height: '100%' }}>
          {(this.state.currentwdg === null) ? < div></div> : <this.state.currentwdg />}
        </div>
      </div>

    )
  }

  createToolbar() {

    let dataraw = {}

    this.workclasses.forEach(function (reactclass, idx) {
      if (!dataraw.hasOwnProperty(reactclass.firstdir)) {
        dataraw[reactclass.firstdir] = {}
      }
      dataraw[reactclass.firstdir][reactclass.label] = reactclass
    });



    let finaldatas = []

    for (var firstdir in dataraw) {
      finaldatas.push(<h6 className="dropdown-header">{firstdir}</h6>)
      for (var seconddir in dataraw[firstdir]) {
        finaldatas.push(<a className="dropdown-item" id={dataraw[firstdir][seconddir].label} onClick={this.handleClick.bind(this)}>{seconddir}</a>)
      }
    };

    return finaldatas
  }

  handleClick(evt) {

    let goodclass = null
    this.workclasses.forEach(function (reactclass, idx) {
      if (reactclass.label === evt.target.id) {
        goodclass = reactclass
      }
    });
    this.setState({ currentwdg: goodclass })

  }


  onclick = (e) => {
    let sourceid = event.target.id
    if (sourceid == 'canvaspick') {
      this.olcanvas.state.map.un('click', this.olcanvas.handleMapClick);
      let evtky = this.olcanvas.state.map.on('click', this.handleMapClick.bind(this));
    }

  }


  async handleMapClick(event) {
    let debug = true
    var clickedCoordinate = this.olcanvas.state.map.getCoordinateFromPixel(event.pixel);

    // ask nearest pk
    let res = await axios.post('http://localhost:8000/lamiafunc/' + this.projectdata.id_project.toString(), {
      func: 'nearest',
      layer: this.state.currentwdg.table,
      coords: clickedCoordinate,
    })
    let response = JSON.parse(res.data)

    // get feature from wfs3
    // ex : http://localhost:8380/qgisserver/wfs3/collections/Infralineaire_qgis/items/1.json
    let temp = this.olcanvas.state.qgisserverurl + 'qgisserver/wfs3/collections/' + this.state.currentwdg.table + '_qgis/items/' + response.nearestpk + '.json'
    let feat = await axios.get(temp)
    debug ? console.log('feat', feat) : null

    // add to sellayer
    let selsource = this.olcanvas.state.sellayer.getSource()
    selsource.clear()
    let jsonfeat = selsource.getFormat().readFeatures(feat.data)

    selsource.addFeatures(jsonfeat)
    selsource.getFeatures()[0].getGeometry().transform('EPSG:4326', 'EPSG:3857')

    this.olcanvas.state.sellayer.setSource(selsource)

    // update form
    this.setState({
      currentfeatprop: {},
    });
    let datas = feat.data.properties
    debug ? console.log('feat.data.properties', datas) : null

    this.setState({
      currentfeatprop: datas,
    });

  }





}

export default ToolTreeWidgetReact;
