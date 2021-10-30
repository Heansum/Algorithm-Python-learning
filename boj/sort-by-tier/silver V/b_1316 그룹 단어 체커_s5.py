n = int(input())
_str = [input() for _ in range(n)]

flag = 0
for j in range(len(_str)):
    tmp = []
    group = []
    for i in range(len(_str[j])):
        if _str[j][i] not in tmp:
            tmp.append(_str[j][i])

    flag = 0
    not_group = 0
    _double = 1
    for i in range(len(_str[j])):
        if flag == 1:
            for index in range(len(group)):
                if _str[j][i] == group[index]:
                    if i > 0:
                        if _str[j][i] != _str[j][i - 1]:
                            not_group = 1
        if _str[j][i] in tmp:
            flag = 1
            group.append(_str[j][i])
        if i > 0:
            if _str[j][i - 1] == _str[j][i]:
                _double = 0
    if not_group:
        n -= 1
print(n)