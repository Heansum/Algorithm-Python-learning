now_meat_temp = int(input())
final_meat_temp = int(input())
need_time_in_cold = int(input())
need_time_in_zero = int(input())
need_time_in_hot = int(input())

time = 0
if now_meat_temp < 0:
    while now_meat_temp != 0:
        time += need_time_in_cold
        now_meat_temp += 1
if now_meat_temp == 0:
    time += need_time_in_zero
if now_meat_temp >= 0:
    while True:
        if now_meat_temp == final_meat_temp:
            break
        time += need_time_in_hot
        now_meat_temp += 1

print(time)