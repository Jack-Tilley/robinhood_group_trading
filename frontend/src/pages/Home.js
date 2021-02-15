import React, { useState } from "react";
import { Link, Redirect } from "react-router-dom";
import { logout } from "../actions/auth";
import { connect } from "react-redux";

const Home = ({ isAuthenticated, logout }) => {
  const [redirect, setRedirect] = useState(false);

  const logout_user = () => {
    logout();
    setRedirect(true);
  };

  const loggedInLinks = () => (
    <a className="btn btn-primary btn-lg" href="/" onClick={logout_user}>
      Logout
    </a>
    // <Link className="btn btn-primary btn-lg" to="/" role="button">
    //   Login
    // </Link>
  );

  const loggedOutLinks = () => (
    <Link className="btn btn-primary btn-lg" to="/login" role="button">
      Login
    </Link>
  );
  return (
    <>
      <div className="container">
        <div className="jumbotron mt-5">
          <h1 className="display-4">Welcome to Auth System!</h1>
          <p className="lead">
            This is an incredible authentication system with production level
            features!
          </p>
          <hr className="my-4" />
          {/* <p>Click the Log In button</p> */}
          {isAuthenticated ? loggedInLinks() : loggedOutLinks()}
        </div>
      </div>
      {redirect ? <Redirect to="/" /> : <></>}
    </>
  );
};
const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { logout })(Home);
