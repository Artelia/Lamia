// import $ from "jquery"
// import L from "leaflet"
import React from 'react';
// import ReactDOM from 'react-dom';
// const { Map: LeafletMap, TileLayer, Marker, Popup } = ReactLeaflet
// import { Map, Marker, Popup, TileLayer } from 'react-leaflet'
import {
  interaction, layer, custom, control, //name spaces
  Interactions, Overlays, Controls,     //group
  Map, Layers, Overlay, Util    //objects
} from "react-openlayers";



class OLCanvasReact extends React.Component {
  constructor(props) {
    super(props)
    // console.log(props)
    this.state = {
      lat: 51.505,
      lng: -0.09,
      zoom: 13
    }
    
  }

  handleClick(e){
      var coord = e.latlng;
      var lat = coord.lat;
      var lng = coord.lng;
      console.log("You clicked the map at latitude: " + lat + " and longitude: " + lng);
  }

  render() {

    const position = [this.state.lat, this.state.lng];
    return (
      <div style={{width:'100%' , height:'400px', backgroundColor: 'yellow'}}>
      {/* <div> */}
        <Map view={{center: [0, 0], zoom: 2}}
            style={{position:'fixed', height:'10px'}}>
          <Layers>
            <layer.Tile/>
          </Layers>
          <Overlays>
          </Overlays>
          <Controls attribution={false} zoom={true}>
            <control.Rotate />
            <control.ScaleLine />
            {/* <control.FullScreen /> */}
            {/* <control.OverviewMap /> */}
            {/* <control.ZoomSlider /> */}
            <control.ZoomToExtent />
            <control.Zoom />
          </Controls>
          <Interactions>
          </Interactions>
        </Map>
      </div>
    );
  }
}


// class Canvas {
//     constructor (props) {

//         console.log(props)
        
//         // var mainiface = props[mainiface]
        
//         var map = L.map('map').setView([48.833, 2.333], 7); // LIGNE 18

//         var mapmargin = 50;
        
//         $(window).on("resize", function () { $("#map").height($(window).height()-10); map.invalidateSize(); }).trigger("resize");
        
        
//         var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', { // LIGNE 20
//             attribution: '© OpenStreetMap contributors',
//             maxZoom: 19
//         });
        
//         map.on('click', function(e){
//             var coord = e.latlng;
//             var lat = coord.lat;
//             var lng = coord.lng;
//             console.log("You clicked the map at latitude: " + lat + " and longitude: " + lng);
//             });
        
//         map.addLayer(osmLayer);
  
  
        
//       }




// }


export default OLCanvasReact;