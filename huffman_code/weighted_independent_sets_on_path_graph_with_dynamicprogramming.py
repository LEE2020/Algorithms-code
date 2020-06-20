import os
##################
##https://wincent.com/wiki/Computing_the_Maximum_Weighted_Independent_Set_of_a_graph_path
#################

def compute_max_weighted_is(data):
    A = [[] for i in range(len(data))]; A[0]= 0 ;A[1]= data[1]
    for i in range(2,len(data)):
        A[i] =  max(A[i-1],A[i-2]+data[i])
    A[-1]=0
    return A

def reconstruciton(A,data):
    
    rst =[]
    index = len(A)-1 
    while index >=1:
        if A[index-1] >= A[index-2] + data[index]:
            index -=1 
        else:
            rst.append(index)
            index -=2

    return rst 

if __name__=="__main__":

    data = []
    with open('mwis.txt') as f:
        for row in f:
            rows = int(row.strip().split()[0])
            if rows == 1000: 
                data.append(0)
                continue
            data.append(rows)

    rst2 = []
    cmt = [1,2,3,4,17,117,517,997]
    A  = compute_max_weighted_is(data)
    print("max_weight:",A[-1])
    rst = reconstruciton(A,data)
    for i in cmt:
        if i in rst: rst2.append(1)
        else:
            rst2.append(0)
    print(rst2)
    print(rst)   




