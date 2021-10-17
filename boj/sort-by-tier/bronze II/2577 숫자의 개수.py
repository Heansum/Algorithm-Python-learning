a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result = str(result)
result = list(result)


def plus(nb):
    nb += 1
    return nb


for i in range(10):
    num = 0
    for j in range(len(result)):
        if int(result[j]) == 0 + i:
            num = plus(num)
    print(num)