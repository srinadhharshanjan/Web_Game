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

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/game?game_type=${gameType}&grid_size=${gridSize}&words=${words}`
        );
        const data = await response.json();
        setGrid(data.grid);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching grid:", error);
        setLoading(false);
      }
    };

    if (gameType && gridSize && words) {
      fetchData();
    }
  }, [gameType, gridSize, words]);

  return (
    <div className="game-container">
      <h1>{gameType === "wordsearch" ? "Word Search" : "Crossword"}</h1>
      {loading ? (
        <p>Loading...</p>
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
