nums = [int(input()) for _ in range(7)]

odds = []
for num in nums:
    if num % 2 == 1:
        odds.append(num)

odds.sort()
total = 0
for i in range(len(odds)):
    total += odds[i]

if not odds:
    print(-1)
else:
    print(total)
    print(odds[0])
