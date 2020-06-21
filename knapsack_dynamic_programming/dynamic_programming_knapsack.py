import os 
import sys
sys.setrecursionlimit(800000)







# top-down 
def knapsack_big(W,n,v,w):
    global A
    if (n,W) in A: return A[n,W]
    if W <= 1 or n == 1 :
        return 0
    if (w[n] > W ):
        A[n,W] = knapsack_big(W,n-1,v,w)
        return A[n,W]
    else:
        #print(W)
        A[n,W] = max(v[n] + knapsack_big(W-w[n],n-1,v,w,),knapsack_big(W,n-1,v,w))
        return A[n,W]


 
#bottom-up 
def knapsack(W,number_items,v,w):
    A = [[0 for x in range(W+1)] for y in range(number_items+1)]
    for i in range(1,number_items+1):
        for x in range(W+1):
            if x < w[i]: A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x],A[i-1][x-w[i]]+v[i])
        if i %100 ==0 : print("i ,x :" , i ,x  , A[i][x])
    return A[-1][-1]
    

if __name__ == "__main__":
    v = []
    w = []
    #global A 
    #A = [[0 for x in range(W+1)] for y in range(number_items+1)]
    global A 
    A = {}
    flag = True
    with open('knapsack_big.txt') as f:
        for row in f:
            rows  = row.strip().split()
            if len(rows) <2 :continue
            if flag:
                W = int(rows[0])
                number_items = int(rows[1])
                flag = False
                v.append(0);w.append(0)
                continue
            v.append( int(rows[0]))
            w.append(int(rows[1]))
    print("computing",type(w))
    #rst= knapsack(W,number_items,v,w) 
    #print("knapsack bottom up : " , rst)
    rst_big = knapsack_big(W,number_items,v,w)
    print("knapsack top down :  " , rst_big)
