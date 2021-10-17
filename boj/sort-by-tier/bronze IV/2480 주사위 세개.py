a, b, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    print(10000 + a * 1000)

if a == b != c:
    print(1000 + a * 100)

if b == c != a:
    print(1000 + b * 100)

if c == a != b:
    print(1000 + c * 100)

if a != b != c:
    if (a > b > c) | (a > c > b):
        print(a * 100)
    elif (b > a > c) | (b > c > a):
        print(b * 100)
    elif (c > a > b) | (c > b > a):
        print(c * 100)