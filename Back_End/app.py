# from flask import Flask, jsonify, request
# from flask_pymongo import PyMongo
# from flask_cors import CORS
# from wordsearch import WordSearchGame  # Import WordSearchGame logic
# from crossword import CrosswordGame

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend communication

# # MongoDB URI (Local MongoDB or MongoDB Atlas)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/word_search_game"
# mongo = PyMongo(app)


# @app.route('/wordsearch', methods=['GET'])
# def generate_wordsearch():
#     # Get grid_size and words from the query parameters
#     grid_size = int(request.args.get('grid_size', 10))  # Default to 10 if not provided
#     words = request.args.get('words', 'apple,banana,grape').split(',')

#     # Create the WordSearchGame instance with the provided parameters
#     game = WordSearchGame(grid_size=grid_size, words=words)
#     grid_data = {
#         "grid": game.get_grid(),
#         "words": game.word_list,
#         "grid_size": game.grid_size
#     }

#     # Save the generated game data to MongoDB
#     mongo.db.games.insert_one(grid_data)

#     # Return the grid and related information as a JSON response
#     return jsonify({"grid": game.get_grid(), "words": words, "grid_size": grid_size})

# @app.route('/crossword', methods=['GET'])
# def generate_crossword():
#     grid_size = int(request.args.get('grid_size', 10))  # Default to 10 if not provided
#     words = request.args.get('words', 'apple,banana,grape').split(',')

#     game = CrosswordGame(grid_size=grid_size, words=words)
#     grid_data = {
#         "grid": game.get_grid(),
#         "words": game.word_list,
#         "grid_size": game.grid_size
#     }

#     mongo.db.games.insert_one(grid_data)
#     return jsonify({"grid": game.get_grid(), "words": words, "grid_size": grid_size})


# @app.route('/history', methods=['GET'])
# def get_history():
#     games = mongo.db.games.find()  # Fetch game history from MongoDB
#     games_list = list(games)
#     return jsonify(games_list)


# if __name__ == "__main__":
#     app.run(debug=True,use_reloader=False)  # Disable the automatic reloader

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from wordsearch import WordSearchGame
from crossword import CrosswordGame

app = Flask(__name__)
CORS(app)
limiter = Limiter(get_remote_address, app=app, default_limits=["2 per 10 seconds"])
cache = {}

@app.route('/game', methods=['GET'])
@limiter.limit("2 per 10 seconds")
def generate_game():
    game_type = request.args.get('game_type', 'wordsearch')
    grid_size = int(request.args.get('grid_size', 10))
    words = request.args.get('words', '').split(',')

    request_key = f"{game_type}_{grid_size}_{'_'.join(words)}"

    if request_key in cache:
        print("Returning cached response")
        return jsonify({"grid": cache[request_key]})

    if game_type == 'wordsearch':
        game = WordSearchGame(grid_size=grid_size, words=words)
    elif game_type == 'crossword':
        game = CrosswordGame(grid_size=grid_size, words=words)
    else:
        return jsonify({"error": "Invalid game type"}), 400

    grid = game.get_grid()
    cache[request_key] = grid

    return jsonify({"grid": grid})

if __name__ == '__main__':
    app.run(debug=True)
