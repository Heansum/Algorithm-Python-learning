string = []
string = input().split(' ')

for item in string:
    if item == '':
        string.remove('')

if string[len(string) - 1] == '':
    string.remove('')

print(len(string))