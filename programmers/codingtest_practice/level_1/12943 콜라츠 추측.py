nb = int(input())


def calculate(num):
    if num == 1:
        return num
    if num % 2 == 0:
        return num / 2
    else:
        return num * 3 + 1


def solution(num):
    answer = 0
    count = 0
    tmp = num

    while tmp != 1:
        if count == 500:
            return -1
        tmp = calculate(tmp)
        count += 1
    print(count)
    answer = count
    return answer


solution(nb)
