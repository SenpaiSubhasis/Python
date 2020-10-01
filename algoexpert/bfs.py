graph = {

    "A":["B","C","D"],
    "B":["E","F"],
    "C":[],
    "D":["G","H"],
    "F":["I","J"],
    "G":["K"],
    "E":[],
    "I":[],
    "J":[],
    "K":[],
    "H":[]
}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = "   ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')