from collections import deque

print("=== ASSESSMENT 3.4: GRAPH TRAVERSAL ===")
print("Last Name Reference: SABANDO\n")

# Paghimo sa Graph gamit ang Adjacency List (SABANDO nodes & edges)
graph = {
    'S': ['A', 'B'],
    'A': ['S', 'N', 'D'],
    'B': ['S', 'O'],
    'N': ['A'],
    'D': ['A', 'O'],
    'O': ['B', 'D']
}


# 1. Breadth-First Search (BFS) para sa Graph
def bfs_graph(g, start_node):
    visited = []
    queue = deque([start_node])
    seen = {start_node}

    while queue:
        node = queue.popleft()
        visited.append(node)

        for neighbor in g.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    print("Graph BFS Traversal:", " -> ".join(visited))


# 2. Depth-First Search (DFS) para sa Graph
def dfs_graph(g, start_node):
    visited = []
    stack = [start_node]
    seen = set()

    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            visited.append(node)
            # Balihon ang pag-push aron makuha ang sakto nga sunod-sunod
            for neighbor in reversed(g.get(node, [])):
                if neighbor not in seen:
                    stack.append(neighbor)

    print("Graph DFS Traversal:", " -> ".join(visited))


# Pagtawag sa mga functions
bfs_graph(graph, 'S')
dfs_graph(graph, 'S')