import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function HomePage() {
  const [gridSize, setGridSize] = useState(10);
  const [words, setWords] = useState("apple,banana,grape");
  const navigate = useNavigate();

  const handleSubmit = (e, gameType) => {
    e.preventDefault();
    // Navigate to the game page with custom grid size, words, and selected game type
    navigate(`/game/${gameType}?grid_size=${gridSize}&words=${words}`);
  };

  return (
    <div>
      <h1>Select a Game</h1>
      <form>
        <div>
          <label>Grid Size: </label>
          <input
            type="number"
            value={gridSize}
            onChange={(e) => setGridSize(e.target.value)}
            min="5"
            max="20"
            required
          />
        </div>

        <div>
          <label>Words (comma-separated): </label>
          <input
            type="text"
            value={words}
            onChange={(e) => setWords(e.target.value)}
            required
          />
        </div>

        <button type="submit" onClick={(e) => handleSubmit(e, 'wordsearch')}>
          Start Word Search
        </button>

        <button type="submit" onClick={(e) => handleSubmit(e, 'crossword')}>
          Start Crossword
        </button>
      </form>
    </div>
  );
}

export default HomePage;
