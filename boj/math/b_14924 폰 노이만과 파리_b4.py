car_speed, fly_speed, distance = map(int, input().split())
result = int(distance / (car_speed * 2)) * fly_speed
print(int(result))