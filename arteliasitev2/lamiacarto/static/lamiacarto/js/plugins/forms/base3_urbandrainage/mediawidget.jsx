// import EditingFormReact from '../editingformwidget'
const EditingFormReact = require('../editingformwidget')
// import $ from 'jquery';
const $ = require('jquery')
// import ReactDOM from "react-dom";
//

class MediaEditingFormReact extends EditingFormReact {

    static firstdir = 'Resources'
    static label = 'Media'
    static table = 'media'

    constructor(props) {
        super(props);
        this.state = { 'currentlayer': '', 'currentfeatprop': {}, 'formui': ':/static/forms/base3/qgswidgets/lamia_form_camera_ui.ui' }
        // let olcanvas = new OLCanvasReact()
        // console.log('ol', olcanvas)
    }

    render() {
        console.log('media render')
        let res = super.render()
        return res

    }

    domLoaded() {
        console.log('okok media')
        console.log($('#spinBox_numphoto'))
        console.log('***', $('input[name="spinBox_numphoto"]'))
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