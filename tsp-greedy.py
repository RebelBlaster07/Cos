import numpy as np

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def greedy_tsp(cities):
    n = len(cities)
    unvisited = list(range(n))
    current_city = 0
    visited = [current_city]
    unvisited.remove(current_city)
    
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: calculate_distance(cities[current_city], cities[city]))
        visited.append(nearest_city)
        current_city = nearest_city
        unvisited.remove(current_city)
    
    # Returning to the start city
    visited.append(visited[0])
    return visited

# Example usage:
cities = [(0, 0), (1, 2), (2, 4), (4, 2), (5, 1)]  # List of cities as (x, y) coordinates
path = greedy_tsp(cities)
print("Visited path:", path)
