import random

def generate_initial_state(n):
    # Random initial placement of queens in each row (0 to n-1 for columns)
    return [random.randint(0, n-1) for _ in range(n)]

def count_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(n):
    current_state = generate_initial_state(n)
    while True:
        current_conflicts = count_conflicts(current_state)
        if current_conflicts == 0:
            return current_state
        neighbors = []
        for i in range(n):
            for j in range(n):
                if current_state[i] != j:
                    new_state = current_state[:]
                    new_state[i] = j
                    neighbors.append(new_state)
        # Select the neighbor with the fewest conflicts
        next_state = min(neighbors, key=count_conflicts)
        if count_conflicts(next_state) >= current_conflicts:
            break
        current_state = next_state

    return None  # If no solution is found

# Example usage
n = 4
solution = hill_climbing(n)
if solution:
    print("Solution:", solution)
    print("Board:")
    for i in range(n):
        row = ['Q' if solution[i] == j else '.' for j in range(n)]
        print(' '.join(row))
else:
    print("No solution found.")
