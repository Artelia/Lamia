const React = require('react');
const { connect } = require('react-redux');
// const QtDesignerForm = require('qwc2/components/QtDesignerForm');
const LamiaQtDesignerForm = require('./../qwc2/LamiaQtDesignerForm');
const VectorLayerUtils = require('qwc2/utils/VectorLayerUtils');

const Message = require('qwc2/components/I18N/Message');

const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"


class EditingFormReact extends React.Component {

    table = null
    childwdg = []
    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

    SKIPUI = false

    constructor(props) {
        super(props);
        // https://www.freecodecamp.org/news/react-changing-state-of-child-component-from-parent-8ab547436271/
        this.currentform = React.createRef()
        this.maintab = React.createRef()
        this.state = { isloading: true, ids: [] }
        this.childrefs = []
        this.ids = {}
        this.maintabref = React.createRef()

        this.PARENTJOIN = null
        this.TABLEFILTERFIELD = null


    }

    render() {
        let qtform = <LamiaQtDesignerForm domLoaded={this.domLoaded} ref={this.currentform}
            updateField={this.updateField} form={this.state.formui} values={this.state.currentfeatprop}
            getKeyvalues={this.getKeyvalues.bind(this)} domLoaded={this.domLoaded.bind(this)} />


        let childdom = []
        this.childwdg.forEach((childwd, idx) => {
            if (true) {
                childdom.push(<input value={idx + 1} type="radio" id={'maintab' + this.table + childwd.label} key={'maintab' + this.table + childwd.label + idx * 3} name={this.table} onChange={this.handleTabChange} />)
                childdom.push(<label htmlFor={'maintab' + this.table + childwd.label} key={'maintab' + this.table + childwd.label + idx * 3 + 1}><Message msgId={'qtdesigner.' + childwd.label} /></label>)
            }
            let Childwd = childwd
            childdom.push(
                <div className="qt-designer-tab" key={'maintab' + this.table + childwd.label + idx * 3 + 2}>
                    {<Childwd
                        ref={this.childrefs[idx]}
                        // setCurrentWidgetInstance={this.props.setCurrentWidgetInstance}
                        mainiface={this.props.mainiface}
                        parentwdg={this}
                        parentproperties={this.state.currentfeatprop} />}
                </div>
            )
        })


        return (
            <div className="qt-designer-tabs" ref={this.maintabref} name={this.table}>
                <input type="radio" value={0} id={'maintab' + this.table} name={this.table} defaultChecked={true} onChange={this.handleTabChange} />
                <label htmlFor={'maintab' + this.table}><Message msgId={'qtdesigner.Properties'} /></label>
                <div className="qt-designer-tab"  >
                    {qtform}
                </div>
                {childdom}

            </div>
        )
    }


    componentDidMount() {
        this.childrefs = []
        this.childwdg.forEach((childwd, idx) => {
            this.childrefs.push(React.createRef())
        })
        // this.getKeyvalues()
    }

    componentDidUpdate() {
        if (this.childrefs) {
            this.childrefs.forEach((childref, idx) => {
                childref.current.updateProperties()
            })
        }
    }


    others_________________________() { }


    async updateProperties() {
        if (this.props.parentproperties) {
            let parentpk = this.props.parentproperties['pk_' + this.props.parentwdg.table]

            if (!parentpk) { return }

            let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/' + this.table

            let res = await axios.post(url, {
                function: 'getids',
                parentjoin: this.PARENTJOIN,
                tablefilterfield: this.TABLEFILTERFIELD,
                choosertreewdgspec: this.CHOOSERTREEWDGSPEC,
                parenttablename: this.props.parentwdg.table,
                parentpk: parentpk,
            })

            this.ids = JSON.parse(res.data)


            if ((Object.entries(this.ids).length === 0) || (!this.ids.pk)) {
                this.setState({ currentfeatprop: {} })
                return
            } else {
                this.displayProperties(this.ids.pk[0])
            }

            if (this.props.mainiface.currentwdginstance === this) {
                this.props.mainiface.idchooserref.current.setState({ ids: this.ids })
            }


        }



    }

