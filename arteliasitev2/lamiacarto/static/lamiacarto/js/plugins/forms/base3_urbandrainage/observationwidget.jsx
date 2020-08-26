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
        // this.props = { childwdg: [MediaEditingFormReact], ...this.props }
    }



}

module.exports = ObservationEditingFormReact;