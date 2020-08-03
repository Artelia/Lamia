import React from 'react';
// import logo from './logo.svg';
// import Flexbox from 'flexbox-react';
// import { View } from 'react-native'; 

//
// import './App.css';
import MainWidgetReact from './mainwidget/mainwidget'
// import LCanvasReact from './canvas/leaflet'
import OLCanvasReact from './canvas/openlayers'

// const QtDesignerForm = require('./qwc2/components/QtDesignerForm');
// import QtDesignerForm from './testqwc2/QtDesignerForm'
import $ from 'jquery'
import Cookies from 'js-cookie'

import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class MainIfaceReact extends React.Component {


  constructor(props) {
    super(props);
    this.mainwidget = React.createRef()
    this.mainwidgetdom = <MainWidgetReact ref={this.mainwidget} />


    // const axios = require('axios');
    // var csrftoken = Cookies.get('csrftoken');

    // axios({
    //   method: 'post',
    //   url: 'http://localhost:8000/posts',
    //   // { headers: { 'X-CSRFToken': csrftoken } },
    //   data: {
    //     firstName: 'Finn',
    //     lastName: 'Williams'
    //   }
    // })
    //   .then(function (reponse) {
    //     //On traite la suite une fois la réponse obtenue 
    //     console.log(reponse);
    //   })
    const querystring = require('querystring');
    // var bodyFormData = new FormData();
    // bodyFormData.set('userName', 'Fred');

    // axios.post('http://localhost:8000/posts', querystring.stringify({ foo: 'bar' })).then(function (reponse) {
    //   console.log(reponse);
    // })

    axios.post('http://localhost:8000/posts', {
      firstName: 'trrt',
      lastName: 'Williams'
    }).then(function (reponse) {
      console.log(reponse);
    })



    //

    // this.ui = React.createRef()
  }



  componentDidMount() {
    // this.ui.current.setState({formdata:1})
  }

  render_() {

    return (<p>render1</p>)

  }

  render() {

    const mydata = JSON.parse(document.getElementById('context').textContent);
    const debug = false;

    let mainp = <p></p>;
    if (debug) {
      mainp = <p style={{ backgroundColor: 'red', }} >{this.constructor.name}</p>
    }

    return (
      // <div style={{ width: '100%', height: '100%' }}>
      <div className="container-fluid" style={{ height: '100%' }}>
        {mainp}


        <div className="row " style={{ height: '100%' }}>
          <div className="col-8 border bg-light">
            {/* <p>OLCanvasReact</p> */}
            {/* <p>{mydata}</p> */}
            <OLCanvasReact mainiface={this} style={{}} />
          </div>
          <div className="col-4 border bg-light">
            {this.mainwidgetdom}
          </div>

        </div>
      </div>

    )
  }
}

export default MainIfaceReact;
