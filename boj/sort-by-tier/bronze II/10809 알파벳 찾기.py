string = input()
string_list = list(string)


def check(_str_list, _char):
    num = -1
    for j in range(len(string)):
        if _str_list[j] == _char:
            num = j
            return str(num)
    return str(num)


output = ''
for k in range(26):
    nb = 97 + k
    output = output + check(string_list, chr(nb)) + ' '

print(output)
