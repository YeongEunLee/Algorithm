data = input()
c = data[0]
r = data[1]

count = 0

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

for i in range(len(columns)):
  if c == columns[i]:
    y = i+1
for j in range(len(rows)):
  if r == rows[j]:
    x = j+1

for i in range(8):
  if x + dx[i] < 9 and x + dx[i] > 0 and y + dy[i] > 0 and y + dy[i] < 9:
    count += 1

print(count)