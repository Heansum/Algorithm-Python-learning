size, nb = input().split(' ')
size = int(size)
nb = int(nb)

arr = []
arr = input().split(' ')

tmp = ''
for i in range(size):
    if int(arr[i]) < nb:
        tmp = tmp + (arr[i]) + ' '
print(tmp)