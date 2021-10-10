nb = int(input())

for x in range(1, nb + 1):
    blank = nb - x
    print(' ' * blank + '*' * x)