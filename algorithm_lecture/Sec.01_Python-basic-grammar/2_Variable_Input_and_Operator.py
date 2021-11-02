'''
변수입력과 연산자
'''
a = input("숫자를 입력하세요 : ")
print(a)

# split 띄어 쓰기로 분리하여 입력 받게 한다
a, b = input("숫자를 입력하세요 : ").split()
print(a + b)

print(type(a))
c = a + b
# 둘다 문자형 string이라서 값이 나오지 않고 string끼리 붙는다

print(type(c))
print(c)


a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(a + b)

# 위 처럼 하나하나 int하기 힘들다, map을 사용해보자
# map을 int형으로 봐꿔준다 여기서 int는 내장함수
# map(mapping)
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# //는 몫을 의미
print(a // b)
# %는 나머지를 의미
print(a % b)
# **는 a의 b진수, b승을 의미
print(a**b)


a = 4.3
b = 5
c = a + b
print(c)
print(type(c))