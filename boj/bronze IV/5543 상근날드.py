burger_a = int(input())
burger_b = int(input())
burger_c = int(input())
drink_a = int(input())
drink_b = int(input())

if burger_a >= burger_b >= burger_c:
    burger = burger_c
elif burger_a >= burger_c >= burger_b:
    burger = burger_b
elif burger_b >= burger_a >= burger_c:
    burger = burger_c
elif burger_b >= burger_c >= burger_a:
    burger = burger_a
elif burger_c >= burger_a >= burger_b:
    burger = burger_b
elif burger_c >= burger_b >= burger_a:
    burger = burger_a

if drink_a >= drink_b:
    drink = drink_b
elif drink_b >= drink_a:
    drink = drink_a

output = drink + burger - 50
print(output)