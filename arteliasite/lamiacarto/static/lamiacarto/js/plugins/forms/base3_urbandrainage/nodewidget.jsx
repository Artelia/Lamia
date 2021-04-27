// import EditingFormReact from '../editingformwidget'
const EditingFormReact = require('../editingformwidget')
const MediaEditingFormReact = require('./mediawidget')
const DeficiencyEditingFormReact = require('./deficiencywidget')
const { collectGroupLayers } = require('qwc2/utils/LayerUtils')
const { timers } = require('jquery')
//

class NodeEditingFormReact extends EditingFormReact {

    static firstdir = 'Assets'
    static label = 'Nodes'
    table = 'node'

    childwdg = [
        MediaEditingFormReact,
        DeficiencyEditingFormReact
    ]

    combostacked = {
        'nodetype': {
            'val': null,
            'stackedname': 'stackedWidget_obs',
            idx: [['60', '62'], ['61'], ['10'], ['21'], ['70', '72', '71']],
        }
    }

    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': ':/forms/base3_urbandrainage/qgswidgets/lamia_form_node_ui.ui',
            ...this.state
        }
        this.childwdg[1].SKIPUI = true
        // this.props = { childwdg: [MediaEditingFormReact], ...this.props }


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
        for (const key of Object.keys(this.combostacked)) {
            $('select[name="' + key + '"]').change(this.buttonClicked)
        }

    }



    buttonClicked = (e) => {
        this.combostacked[e.target.name].val = e.target.options[e.target.selectedIndex].value
    }

    updateStacked = (() => {
        for (const [key, value] of Object.entries(this.combostacked)) {
            let combo = $('select[name="' + key + '"]')
            if (!combo.length) { continue }
            let comboval = 0
            if (this.combostacked[key].val) {
                comboval = this.combostacked[key].val
                this.combostacked[key].val = null
            } else {
                comboval = combo[0].options[combo[0].selectedIndex].value
            }
            let stackedname = this.combostacked[key].stackedname
            let done = false
            for (const [idx, stackedidx] of this.combostacked[key].idx.entries()) {
                if (stackedidx.includes(comboval)) {
                    this.setStackedCurrentIndex(stackedname, idx)
                    done = true
                    break
                }
            }
            if (!done) {
                this.setStackedCurrentIndex(stackedname, this.combostacked[key].idx.length)
            }
        }
    })



    componentDidUpdate() {
        super.componentDidUpdate()
        this.updateStacked()
    }



    //

}

module.exports = NodeEditingFormReact;