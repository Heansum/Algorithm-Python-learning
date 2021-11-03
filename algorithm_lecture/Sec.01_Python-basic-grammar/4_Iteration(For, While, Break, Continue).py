'''
반복문(for, while)
'''
a = range(10)
print(list(a))

a = range(1, 11)
print(list(a))


'''for문'''
for i in range(10):
    print("hello")

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

# 아무일도 안 일어남
for i in range(10, 0):
    print(i)

# 더하는 값을 지정해준다
for i in range(10, 0, -1):
    print(i)


'''while문'''
i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 10
while i >= 1:
    print(i)
    i = i - 1


'''break'''
# break을 쓰게되면 해당 반복문을 빠져나오게 된다
i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1

i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1


'''continue'''
# 어떤 것을 건너 뛰고 싶을 때 continue를 쓴다
for i in range(1, 11):
    # if문 조건이 참일 때 for문을 건너 뛴다
    if i % 2 == 0:
        continue
    print(i)


'''for else 구문'''
# 정상적인 종료가 아니고 break로 종료하게 되면 else문을 거치지 않는다
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)

# 정상적인 종료일 경우(break로 종료 X), else문을 거친다
for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)