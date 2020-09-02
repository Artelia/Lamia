import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import MainIfaceReact from './MainIface';
var path = require('path');
// important for bootstrap working
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

// import * as serviceWorker from './serviceWorker';
// import Canvas from './leaflet/leaflet'
// import 'bootstrap';



class MainIface {
  constructor(props) {


    ReactDOM.render(
      <MainIfaceReact />,
      document.getElementById('root')
    );

    // ReactDOM.render(
    //   <p>MainIface</p>,
    //   document.getElementById('root')
    // );

    // this.canvas = new Canvas(mainiface = this)


  }


}

new MainIface()




// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
