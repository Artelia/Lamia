const React = require('react');
const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

const LayerUtils = require("qwc2/utils/LayerUtils");
const { searchSubLayer } = require('qwc2/utils/LayerUtils');

class StyleChooser extends React.Component {

    constructor(props) {
        super(props);
        this.state = { styles: {} }
        // this.styles = null
    }

    render() {
        console.log('stylerend')
        return (
            <div className="btn-group mr-2" role="group" aria-label="toto group">
                <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Styles
                    </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {this.createStyleDrop.bind(this)()}
                    </div>
                </div>
            </div>

        )

    }

    componentDidMount() {
        this.loadStyles()
    }

    async loadStyles() {
        let stylesurl = 'http://' + window.location.host + '/lamiaapi/' + this.props.mainiface.projectdata.id_project + '/styles'
        let styles = await axios.get(stylesurl)
        console.log(styles)
        this.setState({ styles: styles.data })

    }

    createStyleDrop() {

        if (!this.state.styles) {
            return []
        }
        let finaldatas = []
        for (var item in this.state.styles) {
            finaldatas.push(<a className="dropdown-item" id={item} key={item}
                onClick={this.handleStyleChanged.bind(this)}
            >
                {item}
            </a >
            )
        }
        return finaldatas
    }

    handleStyleChanged = (e) => {
        // console.log('cl', e.target.id)
        const desttyle = e.target.id

        //searchSubLayer
        let layers = this.props.mainiface.props.layers
        console.log(layers)
        let lamialayer = null
        for (let layerid in Object.values(layers)) {
            // console.log(layerid)
            let layer = layers[layerid]
            // console.log(layer)
            if (layer.title.toLowerCase() === 'lamia') {
                lamialayer = layer
                break
            }
        }

        console.log('lamialayer', lamialayer)

        if (!lamialayer) { return }

        // const lamiasublayers = lamialayer.params.LAYERS.split(',')
        const lamiasublayers = lamialayer.sublayers


        let lamiasubstyle = []

        lamiasublayers.forEach((sublay, idx) => {

            if (this.state.styles[desttyle].includes(sublay.name.split('_')[0])) {
                lamiasubstyle.push(desttyle)
                lamialayer.sublayers[idx].style = desttyle
            } else {
                lamiasubstyle.push('default')
                lamialayer.sublayers[idx].visibility = false
                lamialayer.sublayers[idx].style = 'default'
            }
        })

        console.log(lamiasubstyle)

        // lamialayer.params.STYLES = lamiasubstyle.join(',')
        this.props.mainiface.props.changeLayerProperty(lamialayer.uuid, "params.styles", lamiasubstyle.join(','), [], null);
        console.log('layer', this.props.mainiface.props.layers)





        return


        // this.props.mainiface.currentwdginstance.displayProperties(e.target.id)
        if (this.props.layers[0] && this.props.layers[0].params) {
            console.log('*', this.props.layers[0].state)
            const lay = this.props.layers[0].params.LAYERS.split(',')
            // console.log(lay)
            let style = Array(lay.length).fill('default')
            style[3] = 'test1'

            // this.props.layers[0].params.STYLES = style.join(',')
            let uuid = this.props.layers[0].uuid
            // layer.uuid, "visibility", !oldvisibility, grouppath,
            this.props.layers[0].params.STYLES = style.join(',')
            this.props.changeLayerProperty(uuid, "params.styles", style.join(','), [], null);
            // this.props.changeLayerProperty(uuid, "styles", style[8], [8], null);

            console.log('layer', this.props.layers)

        }

    }

}

module.exports = StyleChooser;