// import EditingFormReact from '../editingformwidget'
const EditingFormReact = require('../editingformwidget')
const MediaEditingFormReact = require('./mediawidget')
const DeficiencyEditingFormReact = require('./deficiencywidget')
//

class NodeEditingFormReact extends EditingFormReact {

    static firstdir = 'Assets'
    static label = 'Nodes'
    table = 'node'

    childwdg = [
        MediaEditingFormReact,
        DeficiencyEditingFormReact
    ]

    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': ':/static/forms/base3_urbandrainage/qgswidgets/lamia_form_node_ui.ui',
            ...this.state
        }
        // this.props = { childwdg: [MediaEditingFormReact], ...this.props }
    }



}

module.exports = NodeEditingFormReact;