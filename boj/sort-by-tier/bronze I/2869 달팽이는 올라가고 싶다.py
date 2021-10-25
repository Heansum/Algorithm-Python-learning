import math
up, down, goal = map(int, input().split(' '))

# 낮 2 1 3 2 5
# 밤

count = 0
# while location <= goal:
#     location = location + up
#     if location >= goal:
#         count += 1
#         break
#     location = location - down
#     count += 1
# print(count)


count = (goal - down) / (up - down)

print(math.ceil(count))
