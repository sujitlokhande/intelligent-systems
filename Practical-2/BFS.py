from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def bfs(start, goal):

    queue = deque([(start, [start])])
    visited = set()

    while queue:

        node, path = queue.popleft()

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None


path = bfs('A', 'G')

print("Breadth-First Search")
print("Path:", path)
