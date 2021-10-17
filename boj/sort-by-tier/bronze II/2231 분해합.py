input_num = int(input())


def solution(num):
    for i in range(input_num):
        num = [str(i)]

        output = 0
        for j in range(len(str(i))):
            output = output + int(num[0][j])
        output = output + i
        if output == input_num:
            break;
    if output == input_num:
        return print(i)
    else:
        return print(0)


solution(input_num)