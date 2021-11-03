'''
반복문을 이용한 문제풀이
 1) 1부터 N까지 홀수출력하기
 2) 1부터 N까지의 합 구하기
 3) N의 약수출력하기
'''

# 내가 푼 답
# 1) 1부터 N까지 홀수출력하기
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

# 2) 1부터 N까지의 합 구하기
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# 3) N의 약수출력하기
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# 강사님 답안
# 값을 받아오고 출력해보자
# n = int(input())
# n 까지이기 때문에 n + 1을 해준다
n = int(input())
for i in range(1, n + 1):
    print(i)

# 1) 1부터 N까지 홀수출력하기
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

# 2) 1부터 N까지의 합 구하기
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum = sum + i
# for문이 끝난 후 출력!
print(sum)

# 3) N의 약수출력하기
n = int(input())
for i in range(1, n + 1):
    # n에 i로 나눈 나머지가 0인 값은 n의 약수이며 약수 값은 i가 된다
    if n % i == 0:
        print(i, end=' ')
