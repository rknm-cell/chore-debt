// src/Routes.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import ChoreList from './components/ChoreList';
import Login from './components/Login';
import ChoreCard from './components/ChoreCard';

const Routes: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/chorelist" component={ChoreList} />
        <Route path="/login" component={Login} />
        <Route path="/chores" component={ChoreCard} />
      </Switch>
    </Router>
  );
};

export default Routes;
