# test-case
arr = [4, 3, 2, 1]
# arr = [10]


def solution(arr):
    answer = []
    tmp_arr = []

    answer = arr
    if len(arr) == 1:
        answer = [-1]
        return answer

    for i in arr:
        tmp_arr.append(i)
    tmp_arr.sort()

    _what_you_remove = tmp_arr[0]
    answer.remove(_what_you_remove)
    return answer


print(solution(arr))
