const React = require('react');
const { connect } = require('react-redux');
const { SideBar } = require('qwc2/components/SideBar');
const { addLayer, addLayerFeatures, changeLayerProperty } = require('qwc2/actions/layers')
const { changeSelectionState } = require('qwc2/actions/selection');



const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

const IdChooser = require('./idchooser')
const StyleChooser = require('./stylechooser')

require('./qwc2/style/SideBar.css');
const base3_urbandrainage = require('./forms/base3_urbandrainage/base3_urbandrainage')


class Lamia extends React.Component {
    static propTypes = {}

    static defaultProps = {
        width: '45em',
        minWidth: '30em'
    }

    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

    constructor(props) {
        super();
        this.state = { 'visualmode': 1, 'mainwdg': null, 'values': null, 'widgetsclasses': [], 'styles': {} }
        this.currentwdginstance = null
        this.currentref = React.createRef()
        this.mainwdgrefcreated = false
        this.idchooserref = React.createRef()
        this.stylechooserref = React.createRef()
        this.dbaseworktypeloaded = false
        this.defaultstyleloaded = false
        this.getDBaseWorktype()
    }

    async getDBaseWorktype() {
        // let qgisserverurl = this.projectdata.qgisserverurl.split('?')[0]
        // let qgisserverquery
        // this.projectdata.qgisserverurl.split('?').length > 1 ? qgisserverquery = this.projectdata.qgisserverurl.split('?')[1] : qgisserverquery = null

        // let qgisserverurl = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/styles'
        let qgisserverurl = 'http://' + window.location.host 
        let databaseurl = qgisserverurl + '/qgisserver/' + this.projectdata.id_project + '/wfs3/collections/database_qgis/items/1.json'
        // qgisserverquery ? databaseurl = databaseurl + '?' + qgisserverquery : null
        let feat = await axios.get(databaseurl)
        let worktype = feat.data.properties.businessline
        this.dbaseworktypeloaded = true
        eval('this.setState({widgetsclasses:' + worktype + '})')
    }


    componentWillReceiveProps(nextProps) {
        if (nextProps.layers) {
            let found = nextProps.layers.find(layer => layer.title === "Lamiasel")
            if (!found) {
                let layer = {
                    title: "Lamiasel",
                    type: 'vector',
                    layertreehidden: true,
                };
                nextProps.addLayer(layer);
            }
        }
    }

    shouldComponentUpdate(nextProps, nextState) {

        let returnvalue = false
        if (!this.defaultstyleloaded && Object.keys(this.state.styles).length !== 0) {
            
            if (this.getLamiaLayer() !== null) {
                this.changeStyle("_default")
                this.defaultstyleloaded = true
                returnvalue = true
            }
        }


        if (!this.dbaseworktypeloaded) {
            return false
        }

        if (nextState !== this.state) {
            returnvalue = true
        }

        if (nextProps.point !== this.props.point) {
            if (nextProps.point) {
                let wdg = this.currentwdginstance
                if (wdg && wdg !== undefined) {
                    this.pointClicked.bind(this)(nextProps.point.coordinate)
                }
            }
        }

        return returnvalue
    }

    componentWillReceiveProps_(nextProps) {
        if (nextProps.map !== this.props.map) {
            return false
        }

        let found = this.props.layers.find(layer => layer.title === "Lamiasel")
        if (!found) {
            let layer = {
                title: "Lamiasel",
                type: 'vector'
            };
            this.props.addLayer(layer);
            return false
        }
        if (nextProps.point !== this.props.point) {
            this.handleMapClick()
            return false
        }
        return false
    }

    render() {
        let layersdropdown = this.createLayerDrop.bind(this)()

        let butonmenu = (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <button type="button" className="btn btn-secondary" id="canvaspick" onClick={this.buttonmenuclick.bind(this)}>Pick</button>
                <button type="button" className="btn btn-secondary" onClick={this.buttonmenuclick.bind(this)}>Middle</button>
            </div>
        )

        let extraTitlebarContent = (
            <div className="btn-toolbar " role="group" aria-label="Basic example" style={{ marginLeft: "1em" }}>
                {layersdropdown}
                {<IdChooser ref={this.idchooserref} mainiface={this} />}
                {<StyleChooser ref={this.stylechooserref} mainiface={this} styles={this.state.styles} />}
                {/* {butonmenu} */}
            </div>
        );

        return (
            <div>
                <SideBar id="Lamia" width={this.state.sidebarwidth || this.props.width}
                    title="Lamia" icon="layers"
                    // extraBeforeContent={visibilityCheckbox}
                    // onHide={this.hideLegendTooltip} 
                    extraTitlebarContent={extraTitlebarContent}
                >
                    <div role="body" >
                        {(this.state.mainwdg === null) ? < div></div> : <this.state.mainwdg
                            ref={this.currentref}
                            mainiface={this}
                        />}
                    </div>
                </SideBar>
                {/* {legendTooltip} */}
                {/* <LayerInfoWindow windowSize={this.props.layerInfoWindowSize} bboxDependentLegend={this.props.bboxDependentLegend} /> */}
            </div>
        );
    }


