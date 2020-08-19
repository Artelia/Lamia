/**
 * Copyright 2016, Sourcepole AG.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');
const ReactDOM = require('react-dom');
//popo

const appConfig = require('./appConfig');
const StandardApp = require('qwc2/components/StandardApp');
require('../icons/build/qwc2-icons.css');

// import 'bootstrap/dist/css/bootstrap.min.css';
// import 'bootstrap';

const bootstrap = require('bootstrap')
require('bootstrap/dist/css/bootstrap.min.css')


themes = JSON.parse(JSON.parse(document.getElementById('themes').textContent))

ReactDOM.render(
    <StandardApp appConfig={appConfig} themes={themes} style={{ position: "relative", top: "50px" }} />,
    document.getElementById('container')
);
