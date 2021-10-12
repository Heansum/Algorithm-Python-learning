num = 0
nb = []

for i in range(10):
    num = int(input())
    nb = nb + [num]


def confirm(_list, input_nb):
    flag = 1
    for index in range(len(_list)):
        if int(_list[index]) == input_nb:
            return 0
        elif int(_list[index]) != input_nb:
            flag = 1
    return flag


mod = []
for i in range(10):
    tmp = int(nb[i]) % 42
    if i == 0:
        mod = mod + [tmp]
    elif confirm(mod, tmp):
        mod = mod + [tmp]


output = len(mod)
print(output)
