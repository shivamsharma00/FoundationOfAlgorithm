# Memoization

# opt function
def Compute_OPT(n, jobs, p, M):
    
    if M[n-1] is None:

        if len(jobs) == 0:
            return 0
        else:
            job = jobs[n-1]
            sub_m = jobs[0:p[n-1]]
            M[n-1] = max(job[2]+Compute_OPT((p[n-1]), sub_m, p, M), Compute_OPT(len(jobs[0:n-2]), jobs[0:n-2], p, M))
    print(M)
    return M[n-1] 

# Jobs are in the form (start_time, end_time, Weight)
jobs = [(0,6,23), (1,4,12), (3,5,20), (3,8,26), (4,7,13), (5,9,20), (6,10,11), (8,11,16)]
# sorted the jobs by weight
jobs.sort(key=lambda x : x[1] ) 
p = [0] * len(jobs)
M = [None] * len(jobs)

count = 0
for j in jobs:

    inverted_j = sorted(jobs[0:count], key=lambda x:x[1], reverse=True)
    start_t = j[0]
    
    for (s_t, f_t, w) in inverted_j:
        if f_t<= start_t:
            p[count] = jobs.index((s_t, f_t, w))+1
            break
    count+=1
print(jobs) 

print(Compute_OPT(len(jobs), jobs, p, M))


    # print(inverted_j) 
