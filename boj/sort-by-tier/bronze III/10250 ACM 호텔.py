n = int(input())
nums = [input().split(' ') for _ in range(n)]

for k in range(len(nums)):
    address_list = []
    width = int(nums[k][1])
    for i in range(width):
        high = int(nums[k][0])
        for j in range(high):
            tmp = ''
            if i + 1 < 10:
                tmp = str(j + 1) + '0' + str(i + 1)
            else:
                tmp = str(j + 1) + str(i + 1)
            address_list.append(tmp)

    person_index = int(nums[k][2]) - 1
    print(address_list[person_index])
