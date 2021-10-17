import sys

while True:
    n = [sys.stdin.readline().strip()]
    i = 0
    if n[0] == '0':
        break
    if len(n[0]) == 1:
        print('yes')
    else:
        cmp_nb = int(len(n[0]) / 2)
        nb = 0
        _len = len(n[0])
        while i < cmp_nb:
            # _n = n[0][i]
            # _n_edge = n[0][len(n[0]) - 1 - i]
            if n[0][i] == n[0][len(n[0]) - 1 - i]:
                nb += 1
            i += 1
        if cmp_nb == nb:
            print('yes')
        else:
            print('no')
