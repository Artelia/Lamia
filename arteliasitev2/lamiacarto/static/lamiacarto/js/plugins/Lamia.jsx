
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
const ol = require('openlayers');
const { Map, Layer } = require('qwc2/plugins/map/MapComponents');

const { addLayer, addLayerFeatures } = require('qwc2/actions/layers')

const MapUtils = require('qwc2/utils/MapUtils');

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
        this.state = { 'visualmode': 1, 'currentwdg': null, 'values': null }

        console.log(window.location.host)

    }

    renderBody = () => {
        // return <p>ozieproi</p>
        // return (<ToolTreeWidgetReact />)
        return (null)
    }

    componentDidMount() {
        console.log('componentDidMount', this.props)


        // let layer = {
        //     title: "Lamiasel",
        //     type: 'vector'
        // };
        // this.props.addLayer(layer);

        // this.props.onChange(layer);

        // var selsource = new ol.source.Vector.VectorSource({
        // var selsource = new VectorSource({
        //     format: new GeoJSON(),
        //     // projection: 'EPSG:4326' 
        // });

        // // var sellayer = new ol.layer.Vector.VectorLayer({
        // var sellayer = new VectorLayer({
        //     source: selsource,
        //     // projection: 'EPSG:4326',
        //     style: new Style({
        //         stroke: new Stroke({
        //             color: 'green',
        //             width: 6,
        //         }),

        //         image: new Circle({
        //             radius: 5,
        //             fill: new Fill({ color: 'green' }),
        //             stroke: new Stroke({
        //                 color: 'green', width: 2
        //             }),
        //         })


        //     })
        // });

        // let source = new ol.source.Vector();
        // this.layer = new ol.layer.Vector({
        //     source: source,
        //     zIndex: 1000000,
        //     style: this.editStyle
        // });
        // this.props.map.addLayer(this.layer);

        // let layer = {
        //     title: "Lamiasel",
        //     type: 'vector'
        // };
        // this.props.addLayer(layer);

        console.log('componentDidMount', this.props)
    }


    shouldComponentUpdate(nextProps, nextState) {
        if (nextState !== this.state) {
            return true
        }
        if (nextProps.point == this.props.point) {
            return false
        }
        return true
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

            // let snapStyle = [
            //     new ol.style.Style({
            //         fill: new ol.style.Fill({ color: [255, 255, 255, 0.05] }),
            //         stroke: new ol.style.Stroke({ color: '#3399CC', width: 1 })
            //     }),
            //     new ol.style.Style({
            //         image: new ol.style.RegularShape({
            //             fill: new ol.style.Fill({ color: [255, 255, 255, 0.05] }),
            //             stroke: new ol.style.Stroke({ color: '#3399CC', width: 1 }),
            //             points: 4,
            //             radius: 5,
            //             angle: Math.PI / 4
            //         }),
            //         geometry: (feature) => {
            //             if (feature.getGeometry().getType() === "Point") {
            //                 return new ol.geom.MultiPoint([feature.getGeometry().getCoordinates()]);
            //             } else if (feature.getGeometry().getType() === "LineString") {
            //                 return new ol.geom.MultiPoint(feature.getGeometry().getCoordinates());
            //             } else {
            //                 return new ol.geom.MultiPoint(feature.getGeometry().getCoordinates()[0]);
            //             }
            //         }
            //     })
            // ];
            // this.snapSource = new ol.source.Vector();
            // this.snapLayer = new ol.layer.Vector({
            //     title: 'Lamiasel',
            //     source: this.snapSource,
            //     zIndex: 1000000,
            //     style: snapStyle
            // });
            // // this.props.map.addLayer(this.snapLayer);
            // nextProps.addLayer(this.snapLayer);

        }

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

        let dropdown = this.createToolbar.bind(this)()

        let layersdrop = (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Layers
              </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {dropdown}
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
                {butonmenu}
            </div>
        );

        // let layer = {
        //     title: "Lamiasel",
        //     type: 'vector'
        // };
        // this.props.addLayer(layer);

        let thisiface = { getKeyValues: this.getKeyValues }

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
                        {(this.state.currentwdg === null) ? < div></div> : <this.state.currentwdg
                            point={this.props.map.clickPoint}
                            layers={this.props.layers}
                            addLayerFeatures={this.props.addLayerFeatures}
                            changeSelectionState={this.props.changeSelectionState}
                            selection={this.props.selection} />}
                    </div>
                    {/* {() => ({
                        body: this.renderBody()
                    })} */}
                </SideBar>
                {/* {legendTooltip} */}
                {/* <LayerInfoWindow windowSize={this.props.layerInfoWindowSize} bboxDependentLegend={this.props.bboxDependentLegend} /> */}
            </div>
        );
    }

    getKeyValues() {
        return {}
    }

    buttonmenuclick(evt) {
        console.log('buttonmenuclick')
        console.log(this.props)
    }

    createToolbar() {

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

    handleLayerChanged(evt) {
        let goodclass = null
        console.log('*', evt)
        this.workclasses.forEach(function (reactclass, idx) {
            if (reactclass.label === evt.target.id) {
                // if (reactclass.label === evt) {
                goodclass = reactclass
            }
        });
        this.setState({ currentwdg: goodclass })
    }

}

// module.exports = {
//     LamiaPlugin: Lamia
// }


// module.exports = (iface) => {
//     return {
//         LamiaPlugin: connect(state => ({
//             enabled: state.task ? state.task.id === 'Editing' : false,
//             theme: state.theme ? state.theme.current : null,
//             layers: state.layers ? state.layers.flat : [],
//             map: state.map || {},
//             iface: iface,
//             editing: state.editing || {},
//         }))(Lamia)
//     }
// };


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