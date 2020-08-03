import React from 'react';
// import logo from './logo.svg';
import Flexbox from 'flexbox-react';
// import { View } from 'react-native'; 

//
// import './App.css';
import MainWidgetReact from './mainwidget/mainwidget'
// import LCanvasReact from './canvas/leaflet'
import OLCanvasReact from './canvas/openlayers'

// const QtDesignerForm = require('./qwc2/components/QtDesignerForm');
// import QtDesignerForm from './testqwc2/QtDesignerForm'
import $ from 'jquery'

class MainIfaceReact extends React.Component {


  constructor(props) {
    super(props);
    this.mainwidget = React.createRef()
    this.mainwidgetdom = <MainWidgetReact ref={this.mainwidget} />

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
    const debug = true;

    let mainp = <p></p>;
    if (debug) {
      mainp = <p style={{ backgroundColor: 'red' }} >{this.constructor.name}</p>
    }

    return (
      <div style={{ width: '100%', height: '100%' }}>
        {mainp}


        <div class="container">
          <div class="row">
            <div class="col-8">
              <p>OLCanvasReact</p>
              <p>{mydata}</p>
              <OLCanvasReact mainiface={this} style={{}} />
            </div>
            <div class="col-4">
              2 of 3 (wider)
            </div>

          </div>
        </div>

        <Flexbox flexDirection="row" height="100%" width='100%'>
          {/* <Flexbox flexGrow={1}   flexBasis={'0'} style={{backgroundColor: 'red'}}>
              <p>ptepe</p>
            </Flexbox> */}
          <Flexbox flexGrow={2} flexBasis={'0'} flexShrink={1} height={'100%'}>
            <p>OLCanvasReact</p>
            <p>{mydata}</p>
            <OLCanvasReact mainiface={this} style={{}} />
            {/* <div>Legend<img id="legend"/></div> */}
            {/* <LCanvasReact  mainiface={this}/> */}

          </Flexbox>
          <Flexbox flexGrow={2} flexBasis={'0'} flexShrink={1} >
            {this.mainwidgetdom}
          </Flexbox>
          {/* <Flexbox flexGrow={3} flexBasis={'0'} flexShrink={1} >
            <QtDesignerForm form={'testui.ui'}
              formdata={'1'}
              ref={this.ui}
              values={{ 'name': 'poerz' }}
              updateField={(item) => { return null }}
              style={{ width: '100%' }} />
          </Flexbox> */}
        </Flexbox>

      </div >
    )
  }
}

export default MainIfaceReact;
