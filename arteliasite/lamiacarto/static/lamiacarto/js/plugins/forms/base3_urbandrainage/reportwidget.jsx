// import EditingFormReact from '../editingformwidget'
// const EditingFormReact = require('../editingformwidget')
const EditingFormReact = require('../editingformwidget')
const $ = require('jquery')
// import ReactDOM from "react-dom";
const ReactDOM = require('react-dom')

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
            'formui': ':/static/forms/base3/qgswidgets/lamia_form_report_ui.ui',
            ...this.state
        }

    }


    domLoaded() {
        console.log('okok report')

        // let comb = $('button[name="pushButton_openph"]')

        $('button[name="pushButton_openph"]').click(this.buttonClicked.bind(this))




    }

    buttonClicked() {
        console.log('lklk')
        console.log($('input[name="file"]'))
        console.log($('input[name="file"]').value)
        console.log($('input[name="file"]').val())

        // this.projectdata.id_project pgdbname pgschema
        console.log('***', this.projectdata)


        let url = ("http://" + window.location.host + '/media/'
            + this.projectdata.pgdbname + '/' + this.projectdata.pgschema + '/'
            + $('input[name="file"]').val())
        console.log(url)
        let filename = $('input[name="name"]').val() + '.' + $('input[name="file"]').val().split('.').pop()
        console.log(filename)
        // axios.request({ url, responseType: 'blob' })
        //     .then(({ data }) => {
        //         const downloadUrl = window.URL.createObjectURL(new Blob([data]));
        //         const link = document.createElement('a');
        //         link.href = downloadUrl;
        //         link.setAttribute('download', filename); //any other extension
        //         document.body.appendChild(link);
        //         link.click();
        //         link.remove();
        //     })

        axios.get(url, {
            responseType: 'blob',
        }).then(res => {
            fileDownload(res.data, filename);
        });

    }


}

module.exports = ReportEditingFormReact;