// import EditingFormReact from '../editingformwidget'
// const EditingFormReact = require('../editingformwidget')
const EditingFormReact = require('../editingformwidget')
//

class EdgeEditingFormReact extends EditingFormReact {

    static firstdir = 'Assets'
    static label = 'Edges'
    table = 'edge'

    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': ':/static/forms/base3_urbandrainage/qgswidgets/lamia_form_edge_ui.ui',
            ...this.state
        }

    }


    domLoaded() {
        console.log('okok edge')
        console.log('***', $('[name="networktype"]'))

        let comb = $('select[name="networktype"]')

        comb.append($('<option>', {
            value: 1,
            text: 'My option'
        }));

    }


}

module.exports = EdgeEditingFormReact;