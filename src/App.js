import React from 'react';
import './assets/App.css';
import { HashRouter, Switch, Route } from 'react-router-dom';
// TODO: use BrowserRouter (requires server-side implementation)

import Home from './components/Home'
import Navbar from './components/Navbar';


function App() {
  return (
    <div className="App">
      <HashRouter>
        <Navbar />

        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>

      </HashRouter>
    </div>
  );
}

export default App;
