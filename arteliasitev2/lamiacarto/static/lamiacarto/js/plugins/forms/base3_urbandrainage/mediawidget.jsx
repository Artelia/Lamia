// import EditingFormReact from '../editingformwidget'
const EditingFormReact = require('../editingformwidget')
// import $ from 'jquery';
const $ = require('jquery')
// import ReactDOM from "react-dom";
//

class MediaEditingFormReact extends EditingFormReact {

    static firstdir = 'Resources'
    static label = 'Media'
    table = 'media'

    projectdata = JSON.parse(JSON.parse(document.getElementById('context').textContent))

    constructor(props) {
        super(props);
        this.state = { 'currentlayer': '', 'currentfeatprop': {}, 'formui': ':/static/forms/base3/qgswidgets/lamia_form_camera_ui.ui' }
        // let olcanvas = new OLCanvasReact()
        // console.log('ol', olcanvas)
    }



    componentWillUpdate(nextProps, nextState) {
        console.log('next', nextState)
        console.log('next', nextState.currentfeatprop.file)

        if (nextState.currentfeatprop.file !== this.state.currentfeatprop.file) {

            console.log('***', $('div[name="frame_ph"]'))
            let url = ("http://" + window.location.host + '/media/'
                + this.projectdata.pgdbname + '/' + this.projectdata.pgschema + '/'
                + nextState.currentfeatprop.file)
            // $('div[name="frame_ph"]')
            // $('#theDiv').prepend($('<img>',{id:'theImg',src:'theImg.png'}))
            $("#lamiamedia").remove();
            $('div[name="frame_ph"]').prepend($('<img>', { id: 'lamiamedia', src: url, width: 200 }))
        }
    }

    render() {
        console.log('media render')
        let res = super.render()
        return res

    }

    domLoaded() {
        console.log('okok media')
        // console.log($('#spinBox_numphoto'))
        console.log('***', $('div[name="frame_ph"]'))

        let url = ("http://" + window.location.host + '/media/'
            + this.projectdata.pgdbname + '/' + this.projectdata.pgschema + '/'
            + $('input[name="file"]').val())


    }

    // async componentDidMount() {
    //     // console.log('media componentDidMount')
    //     // await this.currentform.current.componentDidMount()

    //     // console.log('media componentDidMount2')
    //     // let node = ReactDOM.findDOMNode(this);
    //     // console.log(node.querySelector('[name="spinBox_numphoto"]'))

    // }

    componentDidUpdate() {
        // console.log('media componentDidUpdate')
        // $(document).ready(function () {

        //     // jQuery methods go here...
        //     console.log($('popo', 'input[name="spinBox_numphoto"]'))
        // });
        // let node = ReactDOM.findDOMNode(this);
        // console.log(node.querySelector('[name="spinBox_numphoto"]'))



        // var $this = $(ReactDOM.findDOMNode(this));
        // console.log(this.getDOMNode())
        // console.log($('#spinBox_numphoto'))
        // console.log(this.props.children)
        // // console.log($(node))
        // console.log('***', $('input[name="spinBox_numphoto"]'))
        // // console.log($(node).get('[name="spinBox_numphoto"]'))
        // console.log($("*"))

    }

}

// export default MediaEditingFormReact;
module.exports = MediaEditingFormReact;