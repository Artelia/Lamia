// import EditingFormReact from '../editingformwidget'
const EditingFormReact = require('../editingformwidget')
//

class EdgeEditingFormReact extends EditingFormReact {

    static firstdir = 'Assets'
    static label = 'Edges'
    static table = 'edge'

    constructor(props) {
        super(props);
        this.state = { 'currentlayer': '', 'currentfeatprop': {}, 'formui': ':/static/forms/base3_urbandrainage/qgswidgets/lamia_form_edge_ui.ui' }
        // let olcanvas = new OLCanvasReact()
        // console.log('ol', olcanvas)
    }


    domLoaded() {
        console.log('okok edge')
        console.log('***', $('[name="comboBox_typeReseau"]'))

        let comb = $('select[name="comboBox_typeReseau"]')

        comb.append($('<option>', {
            value: 1,
            text: 'My option'
        }));

    }


}

// export default EdgeEditingFormReact;
module.exports = EdgeEditingFormReact;