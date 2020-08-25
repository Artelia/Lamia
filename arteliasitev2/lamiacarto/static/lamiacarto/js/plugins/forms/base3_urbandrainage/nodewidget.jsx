// import EditingFormReact from '../editingformwidget'
const EditingFormReact = require('../editingformwidget')
//

class NodeEditingFormReact extends EditingFormReact {

    static firstdir = 'Assets'
    static label = 'Nodes'
    table = 'node'

    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': ':/static/forms/base3_urbandrainage/qgswidgets/lamia_form_node_ui.ui',
            ...this.state
        }
    }



}

module.exports = NodeEditingFormReact;