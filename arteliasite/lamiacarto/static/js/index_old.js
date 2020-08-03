import React from 'react'
import ReactDOM from 'react-dom'


function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
//popo

const element = <Welcome name="world" />;
ReactDOM.render(
  element,
  document.getElementById('react')
);