import EditingFormReact from '../editingformwidget'
//

class NodeEditingFormReact extends EditingFormReact {

    static firstdir = 'Assets'
    static label = 'Nodes'
    static table = 'node'

    constructor(props) {
        super(props);
        this.state = { 'currentlayer': '', 'currentfeatprop': {}, 'formui': ':/static/forms/base3_urbandrainage/qgswidgets/lamia_form_node_ui.ui' }
        // let olcanvas = new OLCanvasReact()
        // console.log('ol', olcanvas)
    }



}

export default NodeEditingFormReact;