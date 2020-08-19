
const React = require('react');
const { SideBar } = require('qwc2/components/SideBar');
const { setCurrentTask } = require('qwc2/actions/task');
// import ToolTreeWidgetReact from './tooltreewidget'
const ToolTreeWidgetReact = require('./tooltreewidget')

class Lamia extends React.Component {
    static propTypes = {}

    static defaultProps = {
        width: '45em',
        minWidth: '30em'
    }

    state = {}

    constructor(props) {
        super(props);

    }

    renderBody = () => {
        // return <p>ozieproi</p>
        return (<ToolTreeWidgetReact />)
    }

    render() {
        console.log('render Lamia')

        let extraTitlebarContent = null;
        extraTitlebarContent = (<p>porer</p>)

        let tooltree = (<ToolTreeWidgetReact />)
        console.log('tooltree', tooltree)

        return (
            <div>
                <SideBar id="Lamia" width={this.state.sidebarwidth || this.props.width}
                    title="test" icon="layers"
                // extraBeforeContent={visibilityCheckbox}
                // onHide={this.hideLegendTooltip} 
                // extraTitlebarContent={extraTitlebarContent}
                >
                    <div role="body" >
                        {tooltree}
                        {/* <p>ozefpok</p> */}
                        {/* <ToolTreeWidgetReact /> */}
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

}

module.exports = {
    LamiaPlugin: Lamia
}