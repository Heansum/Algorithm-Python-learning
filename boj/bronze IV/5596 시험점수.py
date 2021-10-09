min_info, min_math, min_sci, min_eng = input().split(' ')
man_info, man_math, man_sci, man_eng = input().split(' ')

min_info = int(min_info)
min_math = int(min_math)
min_sci = int(min_sci)
min_eng = int(min_eng)
man_info = int(man_info)
man_math = int(man_math)
man_sci = int(man_sci)
man_eng = int(man_eng)

min_total = min_info + min_math + min_sci + min_eng
man_total = man_info + man_math + man_sci + man_eng

if min_total > man_total:
    print(min_total)
elif min_total < man_total:
    print(man_total)
else:
    print(min_total)