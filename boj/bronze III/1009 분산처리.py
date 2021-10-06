n = int(input())

field = [[int(x) for x in input().split(' ')] for _ in range(n)]

for x,y in field:
    print(x**y % 10)