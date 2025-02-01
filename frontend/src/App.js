import { BrowserRouter as Router, Routes, Route } from "react-router-dom";  // ✅ Use Routes instead of Switch
import HomePage from "./Homepage";
import GamePage from "./GamePage";

function App() {
  return (
    <Router>
      <Routes>  {/* ✅ Use Routes */}
        <Route path="/game/:gameType" element={<GamePage />} />  {/* ✅ Use element instead of component */}
        <Route path="/" element={<HomePage />} />
      </Routes>
    </Router>
  );
}

export default App;
