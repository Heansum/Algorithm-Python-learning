'''
조건문 if(분기, 중첩)
'''
x = 7
if x == 7:
    print("Lucky")
    print("ㅋㅋ")

x = 5
if x != 7:
    print("Lucky")
    print("ㅋㅋ")


'''중첩 if문'''
x = 15
if x >= 10:
    if x % 2 == 1:
        print("10이상의 홀수")

x = 12
if x >= 10:
    if x % 2 == 1:
        print("10이상의 홀수")

x = 9
if x >= 10:
    if x % 2 == 1:
        print("10이상의 홀수")

x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")

x = 7
if x > 0 and x < 10:
    print("10보다 작은 자연수")

# 파이썬에서만 허용
x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")


'''if 분기문'''
x = 10
if x > 0:
    print("양수")
else:
    print("음수")

x = -3
if x > 0:
    print("양수")
else:
    print("음수")


'''다중 if 문'''
# 하나가 걸리면 조건문 전체를 빠져나온다
x = 93
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")

# if문의 경우는 각각 따로 실행된다
x = 93
if x >= 90:
    print('A')
if x >= 80:
    print('B')
if x >= 70:
    print("C")
