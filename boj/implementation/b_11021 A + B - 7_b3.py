n = int(input())
nums = [(input().split(' ')) for _ in range(n)]

for i in range(len(nums)):
    result = 'Case #'
    output = int(nums[i][0]) + int(nums[i][1])
    output = str(output)
    result = result + str(i + 1) + ': ' + output
    print(result)