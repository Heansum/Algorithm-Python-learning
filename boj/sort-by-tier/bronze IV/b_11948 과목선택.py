a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

_list = [a, b, c, d]
_list.sort()
_list.remove(_list[0])

total = 0
for i in range(3):
    total += _list[i]
plus = 0
if e > f:
    plus = e
elif e < f:
    plus = f
else:
    plus = e

total = total + plus
print(total)