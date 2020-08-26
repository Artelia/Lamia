// import EditingFormReact from '../editingformwidget'
// const EditingFormReact = require('../editingformwidget')
const EditingFormReact = require('../editingformwidget')
const $ = require('jquery')
// import ReactDOM from "react-dom";
const ReactDOM = require('react-dom')

const ObservationEditingFormReact = require('./observationwidget')


class DeficiencyEditingFormReact extends EditingFormReact {

    static firstdir = 'State'
    static label = 'Deficiency'
    table = 'deficiency'

    childwdg = [ObservationEditingFormReact]


    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': '',
            ...this.state
        }

    }


    domLoaded() {
    }


}

module.exports = DeficiencyEditingFormReact;