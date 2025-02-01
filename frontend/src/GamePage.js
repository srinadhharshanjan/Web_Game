import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";  // ✅ Import useParams

function GamePage() {
  const { gameType } = useParams();  // ✅ Get gameType from URL params
  const [grid, setGrid] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/game?game_type=${gameType}&grid_size=10&words=apple,banana,grape`
        );
        const data = await response.json();
        setGrid(data.grid);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching grid:", error);
        setLoading(false);
      }
    };

    if (gameType) {
      fetchData();
    }

  }, [gameType]);

  return (
    <div>
      <h2>{gameType === "wordsearch" ? "Word Search" : "Crossword"}</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        grid.map((row, rowIndex) => (
          <div key={rowIndex}>{row.join(" ")}</div>
        ))
      )}
    </div>
  );
}

export default GamePage;
