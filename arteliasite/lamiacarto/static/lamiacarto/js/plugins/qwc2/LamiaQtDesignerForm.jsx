const QtDesignerForm = require('qwc2/components/QtDesignerForm');
const xml2js = require('xml2js');
const ConfigUtils = require('qwc2/utils/ConfigUtils');
const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class LamiaQtDesignerForm extends QtDesignerForm {

    componentDidMount() {
        let url = this.props.form;
        if (url && url.startsWith(":/")) {
            let assetsPath = ConfigUtils.getConfigProp("assetsPath");
            url = assetsPath + this.props.form.substr(1);
        }

        axios.get(url).then(response => {
            this.parseForm(response.data);
            this.props.domLoaded()
        }).catch(e => {
            console.log(e);
        });
    }

    parseForm = (data) => {
        let json;
        let options = {
            explicitArray: false,
            mergeAttrs: true
        };
        xml2js.parseString(data, options, (err, result) => {
            json = result;
        });
        let root = json.ui.widget;
        let keyvals = {};
        this.reformatWidget(root, keyvals);
        if (this.props.iface) {
            this.props.iface.getKeyValues(Object.values(keyvals).map(entry => this.props.mapPrefix + entry.table + ":" + entry.key + ":" + entry.value).join(","), (result) => {
                let keyvalues = Object.entries(keyvals).reduce((res, [key, val]) => assign(res, { [key]: result.keyvalues[this.props.mapPrefix + val.table] }), {});
                this.setState({ keyvalues });
            });
        }
        this.props.getKeyvalues().then(response => {
            this.setState({ keyvalues: response })
        })

        this.setState({ formdata: root });
    }


}

module.exports = LamiaQtDesignerForm;