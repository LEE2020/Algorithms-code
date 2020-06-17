#encoding:utf-8
import math

#Uses python3
import sys

def merge_sort(A):
    if len(A) <= 1:
        return A, 0
    else:
        middle = (len(A)//2)
        left, count_left = merge_sort(A[:middle])
        right, count_right = merge_sort(A[middle:])
        result, count_result = merge(left,right)
        return result, (count_left + count_right + count_result)

def merge(a,b):
    result = []
    count = 0
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a[0])
            a.remove(a[0])
        elif  a[0] > b[0]:
            #count = count + (len(a) - 1)
            result.append(b[0])
            b.remove(b[0])
            count += (len(a)) #this is the important line
   
    if len(a) == 0:
        result = result + b
    else:
        result = result + a
    return result, count

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    #c = n * [0]
    b=[];inversion=0
    for i in open('IntegerArray.txt'):
	    
        #a=list(map(int,i.split()[0]));
        a=int(i.split()[0])
        b.append(a)
	
    array,tmp = merge_sort(b);
    #b.append(array);
       # print(tmp)
       # inversion = inversion +  tmp 
    print(len(array))
    print(tmp)


