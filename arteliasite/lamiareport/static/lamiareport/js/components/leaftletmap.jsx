const React = require('react');

const { Map: LeafletMap, TileLayer, Marker, Popup } = require('react-leaflet')

require('leaflet/dist/leaflet.css')

class ReportMap extends React.Component {

    constructor(props) {
        super()
        this.state = {
            lat: 51.505,
            lng: -0.09,
            zoom: 13
        }
    }


    render() {

        const position = [this.state.lat, this.state.lng];
        return (
            <LeafletMap center={position} zoom={this.state.zoom} zoomControl={false} style={{
                zIndex: "0", width: '100%', height: '100vh'
            }}>
                < TileLayer
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    url='https://{s}.tile.osm.org/{z}/{x}/{y}.png'
                />
                <Marker position={position}>
                    <Popup>
                        A pretty CSS3 popup. <br /> Easily customizable.
              </Popup>
                </Marker>
            </LeafletMap>
        );
    }
}
//
module.exports = ReportMap