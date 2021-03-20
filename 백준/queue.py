import collections

def main():
    n = int(input())
    circuit = list(map(int, input().split()))
    memo = [-1] * n
    visit = [0] * n
    queue = collections.deque()

    queue.append((0, 0))
    ans = 0

    while queue:
      temp, cnt = queue.popleft()
      if visit[temp] == 1:
        ans = max(ans, cnt - memo[temp])
      elif visit[temp] >= 2:
        break
      memo[temp] = cnt
      visit[temp] += 1
      if 0 <= temp + circuit[temp] < n:
        queue.append((temp + circuit[temp], cnt + 1))
    print(ans)

if __name__=="__main__":
    main()