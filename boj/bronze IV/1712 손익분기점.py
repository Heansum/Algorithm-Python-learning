a, b, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

num = 1

cost = a + b * num
profit = c * num
if b >= c:
    print(-1)
else:
    num = a / (c - b)
    cost = a + b * num
    profit = c * num
    if cost >= profit:
        num = num + 1
    num = int(num)
    print(num)