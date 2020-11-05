const EditingFormReact = require('../editingformwidget')
const $ = require('jquery')
const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"
const url = require('url');
//


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
            'formui': ':/forms/base3/qgswidgets/lamia_form_camera_ui.ui',
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

    shouldComponentUpdate() {
        if ($("#lamiamedia")) {
            $("#lamiamedia").remove();
        }
        return true
    }


    render() {
        let res = super.render()
        return res
    }

    componentDidUpdate() {
        this.updateImageFromAWS()
    }

    domLoaded() {
        $('button[name="pushButton_openph"]').click(this.buttonClicked.bind(this))
    }


    async updateImageFromThumbnail() {
        let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project
        let res = await axios.post(url, {
            function: 'thumbnail',
            pkresource: this.state.currentfeatprop.pk_resource,
        })
        let imgsrc = 'data:image/png;base64,' + res.data.base64thumbnail;
        $('div[name="frame_ph"]').prepend($('<img>', { id: 'lamiamedia', src: imgsrc, width: 200 }))

    }

    async updateImageFromAWS() {
        let filename = $('input[name="file"]').val()
        let url = ("http://" + window.location.host + '/media/'
            + this.projectdata.pgdbname + '/' + this.projectdata.pgschema + '/'
            + filename)
        $('div[name="frame_ph"]').prepend($('<img>', { id: 'lamiamedia', src: url, width: 200 }))

    }

    async buttonClicked() {
        const destfilename = $('input[name="file"]').val()
        let baseurl = ("http://" + window.location.host + '/media/'
            + this.props.mainiface.projectdata.pgdbname + '/' + this.props.mainiface.projectdata.pgschema + '/')
        let urljoined = url.resolve(baseurl, destfilename);
        let awsreporturl = await axios.post(urljoined)
        window.open(awsreporturl.data)

    }

}

module.exports = MediaEditingFormReact;