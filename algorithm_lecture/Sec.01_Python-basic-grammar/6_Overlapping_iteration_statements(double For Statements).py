'''
중첩 반복분(2중 for문)
'''
for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()

for i in range(5):
    print('i: ', i, sep='', end=' ')
    for j in range(5):
        print('j: ', j, sep='', end=' ')
    print()

# 별 찍기 5 * 5
for i in range(5):
    for j in range(5):
        print("*", end=' ')
    print()

# 별 찍기 1 2 3 4 5 *
for i in range(5):
    for j in range(i + 1):
        print("*", end=' ')
    print()

# 별 찍기 5 4 3 2 1 *
for i in range(5):
    for j in range(5 - i):
        print("*", end=' ')
    print()
