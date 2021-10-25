k = int(input())

# 18 = 3 * 6 = 5 * 3 + 3
# 18 - 5 18 - 10 18 - 15
# k - 값이 3으로 나누어 질때까지
# 4 % 3 = 1
# 11 = 5 3 3
# 18 = 5 5 5 3

count_k = 1
count = 0
# (k - count_k) % 3 == 0 일 때까지 계속 더하기

# if (k % 3 != 0) & (k % 5 != 0):
#     while count_k % 3 > 0:
#         count_k = k - 5 * count
#         count += 1
#     if count_k < 0:
#         print(-1)
#     else:
#         count -= 1
#         while count_k > 0:
#             if count_k % 3 != 0:
#                 break
#             count_k -= 3
#             count += 1
#         if count_k % 3 != 0:
#             print(-1)
#         print(count)
# else:
#     while k != 0:
#         if k % 5 == 0:
#             k = k - 5
#             count += 1
#         elif k % 3 == 0:
#             k = k - 3
#             count += 1
#         else:
#             break
#     if k != 0:
#         print(-1)
#     else:
#         print(count)



# k = 3 * 3_count + 5 * 5_count


count_3 = 0
count_5 = 0


def dp(nb):
    global count_3
    global count_5
    if nb == 0:
        return
    elif nb < 0:
        return print(-1)
    else:

        nb = 3 * count_3 + count_5



