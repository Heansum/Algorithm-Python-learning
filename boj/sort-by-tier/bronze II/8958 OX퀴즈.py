n = int(input())
arr = [input().split() for _ in range(n)]

for i in range(n):
    tmp = arr[i]
    width = len(tmp[0])
    output = 0
    plus = 1
    for j in range(width):
        if tmp[0][j] == 'O':
            output = output + plus
            plus += 1
        if tmp[0][j] == 'X':
            plus = 1
    print(output)