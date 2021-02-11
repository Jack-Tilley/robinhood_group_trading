import "./App.css";
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import ResetPassword from "./pages/ResetPassword";
import ResetPasswordConfirm from "./pages/ResetPasswordConfirm";
import Activate from "./pages/Activate";

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/signup" component={Signup} />
        <Route exact path="/reset-password" component={ResetPassword} />
        <Route
          exact
          path="/password/reset/confirm/:uid/:token"
          component={ResetPasswordConfirm}
        />
        <Route exact path="/activate/:uid/:token" component={Activate} />
      </Switch>
    </Router>
  );
};

export default App;
