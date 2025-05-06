import random
import time

def calculate_attacks(board):
    """Count queen conflicts"""
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            # Check same row or diagonal conflicts
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def hill_climbing(n):
    # Create random board where board[col] = row position of queen
    board = [random.randint(0, n-1) for _ in range(n)]
    current_attacks = calculate_attacks(board)
    
    while current_attacks > 0:
        improved = False
        
        # Try moving each queen to a better position
        for col in range(n):
            original_row = board[col]
            best_row = original_row
            best_attacks = current_attacks
            
            # Try each possible row for this queen
            for row in range(n):
                if row != original_row:
                    board[col] = row
                    attacks = calculate_attacks(board)
                    
                    if attacks < best_attacks:
                        best_attacks = attacks
                        best_row = row
                        improved = True
            
            # Move queen to best position (might be original position)
            board[col] = best_row
            current_attacks = best_attacks
            
            # If we found improvement, start over with new board
            if improved:
                break
        
        # If no improvement possible, we're at local optimum
        if not improved:
            # For a complete solution, we'd restart with a new random board
            # but for simplicity, we'll just return this local optimum
            return board
    
    return board

if __name__ == "__main__":
    n = int(input("Enter the value of N for N-Queens problem: "))
    
    print("\nSolving using Hill Climbing...")
    start_time = time.time()
    solution = hill_climbing(n)
    end_time = time.time()
    
    # Print solution
    print(f"Solution found: {solution}")
    print(f"Attacks: {calculate_attacks(solution)}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    
    # Print board
    for row in range(n):
        print("".join("Q " if solution[col] == row else ". " for col in range(n)))

# import random
# import time

# # Utility function to calculate the number of attacking pairs
# def attacking_pairs(board):
#     attacks = 0
#     n = len(board)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
#                 attacks += 1
#     return attacks

# # Function to print the board
# def print_board(board):
#     n = len(board)
#     for row in range(n):
#         line = "".join("Q " if board[col] == row else ". " for col in range(n))
#         print(line)
#     print("\n")

# def hill_climbing(n):
#     board = [random.randint(0, n - 1) for _ in range(n)]
#     while True:
#         current_attacks = attacking_pairs(board)
#         if current_attacks == 0:
#             return board
#         neighbors = []
#         for col in range(n):
#             for row in range(n):
#                 if board[col] != row:
#                     new_board = list(board)
#                     new_board[col] = row
#                     neighbors.append(new_board)
#         best_neighbor = min(neighbors, key=attacking_pairs)
#         if attacking_pairs(best_neighbor) >= current_attacks:
#             return board  # Local optimum reached
#         board = best_neighbor

# if __name__ == "__main__":
#     n = int(input("Enter the value of N for N-Queens problem: "))

#     print("\nSolving using Hill Climbing...")
#     start_time = time.time()
#     solution_hc = hill_climbing(n)
#     end_time = time.time()
#     print("Solution:", solution_hc)
#     print_board(solution_hc)
#     print("Execution Time: {:.4f} seconds\n".format(end_time - start_time))