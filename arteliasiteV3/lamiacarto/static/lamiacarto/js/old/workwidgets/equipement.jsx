import React from 'react';
import LamiaField from '../widgets/lamiafield'


class EquipementWdg extends React.Component {
  
    static firstdir = 'Description'
    static seconddir = 'Equipement'

    constructor (props) {
        super(props);

    }

    render() {
        console.log(this.state)
        return (
            <div style={{width:'100%'}}>
            <LamiaField name={'Date'} field={'id_equipement'} table={'Equipement'} state={this.state}/>
        </div>
             )
    }

}

export default EquipementWdg;