// import React from 'react';
const React = require('react');
const { connect } = require('react-redux');

// import QtDesignerForm from './QtDesignerForm'
// const QtDesignerForm = require('./QtDesignerForm');
const QtDesignerForm = require('qwc2/components/QtDesignerForm');
// import OLCanvasReact from './../../canvas/openlayers'
// import OLCanvasReact from '../../canvas/openlayers'
//
// const { clickOnMap } = require("qwc2/actions/map");
const VectorLayerUtils = require('qwc2/utils/VectorLayerUtils');

const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class EditingFormReact extends React.Component {

    table = null

    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

    constructor(props) {
        super(props);
        // https://www.freecodecamp.org/news/react-changing-state-of-child-component-from-parent-8ab547436271/
        this.currentform = React.createRef()
        this.state = { isloading: true }
    }

    componentDidMount() {
        this.getKeyvalues()
    }

    async getKeyvalues() {
        // keyvalues = { 'comboBox_typeReseau': [{ key: 'popo', value: 'tete' }] }

        let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/' + this.table
        let res = await axios.post(url, {
            function: 'dbasetables',
        })
        let dictfields = res.data
        let keyvalues = {}
        for (const [key, value] of Object.entries(dictfields)) {
            if (value.Cst) {
                keyvalues[key] = []
                for (const [keyb, valueb] of Object.entries(value.Cst)) {
                    keyvalues[key].push({ key: valueb[1], value: valueb[0] })
                }
            }
        }
        this.setState({ isloading: false, keyvalues: keyvalues })

    }


    domLoaded() {
        null
    }

    async componentWillReceiveProps(nextProps) {
        // triggered on click on map

        if (!nextProps.point.coordinate) {
            return
        }
        let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/' + this.table
        let res = await axios.post(url, {
            function: 'nearest',
            // layer: this.table,
            coords: nextProps.point.coordinate,
        })
        let response = JSON.parse(res.data)
        let temp = this.projectdata.qgisserverurl + 'qgisserver/wfs3/collections/' + this.table + '_qgis/items/' + response.nearestpk + '.json'
        let feat = await axios.get(temp)

        console.log(feat.data.properties)

        this.setState({ currentfeatprop: feat.data.properties })

        feat.data.geometry = VectorLayerUtils.reprojectGeometry(feat.data.geometry, 'EPSG:4326', 'EPSG:3857')
        let ollayer = this.props.layers.find(layer => layer.title === "Lamiasel")
        this.props.addLayerFeatures(ollayer, [feat.data], true);
    }



    updateField = (key, value) => {


        let tempvar = this.state.currentfeatprop
        Object.assign(tempvar, { [key]: value })

        this.setState({ currentfeatprop: tempvar })

        console.log('updateField', key, value)
        console.log('updateField', this.state.currentfeatprop)
    }



    domLoaded() {
        null
    }

    render() {

        if (this.state.isloading) {
            return (<p>Loading ... </p>)
        }

        let qtform = <QtDesignerForm domLoaded={this.domLoaded} ref={this.currentform}
            updateField={this.updateField} form={this.state.formui} values={this.state.currentfeatprop}
            keyvalues={this.state.keyvalues} domLoaded={this.domLoaded.bind(this)} />

        return (
            <div className="container" style={{ height: '100%' }}>
                {qtform}
            </div>

        )
    }
}

module.exports = EditingFormReact;
