n = input()
n = int(n)

if n % 2 == 0:
    output = ((n / 2) + 1)**2
else:
    output = ((int(n / 2) + 2) * (int(n / 2) + 1))

print(int(output))