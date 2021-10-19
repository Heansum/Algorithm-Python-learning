_filter = input()
arr = input().split(' ')

num = 0
for i in range(len(arr)):
    if _filter == arr[i]:
        num += 1
print(num)