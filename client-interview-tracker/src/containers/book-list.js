import React, { Component } from 'react';
import { connect } from 'react-redux';
// this is used to make sure action flows through reducers.
import { bindActionCreators } from 'redux';
import { selectBook } from '../actions/index';

class BookList extends Component {
  renderList() {
    return this.props.books.map((book) => {
      return (
        <li
          onClick={() => this.props.selectBook(book)}
          className="list-group-item"
          key={book.title}>
          {book.title}
        </li>
      );
    });
  }

  render() {
    return (
      <ul className="list-group col-sm-4">
        {this.renderList()}
      </ul>
    )
  }
}

//this is the glue between react and redux
// if the state changes, this function immediately re-renders the object
function mapStateToProps(state) {
  //Whatever object is return will show up as props inside of BookList
  return {
    books: state.books
  };
}

// Anything returned from this function will end up as props on Booklist container
function mapDispatchToProps(dispatch) {
  // whenever selectBook is called, the result should be passed to all of our reducers

  // value is the action created imported from actions directory
  // dispatch function receives actions and spits them out to the reducers
  return bindActionCreators({ selectBook: selectBook }, dispatch);
}

// connect takes a function and a component and produces a container
// container is a component that is aware of the state from redux
export default connect(mapStateToProps, mapDispatchToProps)(BookList);
