import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

h = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

def a_star(start, goal):

    queue = [(h[start], 0, start, [start])]
    visited = set()

    while queue:

        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_cost in graph[node].items():

            new_cost = cost + edge_cost
            f = new_cost + h[neighbor]

            heapq.heappush(
                queue,
                (f, new_cost, neighbor, path + [neighbor])
            )

    return None, None


path, cost = a_star('A', 'G')

print("A* Search")
print("Path:", path)
print("Total Cost:", cost)
