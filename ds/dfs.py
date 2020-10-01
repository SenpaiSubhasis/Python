graph = {
    "A": set(["B","C"]),
    "B": set(["A","D","E"]),
    "C": set(["A","F"]),
    "D": set(["B"]),
    "E": set(["B","F"]),
    "F": set(["C","E"])
}
#print(graph)

def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
             visited.add(vertex)
             y = graph[vertex]
             complicated = y - visited
             stack.extend(complicated)
    return visited

dfs(graph,'A')

