const { merge } = require('webpack-merge');
const config = require('./webpack.config.js');


const webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const path = require('path');
const nodeEnv = process.env.NODE_ENV || 'development';
const isProd = nodeEnv === 'production';

config.output.path = path.join(__dirname, "lamiacarto", "static", "lamiacarto", 'prod');
config.entry = { 'QWC2App': path.join(__dirname, "lamiacarto", "static", "lamiacarto", "js", "app") }

config.plugins = [
    new BundleTracker({ filename: './lamiacarto/webpack-stats-prod.json' }),
    new webpack.DefinePlugin({
        'process.env': { NODE_ENV: JSON.stringify(nodeEnv) }
    }),
    new webpack.NamedModulesPlugin(),
    new webpack.DefinePlugin({
        "__DEVTOOLS__": !isProd
    }),
    new webpack.NormalModuleReplacementPlugin(/openlayers$/, path.join(__dirname, "qwc2", "libs", "openlayers")),
    new webpack.NoEmitOnErrorsPlugin(),
    new webpack.LoaderOptionsPlugin({
        debug: !isProd,
        minimize: isProd
    })
];

module.exports = merge(config, { mode: 'production', });