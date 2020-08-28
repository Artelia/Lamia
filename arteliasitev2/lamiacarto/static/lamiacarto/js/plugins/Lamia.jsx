
const React = require('react');
const { connect } = require('react-redux');
const { SideBar } = require('qwc2/components/SideBar');
const { setCurrentTask } = require('qwc2/actions/task');
// import ToolTreeWidgetReact from './tooltreewidget'
// const ToolTreeWidgetReact = require('./tooltreewidget')

// import VectorLayer from 'ol/layer/Vector';
// const VectorLayer = require('ol/layer/Vector')

// import VectorSource from 'ol/source/Vector'
// const { VectorSource } = require('ol/source/Vector')
// import { GeoJSON } from 'ol/format';
// const { GeoJSON } = require('ol/format')

// const ol = require('ol');
const VectorLayerUtils = require('qwc2/utils/VectorLayerUtils');
const ol = require('openlayers');
const { Map, Layer } = require('qwc2/plugins/map/MapComponents');

const { addLayer, addLayerFeatures } = require('qwc2/actions/layers')

const MapUtils = require('qwc2/utils/MapUtils');

const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

const EdgeEditingFormReact = require('./forms/base3_urbandrainage/edgewidget')
const NodeEditingFormReact = require('./forms/base3_urbandrainage/nodewidget')
const MediaEditingFormReact = require('./forms/base3_urbandrainage/mediawidget')
const ReportEditingFormReact = require('./forms/base3_urbandrainage/reportwidget')

const { changeSelectionState } = require('qwc2/actions/selection');


class Lamia extends React.Component {
    static propTypes = {}

    static defaultProps = {
        width: '45em',
        minWidth: '30em'
    }

    workclasses = [
        EdgeEditingFormReact,
        NodeEditingFormReact,
        MediaEditingFormReact,
        ReportEditingFormReact
    ]

    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))
    state = {}

    constructor(props) {
        super(props);
        this.state = { 'visualmode': 1, 'mainwdg': null, 'values': null }
        this.currentwdginstance = null
        this.currentref = React.createRef()
        this.mainwdgrefcreated = false
    }

    componentDidMount() {
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.layers) {
            let found = nextProps.layers.find(layer => layer.title === "Lamiasel")
            // console.log('found', !found, found)
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
        if (nextState !== this.state) {
            returnvalue = true
        }

        if (nextProps.point !== this.props.point) {
            if (nextProps.point) {
                this.pointClicked.bind(this)(nextProps.point.coordinate)
            }
        }

        return returnvalue
    }

    componentWillReceiveProps_(nextProps) {
        console.log('componentWillReceiveProps')

        console.log('mapchange', nextProps.map !== this.props.map)
        if (nextProps.map !== this.props.map) {
            return false
        }
        // console.log('shouldComponentUpdate', nextProps)
        // console.log(this.props)
        // console.log('shouldComponentUpdate', nextState)

        // console.log('pp', nextProps === this.props)
        // console.log('pp', nextState === this.state)

        let found = this.props.layers.find(layer => layer.title === "Lamiasel")
        console.log('found', !found, found)
        if (!found) {
            let layer = {
                title: "Lamiasel",
                type: 'vector'
            };
            this.props.addLayer(layer);
            return false
        }
        console.log('point diff', nextProps.point !== this.props.point)
        if (nextProps.point !== this.props.point) {
            this.handleMapClick()
            return false
        }



        // console.log('shouldComponentUpdate', this.props)
        return false
    }

    render() {
        console.log('render Lamia', this.props.point)

        let layersdropdown = this.createLayerDrop.bind(this)()

        let layersdrop = (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Layers
              </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {layersdropdown}
                    </div>
                </div>
            </div>
        )

        let idsdropdown = this.createIdDrop.bind(this)()

        let idsdrop = (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Ids
              </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {idsdropdown}
                    </div>
                </div>
            </div>
        )



        let butonmenu = (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <button type="button" className="btn btn-secondary" id="canvaspick" onClick={this.buttonmenuclick.bind(this)}>Pick</button>
                <button type="button" className="btn btn-secondary" onClick={this.buttonmenuclick.bind(this)}>Middle</button>
            </div>
        )

        let extraTitlebarContent = (
            <div className="btn-toolbar " role="group" aria-label="Basic example" style={{ marginLeft: "1em" }}>
                {layersdrop}
                {idsdrop}
                {butonmenu}
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
                        {/* {tooltree} */}
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
            console.log('click*', wdg.constructor.name)
        }
        wdg.pointClicked(coords)
    }


    buttonmenuclick(evt) {
        console.log('buttonmenuclick')
        console.log(this.props)
    }


    createIdDrop() {


        if (!this.currentwdginstance) { return }

        console.log('createIdDrop', this.currentwdginstance.ids)

        let finaldatas = []


        for (var id in this.currentwdginstance.ids) {
            console.log(id)
            finaldatas.push(<a className="dropdown-item" id={id} key={id}
                onClick={this.handleLayerChanged.bind(this)}
            // onClick={() => this.handleLayerChanged.bind(this)}
            >
                {id}
            </a >
            )
            // finaldatas.push(<a className="dropdown-item" id={dataraw[firstdir][seconddir].label} >{seconddir}</a>)
        }


        return finaldatas
    }

    createLayerDrop() {

        let dataraw = {}

        this.workclasses.forEach(function (reactclass, idx) {
            if (!dataraw.hasOwnProperty(reactclass.firstdir)) {
                dataraw[reactclass.firstdir] = {}
            }
            dataraw[reactclass.firstdir][reactclass.label] = reactclass
        });



        let finaldatas = []

        for (var firstdir in dataraw) {
            finaldatas.push(<h6 className="dropdown-header" key={firstdir}>{firstdir}</h6>)
            for (var seconddir in dataraw[firstdir]) {
                finaldatas.push(<a className="dropdown-item" id={dataraw[firstdir][seconddir].label} key={seconddir}
                    onClick={this.handleLayerChanged.bind(this)}
                // onClick={() => this.handleLayerChanged.bind(this)}
                >
                    {seconddir}
                </a >
                )
                // finaldatas.push(<a className="dropdown-item" id={dataraw[firstdir][seconddir].label} >{seconddir}</a>)
            }
        };

        return finaldatas
    }

    handleLayerChanged = (evt) => {
        let goodclass = null
        this.workclasses.forEach(function (reactclass, idx) {
            if (reactclass.label === evt.target.id) {
                // if (reactclass.label === evt) {
                goodclass = reactclass
            }
        });
        this.mainwdgrefcreated = false
        this.setState({ mainwdg: goodclass })
        // this.setState({ mainwdg: goodclass, currentwdginstance: this.currentref.current })
    }

    setCurrentWidgetInstance = (cwi) => {
        this.currentwdginstance = cwi
        // this.setState({ currentwdginstance: cwi })
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

module.exports = {
    LamiaPlugin: connect(selector,
        {
            addLayer: addLayer,
            addLayerFeatures: addLayerFeatures,
            changeSelectionState: changeSelectionState
        })(Lamia),
    reducers: {
    }
};