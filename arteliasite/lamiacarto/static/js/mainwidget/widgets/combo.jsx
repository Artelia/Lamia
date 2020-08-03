import React from 'react';
import Flexbox from 'flexbox-react';

class LamiaCombo extends React.Component {
  
    constructor (props) {
        super(props);
    }



    render() { 

        var rows=[];
        var propvalue = this.props.valueprop;
        this.props.options.forEach(function (item) {
            // console.log(item, propvalue, item==propvalue)
            if (item == propvalue) {
                rows.push(<option selected value={item} style={{fontFamily: 'Arial', fontSize:10 }} >{item}</option>);
            } else {
                rows.push(<option value={item} style={{fontFamily: 'Arial', fontSize:10 }} >{item}</option>);
            };
        });
                            
        return( <Flexbox flexDirection="row"  flexGrow={1} >
                    <Flexbox flexGrow={1}   flexBasis={'0'} flexShrink={'1'} >
                        <p style={{fontFamily: 'Arial', fontSize:10 }}>{this.props.name}</p>
                    </Flexbox>
                    <Flexbox flexGrow={1}   flexBasis={'0'} flexShrink={'1'}>
                        <select name={this.props.name} id={this.props.name}>
                            {rows}
                        </select>
                    </Flexbox>
                </Flexbox>
            )

    }


}

export default LamiaCombo;