hours, minutes = input().split(' ')
hours = int(hours)
minutes = int(minutes)

now = hours * 60 + minutes
before = now - 45

if before < 0:
    before = before + 1440

hours = int(before / 60)
minutes = before % 60
print(hours, minutes, sep=" ")