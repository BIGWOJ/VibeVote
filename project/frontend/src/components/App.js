import React, { Component } from 'react';
import { createRoot } from 'react-dom/client';

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (<h1>Testing</h1>);
    }
}

const app_div = document.getElementById('app');
const root = createRoot(app_div);
root.render(<App />);