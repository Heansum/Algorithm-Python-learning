import sys

tmp = []
while True:
    data = [sys.stdin.readline().strip().split(' ')]
    tmp.append(data)
    if (int(data[0][0]) == 0) & (int(data[0][1]) == 0) & (int(data[0][2]) == 0):
        break;

for i in range(len(tmp) - 1):
    tmp_list = []
    a = int(tmp[i][0][0])
    b = int(tmp[i][0][1])
    c = int(tmp[i][0][2])
    tmp_list.append(a)
    tmp_list.append(b)
    tmp_list.append(c)
    tmp_list.sort()

    if int(tmp_list[0]) ** 2 + int(tmp_list[1]) ** 2 == int(tmp_list[2]) ** 2:
        print("right")
    else:
        print("wrong")