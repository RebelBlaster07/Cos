##BFS

from collections import deque

def water_jug_bfs():
    visited = set()
    queue = deque()
    queue.append((0, 0))  # (jug4, jug3)

    while queue:
        jug4, jug3 = queue.popleft()

        if (jug4, jug3) in visited:
            continue
        visited.add((jug4, jug3))

        print(f"State: 4L Jug = {jug4}, 3L Jug = {jug3}")

        if jug4 == 2 or jug3 == 2:
            print("Goal reached!")
            return

        # Possible actions:
        possible_moves = [
            (4, jug3),  # Fill 4L
            (jug4, 3),  # Fill 3L
            (0, jug3),  # Empty 4L
            (jug4, 0),  # Empty 3L
            # Pour 4L -> 3L
            (jug4 - min(jug4, 3 - jug3), jug3 + min(jug4, 3 - jug3)),
            # Pour 3L -> 4L
            (jug4 + min(jug3, 4 - jug4), jug3 - min(jug3, 4 - jug4))
        ]

        for state in possible_moves:
            if state not in visited:
                queue.append(state)

# Run the function
water_jug_bfs()

##DFS

def water_jug_dfs():
    stack = [(0, 0)]  # (jug4, jug3)
    visited = set()

    while stack:
        jug4, jug3 = stack.pop()

        if (jug4, jug3) in visited:
            continue
        visited.add((jug4, jug3))

        print(f"State: 4L Jug = {jug4}, 3L Jug = {jug3}")

        if jug4 == 2 or jug3 == 2:
            print("Goal reached!")
            return

        possible_moves = [
            (4, jug3),  # Fill 4L jug
            (jug4, 3),  # Fill 3L jug
            (0, jug3),  # Empty 4L jug
            (jug4, 0),  # Empty 3L jug
            (jug4 - min(jug4, 3 - jug3), jug3 + min(jug4, 3 - jug3)),  # Pour 4L → 3L
            (jug4 + min(jug3, 4 - jug4), jug3 - min(jug3, 4 - jug4))   # Pour 3L → 4L
        ]

        for state in possible_moves:
            if state not in visited:
                stack.append(state)

# Run the DFS solution
water_jug_dfs()
