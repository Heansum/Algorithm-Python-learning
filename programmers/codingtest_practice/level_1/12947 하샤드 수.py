x = int(input())


def solution(x):
    answer = True
    total = 0

    x_list = str(x)
    for i in range(len(x_list)):
        total = total + int(x_list[i])

    if x % total == 0:
        return answer
    answer = False
    return answer
