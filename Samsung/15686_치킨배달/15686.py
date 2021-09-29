import itertools
import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])
            arr[i][j] = 0

# 치킨집 중에 M개 고름 (조합)
result = list(itertools.combinations(chicken, M))

res = sys.maxsize
for i in range(len(result)):
    distance = 0
    for m in range(N):
        for n in range(N):
            if arr[m][n] == 1:
                temp = sys.maxsize
                for j in range(M):
                    temp = min(temp, abs(m - result[i][j][0]) + abs(n - result[i][j][1]))
                distance += temp
    res = min(res, distance)

print(res)