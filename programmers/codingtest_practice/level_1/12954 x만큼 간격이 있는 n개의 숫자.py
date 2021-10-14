def solution(x, n):
    answer = []
    nb = 0
    for i in range(n):
        nb = nb + x
        answer.append(nb)
    return answer