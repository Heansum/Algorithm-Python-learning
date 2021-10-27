n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(len(nums)):
    tmp_num = nums[i]
    q = int(tmp_num / 25)
    tmp_num -= q * 25
    d = int(tmp_num / 10)
    tmp_num -= d * 10
    n = int(tmp_num / 5)
    tmp_num -= n * 5
    print(q, d, n, tmp_num, sep=" ")

