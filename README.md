# Tic Tac Toe Python Game

This is a Python-based Tic Tac Toe game with two modes: Single Player (against AI) and Two Player. It offers a smooth game experience with a user-friendly board interface and an AI opponent that uses the **Minimax algorithm** for optimal play.

## Features

### Single Player Mode (AI)
- AI opponent powered by the **Minimax algorithm** that plays optimally.
- Players can choose their symbol (either `X` or `O`) and play against the AI.

### Two Player Mode
- Local two-player mode where two players can take turns on the same machine.
- Players can choose their own symbols at the start of the game.

### Game Flow Enhancements
- Clear and user-friendly board display.
- Input prompts guide players to enter their moves in a clear format (e.g., `A1`, `B2`, etc.).
- The game announces the winner or a draw after the game ends.

### Minor Bug Fixes
- Fixed input validation to ensure valid moves.
- Enhanced the user interface for better interaction and responsiveness.

## Changes Made
- The game logic was updated to support both single-player (AI) and two-player modes.
- Introduced the `minimax()` function to calculate optimal AI moves.
- Refined the board display and user input prompts for better usability.

## How to Test
1. Run the game by executing `python ttt.py` in your terminal.
2. Choose either **Single Player** or **Two Player** mode.
3. Select your symbol (`X` or `O`) and follow the prompts to make moves.
4. After the game ends, check that the game correctly announces the winner or if it’s a draw, and the board displays accurately after each move.

## Additional Notes
- The game is designed to run with Python 3.x.
- The AI logic is based on the **Minimax algorithm**, which may need to be reviewed for edge cases or performance optimization.

## How to Play
1. When you start the game, you’ll be asked to select between **Single Player** or **Two Player** mode.
2. In **Single Player** mode, you will play against the AI. In **Two Player** mode, two players can take turns.
3. Players input their moves using the format `A1`, `B3`, etc., to place their symbol on the board.
4. After the game ends, the result (winner or draw) is displayed.

---

Feel free to modify or add anything specific as per your project requirements.
