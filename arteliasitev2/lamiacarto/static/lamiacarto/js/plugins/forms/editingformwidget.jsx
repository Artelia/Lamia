const React = require('react');
const { connect } = require('react-redux');
const QtDesignerForm = require('qwc2/components/QtDesignerForm');
const VectorLayerUtils = require('qwc2/utils/VectorLayerUtils');

const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"


class EditingFormReact extends React.Component {

    table = null
    childwdg = []
    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

    constructor(props) {
        super(props);
        // https://www.freecodecamp.org/news/react-changing-state-of-child-component-from-parent-8ab547436271/
        this.currentform = React.createRef()
        this.maintab = React.createRef()
        this.state = { isloading: true, ids: [] }
        this.childrefs = []
        this.ids = {}

        this.PARENTJOIN = null
        this.TABLEFILTERFIELD = null


    }

    // static getDerivedStateFromProps(props, state) {
    //     console.log('getDerivedStateFromProps')
    //     if (props.parentwdg) {
    //         console.log(props.parentwdg.table)
    //         console.log(props.parentproperties)
    //     }
    //     return null

    // }

    render() {
        console.log('render', this.constructor.name)

        if (this.state.isloading) {
            return (<p>Loading ... </p>)
        }

        let qtform = <QtDesignerForm domLoaded={this.domLoaded} ref={this.currentform}
            updateField={this.updateField} form={this.state.formui} values={this.state.currentfeatprop}
            keyvalues={this.state.keyvalues} domLoaded={this.domLoaded.bind(this)} />


        let childdom = []
        this.childwdg.forEach((childwd, idx) => {
            // console.log(childwd)
            // console.log('***', childwd.table, childwd.label)
            childdom.push(<input value={idx + 1} type="radio" id={'maintab' + childwd.label} key={'maintab' + childwd.label + idx * 3} name={this.table} onChange={this.handleTabChange} />)
            childdom.push(<label htmlFor={'maintab' + childwd.label} key={'maintab' + childwd.label + idx * 3 + 1}>{childwd.label}</label>)
            let Childwd = childwd
            childdom.push(
                <div className="qt-designer-tab" key={'maintab' + childwd.label + idx * 3 + 2}>
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
            <div className="qt-designer-tabs" name={this.table}>
                <input type="radio" value={0} id={'maintab' + this.table} name={this.table} defaultChecked={true} onChange={this.handleTabChange} />
                <label htmlFor={'maintab' + this.table}>{'Properties'}</label>
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
        this.getKeyvalues()
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
            console.log('up', this.constructor.name)
            let parentpk = this.props.parentproperties['pk_' + this.props.parentwdg.table]
            console.log('*', this.props.parentwdg.table, this.props.parentproperties['pk_' + this.props.parentwdg.table])

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
            // this.ids = res.data
            console.log('resp ids', this.ids)
            if (Object.entries(this.ids).length === 0) {
                this.setState({ currentfeatprop: {} })
                return
            }

            // if (Object.entries(this.ids.pk).length !== 0) {
            if (this.ids.pk) {
                console.log('***', this.table, this.ids)
                let featdata = await this.getPropertiesFromPk(this.ids.pk[0])
                this.setState({ currentfeatprop: featdata.properties })
            } else {
                this.setState({ currentfeatprop: {} })
            }


        }



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
        let temp = this.projectdata.qgisserverurl + 'qgisserver/wfs3/collections/' + this.table + '_qgis/items/' + pk + '.json'
        let feat = await axios.get(temp)
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
        // keyvalues = { 'comboBox_typeReseau': [{ key: 'popo', value: 'tete' }] }

        let url = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/' + this.table
        let res = await axios.post(url, {
            function: 'dbasetables',
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
        this.setState({ isloading: false, keyvalues: keyvalues })

    }


    handleTabChange = (evt) => {
        // console.log('change', evt.target.value, this.constructor.name)
        // console.log(this.childrefs)
        let currentinstance = null
        if (evt.target.value == 0) {
            currentinstance = this
        } else { currentinstance = this.childrefs[evt.target.value - 1].current }

        this.props.mainiface.setCurrentWidgetInstance(currentinstance)

    }

}

module.exports = EditingFormReact;
