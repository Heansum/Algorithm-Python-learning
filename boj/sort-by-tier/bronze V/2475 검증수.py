a, b, c, d, e = input().split(' ')


def change_to_int(num):
    return int(num)


a_num = change_to_int(a)
b_num = change_to_int(b)
c_num = change_to_int(c)
d_num = change_to_int(d)
e_num = change_to_int(e)


def binary(num):
    return num * num


output = binary(a_num) + binary(b_num) + binary(c_num) + binary(d_num) + binary(e_num)
output = output % 10
print(output)