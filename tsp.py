# def tsp_nearest_neighbor(graph):
#     n = len(graph)
#     visited = [False] * n
#     path = [0]  # Start from city 0
#     visited[0] = True
#     cost = 0
#     current = 0

#     for _ in range(n - 1):
#         next_city = -1
#         min_dist = float('inf')
#         for j in range(n):
#             if not visited[j] and 0 < graph[current][j] < min_dist:
#                 min_dist = graph[current][j]
#                 next_city = j
#         visited[next_city] = True
#         path.append(next_city)
#         cost += min_dist
#         current = next_city

#     cost += graph[current][0]  # Return to starting city
#     path.append(0)

#     print("Visited Path:", path)
#     print("Total Cost:", cost)

# # Example Distance Matrix (Graph)
# graph = [
#     [0, 2, 9, 10],
#     [1, 0, 6, 4],
#     [15, 7, 0, 8],
#     [6, 3, 12, 0]
# ]

# tsp_nearest_neighbor(graph)

import heapq
from itertools import permutations

# Distance matrix
graph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

def tsp_astar(graph):
    n = len(graph)
    start = 0
    cities = list(range(n))
    cities.remove(start)

    # Priority queue: (total_cost, path)
    pq = []
    for perm in permutations(cities):
        path = [start] + list(perm) + [start]
        cost = sum(graph[path[i]][path[i+1]] for i in range(n))
        heapq.heappush(pq, (cost, path))

    best_cost, best_path = heapq.heappop(pq)
    print("A* TSP Path:", best_path)
    print("Total Cost:", best_cost)

tsp_astar(graph)
