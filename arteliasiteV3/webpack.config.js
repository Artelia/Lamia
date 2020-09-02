var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: './lamiacarto/static/lamiacarto/js/index',

  output: {
    path: path.resolve('./lamiacarto/static/lamiacarto/bundles/'),
    filename: "[name]-[hash].js",
  },
  

  plugins: [
    new BundleTracker({ filename: './lamiacarto/webpack-stats.json' }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
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
        test: /\.ui$/i,
        use: 'raw-loader',
      },
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx'],
    //alias: {
    //  forms: path.resolve(__dirname, '..', 'Lamia/worktypeconf/'),
    //},
  }

};