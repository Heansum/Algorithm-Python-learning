_input_num = int(input())

cnt = 0
new_num = 0

# new_num = 10 * (num % 10) + (int(num / 10) + int(num % 10)) % 10


def _new(nb):
    _new_nb = 10 * (nb % 10) + (int(nb / 10) + int(nb % 10)) % 10
    return _new_nb


num = -1
while _input_num != num:
    if cnt == 0:
        num = _input_num
    num = _new(num)
    cnt += 1

print(cnt)
