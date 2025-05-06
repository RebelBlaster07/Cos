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
    
    moves_played = 0
    while moves_played < 9:
        print_board(board)
        
        try:
            pos = int(input(f"Player {player}, choose position (0-8): "))
            if pos < 0 or pos > 8 or board[pos] != " ":
                print("Invalid move! Try again.")
                continue  # Don't increase moves_played
                
            board[pos] = player
            moves_played += 1  # Only increase on valid move
            1
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
                
            if moves_played == 9:
                print_board(board)
                print("It's a tie!")
                break
                
            # Switch player
            player = "O" if player == "X" else "X"
            
        except ValueError:
            print("Enter a number!")

if __name__ == "__main__":
    tic_tac_toe()