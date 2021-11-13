'''
함수 만들기
'''
# 함수 선언
# 큰 프로젝트를 하면 반복되는 코드들이 있다
# 반복되는 부분을 함수형태로 만들어서 반복을 줄인다
def add(a, b):
    c = a + b
    print(c)

add(3, 2)
add(5, 7)

# 함수의 선언은 호출보다 항상 위에!

# 함수의 결과값 반환
def add(a, b):
    c = a + b
    return c

# 함수의 출력이 아닌, 반환 값을 출력
print(add(3, 2))

# 값을 저장한 후 print
x = add(3, 2)
print(x)

# return 되는 함수는 값을 반환하고 그 함수가 종료됨


# 튜플 형태로 return 되는 함수
def add(a, b):
    c = a + b
    d = a - b
    return c, d

print(add(3, 2))


# 소수만 출력되도록 하는 함수
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 함수를 bool 형 처럼 사용해서
# true 면 출력되도록 설정
a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
