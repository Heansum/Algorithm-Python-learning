# 1 6 8~19
# 1 6 12 18 24 30 36
#   6 6 6
#
#
# 1, 2 ~ 7, 8 ~ 19
# 1   2      3
# 1 2 8 20 36
input_num = int(input())
output = 1


# input_num 까지 증가시켜서 카운트!!


def solution(num):
    count = 2
    if input_num == 1:
        return 1
    else:
        j = 1
        while j <= input_num:
            # 1  234567 8910111213141516171819 20
            # 1  2      3                      4
            # 1 + count * 6 1
            # 1 + count * 6 7 1 + count0 * 6 + count1 * 6
            # 1 + count * 6 13 1 + count0 * 6 + count1 * 6 + count2 * 6
            # 1 + count * 6
            # 1 < n <= 7 1 + (count += 1) * 6
            # 7 < n <= 19
            tmp = (count - 2) * 2
            if (input_num > (count - 2) * 6 + 1) & (input_num <= (count - 2) * 6 + (count - 1) * 6 + 1):
                return count
            if j == (count - 2) * 6 + 1:
                if j != 2:
                    count += 1
            j += 1


print(solution(input_num))
