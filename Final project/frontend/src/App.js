import React from "react";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom"
import Home from "./components/Home"
import Divider from "./components/Divider"

class App extends React.Component {
  render() {
    return(
      <Router>
        <Switch>
          <Route path="/divider">
            <Divider />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </Router>
    );
  }
}

export default App;
