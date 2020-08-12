import React from 'react';
// import logo from './logo.svg';
// import Flexbox from 'flexbox-react';
// import { View } from 'react-native'; 

//
// import './App.css';
import MainWidgetReact from './mainwidget/mainwidget'
// import LCanvasReact from './canvas/leaflet'
import OLCanvasReact from './canvas/openlayers'
// import QtDesignerForm from './mainwidget/testqwc2/QtDesignerForm'
import EditingFormReact from './mainwidget/editingformwidget'

// const QtDesignerForm = require('./qwc2/components/QtDesignerForm');
// import QtDesignerForm from './testqwc2/QtDesignerForm'
import $ from 'jquery'
import Cookies from 'js-cookie'

import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class MainIfaceReact extends React.Component {

  projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))
  static debugreact = false

  constructor(props) {
    super(props);
    // this.state = { 'qgisserverurl': null, 'currentfeatprop': {} }
    this.state = { 'qgisserverurl': null }

    // Axios test with rest API
    // axios.post('http://localhost:8000/posts', {
    //   firstName: 'trrt',
    //   lastName: 'Williams'
    // }).then(function (reponse) {
    //   console.log(reponse);
    // });

    //test qgisserverurl
    //
    // this.ui = React.createRef()

    // get static file
    // axios.get('/static/lamiacarto/forms/form.ui').then(response => {
    //   console.log('po', response)
    // }).catch(e => {
    //   console.log(e);
    // });


  }


  componentDidMount() {
    this.loadQgisServerUrl.bind(this)(this.projectdata.qgisserverurl)
  }

  async loadQgisServerUrl(qgisserverurl) {
    let success = false
    try {
      const data = await axios.get(qgisserverurl);
      success = true;
    } catch (error) {
      success = false
    }

    if (success) {
      this.setState({ qgisserverurl: qgisserverurl })
    } else {
      this.setState({ qgisserverurl: false })
    }
  }

  render_() {
    return (<p>render1</p>)
  }



  render() {
    this.debugreact ? console.log('render ', this.constructor.name, this.state.qgisserverurl) : null

    let mainp = <p></p>;
    if (this.debugreact) {
      mainp = <p style={{ backgroundColor: 'red', }} >{this.constructor.name}</p>
    }


    let loader_ = (
      <div className="container-fluid">
        <div className="row justify-content-center">
          <div className="spinner-border" role="status">
            <span className="sr-only">Loading...</span>
          </div>
        </div>
        <div className="row justify-content-center">
          <strong>Collecting data</strong>
        </div>
      </div>
    )

    let loader = (<div className="loader" ng-hide="data.length > 0"></div>)


    if ([null].includes(this.state.qgisserverurl)) {
      loader = loader
      // loader = (<button className="btn btn-primary" type="button" style={{ position: 'absolute', top: '50%' }} disabled>
      //   <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
      // Loading...
      // </button>)
    } else if (([false].includes(this.state.qgisserverurl))) {
      loader = loader
    } else {
      loader = null
    }

    return (
      < div className="row " style={{ height: '100%' }}>
        {loader}
        <div className="col-8 border bg-light">
          <OLCanvasReact mainiface={this} qgisserverurl={this.state.qgisserverurl} style={{}} />
        </div>
        <div className="col-4 border bg-light">
          <EditingFormReact />
        </div>
      </div >

    )
  }
}

export default MainIfaceReact;
