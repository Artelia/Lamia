import EditingFormReact from './editingformwidget'

class EdgeEditingFormReact extends EditingFormReact {

    static firstdir = 'TOTO'
    static label = 'Edges'
    table = 'edge'

    constructor(props) {
        super(props);
        this.state = { 'currentlayer': '', 'currentfeatprop': {}, 'formui': ':/lamia_form_edge_ui.ui' }
        // let olcanvas = new OLCanvasReact()
        // console.log('ol', olcanvas)
    }

}

export default EdgeEditingFormReact;