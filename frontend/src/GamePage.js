import React, { useState, useEffect } from "react"; 
// Importing React and hooks (useState for managing state, useEffect for side effects)

import { useParams, useLocation } from "react-router-dom"; 
// Importing hooks from react-router-dom for route handling

import "./styles.css"; 
// Importing the CSS file for styling

// Custom hook to get query parameters from the URL
function useQuery() {
  return new URLSearchParams(useLocation().search); 
  // Creates a URLSearchParams object to access query parameters
}

function GamePage() {
  // Extract the game type parameter from the URL path (e.g., "wordsearch" or "crossword")
  const { gameType } = useParams();

  // Retrieve query parameters from the URL
  const query = useQuery();
  const gridSize = query.get("grid_size"); // Extracts the grid size from the URL
  const words = query.get("words"); // Extracts the list of words from the URL

  // State variables for managing game data
  const [grid, setGrid] = useState([]); // Stores the grid data fetched from the backend
  const [loading, setLoading] = useState(true); // Controls loading state
  const [errorMessage, setErrorMessage] = useState(""); // Stores error messages if any occur

  // Fetch grid data from the backend when the component mounts or when dependencies change
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/game?game_type=${gameType}&grid_size=${gridSize}&words=${words}`
        ); 
        // Fetch data from backend API, passing gameType, gridSize, and words as query parameters

        if (!response.ok) {
          throw new Error(`Error: ${response.status} - ${response.statusText}`);
          // If response is not OK (error status), throw an error
        }

        const data = await response.json(); 
        // Parse the response as JSON

        if (data.error) {
          throw new Error(data.error); 
          // If the backend sends an error message, throw an error
        }

        setGrid(data.grid); 
        // Update grid state with the received data
        setLoading(false); 
        // Set loading to false since data has been fetched successfully
      } catch (error) {
        console.error("The words are too big for the given grid size:", error.message);
        // Log the error to the console for debugging
        setErrorMessage(error.message); 
        // Update error message state to display it to the user
        setLoading(false); 
        // Stop the loading state
      }
    };

    // Ensure all required parameters are provided before fetching data
    if (gameType && gridSize && words) {
      fetchData(); 
      // Call the fetchData function if all parameters exist
    } else {
      setErrorMessage("Invalid parameters! Please provide game type, grid size, and words.");
      // If parameters are missing, display an error message
      setLoading(false); 
      // Stop the loading state
    }
  }, [gameType, gridSize, words]); 
  // Dependency array: Effect runs when any of these values change

  return (
    <div className="game-container">
      {/* Display the game title based on the game type */}
      <h1>{gameType === "wordsearch" ? "Word Search" : "Crossword"}</h1>

      {loading ? (
        <p>Loading...</p>
        // Show a loading message while data is being fetched
      ) : errorMessage ? (
        <div className="error-message">
          <p>{errorMessage}</p>
        </div>
        // If there is an error message, display it inside a styled div
      ) : (
        <div className="grid-wrapper">
          {/* Grid container dynamically adjusting to the grid size */}
          <div className="grid-container" style={{ gridTemplateColumns: `repeat(${gridSize}, 1fr)` }}>
            {grid.map((row, rowIndex) =>
              row.map((cell, colIndex) => (
                <div key={`${rowIndex}-${colIndex}`} className="grid-cell">
                  {cell}
                  {/* Display the letter or character inside each grid cell */}
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
// Exporting the GamePage component so it can be used in other parts of the application
