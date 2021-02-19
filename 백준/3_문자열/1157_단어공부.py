word = input()

word = word.upper()

dic = dict()
for i in word:
  dic[i] = word.count(i)

m = max(list(dic.values()))

lst = [k for k, v in dic.items() if v == m]

if len(lst) >= 2:
  print("?")
else:
  print(''.join(lst))