a, b = input().split()
a = int(a)
b = int(b)


if b < 11:
    add = 'Right'

if b >= 11:
    add = 'Left'
    b = 21 - b

a = 11 - a
print(add, a, b)

