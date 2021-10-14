nb = int(input())


def calculate(num):
    if num == 9:
        return 3
    if num == 8:
        return 4
    if (num == 3) | (num == 2) | (num == 1):
        return 1
    if num == 2:
        return 1
    if num == 1:
        return 1
    elif num % 2 == 0: # 10 12 14 16 18 20
        if (num % 5 == 0) & (num != 10):
            return num / 2
        # if (num - 1) % 3 == 0:
        #     return num - 1
        if num == 10:
            num -= 1
            return num
        else:
            return num / 2
    elif num % 3 == 0:
        if (num - 1) % 2 == 0:
            num -= 1
            return num
        return num / 3
    elif (num % 2 != 0) & ((num - 1) % 3 == 0):
        return num - 1
    elif (num % 3 != 0) & ((num - 1) % 2 == 0):
        return num - 1
    else:
        num -= 1
        return num


def solution(num):
    count = 0
    if num == 1:
        return count
    while num != 1:
        num = calculate(num)
        count += 1
        # if num % 3 == 0:
        #     num = num / 3
        #     count += 1
        # elif num % 2 == 0:
        #     if ((num - 1) % 3 == 0) & ((num - 1) % 5 != 0):
        #         num = num - 1
        #         count += 1
        #     elif (num - 1) % 3 == 0:
        #         num = num - 1
        #         count += 1
        #     else:
        #         num = num / 2
        #         count += 1
        # elif (num % 2 == 0) & (num % 3 != 0):
        #     num = num - 1
        #     count += 1
        # elif (num % 2 != 0) & (num % 3 != 0):
        #     num = num - 1
        #     count += 1
    return count


print(solution(nb))