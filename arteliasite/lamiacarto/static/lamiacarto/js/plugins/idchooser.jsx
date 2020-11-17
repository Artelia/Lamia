const React = require('react');

class IdChooser extends React.Component {

    constructor(props) {
        super(props);
        this.state = { ids: {} }
    }

    render() {
        return (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Ids
                    </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {this.createIdDrop.bind(this)()}
                    </div>
                </div>
            </div>

        )

    }

    createIdDrop() {
        if (!this.state.ids.pk) {
            return []
        }
        let finaldatas = []

        for (var key in Object.keys(this.state.ids.pk)) {
            finaldatas.push(<a className="dropdown-item" id={this.state.ids.pk[key]} key={key}
                onClick={this.handleLayerChanged.bind(this)}
            >
                {this.state.ids.id[key]}
            </a >
            )
        }
        return finaldatas
    }

    handleLayerChanged = (e) => {
        this.props.mainiface.currentwdginstance.displayProperties(e.target.id)
    }

}

module.exports = IdChooser;