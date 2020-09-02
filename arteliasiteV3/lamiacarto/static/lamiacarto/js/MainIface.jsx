import React from 'react';
// import logo from './logo.svg';
// import Flexbox from 'flexbox-react';
// import { View } from 'react-native'; 

//
// import './App.css';
// import MainWidgetReact from './mainwidget/mainwidget'
// import LCanvasReact from './canvas/leaflet'
import OLCanvasReact from './canvas/openlayers'
// import QtDesignerForm from './mainwidget/testqwc2/QtDesignerForm'
// import EditingFormReact from './mainwidget/editingformwidget'
import ToolTreeWidgetReact from './mainwidget/tooltreewidget'


// const QtDesignerForm = require('./qwc2/components/QtDesignerForm');
// import QtDesignerForm from './testqwc2/edgewidget'
import $ from 'jquery'
import Cookies from 'js-cookie'

import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class MainIfaceReact extends React.Component {


  constructor(props) {
    super(props);

    // this.state = { 'qgisserverurl': null, 'currentfeatprop': {} }
    // this.state = { 'qgisserverurl': null }

    // Axios test with rest API
    // axios.post('http://localhost:8000/lamiaapi/1', {
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


  render() {

    return (
      <div className="container-fluid" style={{ height: '100%' }}>
        < div className="row " style={{ height: '100%' }}>

          <div className="col-8 border bg-light">
            <OLCanvasReact />
          </div>
          <div className="col-4 border bg-light">
            {/* <EditingFormReact /> */}
            {/* <EdgeEditingFormReact /> */}
            <ToolTreeWidgetReact />
          </div>
        </div >
      </div>
    )
  }
}

export default MainIfaceReact;
