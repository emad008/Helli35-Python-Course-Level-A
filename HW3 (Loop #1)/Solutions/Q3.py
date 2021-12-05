n = int(input())


# n = 5

# 1 , i = 0 -- zero based
# 1 1 , i = 1 
# 1 2 1 , i = 2
# 1 3 3 1 , i = 3
# 1 4 6 4 1 , i = 4

for i in range(n):
    for j in range(i + 1): # [0, i]
        i_factoriel = 1
        for k in range(1, i + 1): # k = 1, k = 2, k = 3, ..., k = i 
            i_factoriel *= k

        j_factoriel = 1
        for k in range(1, j + 1):
            j_factoriel *= k

        ij_factoriel = 1
        for k in range(1, i - j + 1):
            ij_factoriel *= k
        
        # i! // (j! * (i - j)!)
        print(i_factoriel // (j_factoriel * ij_factoriel), end=' ')
    print()
