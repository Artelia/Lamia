// import EditingFormReact from '../editingformwidget'
// const EditingFormReact = require('../editingformwidget')
const EditingFormReact = require('../editingformwidget')
const $ = require('jquery')
// import ReactDOM from "react-dom";
const ReactDOM = require('react-dom')
const url = require('url');

const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

// import fileDownload from 'js-file-download';
const fileDownload = require('js-file-download')



class ReportEditingFormReact extends EditingFormReact {

    static firstdir = 'Resources'
    static label = 'Reports'
    table = 'report'

    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

    constructor(props) {
        super(props);
        this.state = {
            'currentlayer': '',
            'currentfeatprop': {},
            'formui': ':/forms/base3/qgswidgets/lamia_form_report_ui.ui',
            ...this.state
        }

    }


    domLoaded() {
        $('button[name="pushButton_openph"]').click(this.buttonClicked.bind(this))
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

module.exports = ReportEditingFormReact;