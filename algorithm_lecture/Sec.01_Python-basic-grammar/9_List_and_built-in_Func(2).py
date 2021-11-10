'''
리스트와 내장함수(2)
'''
# 리스트 슬라이스
a = [23, 12, 36, 53, 19]
# 리스트 슬라이스 3 인덱스 전까지
print(a[:3])
# 리스트 슬라이스 1 인덱스 부터 4인덱스 전까지
print(a[1:4])

# 리스트 길이 반환 함수
print(len(a))


# 리스트 개별 인덱스에 접근
for i in range(len(a)):
    print(a[i], end=' ')
print()


# a 리스트의 값을 꺼내 접근
for x in a:
    print(x, end=' ')
print()


for x in a:
    # 리스트의 값 중 만족하는 값만 출력, 홀수 출
    if x % 2 == 1:
        print(x, end=' ')
print()


# 리스트에 튜플 형태로 접근하게 하는 enumerate 함수
# (인덱스, 값)
for x in enumerate(a):
    print(x)


# 대괄호를 열면 리스트
# 소괄호를 열면 튜플
b = (1, 2, 3, 4, 5)
print(b[0])
# 튜플 값은 변경 불가능
# b[0] = 7
print(b[0])


# 해당 튜플의 원소로 접근
for x in enumerate(a):
    print(x[0], x[1])
print()

# 위와 동일하지만, 각각의 변수 값에 할당
for index, value in enumerate(a):
    print(index, value)
print()


# all 함수, (리스트 안의 각각의 요소에 접근) => 소괄호 안
# all 함수는 조건이 모두가 참이어야 true 값을 반환한다
if all(60 > x for x in a):
    print("YES")
else:
    print("NO")

# 거짓의 경우
if all(50 > x for x in a):
    print("YES")
else:
    print("NO")


# any 함수, 하나만 참이어도 true 값 반환
# 모두 거짓이면 false 값 반환
if any(15 > x for x in a):
    print("YES")
else:
    print("NO")

if any(11 > x for x in a):
    print("YES")
else:
    print("NO")
