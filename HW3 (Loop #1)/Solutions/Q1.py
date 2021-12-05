n = int(input())

flag = True
next_prime = n + 1
while flag:
    flag = False
    i = 2
    while i * i <= next_prime:
        if next_prime % i == 0:
            flag = True
        i += 1 
    next_prime += 1

print(next_prime - 1)
