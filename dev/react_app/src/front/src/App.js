import React, { Component } from 'react';
import './App.css';
import UploadForm from "./containers/UploadForm";
import Root from "./Root";


class App extends Component {
  render() {
    return (
      <Root>
      <div className="App">
        <UploadForm/>
      </div>
      </Root>
    );
  }
}

export default App;
