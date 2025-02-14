import React, { useState } from "react"; // Import React and useState hook for state management
import { useNavigate } from "react-router-dom"; // Import useNavigate for navigation
import "./styles.css"; // Import CSS file for styling

function HomePage() {
  // useNavigate hook to handle navigation between pages
  const navigate = useNavigate();

  // State for grid size, initialized with a default value of "10"
  const [gridSize, setGridSize] = useState("10");

  // State for words input, initialized with some default words
  const [words, setWords] = useState("apple,banana,grape");

  // Function to handle game start, navigating to the appropriate game page
  const handleStartGame = (gameType) => {
    navigate(`/game/${gameType}?grid_size=${gridSize}&words=${words}`);
    // Navigates to `/game/wordsearch` or `/game/crossword` with query parameters for grid size and words
  };

  return (
    <div className="home-container">
      {/* Page title */}
      <h1>Select a Game</h1>

      {/* Grid size selection */}
      <div className="form-group">
        <label>Grid Size:</label>
        <select value={gridSize} onChange={(e) => setGridSize(e.target.value)}>
          {Array.from({ length: 19 }, (_, i) => i + 2).map((size) => (
            <option key={size} value={size}>
              {size} × {size} {/* Displaying as "N × N" format */}
            </option>
          ))}
        </select>
      </div>

      {/* Words input field */}
      <div className="form-group">
        <label>Words (comma-separated):</label>
        <input
          type="text"
          value={words}
          onChange={(e) => setWords(e.target.value)}
        />
      </div>

      {/* Buttons to start Word Search or Crossword game */}
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

export default HomePage; // Exporting the HomePage component for use in other parts of the application
