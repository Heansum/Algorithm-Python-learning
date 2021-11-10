n = int(input())
nums = [input().split() for _ in range(n)]

for i in range(n):
    num = int(nums[i][0]) + int(nums[i][1])
    print("Case #" + str(i + 1) + ": " + nums[i][0] + " + " + nums[i][1] + " " + "= " + str(num))
