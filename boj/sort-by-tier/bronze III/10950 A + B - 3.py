n = int(input())
arr = [input().split(' ') for _ in range(n)]

for i in range(n):
    output = int(arr[i][0]) + int(arr[i][1])
    print(output)