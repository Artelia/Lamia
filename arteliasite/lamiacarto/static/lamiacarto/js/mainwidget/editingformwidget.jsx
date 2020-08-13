import React from 'react';
import QtDesignerForm from './testqwc2/QtDesignerForm'
import OLCanvasReact from '../canvas/openlayers'

import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"


class EditingFormReact extends React.Component {
    static olcanvas = new OLCanvasReact()
    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))
    table = null

    constructor(props) {
        super(props);
        this.state = { 'currentlayer': '', 'currentfeatprop': {}, 'formui': ':/lamia_form_edge_ui.ui' }
        // let olcanvas = new OLCanvasReact()
        // console.log('ol', olcanvas)
    }

    updateField = (key, value) => {
        console.log('update2', key, value)

        let tempvar = this.state.currentfeatprop
        Object.assign(tempvar, { [key]: value })

        this.setState({ currentfeatprop: tempvar })
        console.log('setState', this.state.currentfeatprop)
    }

    onclick = (e) => {
        let sourceid = event.target.id
        if (sourceid == 'canvaspick') {
            console.log(EditingFormReact.olcanvas)
            // EditingFormReact.olcanvas.state.map.removeEventListener('click')
            // EditingFormReact.olcanvas.disconnectEventKey(EditingFormReact.olcanvas.olclickevtkey)
            EditingFormReact.olcanvas.state.map.un('click', EditingFormReact.olcanvas.handleMapClick);
            let evtky = EditingFormReact.olcanvas.state.map.on('click', this.handleMapClick.bind(this));
            // this.getres(EditingFormReact.olcanvas.handleMapClick)
            console.log(evtky)
        }

    }


    async handleMapClick(event) {
        // create WKT writer
        // var wktWriter = new ol.format.WKT();

        let debug = true

        // derive map coordinate (references map from Wrapper Component state)
        var clickedCoordinate = EditingFormReact.olcanvas.state.map.getCoordinateFromPixel(event.pixel);
        // console.log('*', clickedCoordinate)

        // ask nearest pk
        let res = await axios.post('http://localhost:8000/lamiafunc/' + this.projectdata.id_project.toString(), {
            func: 'nearest',
            layer: this.table,
            coords: clickedCoordinate,
        })
        // console.log(res)
        let response = JSON.parse(res.data)

        // get feature from wfs3
        // ex : http://localhost:8380/qgisserver/wfs3/collections/Infralineaire_qgis/items/1.json
        let temp = EditingFormReact.olcanvas.state.qgisserverurl + 'qgisserver/wfs3/collections/' + this.table + '_qgis/items/' + response.nearestpk + '.json'
        let feat = await axios.get(temp)
        debug ? console.log('feat', feat) : null

        // add to sellayer
        let selsource = EditingFormReact.olcanvas.state.sellayer.getSource()
        selsource.clear()
        let jsonfeat = selsource.getFormat().readFeatures(feat.data)

        selsource.addFeatures(jsonfeat)
        selsource.getFeatures()[0].getGeometry().transform('EPSG:4326', 'EPSG:3857')

        EditingFormReact.olcanvas.state.sellayer.setSource(selsource)

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

    onclick__(e) {
        let sourceid = event.target.id
        if (sourceid == 'canvaspick') {
            console.log(this.olcanvas)
        }

    }

    render() {

        return (
            <div className="container" style={{ height: '100%' }}>

                <div className="row">


                    <div className="col-md-12 mb-4">

                        <div className="btn-group" role="group" aria-label="Basic example">
                            <button type="button" className="btn btn-secondary" id="canvaspick" onClick={this.onclick}>Pick</button>
                            <button type="button" className="btn btn-secondary" onClick={this.onclick}>Middle</button>
                            <button type="button" className="btn btn-secondary" onClick={this.onclick}>Right</button>
                        </div>

                    </div>
                </div>
                <div className="row" style={{ height: '100%' }}>
                    <QtDesignerForm updateField={this.updateField} form={this.state.formui} values={this.state.currentfeatprop} />
                </div>
            </div>

        )
    }
}



export default EditingFormReact;