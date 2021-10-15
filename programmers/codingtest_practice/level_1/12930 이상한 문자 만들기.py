s = input()


def solution(s):
    answer = ''

    tmp = s.split(' ')

    arr = []

    for i in range(len(tmp)):
        tmp_2 = ''
        for j in range(len(tmp[i])):
            _tmp = 0
            _ascii = ord(tmp[i][j])
            if j % 2 == 0:
                if (_ascii >= 97) & (_ascii <= 122):
                    _tmp = _ascii - 32
                    tmp_2 = tmp_2 + chr(_tmp)
                else:
                    tmp_2 = tmp_2 + tmp[i][j]
            else:
                if (_ascii >= 65) & (_ascii <= 90):
                    _tmp = _ascii + 32
                    tmp_2 = tmp_2 + chr(_tmp)
                else:
                    tmp_2 = tmp_2 + tmp[i][j]
        arr.append(tmp_2)
    for i in range(len(arr)):
        answer = answer + arr[i]
        if i != len(arr) - 1:
            answer = answer + ' '

    return answer


_str = solution(s)
print(_str)
