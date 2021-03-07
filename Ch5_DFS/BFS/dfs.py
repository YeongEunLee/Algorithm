def dfs(graph, v, visited):
  visited[v] = True
  print(v, end='')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [],
  [2, 3, 8], #노드 1과 연결된 노드 번호
  [1, 7], #노드 2과 연결된 노드 번호
  [1, 4, 5], #노드 3과 연결된 노드 번호 
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)