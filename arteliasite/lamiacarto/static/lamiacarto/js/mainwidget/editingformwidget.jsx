import React from 'react';
import QtDesignerForm from './testqwc2/QtDesignerForm'
import OLCanvasReact from '../canvas/openlayers'

import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"


class EditingFormReact extends React.Component {
    static olcanvas = new OLCanvasReact()
    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

    constructor(props) {
        super(props);
        this.state = { 'currentlayer': '', 'currentfeatprop': {} }
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

        // derive map coordinate (references map from Wrapper Component state)
        var clickedCoordinate = EditingFormReact.olcanvas.state.map.getCoordinateFromPixel(event.pixel);
        console.log('*', clickedCoordinate)

        axios.post('http://localhost:8000/lamiafunc/' + this.projectdata.id_project.toString(), {
            func: 'nearest',
            layer: 'Infralineaire',
            coords: clickedCoordinate,
        }).then(function (reponse) {
            console.log('***', reponse);
            let pk = reponse.nearestpk
            let feat = EditingFormReact.olcanvas.state.qgislayer.getSource().getFeatureById(pk)
            console.log(feat)
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
                    <QtDesignerForm updateField={this.updateField} form={':/form.ui'} values={this.state.currentfeatprop} />
                </div>
            </div>

        )
    }
}



export default EditingFormReact;