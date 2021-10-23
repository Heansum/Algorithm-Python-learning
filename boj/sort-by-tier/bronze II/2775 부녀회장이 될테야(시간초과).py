# 0층은 각각 호 번호만큼 산다.
# 1층의 1호는 (1 - 1)층의 1호 사람 수만큼 f == 1, b == 3 -> f == 0, total(b)
# 1층의 2호는 (1 - 1)층의 1 + 2호 사람 수 만큼
# 1층의 3호는 (1 - 1)층의 1 + 2 + 3호 사람 수 만큼
# 1층의 4호는 (1 - 1)층의 1 + 2 + 3 + 4호 사람 수 만큼
# 2층의 1호는 (2 - 1)층의 1호 사람 수 만큼 (1)
# 2층의 2호는 (2 - 1)층의 1 + 2호 사람 수 만큼 (1) + (1 + 2)
# 2층의 3호는 (2 - 1)층의 1 + 2 + 3호 사람 수 만큼  (1) + (1 + 2) + (1 + 2 + 3)
# f == 2, b == 3 -> f == 1, total(b) -> f == 0, total(total(b))

# n층의 b호 사람 수는, n - 1층의 b호까지 더한 사람 수 이다
# n - 1층의 b호 사람 수는, n - 2층의 b호까지 더한 사람 수 이다
# n - 3층의 ....
# 탈출 조건 => Floor is zero.
# def count
# if floor == 0:
#   return 호수
# else:
#   return floor - 1
# count(n) = total(count(n - 1))

# 0층이면 탈출
n = int(input())
nums = [input() for _ in range(2 * n)]


def solution(f, b):
    if f == 0:
        return b
    else:
        i = 1
        total = 0
        while i <= b:
            total += solution(f - 1, i)
            i += 1
        return total


for i in range(0, len(nums), 2):
    f = int(nums[i])
    b = int(nums[i + 1])
    output = solution(f, b)
    print(output)

# f = int(input())
# b = int(input())


