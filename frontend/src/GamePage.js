import React, { useState, useEffect } from "react";
import { useParams, useLocation } from "react-router-dom";
import "./styles.css"; // Import the updated CSS file

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

function GamePage() {
  const { gameType } = useParams();
  const query = useQuery();
  const gridSize = query.get("grid_size");
  const words = query.get("words");

  const [grid, setGrid] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState(""); // Error message state

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/game?game_type=${gameType}&grid_size=${gridSize}&words=${words}`
        );
        
        if (!response.ok) {
          throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();

        if (data.error) {
          throw new Error(data.error); // Handle backend errors
        }

        setGrid(data.grid);
        setLoading(false);
      } catch (error) {
        console.error("The words are too big for the given grid size:", error.message);
        setErrorMessage(error.message);
        setLoading(false);
      }
    };

    if (gameType && gridSize && words) {
      fetchData();
    } else {
      setErrorMessage("Invalid parameters! Please provide game type, grid size, and words.");
      setLoading(false);
    }
  }, [gameType, gridSize, words]);

  return (
    <div className="game-container">
      <h1>{gameType === "wordsearch" ? "Word Search" : "Crossword"}</h1>

      {loading ? (
        <p>Loading...</p>
      ) : errorMessage ? (
        <div className="error-message">
          <p>{errorMessage}</p>
        </div>
      ) : (
        <div className="grid-wrapper">
          <div className="grid-container" style={{ gridTemplateColumns: `repeat(${gridSize}, 1fr)` }}>
            {grid.map((row, rowIndex) =>
              row.map((cell, colIndex) => (
                <div key={`${rowIndex}-${colIndex}`} className="grid-cell">
                  {cell}
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default GamePage;
