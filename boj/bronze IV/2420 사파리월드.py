n, m = input().split(' ')

n = int(n)
m = int(m)

if n > m:
    print(n - m)
elif n < m:
    print(m - n)
else:
    print(0)