nb = int(input())


def factorial(nb):
    if nb == 0:
        return 1
    else:
        return nb * factorial(nb - 1)


print(factorial(nb))

