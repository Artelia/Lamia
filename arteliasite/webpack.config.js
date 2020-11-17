const webpack = require('webpack');
const path = require('path');
const os = require('os');
// const BundleTracker = require('webpack-bundle-tracker');
const styleConfig = require("./lamiacarto/qwc2config/styleConfig");

const nodeEnv = process.env.NODE_ENV || 'development';
const isProd = nodeEnv === 'production';


let styleReplacements = Object.keys(styleConfig).map(key => ({ search: "@" + key + "@", replace: styleConfig[key], flags: "g" }));

const plugins = [
  // new BundleTracker({ filename: './lamiacarto/webpack-stats.json' }),
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

if (!isProd) {
  plugins.push(new webpack.HotModuleReplacementPlugin());
}

module.exports = {
  context: __dirname,

  devtool: isProd ? 'source-map' : 'eval',
  mode: nodeEnv === "production" ? "production" : "development",
  entry: {
    'webpack-dev-server': 'webpack-dev-server/client?http://0.0.0.0:3233',
    'webpack': 'webpack/hot/only-dev-server',
    'QWC2App': path.join(__dirname, "lamiacarto", "static", "lamiacarto", "js", "app_carto"),
    'LamiaReport': path.join(__dirname, "lamiareport", "static", "lamiareport", "js", "app_report")
  },
  output: {
    path: path.join(__dirname, "staticbundles", 'bundles'),
    // publicPath: "/dist/",
    // publicPath: "/static/lamiacarto/dist/",
    filename: '[name].js'
  },
  plugins,
  resolve: {
    extensions: [".mjs", ".js", ".jsx"],
    symlinks: false,
    alias: {
      qwc2: path.resolve(__dirname, 'qwc2'),
      lamiacarto: path.resolve(__dirname, 'lamiacarto'),
    }
  },
  module: {
    rules: [
      {
        test: /\.(woff|woff2)(\?\w+)?$/,
        use: {
          loader: "url-loader",
          options: {
            limit: 50000,
            mimetype: "application/font-woff",
            name: "fonts/[name].[ext]",
          }
        }
      },
      {
        test: /\.css$/,
        use: [
          { loader: 'style-loader' },
          { loader: 'css-loader' },
          { loader: 'string-replace-loader', options: { multiple: styleReplacements } }
        ]
      },
      {
        test: /\.(ttf|eot|svg)(\?v=[0-9].[0-9].[0-9])?$/, use: {
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
            esModule: false
          }
        }
      },
      {
        test: /\.(png|jpg|gif)$/, use: {
          loader: 'url-loader',
          options: {
            name: '[path][name].[ext]',
            limit: 8192,
            esModule: false
          }
        }
      },
      {
        test: /\.jsx?$/,
        exclude: os.platform() === 'win32' ? /node_modules\\(?!(qwc2)\\).*/ : /node_modules\/(?!(qwc2)\/).*/,
        use: {
          loader: 'babel-loader',
          options: { babelrcRoots: ['.', path.resolve(__dirname, 'node_modules', 'qwc2')] }
        }
      },
      {
        test: /\.mjs$/,
        type: 'javascript/auto',
      }
    ]
  },
  devServer: {
    hot: true,
    contentBase: './',
    writeToDisk: true,
  }
};
