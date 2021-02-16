r, c = map(int, input().split())

rows = []

for i in range(r):
  for j in range(c):
    rows.append(input()[j])

print(rows)