s = input()


def solution(s):
    answer = ''
    tmp_list = []
    for _str in s:
        tmp_list.append(_str)
    tmp_list.sort(reverse=True)
    for _one_str in tmp_list:
        answer += _one_str

    return answer


print(solution(s))
