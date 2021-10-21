t = int(input())

a_count = 0
b_count = 0
c_count = 0

if t % 10 != 0:
    print(-1)
else:
    a_count = int(t / 300)
    b_count = int((t - a_count * 300) / 60)
    c_count = int((t - a_count * 300 - b_count * 60) / 10)
    print(a_count, b_count, c_count, sep=" ")