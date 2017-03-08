import React from 'react';
import { Route, IndexRoute } from 'react-router';
import App from './components/App';
import Home from './components/homepage/Home';
import Documents from './containers/documents/Documents-list';


export default (
  <Route path='/' component={App} >
    <IndexRoute component={Home} />
    <Route path='documents' component={Documents} />
  </Route>
)
