n = int(input())
nums = []
nums = input().split(' ')

for i in range(len(nums) - 1):
    j = i + 1
    while j < len(nums):
        if int(nums[i]) > int(nums[j]):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        j += 1

highest = nums[len(nums) - 1]


def change(nb, high):
    nb = (nb / high) * 100
    return nb


for i in range(len(nums)):
    nums[i] = change(int(nums[i]), int(highest))

nums[len(nums) - 1] = float(nums[len(nums) - 1])

total = 0
for i in range(len(nums)):
    total = total + float(nums[i])

total = total / n
print(total)