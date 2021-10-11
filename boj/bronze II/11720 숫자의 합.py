n = int(input())

arr = input().split()

tmp = []

for i in range(n):
    tmp.append(arr[0][i])

output = 0
for i in range(len(tmp)):
    output = output + int(tmp[i])
print(output)