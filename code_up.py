num = int(input())
number = input()

sum = 0
for i in range(num):
    new = number.split(" ")
for i in new:
    if int(i) % 5 == 0:
        sum += int(i)
print(sum)
