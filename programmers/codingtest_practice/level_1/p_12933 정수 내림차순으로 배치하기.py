n = int(input())


def solution(n):
    answer = 0
    n_str = str(n)
    nb_list = []

    for i in range(len(n_str)):
        nb_list.append(n_str[i])
    nb_list.sort(reverse=True)

    output_str = ''

    for i in range(len(nb_list)):
        output_str = output_str + nb_list[i]

    answer = int(output_str)
    return answer


a = solution(n)
print(a)