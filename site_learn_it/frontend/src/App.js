import React, { Component } from 'react';
import { BrowserRouter, Switch } from 'react-router-dom'
import { Route, Link } from 'react-router-dom'


import  Main from './Main'
import './App.css';
import CoursesList from './Courses'
import Course from './Course'

import FormContainer from "./containers/CreateCourseFormContainer";
import EditFormContainer from "./containers/EditCourseFormContainer";


const BaseLayout = () => (
  <div className="container-fluid">
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand" href="/">Learn IT</a>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div className="navbar-nav">
          <a className="nav-item nav-link" href="/courses">Курсы</a>
          <a className="nav-item nav-link" href="/contacts">Контакты</a>
        </div>
      </div>
    </nav>

    <div className="content">
      <Switch>
        <Route path="/" exact component={Main} />
        <Route path="/courses" exact component={CoursesList} />
        <Route path="/course/:pk" exact component={Course} />
        <Route path="/courses/edit/:pk" exact component={EditFormContainer} />
        <Route path="/courses/create" exact component={FormContainer} />
      </Switch>
    </div>
  </div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;