// src/Routes.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import ChoreList from './components/ChoreList';
import Login from './components/Login';

const Routes: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/chorelist" component={ChoreList} />
        <Route path="/login" component={Login} />
        <Route path="/chores" component={Chore} />
      </Switch>
    </Router>
  );
};

export default Routes;
