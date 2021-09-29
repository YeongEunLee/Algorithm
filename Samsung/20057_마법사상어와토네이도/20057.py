import sys
sys.stdin = open("input.txt", "r")

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]

# 다시 구현해보기 ㅠ 블로그 참고함
def sand_move(pos, direction_ind, mat):
    rate = [2, 10, 7, 1, 5, 10, 7, 1, 2]
    sand_mat = [
                   [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0)],
                   [(0, -2), (1, -1), (0, -1), (-1, -1), (2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)]
                   ]
    res = 0
    y = mat[pos[0]][pos[1]]
    mat[pos[0]][pos[1]] = 0
    alpha = y
    for idx, pos_tmp in enumerate(sand_mat[direction_ind % 2]):
        r = pos[0] + pos_tmp[0] * (-1) ** (direction_ind // 2)
        c = pos[1] + pos_tmp[1] * (-1) ** (direction_ind // 2)
        val_tmp = (y * rate[idx]) // 100
        if val_tmp:
            alpha -= val_tmp
            if 0 <= r < N and 0 <= c < N:
                mat[r][c] += val_tmp
            else:
                res += val_tmp
    r = pos[0] + direction[direction_ind][0]
    c = pos[1] + direction[direction_ind][1]
    if 0 <= r < N and 0 <= c < N:
        mat[r][c] += alpha
    else:
        res += alpha
    return res

res = 0
#회전 :
s = [N//2, N//2]
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)] #왼 아 오 위
ind = 0
visit[s[0]][s[1]] = True
while s != [0, 0]:
    s[0] += direction[ind][0]
    s[1] += direction[ind][1]
    visit[s[0]][s[1]] = True
    #모래
    res += sand_move(s, ind, mat)
    #회전
    ind = (ind + 1) % 4
    if visit[s[0] + direction[ind][0]][s[1] + direction[ind][1]]:
        ind = (ind - 1) % 4
print(res)