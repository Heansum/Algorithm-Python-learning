input_nb = int(input())
divisor = int(input())

nb = int(input_nb / 100) * 100

while nb % divisor != 0:
    nb += 1

output = nb % 100
if output <= 9:
    result = ''
    result = '0' + str(output)
    print(result)
else:
    print(output)