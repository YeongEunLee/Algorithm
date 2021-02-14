n, k = map(int, input().split())

jewelry = {}
for i in range(n):
  m, v = map(int, input().split())
  jewelry[m] = v

bag = []
for i in range(k):
  bag.append(int(input()))

res = []
for b in bag:
  if max(jewelry) < bag:
    res.append(max(jewelry.values))
    
