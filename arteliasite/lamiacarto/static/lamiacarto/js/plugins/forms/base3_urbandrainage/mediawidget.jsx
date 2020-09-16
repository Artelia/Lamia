const EditingFormReact = require('../editingformwidget')
const $ = require('jquery')
const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"
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


    render() {
        let res = super.render()
        return res

    }

    componentDidUpdate() {
        $("#lamiamedia").remove();
        this.updateImage()
    }


    async updateImage() {
        $("#lamiamedia").remove();
        // console.log(this.state.currentfeatprop)
        // console.log('updateImage', this.state.currentfeatprop.thumbnail)
        // if ((this.state.currentfeatprop.thumbnail) && (this.state.currentfeatprop.thumbnail !== undefined)) {
        //     console.log(btoa(unescape(encodeURIComponent(this.state.currentfeatprop.thumbnail))))
        //     let imgsrc = 'data:image/png;base64,' + btoa(unescape(encodeURIComponent(this.state.currentfeatprop.thumbnail)));
        //     // let imgsrc = 'data:image/png;base64,' + this.state.currentfeatprop.thumbnail;
        //     $('div[name="frame_ph"]').prepend($('<img>', { id: 'lamiamedia', src: imgsrc, width: 200 }))
        // }

        // if ((this.state.currentfeatprop.file) && (this.state.currentfeatprop.file !== undefined)) {
        //     let url = ("http://" + window.location.host + '/media/'
        //         + this.projectdata.pgdbname + '/' + this.projectdata.pgschema + '/'
        //         + this.state.currentfeatprop.file)
        //     $("#lamiamedia").remove();
        //     $('div[name="frame_ph"]').prepend($('<img>', { id: 'lamiamedia', src: url, width: 200 }))
        // } else {
        //     $("#lamiamedia").remove();
        // }

        let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project
        let res = await axios.post(url, {
            function: 'thumbnail',
            pkresource: this.state.currentfeatprop.pk_resource,
        })
        // console.log(res.data.base64thumbnail)
        // let imgsrc = 'data:image/png;base64,' + btoa(unescape(encodeURIComponent(res)));
        let imgsrc = 'data:image/png;base64,' + res.data.base64thumbnail;
        $('div[name="frame_ph"]').prepend($('<img>', { id: 'lamiamedia', src: imgsrc, width: 200 }))


    }



}

module.exports = MediaEditingFormReact;