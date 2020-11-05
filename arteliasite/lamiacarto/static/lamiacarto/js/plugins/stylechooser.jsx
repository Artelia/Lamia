const React = require('react');
const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

const LayerUtils = require("qwc2/utils/LayerUtils");
const { searchSubLayer } = require('qwc2/utils/LayerUtils');

class StyleChooser extends React.Component {

    constructor(props) {
        super(props);
        // this.state = { styles: {} }
        // this.styles = null
    }

    render() {
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


    createStyleDrop() {

        if (!this.props.styles) {
            return []
        }
        let finaldatas = []
        for (var item in this.props.styles) {
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
        const desttyle = e.target.id
        this.props.mainiface.changeStyle.bind(this)(desttyle)
    }



}

module.exports = StyleChooser;