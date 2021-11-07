x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

x_list = [x_1, x_2, x_3]
y_list = [y_1, y_2, y_3]


need_x = 0
need_y = 0
if x_list[0] == x_list[1]:
    need_x = x_3
elif x_list[1] == x_list[2]:
    need_x = x_1
else:
    need_x = x_2

if y_list[0] == y_list[1]:
    need_y = y_3
elif y_list[1] == y_list[2]:
    need_y = y_1
else:
    need_y = y_2

print(need_x, need_y, end=' ')