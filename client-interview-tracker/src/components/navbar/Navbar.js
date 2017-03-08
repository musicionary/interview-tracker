import React, { Component } from 'react';
import { Link } from 'react-router';

class Navbar extends Component {
  render() {
    return (
      <header>
        <nav>
          <div className="nav-wrapper blue darken-3">
            <Link to='/' className="brand-logo">Interview Tracker</Link>
            <ul id="nav-mobile" className="right hide-on-med-and-down">
              <li><Link to="documents">Documents</Link></li>
              <li><a href="">About</a></li>
              <li><a href="">Contact</a></li>
            </ul>
          </div>
        </nav>
      </header>
    );
  }
}

export default Navbar;
