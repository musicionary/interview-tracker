import React, { Component } from 'react';
import { connect } from 'react-redux';
import { fetchDocuments } from '../actions/index';

class Documents extends Component {
  componentWillMount() {
    this.props.fetchDocuments();
  }
  render() {
    return (
      <div>
        <h1>Documents</h1>
      </div>

    );
  }
}

export default connect(null, );
