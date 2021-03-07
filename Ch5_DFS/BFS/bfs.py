from collections import deque

def bfs(graph, start, visited):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  #큐가 빌 때까지 반복
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

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

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)