const React = require('react');

const { Map: LeafletMap, GeoJSON, TileLayer, Marker, Popup } = require('react-leaflet')
require('leaflet/dist/leaflet.css')

const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class ReportMap extends React.Component {

    constructor(props) {
        super()
        this.mapref = React.createRef()
        this.geojsonref = React.createRef()
        this.selectionref = React.createRef()
        this.selecteddata = {}
        this.state = {
            wfsdata: {},
        }
    }


    render() {
        return (
            <LeafletMap
                zoomControl={false}
                style={{
                    zIndex: "0", width: '100%',
                    height: '100%',
                }} onMoveend={this.handleMoveend} onzoomEnd={this.handleMoveend} ref={this.mapref} >
                < TileLayer
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url='https://{s}.tile.osm.org/{z}/{x}/{y}.png'
                />
                {this.state.wfsdatas ? <GeoJSON data={this.state.wfsdatas} ref={this.geojsonref} style={this.setGeoJsonStyle} /> : null}
                {/* {this.getCurrentFeature()} */}
            </LeafletMap >

        );
    }

    getCurrentFeature = () => {
        if (!this.state.wfsdatas) {
            return null
        }

        let jsonfiltered = this.state.wfsdatas.features.filter((feat) => {
            return (
                feat.id === this.props.currentid
            );
        });
        this.selecteddata.features = jsonfiltered
        // return this.selecteddata
        return (<GeoJSON data={this.selecteddata} style={{ fillColor: 'red' }} />)
    }

    setGeoJsonStyle = (feature) => {
        if (feature.id === this.props.currentid) {
            return {
                fillColor: 'red',
                weight: 2,
                opacity: 1,
                color: 'red',
            }
        } else {
            return {
                fill: false,
                fillColor: 'blue',
                weight: 2,
                opacity: 0.2,
                color: 'blue',
            }
        }
    }

    async componentDidMount() {
        //download report wfs
        let qgisserverurl = this.props.mainiface.projectdata.qgisserverurl.split('?')[0]
        let qgisserverquery
        this.props.mainiface.projectdata.qgisserverurl.split('?').length > 1 ? qgisserverquery = this.props.mainiface.projectdata.qgisserverurl.split('?')[1] : qgisserverquery = null
        let databaseurl = qgisserverurl + "/qgisserver/wfs?request=GetFeature&service=WFS&version=1.0.0&outputFormat=application/json&typeName=report_qgis"
        qgisserverquery ? databaseurl = databaseurl + '&' + qgisserverquery : null
        const feat = await axios.get(databaseurl)

        //fit initial bounds
        const leafbound = [[feat.data.bbox[1], feat.data.bbox[0]], [feat.data.bbox[3], feat.data.bbox[2]]]

        this.mapref.current.leafletElement.fitBounds(leafbound)

        this.props.geoJsonLayerChanged(feat.data)
        this.props.bboxChanged([feat.data.bbox[0], feat.data.bbox[1], feat.data.bbox[2], feat.data.bbox[3]])
        this.selecteddata = Object.assign({}, feat.data)
        this.selecteddata.features = []
        this.setState({ 'wfsdatas': feat.data })
    }

    handleMoveend = (evt) => {
        const leafbbox = this.mapref.current.leafletElement.getBounds()
        this.props.bboxChanged([
            leafbbox._southWest.lng,
            leafbbox._southWest.lat,
            leafbbox._northEast.lng,
            leafbbox._northEast.lat,
        ])
    }
}

module.exports = ReportMap