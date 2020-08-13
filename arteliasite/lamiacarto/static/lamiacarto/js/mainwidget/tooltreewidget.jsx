import React from 'react';
// import TreeView from 'react-simple-jstree';

// import TreeView from '@material-ui/lab/TreeView';
// import TreeItem from '@material-ui/lab/TreeItem';
// import { makeStyles } from '@material-ui/core/styles';
// import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
// import ChevronRightIcon from '@material-ui/icons/ChevronRight';

// import Tree from '@naisutech/react-tree'
import TreeMenu from 'react-simple-tree-menu';
// import '../../node_modules/react-simple-tree-menu/dist/main.css';
import 'react-simple-tree-menu/dist/main.css'

import EdgeEditingFormReact from './edgewidget'


class ToolTreeWidgetReact extends React.Component {

  workclasses = [
    EdgeEditingFormReact,
  ]

  constructor(props) {
    super(props);
    // this.mainiface = this.props.mainiface
    // this.toolswdg = this.props.toolswdg

    this.state = { 'visualmode': 1, 'currentwdg': null }

    // let workclasses = this.mainiface.toolsdom.type.workclasses

    this.finaldatas = this.getTreeDatas(this.workclasses)

  }

  getTreeDatas(workclasses) {
    console.log(workclasses)
    let dataraw = {}

    workclasses.forEach(function (reactclass, idx) {
      if (!dataraw.hasOwnProperty(reactclass.firstdir)) {
        dataraw[reactclass.firstdir] = {}
      }
      dataraw[reactclass.firstdir][reactclass.label] = reactclass
    });

    // for (const [key, value] of Object.entries(workclasses)) {
    //   if (!dataraw.hasOwnProperty(value.firstdir)) {
    //     dataraw[value.firstdir] = []
    //   }
    //   dataraw[value.firstdir].push(value.seconddir)
    // }

    console.log('dataraw', dataraw)

    let finaldatas = {}

    for (var firstdir in dataraw) {
      finaldatas[firstdir] = {
        label: firstdir,
        nodes: {}
      };
      for (const [key, value] of Object.entries(dataraw[firstdir])) {
        var seconddirvalue = key
        finaldatas[firstdir].nodes[seconddirvalue] = {
          label: seconddirvalue,
          class: value,
          nodes: {}
        };
      }
      // for (var seconddir in dataraw[firstdir]) {
      //   var seconddirvalue = dataraw[firstdir][seconddir]
      //   finaldatas[firstdir].nodes[seconddirvalue] = {
      //     label: seconddirvalue,
      //     nodes: {}
      //   };
      // }

    };
    console.log('finaldatas', finaldatas)
    return finaldatas


  }



  handleClick(evt) {
    // console.log('pp', evt)
    // var tablename = evt.label.toLowerCase()
    // console.log('evt.label.toLowerCase()', evt.label.toLowerCase())
    // this.toolswdg.current.setState({ 'currentwdg': tablename })
    if (evt.class) {
      this.setState({ currentwdg: evt.class })
    } else {
      this.setState({ currentwdg: null })
    }

  }


  render() {
    // let curentreact = null
    // if (!this.state.currentwdg === null) {
    //   curentreact = <this.state.currentwdg />
    // }
    // let curentreact = (!this.state.currentwdg === null) ? < { this.state.currentwdg } /> : null
    console.log(this.state.currentwdg)



    return (
      // <div style={{ width: '100%', backgroundColor: 'darkgray ' }}>

      < div className="row " style={{ height: '100%' }}>
        {/* <div className="col-4 border bg-light"> */}
        <div className="col-4">
          <TreeMenu data={this.finaldatas} onClickItem={this.handleClick.bind(this)} initialOpenNodes={['TOTO', 'Ressources']} />
        </div>
        {/* <div className="col-6 border bg-light"> */}
        <div className="col">
          {(this.state.currentwdg === null) ? < div></div> : <this.state.currentwdg />}
        </div>
      </div>

    )
  }

}

export default ToolTreeWidgetReact;