    componentDidMount() {
        this.loadStyles()
    }


    componentDidUpdate() {
        if (!this.mainwdgrefcreated) {
            this.mainwdgrefcreated = true
            this.currentwdginstance = this.currentref.current
        }
    }


    others_________________________() { }

    async pointClicked(coords) {
        let wdg = this.currentwdginstance
        while (wdg.props.parentwdg) {
            wdg = wdg.props.parentwdg
        }
        wdg.pointClicked(coords)
    }


    buttonmenuclick(evt) {
        console.log('buttonmenuclick')
    }


    createIdDrop() {
        if (!this.currentwdginstance) { return }
        let finaldatas = []
        for (var id in this.state.ids) {
            finaldatas.push(<a className="dropdown-item" id={id} key={id}
                onClick={this.handleLayerChanged.bind(this)}
            >
                {id}
            </a >
            )
        }
        return finaldatas
    }

    createLayerDrop() {

        let dataraw = {}
        for (const reactclass of Object.values(this.state.widgetsclasses)) {
            if (!dataraw.hasOwnProperty(reactclass.firstdir)) {
                dataraw[reactclass.firstdir] = {}
            }
            dataraw[reactclass.firstdir][reactclass.label] = reactclass
        };

        let finaldatas = []
        for (var firstdir in dataraw) {
            finaldatas.push(<h6 className="dropdown-header" key={firstdir}>{firstdir}</h6>)
            for (var seconddir in dataraw[firstdir]) {
                finaldatas.push(<a className="dropdown-item" id={dataraw[firstdir][seconddir].label} key={seconddir}
                    onClick={this.handleLayerChanged.bind(this)}
                >
                    {seconddir}
                </a >
                )
            }
        };

        return (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Layers
              </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {finaldatas}
                    </div>
                </div>
            </div>
        )
    }

    handleLayerChanged = (evt) => {
        let goodclass = null
        for (const reactclass of Object.values(this.state.widgetsclasses)) {
            if (reactclass.label === evt.target.id) {
                goodclass = reactclass
                break
            }
        };

        this.mainwdgrefcreated = false
        this.setState({ mainwdg: goodclass })
    }

    setCurrentWidgetInstance = (cwi) => {
        this.currentwdginstance = cwi
        this.idchooserref.current.setState({ ids: cwi.ids })
    }


    //* Style func

    async loadStyles() {
        let stylesurl = 'http://' + window.location.host + '/lamiaapi/' + this.projectdata.id_project + '/styles'
        let styles = await axios.get(stylesurl)
        this.setState({ styles: styles.data })
    }


    changeStyle = (deststyle) => {
        let lamialayer = this.getLamiaLayer()
        if (!lamialayer) { return }

        const lamiasublayers = lamialayer.sublayers
        let lamiasubstyle = []

        lamiasublayers.forEach((sublay, idx) => {
            if (this.state.styles[deststyle].includes(sublay.name.split('_')[0])) {
                lamiasubstyle.push(deststyle)
                lamialayer.sublayers[idx].style = deststyle
            } else {
                lamiasubstyle.push('default')
                lamialayer.sublayers[idx].visibility = false
                lamialayer.sublayers[idx].style = 'default'
            }
        })
        this.props.changeLayerProperty(lamialayer.uuid, "params.styles", lamiasubstyle.join(','), [], null);
        // return
    }

    getLamiaLayer() {
        let layers = this.props.layers
        let lamialayer = null
        for (let layerid in Object.values(layers)) {
            let layer = layers[layerid]
            if (layer.title.toLowerCase() === 'lamia') {
                lamialayer = layer
                break
            }
        }
        return lamialayer
    }
}


const selector = (state) => ({
    // enabled: state.task ? state.task.id === 'Editing' : false,
    // theme: state.theme ? state.theme.current : null,
    layers: state.layers ? state.layers.flat : [],
    map: state.map || {},
    point: state.map && state.map.clickPoint,
    selection: state.selection,
    // iface: iface,
    // editing: state.editing || {},
})

//

module.exports = {
    LamiaPlugin: connect(selector,
        {
            addLayer: addLayer,
            addLayerFeatures: addLayerFeatures,
            changeSelectionState: changeSelectionState,
            changeLayerProperty: changeLayerProperty,
        })(Lamia),
    reducers: {
    }
};