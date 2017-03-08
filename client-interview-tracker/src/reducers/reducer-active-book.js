//all reducers get two arguments: current state and action
// only called when an action occurs.  so we need to specify the action.
// state argument is not app state.  It's only the state this reducer is responsible for.
export default function(state = null, action) {
  switch (action.type) {
    case 'BOOK_SELECTED':
      //return the selected book
      return action.payload;
  }
  //if we don't care about current action - pass the state through
  return state;
}
