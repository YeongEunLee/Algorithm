N = int(input())
P = int(input()) # 인덱스 번호 맞추기 위해 한 줄 추가

graph = [[0]*(N+1) for _ in range(N+1)] 
done = [] 
for _ in range(P): 
  x, y = map(int, input().split()) 
  graph[x][y], graph[y][x] = 1, 1 
  
  def dfs(v): 
    done.append(v)
    for k in range(1, N+1):
    # 1 ~ n번까지 
      if (k not in done) and (graph[v][k] == 1): 
        dfs(k)
        return (len(done) - 1) # 1번을 제외한 컴퓨터 수 print(dfs(1))
