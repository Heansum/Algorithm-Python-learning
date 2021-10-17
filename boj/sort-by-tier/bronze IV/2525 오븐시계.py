hours, minutes = input().split(' ')
making_time = input()

hours = int(hours)
minutes = int(minutes)
making_time = int(making_time)

if making_time > 60:
    hours = hours + int(making_time / 60)
    minutes = minutes + making_time % 60
    if minutes > 60:
        hours = hours + 1
        minutes = minutes - 60
    if minutes == 60:
        hours = hours + 1
        minutes = minutes - 60
    if hours >= 24:
        hours = hours % 24


elif making_time <= 60:
    hours = hours + int(making_time / 60)
    minutes = minutes + making_time % 60
    if minutes > 60:
        hours = hours + 1
        minutes = minutes - 60
    if minutes == 60:
        hours = hours + 1
        minutes = minutes - 60
    if hours >= 24:
        hours = hours % 24


if minutes > 60:
    hours = hours + 1
    minutes = minutes - 60
if minutes == 60:
    hours = hours + 1
    minutes = minutes - 60


print(hours, minutes, sep=" ")