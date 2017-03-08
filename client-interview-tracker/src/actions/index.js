//create the action

export const FETCH_DOCUMENTS = 'FETCH_DOCUMENTS';


export function fetchDocuments(book) {
  //select book is an action creator.  it needs to return an action -> an object with a type property
  return {
    //every action must have a type that describes the purpose of the action
    //type is always uppercase.
    type: 'BOOK_SELECTED',
    // the payload is the data
    payload: book
  };
}
