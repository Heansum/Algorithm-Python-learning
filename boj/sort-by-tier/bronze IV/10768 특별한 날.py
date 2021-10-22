first_input = int(input())
second_input = int(input())

if first_input == 1:
    print("Before")
elif first_input == 2:
    if second_input < 18:
        print("Before")
    elif second_input == 18:
        print("Special")
    else:
        print("After")
else:
    print("After")
