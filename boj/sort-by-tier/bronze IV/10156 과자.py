price, count, my_money = input().split(' ')
price = int(price)
count = int(count)
my_money = int(my_money)

payment = price * count
if payment > my_money:
    need_money = payment - my_money
    print(need_money)
else:
    print(0)
