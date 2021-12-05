a = int(input())
e = a
d = 0

while a != 0 :
    b = a % 10
    d = d * 10 + b
    a //= 10

if e == d :
    print("YES")

else :
    print("NO")
