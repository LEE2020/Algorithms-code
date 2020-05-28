import os 
import time
import sys
sys.setrecursionlimit(100000)

def QuickSortFirst(A):
    global cnt_first,cnt_last,cnt_mid
    if len(A)  == 1 or len(A) ==0 :
        return A
    else:
        cnt_first += len(A)  -1 
        #if len(A)<=1: return A 
        l = 0 
        #left,right,pos  = partition_first(A,l, n )
        #print(cnt_first,len(left),len(right),pos)
        pivot = A[0]
        swap_pos = l+1
        for j in range(l+1,len(A)):
            if A[j]<pivot:
                A[j],A[swap_pos]=A[swap_pos],A[j]
                swap_pos +=1 
        A[0],A[swap_pos-1]=A[swap_pos-1],A[0] 
        #left = A[:swap_pos -1];right = A[swap_pos:]   
        first_part   = QuickSortFirst(A[:swap_pos-1])
        second_part  = QuickSortFirst(A[swap_pos:])
        first_part.append(A[swap_pos-1])
		   
    return (first_part+second_part)

def QuickSortLast(A):
    global cnt_last
    if len(A) == 0 or len(A) == 1 : 
        return A
    else:
        cnt_last +=len(A)-1 
        A[-1],A[0]=A[0],A[-1]
        l=0
        pivot = A[0]
        swap_pos = l+1
        for j in range(l+1,len(A)):
            if A[j]<pivot:
                A[j],A[swap_pos]=A[swap_pos],A[j]
                swap_pos +=1 
        A[swap_pos -1 ],A[0] = A[0],A[swap_pos-1]
        first_part = QuickSortLast(A[:swap_pos-1])
        second_part = QuickSortLast(A[swap_pos:])
        first_part.append(A[swap_pos-1])
    return (first_part + second_part)

def QuickSortLast2(A):
    global cnt_last
    if len(A)==1 or len(A)==0: return A 
    else:
        cnt_last +=len(A)-1
        #l=-1
        pivot = A[-1]
        swap_pos = len(A)-2
        for j in range(len(A)-2,-1,-1):
            if A[j] > pivot:
                A[j],A[swap_pos]=A[swap_pos],A[j]
                swap_pos -=1 
        A[-1],A[swap_pos+1]=A[swap_pos+1],A[-1]
     #   left= A[:swap_pos+1];right = A[swap_pos+2:]
        first_part   = QuickSortLast2(A[:swap_pos+1])
        second_part  = QuickSortLast2(A[swap_pos+2:])
        first_part.append(A[swap_pos+1])
    return (first_part + second_part)

def middle(x):
    if len(x)%2 ==0:
        return int(len(x)/2-1) 
    else:
        return int(len(x)/2)
def medim(x):
    mid = middle(x)
    #first=float(x[0]);last=float(x[-1]);mid=float(middle(x))
    if (x[0]-x[-1])*(x[0]-x[mid])<0 :
        return 0
    elif (x[-1]-x[0])*(x[-1]-x[mid]) < 0 :
        return -1
    else:
        return mid
def QuickSortMedim(A,n):
    global cnt_mid
    if n==1 or n==0: return A
    else:
        k = medim(A)
        if k!=0: A[0],A[k]=A[k],A[0]
        cnt_mid += len(A)-1
        l=0 
        pivot=A[l];swap_pos = l+1
        for j in range(l+1,n):
            if A[j]<pivot:
                A[j],A[swap_pos]=A[swap_pos],A[j]
                swap_pos +=1 
        A[0],A[swap_pos-1]=A[swap_pos-1],A[0]
        first_part = QuickSortMedim(A[:swap_pos-1],len(A[:swap_pos-1]))
        second_part = QuickSortMedim(A[swap_pos:],len(A[swap_pos:]))
        first_part.append(A[swap_pos-1])
        return (first_part+second_part)



if __name__ == "__main__":
    a=[]
    with open('QuickSort.txt') as f:
         for i in f:
            a.append(float(i.split("\n")[0]))
  #  print(type(a[0]),a[-1])
    cnt_first=0;cnt_last=0;cnt_mid=0
    starttime  = time.time()
    array2 = QuickSortLast(a)
    a=[]
    with open('QuickSort.txt') as f:
        for i in f:
            a.append(float(i.split("\n")[0]))
    array  = QuickSortFirst(a)
    a = []
    with open('QuickSort.txt') as f:
        for i in f:
            a.append(float(i.split("\n")[0]))
    array3 = QuickSortMedim(a,len(a))
    endtime = time.time()
    print("first  element , length of orignal : a  && sorted of array  " + str(len(a))+ "   unique " + str(len(set(a)) ))
    print("last  element : " + str(len(array))+"/"+str(len(set(array))))
    print("last  element : " + str(len(array2))+"/"+str(len(set(array2))))
    print("medium element : " + str(len(array3)) + "/"+str(len(list(set(array3)))))
    print("first / last/ mid comparision numbers : " + str(cnt_first)+"/"+str(cnt_last)+"/"+str(cnt_mid))
