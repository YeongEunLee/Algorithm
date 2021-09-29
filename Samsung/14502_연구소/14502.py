import sys
import copy

sys.stdin = open("input.txt", "r")

N, M = map(int, input().strip().split())
nmlst = []
for i in range(N):
    L = list(map(int, input().strip().split()))
    nmlst.append(L)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0  # clean 지역의 개수를 resurn 하기 위한 변수
def virus(r, c, sel_nmlst):
    if sel_nmlst[r][c] == 2:
        # 4방향을 확인하고 범위out, 벽을만나면 중지함
        for dir in range(4):
            nr = r + dx[dir]
            nc = c + dy[dir]
            if nr >= 0 and nc >= 0 and nr < N and nc < M:
                if sel_nmlst[nr][nc] == 0:
                    sel_nmlst[nr][nc] = 2
                    virus(nr, nc, sel_nmlst)
                    
def wall(start, count):
    global res
    if count == 3:  # 벽3개 선택하면 종료
        sel_nmlst = copy.deepcopy(nmlst)  # deepcopy로 벽이 선택된 배열 복사
        for r in range(N):
            for c in range(M):
                virus(r, c, sel_nmlst)
        safe_counts = sum(i.count(0) for i in sel_nmlst)  # 깨끗한 지역
        res = max(res, safe_counts)
        resurn True

    else:
        for i in range(start, N * M):  # 2차원 배열
            r = i // M #몫
            c = i % M #나머지
            if nmlst[r][c] == 0:  # 안전영역인이면 벽으로 바꿀 수 ㅇㅋ
                nmlst[r][c] = 1  # 벽으로 바꾸기
                wall(i, count + 1) #count + 1해서 wall함수 돌림
                nmlst[r][c] = 0

wall(0, 0)
print(res)