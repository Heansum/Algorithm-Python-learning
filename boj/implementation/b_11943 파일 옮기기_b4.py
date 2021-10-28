a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))

output = 0
if (a + d) > (b + c):
    output = b + c
else:
    output = a + d

print(output)