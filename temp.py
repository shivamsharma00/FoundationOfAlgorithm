M = [[0 for i in range(3)] for j in range(3)]
count = 0

for i in range(3):
    for j in range(3):
        l = M[i] 
        l[j] =  count
        count +=1

    for i in range(3):
        print(M[i])
