a, b = input().split(' ')
a = list(a)
b = list(b)


def change_component(_str):
    tmp_0 = _str[0]
    tmp_2 = _str[2]
    _str[0] = tmp_2
    _str[2] = tmp_0
    return _str


a = change_component(a)
b = change_component(b)


def change_to_str(_list):
    tmp = ''
    for i in range(len(_list)):
        tmp = tmp + _list[i]
    return tmp


a = change_to_str(a)
b = change_to_str(b)

if a > b:
    print(a)
elif a < b:
    print(b)
