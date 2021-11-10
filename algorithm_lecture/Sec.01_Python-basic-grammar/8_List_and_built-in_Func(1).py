'''
리스트와 내장 함수(1)
'''
import random as r
# 리스트 생성 방법 1
a = []
print(a)

# 리스트 생성 방법 2
b = list()
print(b)

# list a에 값을 넣는 것
a = [1, 2, 3, 4, 5]
print(a)
print(a[0])

# list b에 값을 넣는 법
# range 로도 가능하다
b = list(range(1, 11))
print(b)

# list 를 서로 합칠 수 있다
c = a + b
print(c)


# append 리스트 내장 함수
print(a)
a.append(6)
print(a)

# insert 리스트 내장 함수
# 해당 인덱스에 값을 넣는다
a.insert(3, 7)
print(a)

# pop 리스트 내장 함수
# 맨 뒤의 값을 제거한다
a.pop()
print(a)

# 인덱스를 입력해주면 그 인덱스의 값을 제거해 준다
a.pop(3)
print(a)

# remove 리스트 내장 함수
# 입력하는 값을 찾아서 제거해 준다
a.remove(4)
print(a)

# index 리스트 내장 함수
# 해당 값의 인덱스를 찾아준다
print(a.index(5))

# sum 리스트 내장 함수
# 해당 리스트의 모든 값을 더해준다
a = list(range(1, 11))
print(a)
print(sum(a))

# max 리스트 내장 함수
# 해당 리스트의 가장 큰 값을 반환한다
print(max(a))

# min 리스트 내장 함수
# 해당 리스트의 가장 작은 값을 반환한다
print(min(a))

# 만약 복수 개의 인자를 넣으면
# 그 중에서 최소 값을 찾아준다 (최대값도 동일 하다)
# 즉, 인자 값이 리스트 형태로 들어가기 때문에 그 중에서 찾아주는 것!
print(min(7, 5))
print(min(7, 3, 5))

# random 의 내장 함수 shuffle
# 해당 리스트의 값들을 무작위로 섞는 함수
print(a)
r.shuffle(a)
print(a)

# sort 리스트 내장 함수
# 오름 차순으로 정렬
a.sort()
print(a)

# 내림 차순으로 정렬
a.sort(reverse=True)
print(a)

# clear 리스트 내장 함수
# 리스트안의 값들을 제거
a.clear()
print(a)
