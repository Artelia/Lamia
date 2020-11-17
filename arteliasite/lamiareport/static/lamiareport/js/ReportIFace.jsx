const React = require('react');

const ReportMap = require('./components/leaftletmap');
const ReportCatalog = require('./components/reportcatalog');

class ReportIFace extends React.Component {

  projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

  constructor(props) {
    super()
    // this.state.bbox = []
    this.state = {
      bbox: [],
      idproperties: null,
      geojsonfeat: [],
      currentid: null
    }
  }


  render() {

    return (
      <div className="container-fluid" style={{ height: '100%' }}>
        <div className="row" style={{ height: '100%' }}>
          <div className="col" >
            <ReportMap
              mainiface={this}
              bboxChanged={this.bboxChanged.bind(this)}
              geoJsonLayerChanged={this.geoJsonLayerChanged.bind(this)}
              currentid={this.state.currentid}
            />
          </div>
          <div className="col">
            <ReportCatalog
              mainiface={this}
              bbox={this.state.bbox}
              idproperties={this.state.idproperties}
              geojsonfeat={this.state.geojsonfeat}
              reportidHovered={this.reportidHovered.bind(this)}
            />
          </div>
        </div>
      </div>

    )
  }

  bboxChanged(newbb) {
    this.setState({ bbox: newbb })
  }

  geoJsonLayerChanged(geojson) {
    let idproperties = {}
    for (const feat in geojson.features) {
      idproperties[geojson.features[feat].id.split('.')[1]] = geojson.features[feat].properties
    }
    this.setState({ idproperties: idproperties, geojsonfeat: geojson.features })
  }

  reportidHovered(id) {
    this.setState({ currentid: id })
  }

}
//
module.exports = ReportIFace
