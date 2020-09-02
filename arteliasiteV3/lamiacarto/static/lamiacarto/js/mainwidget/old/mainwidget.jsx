
import React from 'react';
import Flexbox from 'flexbox-react';
// import ToolTreeWidgetReact from './tooltreewidget'
// import ToolsWidgetReact from './toolswidget'
// import $ from "jquery";



class MainWidgetReact extends React.Component {

  // dbasetables = require('../dbasetables.json');
  // static toolwdgclass = ToolsWidgetReact

  constructor(props) {
    super(props);
    // this.toolswidget = React.createRef()
    // this.toolsdom = <ToolsWidgetReact mainiface={this} ref={this.toolswidget} />
    // this.treewdg = React.createRef()
    // this.treedom = <ToolTreeWidgetReact mainiface={this} toolswdg={this.toolswidget} ref={this.treewdg} />

  }

  render() {
    const debug = false;

    let mainp = <p></p>;
    if (debug) {
      mainp = <p style={{ backgroundColor: 'red' }} >{this.constructor.name}</p>
    }

    return (
      <div>
        {mainp}
        <p>okok</p>
      </div>
    )

  }

  render_() {
    let divstyle = { padding: '2px', borderWidth: '1px', borderColor: 'black', borderStyle: 'inset' }
    return (


      <div style={{ width: '100%', height: '100%', backgroundColor: 'transparent' }}>

        <Flexbox flexDirection="row" height={'100%'}>

          <Flexbox flexGrow={1} flexBasis={'0'} flexShrink={1} style={divstyle}>
            {this.treedom}
          </Flexbox>
          <Flexbox flexGrow={3} flexBasis={'0'} flexShrink={1} style={divstyle}>
            {this.toolsdom}
          </Flexbox>
        </Flexbox>
      </div>


    )
  }
}


export default MainWidgetReact;