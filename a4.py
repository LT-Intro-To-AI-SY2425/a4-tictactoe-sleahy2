class TTTBoard:
    """A tic tac toe board
    
    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    def __init__(self):
        # Initialize the board as a 3x3 grid filled with '*' to represent empty spots
        self.board = [["*" for _ in range(3)] for _ in range(3)]
        # Initialize moves count to keep track of how many moves have been made
        self.moves_count = 0

    def __str__(self):
        # This will make the board printable (for displaying in the game)
        return "\n".join([" | ".join(row) for row in self.board])

    def make_move(self, player: str, position: int) -> bool:
        """Place a player's mark on the board at the specified position"""
        row, col = divmod(position, 3)
        if self.board[row][col] == "*":  # Check if the spot is available
            self.board[row][col] = player
            self.moves_count += 1
            return True
        return False

    def game_over(self) -> bool:
        """Check if the game is over"""
        return self.moves_count >= 9 or self.has_won("X") or self.has_won("O")

    def has_won(self, player: str) -> bool:
        """Check if a player has won"""
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Check row
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Check column
                return True
        # Check diagonals
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def clear(self) -> None:
        """Reset the board to its initial empty state"""
        self.board = [["*" for _ in range(3)] for _ in range(3)]
        self.moves_count = 0


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe with moves directly made within the function"""
    
    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    # Example of manually calling make_move without using a predefined list of moves
    # This simulates a sequence of moves directly
    brd.make_move("X", 8)  # X moves to position 8 (bottom-right corner)
    brd.make_move("O", 7)  # O moves to position 7 (bottom-middle)
    brd.make_move("X", 5)  # X moves to position 5 (center)
    brd.make_move("O", 6)  # O moves to position 6 (bottom-left)
    brd.make_move("X", 2)  # X moves to position 2 (top-right)
    
    # Check if game is over after the moves
    print(brd)
    print(f"Game over! {brd.game_over()}")
    
    if brd.has_won("X"):
        print("X wins!")
    elif brd.has_won("O"):
        print("O wins!")
    else:
        print("Board full, cat's game!")


if __name__ == "__main__":
    # uncomment to play 
    play_tic_tac_toe()
