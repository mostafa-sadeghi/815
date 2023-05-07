i = 0 
t = 0
while i < 10:
    n = int(input('enter a number: '))
    m = n % 2
    if m != 0:
        t = t + n
    i = i + 1

print(t)

for i in range(10):
    n = int(input('enter a number: '))
    m = n % 2
    if m != 0:
        t = t + n

print(t)