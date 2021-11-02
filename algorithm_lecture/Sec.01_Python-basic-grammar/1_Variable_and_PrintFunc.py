'''
변수명 정하기
 1) 영문과 숫자, _ 로 이루어진다.
 2) 대소문자를 구분한다.
 3) 문자나, _ 로 시작한다.
 4) 특수문자를 사용하면 안된다. (&, % 등)
 5) 키워드를 사용하면 안된다.(if, for 등)
'''

a = 1
A = 2
c = 3
print(a, A, c)

a = 1
A = 2
A1 = 3
print(a, A, A1)

a = 1
A = 2
A1 = 3
_b = 4
print(a, A, A1, _b)

# 주석
'''
여러줄 주석
'''

a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
# 메모리가 허용하는 만큼 크기 가능
a = 123455634654564566
print(a)
print(type(a))
# 실수형은 8바이트까지 저장 가능, 그 이상은 데이터 손실
a = 12.123456789123456789
print(a)
print(type(a))
a = 'student'
print(a)
print(type(a))

# 출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
# sep의 경우는 각각의 변수 사이에 넣은 값만큼 분리해준다
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='')
print(a, b, c, sep='\n')

'''
end의 경우, print함수는 항상 개행 되어지는데, 개행 대신에 
다른 값을 넣어 개행 말고 다른 형태가 되도록 한다.
'''
print(a, end=' ')
print(b, end=' ')
print(c)
