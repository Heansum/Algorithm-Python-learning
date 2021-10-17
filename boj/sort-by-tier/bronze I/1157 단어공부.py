import operator

word = input()
word_arr = list(word)

word_ascii = []

for x in word_arr:
    _ascii = ord(x)
    if (_ascii >= 97) & (_ascii <= 122):
        _ascii = _ascii - 32
    word_ascii.append(_ascii)

num = 0
var = []

for x in word_ascii:
    if x not in var:
        var.append(x)

var_dic = {}

for nb in var:
    tmp = 0
    for j in range(len(word_ascii)):
        if nb == word_ascii[j]:
            tmp += 1
    for k in range(len(var)):
        var_dic[nb] = tmp

var_dic = sorted(var_dic.items(), key=operator.itemgetter(1))
if len(var_dic) == 1:
    var_nb = var_dic[len(var_dic) - 1][0]
    output = chr(var_nb)
    print(output)
if len(var_dic) > 1:
    if var_dic[len(var_dic) - 1][1] == var_dic[len(var_dic) - 2][1]:
        print('?')
    else:
        var_nb = (var_dic[len(var_dic) - 1][0])
        output = chr(var_nb)
        print(output)
