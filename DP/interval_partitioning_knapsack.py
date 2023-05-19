# The Knapsack problem can be considered as filling up an n-by-W
# array using the following algorithm.

# Input: n, W, w1,…,wn, v1,…,vn
# for w = 0 to W
# M[0, w] = 0
# for i = 1 to n
# for w = 1 to W
# if (wi > w)
# M[i, w] = M[i-1, w]
# else
# M[i, w] = max {M[i-1, w], vi + M[i-1, w-wi]}
# return M[n, W]


if __name__ == "__main__":
    
    table = [(1,1,1), (2,6,2), (3,18,5), (4,22,6), (5,28,7)]
    n = len(table)
    print(n+1)
    capacity = 11
    
    M = [[0 for i in range(capacity+1)] for j in range(n+1)]
    # for i in range(n+1):
    #     print(M[i])
    
    print()

    for i in range(1, n+1):
        for w in range(1, capacity+1):

            if (table[i-1][2] > w):
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = max(M[i-1][w], (table[i-1][1]+M[i-1][w-table[i-1][2]]))

    for i in range(n+1):
        print(M[i])
