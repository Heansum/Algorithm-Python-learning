a, b, c, d = map(int, input().split())
cmp_one = b + c
cmp_two = a + d
if cmp_one >= cmp_two:
    print(cmp_one - cmp_two)
elif cmp_two >= cmp_one:
    print(cmp_two - cmp_one)
