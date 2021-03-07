n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

#연결 요소의 개수를 구하면 됌 -> BFS 또는 DFS로 표현 할 수 있음
def dfs(x, y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >=m:
    return False
  #현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우 의 위치도 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1
print(result)