// import React from 'react';
const React = require('react');

// import QtDesignerForm from './QtDesignerForm'
const QtDesignerForm = require('./QtDesignerForm');
// const QtDesignerForm = require('qwc2/components/QtDesignerForm');
// import OLCanvasReact from './../../canvas/openlayers'
// import OLCanvasReact from '../../canvas/openlayers'
//
// const { clickOnMap } = require("qwc2/actions/map");



class EditingFormReact extends React.Component {
    // static olcanvas = new OLCanvasReact()

    table = null

    constructor(props) {
        super(props);
        // this.state = { 'currentlayer': '', 'currentfeatprop': {}, 'formui': ':/lamia_form_edge_ui.ui' }
        // https://www.freecodecamp.org/news/react-changing-state-of-child-component-from-parent-8ab547436271/
        this.currentform = React.createRef()
        // let olcanvas = new OLCanvasReact()
        // console.log('ol', olcanvas)
    }

    updateField = (key, value) => {


        let tempvar = this.state.currentfeatprop
        Object.assign(tempvar, { [key]: value })

        this.setState({ currentfeatprop: tempvar })

        console.log('updateField', key, value)
        console.log('updateField', this.state.currentfeatprop)
    }


    onclick__(e) {
        let sourceid = event.target.id
        if (sourceid == 'canvaspick') {
            console.log(this.olcanvas)
        }

    }

    domLoaded() {
        null
    }

    render() {

        let qtform = <QtDesignerForm domLoaded={this.domLoaded} ref={this.currentform}
            updateField={this.updateField} form={this.state.formui} values={this.state.currentfeatprop} />

        return (
            <div className="container" style={{ height: '100%' }}>

                {/* <div className="row">


                    <div className="col-md-12 mb-4">

                        <div className="btn-group" role="group" aria-label="Basic example">
                            <button type="button" className="btn btn-secondary" id="canvaspick" onClick={this.onclick}>Pick</button>
                            <button type="button" className="btn btn-secondary" onClick={this.onclick}>Middle</button>
                            <button type="button" className="btn btn-secondary" onClick={this.onclick}>Right</button>
                        </div>

                    </div>
                </div> */}
                {/* <div className="row" style={{ height: '100%' }}>
                    <QtDesignerForm updateField={this.updateField} form={this.state.formui} values={this.state.currentfeatprop} />
                </div> */}
                {/* <QtDesignerForm updateField={this.updateField} form={this.state.formui} values={this.state.currentfeatprop} /> */}
                {qtform}
            </div>

        )
    }
}



// export default EditingFormReact;
module.exports = EditingFormReact;
// module.exports = { EditingPlugin: EditingFormReact };

// module.exports = (iface) => {
//     return {
//         EditingPlugin: connect(state => ({
//             enabled: state.task ? state.task.id === 'Editing' : false,
//             theme: state.theme ? state.theme.current : null,
//             layers: state.layers ? state.layers.flat : [],
//             map: state.map || {},
//             iface: iface,
//             editing: state.editing || {},
//         })
//             //  ,{
//             //     clickOnMap: clickOnMap,
//             //     changeEditingState: changeEditingState,
//             //     setCurrentTaskBlocked: setCurrentTaskBlocked,
//             //     refreshLayer: refreshLayer,
//             //     changeLayerProperty: changeLayerProperty
//             // }
//         )(EditingFormReact)
//     }
// };