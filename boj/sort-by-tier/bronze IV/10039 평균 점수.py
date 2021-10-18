nums = [int(input()) for _ in range(5)]

total = 0
for i in range(len(nums)):
    if int(nums[i]) < 40:
        nums[i] = 40
    total += nums[i]
mid = int(total / 5)
print(mid)