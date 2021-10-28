first_angle = int(input())
second_angle = int(input())
third_angle = int(input())

total = first_angle + second_angle + third_angle
flag_two_equal = 0
if first_angle == second_angle:
    flag_two_equal = 1
elif first_angle == third_angle:
    flag_two_equal = 1
elif second_angle == third_angle:
    flag_two_equal = 1

if first_angle == second_angle == third_angle == 60:
    print("Equilateral")
elif total == 180:
    if flag_two_equal:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
