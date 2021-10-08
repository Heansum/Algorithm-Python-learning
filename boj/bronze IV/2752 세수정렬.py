arr = []
arr = input().split(' ')
arr[0] = int(arr[0])
arr[1] = int(arr[1])
arr[2] = int(arr[2])

i = 0
while i <= 1:
    j = i + 1
    while j <= 2:
        if arr[i] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
        j = j + 1
    i = i + 1

print(arr[0], arr[1], arr[2], sep=" ")