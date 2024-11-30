import os
import random
import time

def clear_screen():
    """Clear the console for better user experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Displays the Tic Tac Toe board."""
    clear_screen()
    print("\nTIC TAC TOE")
    print("   1   2   3")
    for i, row in enumerate(board):
        print(f"{chr(65 + i)}  " + " | ".join(row))
        if i < 2:
            print("  ---|---|---")
    print("\n")

def check_winner(board):
    """Checks for a winner or a draw."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]  # Return 'X' or 'O'

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]  # Return 'X' or 'O'

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Return 'X' or 'O'
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Return 'X' or 'O'

    # Check for draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"  # Return 'Draw'

    return None  # Game is still ongoing

def ai_move(board, ai_symbol, player_symbol):
    """AI chooses the best move randomly."""
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(available_moves)

def get_player_move(board):
    """Prompts the player to enter their move."""
    while True:
        move = input("Enter your move: ").strip().upper()
        if len(move) == 2 and move[0] in "ABC" and move[1] in "123":
            row = "ABC".index(move[0])
            col = int(move[1]) - 1
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken. Try again.")
        else:
            print("Invalid input. Use format A1, B2, etc.")

def tic_tac_toe():
    """Main game logic."""
    while True:
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print("1. Single Player (vs AI)")
        print("2. Two Player")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "3":
            print("Thanks for playing!")
            break
        elif choice not in ["1", "2"]:
            print("Invalid choice. Try again.")
            time.sleep(2)
            continue

        # Initialize board and players
        board = [[" " for _ in range(3)] for _ in range(3)]
        if choice == "1":
            player_symbol = input("Choose your symbol (X or O): ").strip().upper()
            ai_symbol = "O" if player_symbol == "X" else "X"
            player_name = "Player 1"
            current_player = player_symbol if random.choice([True, False]) else ai_symbol
        else:
            player_1 = input("Enter Player 1's name (X): ").strip() or "Player 1"
            player_2 = input("Enter Player 2's name (O): ").strip() or "Player 2"
            players = {"X": player_1, "O": player_2}
            current_player = "X"

        # Game loop
        winner = None
        while not winner:
            print_board(board)
            if choice == "1":  # Single Player
                if current_player == player_symbol:
                    print(f"{player_name}'s turn ({player_symbol}):")
                    row, col = get_player_move(board)
                else:
                    print(f"AI's turn ({ai_symbol}):")
                    time.sleep(1)
                    row, col = ai_move(board, ai_symbol, player_symbol)
            else:  # Two Player
                print(f"{players[current_player]}'s turn ({current_player}):")
                row, col = get_player_move(board)

            board[row][col] = current_player
            winner = check_winner(board)
            current_player = "O" if current_player == "X" else "X"

        print_board(board)
        if winner == "Draw":
            print("It's a draw!")
        else:
            if choice == "1":
                if winner == player_symbol:
                    print(f"Congratulations! {player_name} wins!")
                else:
                    print("AI wins!")
            else:
                print(f"Congratulations! {players[winner]} wins!")

        input("\nPress Enter to play again...")

if __name__ == "__main__":
    tic_tac_toe()
