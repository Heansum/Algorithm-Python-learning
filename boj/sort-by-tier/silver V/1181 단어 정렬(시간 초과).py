n = int(input())
input_arrs = [input().split() for _ in range(n)]

# 1. overlap check
# 2. sort
#  (1) length
#  (2) if length is equal, sorting by ascii

# 1. remove overlap
_arrays = []
for i in input_arrs:
    if i not in _arrays:
        _arrays.append(i)


# 2. sort
# 2. (1) sort by length
for i in range(len(_arrays) - 1):
    j = i + 1
    while j <= len(_arrays) - 1:
        if len(_arrays[i][0]) > len(_arrays[j][0]):
            tmp = _arrays[i][0]
            _arrays[i][0] = _arrays[j][0]
            _arrays[j][0] = tmp
        j += 1

# 2. (2) if length is equal, sorting by ascii
for i in range(len(_arrays) - 1):
    j = i + 1
    while j <= len(_arrays) - 1:
        if len(_arrays[i][0]) == len(_arrays[j][0]):
            tmp_1 = []
            tmp_2 = []
            tmp_1 = _arrays[i][0]
            tmp_2 = _arrays[j][0]
            flag = 0
            for k in range(len(tmp_1)):
                if ord(tmp_1[k]) != ord(tmp_2[k]):
                    if (ord(tmp_1[k]) > ord(tmp_2[k])) & (flag == 0):
                        temp = _arrays[i][0]
                        _arrays[i][0] = _arrays[j][0]
                        _arrays[j][0] = temp
                        flag = 1
        j += 1

for i in range(len(_arrays)):
    print(_arrays[i][0])