    async displayProperties(pk) {
        let featdata = {}
        if (pk !== undefined) {
            featdata = await this.getPropertiesFromPk(pk)
            featdata = featdata.properties
        }
        this.setState({ currentfeatprop: featdata })
    }

    async pointClicked(coords) {

        let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/' + this.table
        let res = await axios.post(url, {
            function: 'nearest',
            // layer: this.table,
            coords: coords,
        })
        let response = JSON.parse(res.data)

        // let temp = this.projectdata.qgisserverurl + 'qgisserver/wfs3/collections/' + this.table + '_qgis/items/' + response.nearestpk + '.json'
        // let feat = await axios.get(temp)
        let featdata = await this.getPropertiesFromPk(response.nearestpk)

        this.setState({ currentfeatprop: featdata.properties })



        featdata.geometry = VectorLayerUtils.reprojectGeometry(featdata.geometry, 'EPSG:4326', 'EPSG:3857')
        let ollayer = this.props.mainiface.props.layers.find(layer => layer.title === "Lamiasel")
        this.props.mainiface.props.addLayerFeatures(ollayer, [featdata], true);

    }

    async getPropertiesFromPk(pk) {

        // let qgisserverurl = this.projectdata.qgisserverurl.split('?')[0]
        // let qgisserverquery
        // this.projectdata.qgisserverurl.split('?').length > 1 ? qgisserverquery = this.projectdata.qgisserverurl.split('?')[1] : qgisserverquery = null
        // let databaseurl = qgisserverurl + '/wfs3/collections/' + this.table + '_qgis/items/' + pk + '.json'
        // qgisserverquery ? databaseurl = databaseurl + '?' + qgisserverquery : null

        let qgisserverurl = 'http://' + window.location.host
        let databaseurl = qgisserverurl + '/qgisserver/' + this.projectdata.id_project + '/wfs3/collections/' + this.table + '_qgis/items/' + pk + '.json'

        // let temp = this.projectdata.qgisserverurl + 'qgisserver/wfs3/collections/' + this.table + '_qgis/items/' + pk + '.json'
        let feat = await axios.get(databaseurl)
        return feat.data
    }

    updateField = (key, value) => {
        let tempvar = this.state.currentfeatprop
        Object.assign(tempvar, { [key]: value })
        this.setState({ currentfeatprop: tempvar })
    }

    domLoaded() {
        null
    }

    async getKeyvalues() {
        let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/' + this.table
        let res = await axios.post(url, {
            function: 'dbasetables',
            locale: (navigator ? navigator.language || navigator.browserLanguage : "en"),
        })
        let dictfields = res.data
        let keyvalues = {}
        for (const [key, value] of Object.entries(dictfields)) {
            if (value.Cst) {
                keyvalues[key] = []
                for (const [keyb, valueb] of Object.entries(value.Cst)) {
                    keyvalues[key].push({ key: valueb[1], value: valueb[0] })
                }
            }
        }
        return keyvalues
    }


    handleTabChange = (evt) => {
        let currentinstance = null
        if (evt.target.value == 0) {
            currentinstance = this
        } else { currentinstance = this.childrefs[evt.target.value - 1].current }

        this.props.mainiface.setCurrentWidgetInstance(currentinstance)

    }

    setStackedCurrentIndex = ((stackedname, stackedindex) => {
        let elm = $('div[name="' + stackedname + '"]')
        if (!elm.length) { return }
        elm[0].childNodes.forEach((node, idx) => {
            let toto = $(node)
            if (stackedindex === idx) {
                toto.css("display", 'block')
            } else {
                toto.css("display", 'none')
            }
        })
    })


}

module.exports = EditingFormReact;
