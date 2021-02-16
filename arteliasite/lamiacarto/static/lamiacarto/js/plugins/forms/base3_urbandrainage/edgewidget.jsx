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
            'formui': ':/forms/base3_urbandrainage/qgswidgets/lamia_form_edge_ui.ui',
            ...this.state
        }

        this.PARENTJOIN = {
            "facility": {
                "colparent": "id_facility",
                "colthistable": "lid_facility",
                "tctable": null,
                "tctablecolparent": null,
                "tctablecolthistable": null,
            }
        }

    }


    domLoaded() {
        let comb = $('select[name="networktype"]')
        comb.append($('<option>', {
            value: 1,
            text: 'My option'
        }));

    }


}

module.exports = EdgeEditingFormReact;