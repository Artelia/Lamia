import React from 'react';
import LamiaField from '../widgets/lamiafield'


class InfralineaireWdg extends React.Component {

    static firstdir = 'Description'
    static seconddir = 'Infralineaire'
  
    constructor (props) {
        super(props);
        



    }



    render() {
        // console.log(this.state)
        return ( 
        <div style={{width:'100%'}}>
            
            <LamiaField name={'Type de digue'} field={'description1'} table={'Infralineaire'} state={this.state}/>
            <LamiaField name={'Sous-type de digue'} field={'description2'} table={'Infralineaire'} state={this.state}/>
            <LamiaField name={'Classement'} field={'classement'} table={'Infralineaire'} state={this.state}/>
            <LamiaField name={'ID'} field={'id_infralineaire'} table={'Infralineaire'} state={this.state}/>


        </div>
        )
    }

}

export default InfralineaireWdg;

