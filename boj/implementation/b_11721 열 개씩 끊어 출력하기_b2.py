_str = input()

for i in range(len(_str)):
    print(_str[i], end='')
    if (i + 1) % 10 == 0 and i != 0:
        print()
