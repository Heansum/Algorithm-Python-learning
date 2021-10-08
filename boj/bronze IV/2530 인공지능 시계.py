hours, minutes, seconds = input().split(' ')
making_time = int(input())

hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)

now_time = hours * 60 * 60 + minutes * 60 + seconds

after_cooking_time = now_time + making_time

if after_cooking_time >= 86400:
    after_cooking_time = after_cooking_time % 86400

hours = after_cooking_time / 3600
hours = int(hours)
after_cooking_time = after_cooking_time - hours * 3600
minutes = after_cooking_time / 60
minutes = int(minutes)
seconds = after_cooking_time % 60
print(hours, minutes, seconds, sep=" ")