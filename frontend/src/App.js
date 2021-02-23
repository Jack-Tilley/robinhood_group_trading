import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Activate from "./pages/Activate";
import ResetPassword from "./pages/ResetPassword";
import ResetPasswordConfirm from "./pages/ResetPasswordConfirm";
// import Facebook from "./pages/Facebook";
// import Google from "./pages/Google";

import { createMuiTheme, ThemeProvider } from "@material-ui/core/styles";
import purple from "@material-ui/core/colors/purple";
import green from "@material-ui/core/colors/green";
import blue from "@material-ui/core/colors/blue";
import red from "@material-ui/core/colors/red";

import { Provider } from "react-redux";
import store from "./store";

import Layout from "./hocs/Layout";
import Appbar from "./components/Appbar";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: blue[200],
    },
    secondary: {
      main: red[500],
    },
  },
});

const App = () => (
  <ThemeProvider theme={theme}>
    <Provider store={store}>
      <Router>
        <Appbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/signup" component={Signup} />
          {/* <Route exact path="/facebook" component={Facebook} />
          <Route exact path="/google" component={Google} /> */}
          <Route exact path="/reset-password" component={ResetPassword} />
          <Route
            exact
            path="/password/reset/confirm/:uid/:token"
            component={ResetPasswordConfirm}
          />
          <Route exact path="/activate/:uid/:token" component={Activate} />
        </Switch>
      </Router>
    </Provider>
  </ThemeProvider>
);

export default App;

// {/* <Router>
//   <Layout>
//     <Switch>
//       <Route exact path="/" component={Home} />
//       <Route exact path="/login" component={Login} />
//       <Route exact path="/signup" component={Signup} />
//       {/* <Route exact path="/facebook" component={Facebook} />
//           <Route exact path="/google" component={Google} /> */}
//       <Route exact path="/reset-password" component={ResetPassword} />
//       <Route
//         exact
//         path="/password/reset/confirm/:uid/:token"
//         component={ResetPasswordConfirm}
//       />
//       <Route exact path="/activate/:uid/:token" component={Activate} />
//     </Switch>
//   </Layout>
// </Router>; */}
