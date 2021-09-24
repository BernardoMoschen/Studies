"""
Program that reads a start time and a duration time, calculating the end time.
- without "datetime." (lib)
"""

hi = int(input('Type the start time: '))
mi = int(input('Type the start minute: '))
si = int(input('Type the start second: '))
time = int(input('Enter duration in seconds: '))

hs = 3600
h = int(time / hs)
m = int((time - (h * hs)) / 60)
s = int((time - (h * hs) - (m * 60)))

hf = hi + h
mf = mi + m
sf = si + s

print(f'The start time is: {hi}h, {mi}m e {si}s')

if hf >= 24:
    hfi = hf - 24
    print(f'The closing time is: {hfi}h, {mf}m e {sf}s')
else:
    print(f'The closing time is: {hf}h, {mf}m e {sf}s')
