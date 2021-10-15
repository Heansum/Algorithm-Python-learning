n, m = input().split(' ')
n = int(n)
m = int(m)

# output = []
#
#
# def find(num):
#     tmp = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             tmp.append(i)
#     return tmp
#
#
# n_arr = []
# m_arr = []
# n_arr = find(n)
# m_arr = find(m)
#
#
# tmp_min = []
# for i in range(len(n_arr)):
#     for j in range(len(m_arr)):
#         if n_arr[i] == m_arr[j]:
#             tmp_min.append(m_arr[j])
#
# _min = tmp_min[len(tmp_min) - 1]
# output.append(_min)
#
#
# tmp_max = 0
# if tmp_min[len(tmp_min) - 1] != 1:
#     if n > m:
#         if n % m == 0:
#             output.append(n)
#     elif n < m:
#         if m % n == 0:
#             output.append(m)
#     else:
#         output.append(n)
# else:
#     output.append(n * m)
# print(output)


def solution(n, m):
    answer = []
    n_arr = []
    m_arr = []

    tmp_min = []

    def find(num):
        tmp = []
        for i in range(1, num + 1):
            if num % i == 0:
                tmp.append(i)
        return tmp

    n_arr = find(n)
    m_arr = find(m)

    for i in range(len(n_arr)):
        for j in range(len(m_arr)):
            if n_arr[i] == m_arr[j]:
                tmp_min.append(m_arr[j])

    _min = tmp_min[len(tmp_min) - 1]
    answer.append(_min)

    tmp_max = 0
    if tmp_min[len(tmp_min) - 1] != 1:
        if n > m:
            if n % m == 0:
                answer.append(n)
        elif n < m:
            if m % n == 0:
                answer.append(m)
        else:
            answer.append(n)
    else:
        answer.append(n * m)
    return answer
