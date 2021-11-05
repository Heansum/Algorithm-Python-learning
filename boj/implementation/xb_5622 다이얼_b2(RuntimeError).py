_str = input()
_str_arr = []

for i in range(len(_str)):
    _str_arr.append(_str[i])


output = 0


def _checker(_input_str):
    if 65 <= ord(_input_str) <= 67:
        return 3
    elif 68 <= ord(_input_str) <= 70:
        return 4
    elif 71 <= ord(_input_str) <= 73:
        return 5
    elif 74 <= ord(_input_str) <= 76:
        return 6
    elif 77 <= ord(_input_str) <= 79:
        return 7
    elif 80 <= ord(_input_str) <= 82:
        return 8
    elif 83 <= ord(_input_str) <= 85:
        return 9
    elif 86 <= ord(_input_str) <= 88:
        return 10


for i in range(len(_str_arr)):
    output += _checker(_str_arr[i])

print(output)