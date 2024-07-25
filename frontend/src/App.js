import logo from './logo.svg';
import React, { useState } from 'react';
import './App.css';

function App() {
    const [showChat, setShowChat] = useState(false);

  return (
      <div className="App">
        <h1>Welcome to Vidi</h1>
        <button className="chat-icon" onClick={() => setShowChat(true)}>💬</button>
        {showChat && (
            <div className="chat-popup">
              <div className="chat-header">
                <h3>Chat with Us!</h3>
                <button onClick={() => setShowChat(false)} className="close-button">✖</button>
              </div>
              <iframe
                  src="http://localhost:8501"
                  height="550"
                  width="1000"
                  title="Chat"
              ></iframe>
            </div>
        )}
      </div>
  );
}

export default App;
