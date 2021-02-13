n = int(input())
c = list(map(int, input().split()))

c.sort()
sum = []
for x in range(n):
  sum.append(c[0] + c[-1])
  c.remove(c[0])
  c.remove(c[-1])
sum.sort()
print(sum[0])