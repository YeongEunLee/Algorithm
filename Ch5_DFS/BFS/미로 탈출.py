from collections import deque

#bfs
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  #queue가 빌때까지 반복
  while queue:
    x, y = queue.popleft()
    #현재 위치에서 4가지 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #공간 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]

# N, M을 공백을 기준으로 입력 받음
n, m = map(int, input().split())

#2차원 리스트로 map 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

#이동할 네가지의 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
