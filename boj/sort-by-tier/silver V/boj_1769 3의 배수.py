import sys
n = sys.stdin.readline().strip()
# print(type(n))
# print(n)
# n_list = []
#
# for i in range(len(n)):
#     n_list.append(int(n[i]))
#
# total = 0
# for j in range(len(n_list)):
#     total += n_list[j]

cnt = 0


def changer(_str_nb):
    global cnt
    if len(_str_nb) < 2:
        return _str_nb
    else:
        cnt += 1
        # tmp_nb = str(nb)
        tmp_list = []
        total = 0
        # for i in range(len(tmp_nb)):
        #     tmp_list.append(int(tmp_nb[i]))
        for j in range(len(_str_nb)):
            total = total + int(_str_nb[j])
        total = str(total)
        return changer(total)


output = changer(n)

print(cnt)
if int(output) % 3 != 0:
    print("NO")
else:
    print("YES")
