import React from 'react';
import LamiaField from '../widgets/lamiafield'


class PhotoWdg extends React.Component {
  
    static firstdir = 'Ressources'
    static seconddir = 'Photo'

    constructor (props) {
        super(props);

    }

    render() {
        console.log(this.state)
        return (
            <div style={{width:'100%'}}>
            <LamiaField name={'Date'} field={'datetimecreation'} table={'Photo'} state={this.state}/>
            <LamiaField name={'File'} field={'file'} table={'Photo'} state={this.state}/>
        </div>
             )
    }

}

export default PhotoWdg;