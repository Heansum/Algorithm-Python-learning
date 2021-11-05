'''
문자열과 내장함수
'''
msg = "It is Time"
# 문자열 내장함수 upper
print(msg.upper())

# 문자열 내장함수 lower
print(msg.lower())
print(msg)

# tmp에 msg변수에 담긴 값이 upper 된 값이 들어감
tmp = msg.upper()

print(tmp)

# 문자열 내장함수 find
print(tmp.find('T'))
print(tmp.count('T'))
print(msg)

# slice 기능 해당String 인덱스 전 까지만
print(msg[:2])
print(msg[3:5])
print(len(msg))

# for 문으로 하나씩 접근
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

# for in 으로 접근
# msg 문자 하나하나로 접근
for x in msg:
    print(x, end=' ')
print()

# isupper 내장 함수
# msg 에서 꺼내와서 x가 대문자면 출력
for x in msg:
    if x.isupper():
        print(x, end='')
print()

# islower 내장 함수
# msg 에서 꺼내와서 x가 소문자면 출력
for x in msg:
    if x.islower():
        print(x, end='')
print()

# isalpha 내장 함수
# 공백 제외, 알파벳만 출력
for x in msg:
    if x.isalpha():
        print(x, end='')
print()

# ord 내장 함수
# String의 ascii 코드 출력
tmp = 'AZ'
for x in tmp:
    print(ord(x))

tmp = 'az'
for x in tmp:
    print(ord(x))

# chr 내장 함수
# 수를 String으로 출력
tmp = 65
chr(tmp)
