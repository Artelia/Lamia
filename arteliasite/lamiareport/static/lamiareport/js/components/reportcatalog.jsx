const React = require('react');
const path = require('path');
const url = require('url');
const fileDownload = require('js-file-download')
const axios = require('axios');
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

class ReportCatalog extends React.Component {

    constructor(props) {
        super()
        this.state = { bboxids: [], jsonfiltered: [] }
        this.sortmethod = 'date'
    }

    shouldComponentUpdate(nextProps, nextState) {
        // console.log('sould*', this.state === nextState)
        // console.log('sould* bbox', this.props.bbox === nextProps.bbox)
        // if (this.state === nextState) {
        if (this.props.bbox !== nextProps.bbox) {
            // this.getPksWithinBbox()
            this.getJsonfeaturesWithinBBox()
            return false
        }
        return true
    }

    generateThumb() {
        let arreturn = []
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        const locale = navigator ? navigator.language || navigator.browserLanguage : "en"
        for (const idx in this.state.jsonfiltered) {
            let filteredfeat = this.state.jsonfiltered[idx]
            // console.log(filteredfeat)
            arreturn.push(
                <div className="col-md-4"
                    id={filteredfeat.id}
                    key={'mainthumb' + filteredfeat.id}
                    style={{ padding: '5px', zIndex: '0' }}
                    onMouseEnter={this.handleBoxToggle}
                    onMouseLeave={this.handleBoxToggleLeave}
                >
                    <div className="product py-1"
                        style={{ zIndex: '0', backgroundColor: 'rgba(0,55,90,0.5)', borderRadius: '5px', position: 'relative' }}
                    // onMouseEnter={this.handleBoxToggle}
                    // onMouseLeave={this.handleBoxToggleLeave}
                    >
                        <span style={{ fontSize: '10px' }}>{new Date(filteredfeat.properties.datetimeresource).toLocaleDateString(locale, options)}</span>
                        <div className="about text-center">
                            <span style={{ fontSize: '14px' }} >{filteredfeat.properties.name}</span>
                        </div>
                        <div className="cart-button mt-3 px-2 d-flex justify-content-between align-items-center">
                            <button style={{ fontSize: '12px' }} filename={filteredfeat.properties.file} className="btn btn-primary text-uppercase" onClick={this.reportButtonclicked.bind(this)}>View</button>
                        </div>
                    </div>
                </div>
            )
        }
        return arreturn
    }



    render() {
        return (
            <div>
                <div className="row g-2" >
                    <div className="btn-group mr-2 py-1" role="group" aria-label="First group">
                        <div className="dropdown">
                            <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                Sort by ...
                            </button>
                            <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                <a className="dropdown-item" id="date" onClick={this.sortChanged.bind(this)}                                >
                                    Date
                                </a >
                                <a className="dropdown-item" id="name" onClick={this.sortChanged.bind(this)}                                >
                                    Name
                                </a >
                            </div>
                        </div>
                    </div>
                </div>

                <div className="row g-2" style={{ overflowY: 'scroll', maxHeight: 'calc(100vh - 130px)' }}>
                    {this.generateThumb()}
                </div>
            </div>
        )
    }

    handleBoxToggle = (evt) => {
        let actualnode = evt.target
        while (!actualnode.id) {
            actualnode = actualnode.parentNode
        }
        this.props.reportidHovered(actualnode.id)
    }

    handleBoxToggleLeave = (evt) => {
        // console.log('leave')
        this.props.reportidHovered(null)
    }

    sortChanged = (evt) => {
        console.log(evt.target.id)
        this.sortmethod = evt.target.id
        this.getJsonfeaturesWithinBBox()
    }

    async getPksWithinBbox() {
        if (true) {
            let url = 'http://' + window.location.host + '/lamiaapi/' + this.props.mainiface.projectdata.id_project + '/report'
            let res = await axios.post(url, {
                function: 'bboxfilter',
                bbox: this.props.bbox,
            })

            if (res.data !== this.state.bboxids) {
                this.setState({ bboxids: res.data })
            }
        }
    }

    getJsonfeaturesWithinBBox = () => {
        if (!this.props.geojsonfeat) {
            return
        }

        let jsonfiltered = this.props.geojsonfeat.filter((feat) => {
            return (
                feat.bbox[0] > this.props.bbox[0]
                && feat.bbox[1] > this.props.bbox[1]
                && feat.bbox[2] < this.props.bbox[2]
                && feat.bbox[3] < this.props.bbox[3]
            );
        });
        if (this.sortmethod === 'date') {
            jsonfiltered.sort((a, b) => {
                return (new Date(b.properties.datetimeresource) - new Date(a.properties.datetimeresource))
            })
        } else if (this.sortmethod === 'name') {
            jsonfiltered.sort((a, b) => {
                if (a.properties.name < b.properties.name) {
                    return -1;
                }
                if (b.properties.name < a.properties.name) {
                    return 1;
                }
                return 0;
            })
        }
        this.setState({ jsonfiltered: jsonfiltered })

    }

    async reportButtonclicked(evt) {
        const destfilename = evt.target.getAttribute('filename')
        let baseurl = ("http://" + window.location.host + '/media/'
            + this.props.mainiface.projectdata.pgdbname + '/' + this.props.mainiface.projectdata.pgschema + '/')
        let urljoined = url.resolve(baseurl, destfilename);
        let awsreporturl = await axios.post(urljoined)
        window.open(awsreporturl.data)


    }

}

module.exports = ReportCatalog