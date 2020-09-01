import React from 'react';
import LamiaCombo from './widgets/combo'
import InfralineaireWdg from './workwidgets/infralineaire'
import PhotoWdg from './workwidgets/photo'
import EquipementWdg from './workwidgets/equipement'


class ToolsWidgetReact extends React.Component {

    static workclasses = { 'infralineaire': InfralineaireWdg,
                        'photo': PhotoWdg,
                        'equipement': EquipementWdg,

    }
  
    constructor (props) {
        super(props);
        this.state={currentwdg:''};
        this.dbasetables = this.props.mainiface.dbasetables

        this.currentwdg = React.createRef()

        this.workwdg = { 'infralineaire': <InfralineaireWdg mainiface={this.props.mainiface} ref={this.currentwdg}/>,
                        'photo':          <PhotoWdg mainiface={this.props.mainiface}  ref={this.currentwdg}/>,
                        'equipement':          <EquipementWdg mainiface={this.props.mainiface}  ref={this.currentwdg}/>,

        }
    }



    componentDidMount() {
      console.log('tools mounted')

    }
    
    render() {
      // console.log('render tools', this.state.currentwdg)
      // console.log('oo', ToolsWidgetReact.workclasses[this.state.currentwdg])
      
      return (
        <div style={{width:'100%' , height:'100%', backgroundColor:'lightgray '}}>
          {this.workwdg[this.state.currentwdg]}
        </div>
      )
    }
  }

  export default ToolsWidgetReact;