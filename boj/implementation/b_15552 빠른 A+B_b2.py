import sys

n = sys.stdin.readline().strip()
n = int(n)
for i in range(0, n):
    _input = sys.stdin.readline().rstrip()
    a, b = _input.split(" ")
    a = int(a)
    b = int(b)
    print(a + b)