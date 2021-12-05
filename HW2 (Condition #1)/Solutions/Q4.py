a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())

if a1 > b1:
    tmp = a1
    a1 = b1
    b1 = tmp

if a2 > b2:
    tmp = a2
    a2 = b2
    b2 = tmp

if a3 > b3:
    tmp = a3
    a3 = b3
    b3 = tmp

print(a1 + a2 + a3)

