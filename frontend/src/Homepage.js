import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./styles.css"; // Import CSS for styling

function HomePage() {
  const navigate = useNavigate();
  const [gridSize, setGridSize] = useState("10"); // Default grid size
  const [words, setWords] = useState("apple,banana,grape");

  const handleStartGame = (gameType) => {
    navigate(`/game/${gameType}?grid_size=${gridSize}&words=${words}`);
  };

  return (
    <div className="home-container">
      <h1>Select a Game</h1>

      <div className="form-group">
        <label>Grid Size:</label>
        <select value={gridSize} onChange={(e) => setGridSize(e.target.value)}>
          {Array.from({ length: 19 }, (_, i) => i + 2).map((size) => (
            <option key={size} value={size}>
              {size} × {size}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label>Words (comma-separated):</label>
        <input
          type="text"
          value={words}
          onChange={(e) => setWords(e.target.value)}
        />
      </div>

      <div className="button-group">
        <button className="start-button" onClick={() => handleStartGame("wordsearch")}>
          Start Word Search
        </button>
        <button className="start-button" onClick={() => handleStartGame("crossword")}>
          Start Crossword
        </button>
      </div>
    </div>
  );
}

export default HomePage;
