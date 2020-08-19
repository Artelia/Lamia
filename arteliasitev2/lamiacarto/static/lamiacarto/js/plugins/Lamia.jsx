
const React = require('react');
const { SideBar } = require('qwc2/components/SideBar');
const { setCurrentTask } = require('qwc2/actions/task');
// import ToolTreeWidgetReact from './tooltreewidget'
// const ToolTreeWidgetReact = require('./tooltreewidget')

const EdgeEditingFormReact = require('./forms/base3_urbandrainage/edgewidget')

class Lamia extends React.Component {
    static propTypes = {}

    static defaultProps = {
        width: '45em',
        minWidth: '30em'
    }

    workclasses = [
        EdgeEditingFormReact,
        // NodeEditingFormReact,
        // MediaEditingFormReact
    ]

    state = {}

    constructor(props) {
        super(props);
        this.state = { 'visualmode': 1, 'currentwdg': null }

    }

    renderBody = () => {
        // return <p>ozieproi</p>
        // return (<ToolTreeWidgetReact />)
        return (null)
    }

    render() {
        console.log('render Lamia')


        let dropdown = this.createToolbar.bind(this)()

        let layersdrop = (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <div className="dropdown">
                    <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Layers
              </button>
                    <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                        {dropdown}
                    </div>
                </div>
            </div>
        )

        let butonmenu = (
            <div className="btn-group mr-2" role="group" aria-label="First group">
                <button type="button" className="btn btn-secondary" id="canvaspick" onClick={this.onclick}>Pick</button>
                <button type="button" className="btn btn-secondary" onClick={this.onclick}>Middle</button>
                <button type="button" className="btn btn-secondary" onClick={this.onclick}>Right</button>
            </div>
        )

        let extraTitlebarContent = (
            <div className="btn-toolbar " role="group" aria-label="Basic example" style={{ marginLeft: "1em" }}>
                {layersdrop}
                {butonmenu}
            </div>
        );


        return (
            <div>
                <SideBar id="Lamia" width={this.state.sidebarwidth || this.props.width}
                    title="Lamia" icon="layers"
                    // extraBeforeContent={visibilityCheckbox}
                    // onHide={this.hideLegendTooltip} 
                    extraTitlebarContent={extraTitlebarContent}
                >
                    <div role="body" >
                        {/* {tooltree} */}
                        {(this.state.currentwdg === null) ? < div></div> : <this.state.currentwdg />}
                    </div>
                    {/* {() => ({
                        body: this.renderBody()
                    })} */}
                </SideBar>
                {/* {legendTooltip} */}
                {/* <LayerInfoWindow windowSize={this.props.layerInfoWindowSize} bboxDependentLegend={this.props.bboxDependentLegend} /> */}
            </div>
        );
    }

    createToolbar() {

        let dataraw = {}

        this.workclasses.forEach(function (reactclass, idx) {
            if (!dataraw.hasOwnProperty(reactclass.firstdir)) {
                dataraw[reactclass.firstdir] = {}
            }
            dataraw[reactclass.firstdir][reactclass.label] = reactclass
        });



        let finaldatas = []

        for (var firstdir in dataraw) {
            finaldatas.push(<h6 className="dropdown-header">{firstdir}</h6>)
            for (var seconddir in dataraw[firstdir]) {
                finaldatas.push(<a className="dropdown-item" id={dataraw[firstdir][seconddir].label} onClick={this.handleLayerChanged.bind(this)}>{seconddir}</a>)
                // finaldatas.push(<a className="dropdown-item" id={dataraw[firstdir][seconddir].label} >{seconddir}</a>)
            }
        };

        return finaldatas
    }

    handleLayerChanged(evt) {
        let goodclass = null
        this.workclasses.forEach(function (reactclass, idx) {
            if (reactclass.label === evt.target.id) {
                goodclass = reactclass
            }
        });
        this.setState({ currentwdg: goodclass })
    }

}

module.exports = {
    LamiaPlugin: Lamia
}