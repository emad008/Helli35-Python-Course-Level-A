for i in range(100, 1000):
    s = str(i)
    sum = 0
    for c in s:
        sum += int(c) * int(c) * int(c)
    
    if sum == i:
        print(i)
