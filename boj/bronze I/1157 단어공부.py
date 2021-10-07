word = input()
word_arr = list(word)

word_ascii = []

for x in word_arr:
    word_ascii.append(ord(x))
    print(x)
    print(word_ascii)

num = 0
var = []

for x in word_ascii:
    if x not in var:
        var.append(x)
print(var)



print(word_ascii)
