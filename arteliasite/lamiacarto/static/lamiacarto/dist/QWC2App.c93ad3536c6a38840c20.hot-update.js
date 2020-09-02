webpackHotUpdate("QWC2App",{

/***/ "./lamiacarto/static/lamiacarto/js/app.jsx":
/*!*************************************************!*\
  !*** ./lamiacarto/static/lamiacarto/js/app.jsx ***!
  \*************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("/**\n * Copyright 2016, Sourcepole AG.\n * All rights reserved.\n *\n * This source code is licensed under the BSD-style license found in the\n * LICENSE file in the root directory of this source tree.\n */\nvar React = __webpack_require__(/*! react */ \"./node_modules/react/index.js\");\n\nvar ReactDOM = __webpack_require__(/*! react-dom */ \"./node_modules/react-dom/index.js\"); //popo\n\n\nvar appConfig = __webpack_require__(/*! ./appConfig */ \"./lamiacarto/static/lamiacarto/js/appConfig.js\");\n\nvar StandardApp = __webpack_require__(/*! qwc2/components/StandardApp */ \"./qwc2/components/StandardApp.jsx\");\n\n__webpack_require__(/*! ../icons/build/qwc2-icons.css */ \"./lamiacarto/static/lamiacarto/icons/build/qwc2-icons.css\"); // import 'bootstrap/dist/css/bootstrap.min.css';\n// import 'bootstrap';\n\n\nvar bootstrap = __webpack_require__(/*! bootstrap */ \"./node_modules/bootstrap/dist/js/bootstrap.js\");\n\n__webpack_require__(/*! bootstrap/dist/css/bootstrap.min.css */ \"./node_modules/bootstrap/dist/css/bootstrap.min.css\");\n\ncontext = JSON.parse(JSON.parse(document.getElementById('themes').textContent));\nReactDOM.render( /*#__PURE__*/React.createElement(StandardApp, {\n  appConfig: appConfig,\n  themes: themes,\n  style: {\n    position: \"relative\",\n    top: \"50px\"\n  }\n}), document.getElementById('container'));\n\n//# sourceURL=webpack:///./lamiacarto/static/lamiacarto/js/app.jsx?");

/***/ })

})