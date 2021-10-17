first = int(input())
second = input()
first_output = first * int(second[2])
second_output = first * int(second[1])
third_output = first * int(second[0])
result = first_output + second_output * 10 + third_output * 100

print(first_output)
print(second_output)
print(third_output)
print(result)