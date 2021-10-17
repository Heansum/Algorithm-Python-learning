x, y, w, h = input().split(' ')
x = int(x)
y = int(y)
w = int(w)
h = int(h)

if x > w / 2:
    distance_x = w - x
elif x <= w / 2:
    distance_x = x

if y > h / 2:
    distance_y = h - y
elif y <= h / 2:
    distance_y = y

if distance_x > distance_y:
    print(distance_y)
elif distance_y > distance_x:
    print(distance_x)
else:
    print(distance_x)