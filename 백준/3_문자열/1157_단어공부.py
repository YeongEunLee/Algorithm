word = input().upper()

dic = dict()
for i in word:
  dic[i] = word.count(i)

m = max(list(dic.values()))

reverse_dict= dict(map(reversed, dic.items()))

lst = reverse_dict[m]


print(lst)
"""
if len(lst) >= 2:
  print("?")
else:
  print(''.join(lst))
"""