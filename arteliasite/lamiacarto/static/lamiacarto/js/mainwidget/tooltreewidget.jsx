import React from 'react';
// import TreeView from 'react-simple-jstree';

// import TreeView from '@material-ui/lab/TreeView';
// import TreeItem from '@material-ui/lab/TreeItem';
// import { makeStyles } from '@material-ui/core/styles';
// import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
// import ChevronRightIcon from '@material-ui/icons/ChevronRight';

// import Tree from '@naisutech/react-tree'
import TreeMenu from 'react-simple-tree-menu';
import '../../node_modules/react-simple-tree-menu/dist/main.css';


class ToolTreeWidgetReact extends React.Component {

  
    constructor (props) {
        super(props);
        this.mainiface = this.props.mainiface
        this.toolswdg = this.props.toolswdg

        this.state={'visualmode': 1}
        
        let workclasses = this.mainiface.toolsdom.type.workclasses

        this.finaldatas = this.getTreeDatas(workclasses)

    }

    getTreeDatas (workclasses) {
      let dataraw = {}
      for (const [key, value] of Object.entries(workclasses)) {
        if (!dataraw.hasOwnProperty(value.firstdir)) {
          dataraw[value.firstdir] = []
        }
        dataraw[value.firstdir].push(value.seconddir)
      }

      let finaldatas = {}

      for (var firstdir in dataraw){
        finaldatas[firstdir] = {label: firstdir,
                                nodes:{}};
        for (var seconddir in dataraw[firstdir]) {
          var seconddirvalue = dataraw[firstdir][seconddir]
          finaldatas[firstdir].nodes[seconddirvalue] = {label: seconddirvalue,
                                                  nodes:{}};
        }

      };
      return finaldatas


    }



    handleClick(evt) {
      // console.log('pp', evt)
      var tablename = evt.label.toLowerCase()
      this.toolswdg.current.setState({'currentwdg': tablename})
    }


    render() {
        return ( 
          <div style={{width:'100%', backgroundColor:'darkgray  '}}>
            <TreeMenu  data={this.finaldatas} onClickItem={this.handleClick.bind(this)} initialOpenNodes={['Description','Ressources']}/>
          </div>
        )
    }

}

export default ToolTreeWidgetReact;
