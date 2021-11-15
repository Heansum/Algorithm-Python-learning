'''
람다 함수
'''
# 기본적인 함수 호출
def plus_one(x):
    return x + 1

print(plus_one(1))

# 람다 함수 호출
# return 값을 변경시킬 때 주로 사용
# 변수 이름에 할당
plus_two = lambda x: x + 2
print(plus_two(1))

a = [1, 2, 3]
# map 을 사용하여 객체형태로 변환시킨다
# map 형태로 있는 것을 list 형태로 출력한다
print(list(map(plus_one, a)))

# 람다 함수를 사용하는 이유
# 내장 함수의 인자로 사용할 때 아래처럼 변수를 지정해
# 편리하게 사용할 수 있다
print(list(map(lambda x: x + 1, a)))
