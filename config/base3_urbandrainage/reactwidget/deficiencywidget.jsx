const EditingFormReact = require('lamiacarto/static/lamiacarto//editingformwidget/js/plugins/forms/editingformwidget')
const $ = require('jquery')
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


        let tempparentjoin = {}
        let linkdict = {
            "colparent": "id_descriptionsystem",
            "colthistable": "lid_descriptionsystem",
            "tctable": null,
            "tctablecolparent": null,
            "tctablecolthistable": null,
        }
        let tables = ["node", "edge", "equipment"]
        tables.forEach((el) => {
            tempparentjoin[el] = linkdict
        })
        this.PARENTJOIN = tempparentjoin


    }


    domLoaded() {
    }


}

module.exports = DeficiencyEditingFormReact;