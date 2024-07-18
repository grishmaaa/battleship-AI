## README

# Battleship Game with AI

This project is a Python implementation of the classic game "Battleship" with a graphical user interface (GUI) using Pygame and artificial intelligence (AI) for gameplay.

### Project Structure

- `tournament.py`: Simulates multiple games to analyze the performance of the AI.
- `gui.py`: Implements the graphical interface and handles user interactions.
- `engine.py`: Contains the game logic, including ship placement, player actions, and AI strategies.

### Requirements

- Python 3.x
- Pygame
- Matplotlib

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd battleship-game
   ```

2. **Install required packages:**
   ```bash
   pip install pygame matplotlib
   ```

### Running the Game

1. **Start the game with GUI:**
   ```bash
   python gui.py
   ```

2. **Run the tournament simulation:**
   ```bash
   python tournament.py
   ```

### Gameplay

- The game consists of two players, each with a 10x10 grid.
- Ships are randomly placed on each player's grid.
- Players take turns to fire shots at the opponent's grid.
- The game ends when all of one player's ships are sunk.

### Controls

- **Mouse Click:** Fire a shot at the opponent's grid.
- **ESC:** Exit the game.
- **Space:** Pause/Unpause the game.
- **Enter:** Restart the game.

### AI Strategies

- **Random AI:** Fires shots randomly at unknown squares.
- **Basic AI:** Fires shots based on a more sophisticated strategy:
  - Targets neighboring squares of known hits.
  - Follows a checkerboard pattern to optimize search.
  - Falls back to random moves if no better options are available.

### Tournament Simulation

The `tournament.py` script runs multiple games between two AIs to analyze their performance. It records the number of wins and shots taken to complete the game.

### Example Output

When running `tournament.py`, you will see the number of wins for each AI and a bar chart showing the distribution of the number of shots taken in each game.

### Customization

You can customize various aspects of the game, such as:
- Grid size and ship sizes in `engine.py`.
- AI behavior in the `basic_ai` and `random_ai` methods.
- GUI appearance and interactions in `gui.py`.

### Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.
