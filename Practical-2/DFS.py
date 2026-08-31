graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def dfs(start, goal):

    stack = [(start, [start])]
    visited = set()

    while stack:

        node, path = stack.pop()

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in reversed(graph[node]):

            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [neighbor])
                )

    return None


path = dfs('A', 'G')

print("Depth-First Search")
print("Path:", path)
