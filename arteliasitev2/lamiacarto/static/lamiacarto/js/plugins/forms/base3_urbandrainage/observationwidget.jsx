// import EditingFormReact from '../editingformwidget'
const EditingFormReact = require('../editingformwidget')
//

class ObservationEditingFormReact extends EditingFormReact {

    static firstdir = 'State'
    static label = 'Observations'
    table = 'observation'


    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': ':/static/forms/base3_urbandrainage/qgswidgets/lamia_form_observation_ui.ui',
            ...this.state
        }

        this.PARENTJOIN = {
            "deficiency": {
                "colparent": "id_deficiency",
                "colthistable": "lid_deficiency",
                "tctable": null,
                "tctablecolparent": null,
                "tctablecolthistable": null,
            }
        }

        this.CHOOSERTREEWDGSPEC = {
            "colshow": ["datetimeobservation"],
            "sort": ["datetimeobservation", "DESC"],
        }




    }



}

module.exports = ObservationEditingFormReact;