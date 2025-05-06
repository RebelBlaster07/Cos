def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-----------")

def check_winner(board, player):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if all(board[pos] == player for pos in win):
            return True
    return False

def tic_tac_toe():
    # Show position reference
    print("Positions:")
    print_board(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
    print()
    
    # Game board
    board = [" " for _ in range(9)]
    player = "X"
    
    for _ in range(9):  # Maximum 9 moves possible
        print_board(board)
        
        try:
            pos = int(input(f"Player {player}, choose position (0-8): "))
            if pos < 0 or pos > 8 or board[pos] != " ":
                print("Invalid move! Try again.")
                continue
                
            board[pos] = player
            
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
                
            if " " not in board:
                print_board(board)
                print("It's a tie!")
                break
                
            # Switch player
            player = "O" if player == "X" else "X"
            
        except ValueError:
            print("Enter a number!")

if __name__ == "__main__":
    tic_tac_toe()

# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)

# def check_winner(board, player):
#     # Check rows
#     for row in board:
#         if row.count(player) == 3:
#             return True
    
#     # Check columns
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] == player:
#             return True
    
#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] == player:
#         return True
#     if board[0][2] == board[1][1] == board[2][0] == player:
#         return True
    
#     return False

# def is_board_full(board):
#     for row in board:
#         if " " in row:
#             return False
#     return True

# def tic_tac_toe():
#     # Initialize empty board
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"
    
#     while True:
#         # Print current board
#         print_board(board)
        
#         # Get player's move
#         try:
#             row = int(input(f"Player {current_player}, enter row (0-2): "))
#             col = int(input(f"Player {current_player}, enter column (0-2): "))
            
#             # Check if move is valid
#             if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
#                 print("Invalid move! Try again.")
#                 continue
                
#             # Make the move
#             board[row][col] = current_player
            
#             # Check for winner
#             if check_winner(board, current_player):
#                 print_board(board)
#                 print(f"Player {current_player} wins!")
#                 break
                
#             # Check for tie
#             if is_board_full(board):
#                 print_board(board)
#                 print("It's a tie!")
#                 break
                
#             # Switch player
#             current_player = "O" if current_player == "X" else "X"
            
#         except ValueError:
#             print("Please enter numbers only!")

# if __name__ == "__main__":
#     print("Welcome to Tic-Tac-Toe!")
#     tic_tac_toe()