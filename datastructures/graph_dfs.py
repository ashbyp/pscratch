# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')


def dfs1(graph, node):
    # node is the starting position
    # graph is the graph in dictionary format
    visited = []
    queue = []

    queue.append(node)
    visited.append(node)

    while queue:
        s = queue.pop()
        print(s, end=' ')
        for x in graph[s][::-1]:
            if x not in visited:
                visited.append(x)
                queue.append(x)

print()
dfs1(graph, 'A')


