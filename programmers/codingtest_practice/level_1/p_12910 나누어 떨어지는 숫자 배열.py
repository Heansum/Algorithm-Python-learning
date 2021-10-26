# test case
# arr = [5, 9, 7, 10]
# arr = [2, 36, 1, 3]
# arr = [3, 2, 6]


def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer

# test execute
# print(solution(arr, 10))
