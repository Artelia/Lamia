const EditingFormReact = require('../editingformwidget')
const $ = require('jquery')


class MediaEditingFormReact extends EditingFormReact {

    static firstdir = 'Resources'
    static label = 'Media'
    table = 'media'

    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))



    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': ':/static/forms/base3/qgswidgets/lamia_form_camera_ui.ui',
        }

        let tempparentjoin = {}
        let linkdict = {
            "colparent": "id_object",
            "colthistable": "id_resource",
            "tctable": "Tcobjectresource",
            "tctablecolparent": "lid_object",
            "tctablecolthistable": "lid_resource",
        }
        let tables = [
            "observation",
            "node",
            "edge",
            "surface",
            "equipment",
            "facility",
        ]
        tables.forEach((el) => {
            tempparentjoin[el] = linkdict
        })
        this.PARENTJOIN = tempparentjoin
        this.TABLEFILTERFIELD = { "typemedia": "PHO" }




    }


    render() {
        let res = super.render()
        return res

    }

    componentDidUpdate() {
        this.updateImage()
    }


    updateImage = () => {
        if (this.state.currentfeatprop.file) {
            let url = ("http://" + window.location.host + '/media/'
                + this.projectdata.pgdbname + '/' + this.projectdata.pgschema + '/'
                + this.state.currentfeatprop.file)
            $("#lamiamedia").remove();
            $('div[name="frame_ph"]').prepend($('<img>', { id: 'lamiamedia', src: url, width: 200 }))
        } else {
            $("#lamiamedia").remove();
        }
    }



}

module.exports = MediaEditingFormReact;