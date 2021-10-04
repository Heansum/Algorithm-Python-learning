people_num, field_size = input().split(' ')

people_num = int(people_num)
field_size = int(field_size)

primary_num = people_num * field_size

a, b, c, d, e = input().split(' ')

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

a = a - primary_num
b = b - primary_num
c = c - primary_num
d = d - primary_num
e = e - primary_num

print(a, b, c, d, e, sep=' ')