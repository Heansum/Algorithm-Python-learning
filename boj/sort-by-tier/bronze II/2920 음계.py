arr = input().split(' ')


def check_ascending(arr):
    for i in range(len(arr)):
        if not int(arr[i]) == i + 1:
            return 0
        if i == 7:
            return 1


def check_descending(arr):
    for i in range(len(arr)):
        if not int(arr[i]) == 8 - i:
            return 0
        if i == 7:
            return 1


if check_ascending(arr):
    print('ascending')
elif check_descending(arr):
    print('descending')
else:
    print('mixed')