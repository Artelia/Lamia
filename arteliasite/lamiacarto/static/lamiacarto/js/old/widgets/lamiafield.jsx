import React from 'react';
import Flexbox from 'flexbox-react';

class LamiaField extends React.Component {
  
    static dbasetables =  require('../../dbasetables.json');

    constructor (props) {
        super(props);
        // name={'test'} field={'commentaire'} table={'infralineaire'} state={this.state}
        this.name = this.props.name
        this.field = this.props.field
        this.table = this.props.table
        
    }





    render() { 
        this.state = this.props.state
        let rows = [];
        let nothinselected = <div><p> Nothing selected </p></div>
        let tabledbasetable = LamiaField.dbasetables[this.table].fields;
        let features = null


        if (this.state === null) {
            rows.push( nothinselected)
        } else {
            // console.log(this.state)
            features = this.state.featureprops.features
            console.log('test', features.length , features.length === 0)
            if ( features.length === 0 ) {
                console.log('ok')
                rows.push(nothinselected )
            };
        };

        let datatype = 'txt'
        if (rows.length  === 0) {
            let featurevalue = features[0].properties[this.field]

            if (tabledbasetable.hasOwnProperty(this.field) 
                    && tabledbasetable[this.field].hasOwnProperty('Cst')) {
                datatype = 'combo'
                var cst = tabledbasetable[this.field].Cst
                var longname = cst.map(function(value,index) { return value[0]; });
                var shortname = cst.map(function(value,index) { return value[1]; });
                var longnamevalueindex = shortname.indexOf(featurevalue)
                var longnamevalue = longname[longnamevalueindex]

                longname.forEach(function (item) {
                    if (item == longnamevalue) {
                        rows.push(<option selected value={item} style={{fontFamily: 'Arial', fontSize:10 }} >{item}</option>);
                    } else {
                        rows.push(<option value={item} style={{fontFamily: 'Arial', fontSize:10 }} >{item}</option>);
                    };
                });

            } else {
                datatype = 'txt'
                rows.push(<p style={{fontFamily: 'Arial'}}>{featurevalue}</p>)

            };
        };

        let name = <p>{this.name}</p>

        if (datatype === 'combo') {
            return (
                <div style={{width:'100%' , height:'30px'}}>
                    <Flexbox flexDirection="row"  flexGrow={1} >
                        <Flexbox flexGrow={1}   flexBasis={'0'} flexShrink={'1'} >
                            {name}
                        </Flexbox>
                        <Flexbox flexGrow={2}   flexBasis={'0'} flexShrink={'1'} height={'30px'}>
                            <select style={{width:'100%', height:'30px'}}>
                                {rows}
                            </select>
                        </Flexbox>
                    </Flexbox>
                </div>
            )
        } else {
            return (
                <div style={{width:'100%' , height:'30px'}}>
                    <Flexbox flexDirection="row"  flexGrow={1} >
                        <Flexbox flexGrow={1}   flexBasis={'0'} flexShrink={'1'} >
                            {name}
                        </Flexbox>
                        <Flexbox flexGrow={2}   flexBasis={'0'} flexShrink={'1'}>
                            {rows}
                        </Flexbox>
                    </Flexbox>
                </div>
            )

        }

    }
}




export default LamiaField;