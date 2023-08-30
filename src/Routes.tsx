// src/Routes.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';

const Routes: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/chorelist" component={About} />
        <Route path="/login" component={Contact} />
      </Switch>
    </Router>
  );
};

export default Routes;
