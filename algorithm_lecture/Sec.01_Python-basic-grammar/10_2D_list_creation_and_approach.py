'''
2차원 리스트 생성과 접근
'''
# 1차원 리스트 생성 예시
a = [0] * 10
print(a)

a = [0] * 3
print(a)

# 2차원 리스트 생성
# for 다음 _를 쓰면 변수 없이 반복한다
a = [[0] * 3 for _ in range(3)]
print(a)

# 2차원 요소에 접근 및 변경
a[0][1] = 1
print(a)
a[1][1] = 2
print(a)

# for 문으로 2차원 배열안의 1차원 배열 접근
for x in a:
    print(x)

# for 문으로 2차원 배열안의 1차원 배열 안의 요소에 접근
for x in a:
    for y in x:
        print(y, end=' ')
    print()
