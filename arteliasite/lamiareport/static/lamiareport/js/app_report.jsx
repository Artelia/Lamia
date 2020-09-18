/**
 * Copyright 2016, Sourcepole AG.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');
const ReactDOM = require('react-dom');
const ReportIFace = require('./ReportIFace');

ReactDOM.render(
    <ReportIFace />,
    document.getElementById('container')
);
