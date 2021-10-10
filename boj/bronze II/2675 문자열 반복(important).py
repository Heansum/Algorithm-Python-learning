n = int(input())
arr = [[ str(x) for x in input().split(' ')] for _ in range(n)]

for i in range(len(arr)):
    num = int(arr[i][0])
    output = ''
    for j in range(len(arr[i][1])):
        tmp = arr[i][1]
        output = output + num * tmp[j]
    print(output)