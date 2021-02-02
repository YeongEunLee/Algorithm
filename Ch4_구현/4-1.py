n = int(input()) #여러개일 때 n, m = list(map(int, input().split()))이런 식으로
plans = input().split() #string이므로 int로 변환하지 않음 

x, y = 1, 1

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획 확인 후 더하기
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny <1 or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x, y)
