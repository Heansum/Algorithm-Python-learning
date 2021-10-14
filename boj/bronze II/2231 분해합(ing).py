# 216 + 2 + 1 + 6 = 225
# 225
input_num = int(input())

output = 0
while output != input_num:
    tmp = []
    # for i in range(input_num):
    #     num = i
    #     print(num)

    for j in range(len(output)):
        tmp.append(output[j])
    output += 1
    print(output)

# 198 + 1 + 9 + 8 = 216