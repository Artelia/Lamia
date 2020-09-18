const React = require('react');

const ReportMap = require('./components/leaftletmap');

class ReportIFace extends React.Component {

  constructor(props) {
    super()

  }


  render() {

    return (
      <div className="container-fluid" >
        <div className="row">
          <div className="col-6">
            <ReportMap />
          </div>
          <div className="col">
            toto
          </div>
        </div>
      </div>

    )
  }
}
//
module.exports = ReportIFace
