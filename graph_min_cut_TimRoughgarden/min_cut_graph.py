import os
import sys
import numpy as np 
import random 

def randomSelect(graph,inT,noD):
    #noD.add(100)
    #noD.add(3)
    random.seed(random.randint(1,40000))
     
    listall = [ i for i in range(1,201)]  
    #print(listall)
    if len(inT) != 0 :
        
        inT_connected = []
        for i in inT:
            for j in graph[i]:
                inT_connected.append(int(j))
        listall = list(set(listall).intersection(set(inT_connected)))  
    listall = list(set(listall).difference(inT))
    listchoose = list(set(listall).difference(noD))
        
    if len(listchoose) == 0 :
        return  0 
    else:
        tmp = random.sample(listchoose,1)[0]
       # print("now point....."+ str(tmp))
        return tmp 
    
        
        



def min_cut(graph,A,B):
    rst = 0 
    while len(A)  != 199 :
        contractionPointA = randomSelect(graph,A,B)
        if contractionPointA != 0 :
            #print(contractionPointA)
            A.add(contractionPointA) 
            rst +=1 
        #contractionPointB = randomSelect(graph,B,A)
        #if contractionPointB != 0 :
        #    B.add(contractionPointB)
        #    rst +=1 
        #print("now len(A) + len(B) : " +str(len(A) + len(B))+ " now contraction numbers : "  + str(rst) ) 
    rst,B = crossingEdges(graph,A,B)
    return A,B,rst 


def crossingEdges(graph,A,B):
    cnt = 0;#A ,B = set(),set()
    listall = [i for i in range(1,201)]
    B = set(list(set(listall).difference(A)))
    if len(A & B) !=0 :
        sys.stdout.write("wrong cut,there elements in both a and b!!")
    else:
        for i in A:
            for j in B:
                C = set(graph[i])
                tmp = len(C & B)
                cnt += tmp 

    return cnt,B       
if __name__ == "__main__" :
    graph = dict();fields=[]
    with open('kargerMinCut.txt') as f:
        for row in f:
            rows=row.strip().split('\t')
            graph[int(rows[0])]=list(map(int,rows[1:]))
    #print(graph)
    global A ; global B;global rst
    #A= set();B= set();rst = 0
    #for i in range(100):
    #    rst1 = randomSelect(graph,A,B)
    nn={};D = set()
    for i in range(40000):
        A = set();B = set();rst=0
        _,B,rst1 = min_cut(graph,A,B)
		
        if rst1 not in nn and list(B)[0] not in D:
            nn[rst1]=1
            D.add(list(B)[0])
        elif rst1 in nn and list(B)[0] not in D:
            nn[rst1]+=1 
            D.add(list(B)[0])
        print(" contraction numbers : "+ str(rst1))

print(sorted(nn.items(),key = lambda item:item[0]))

print(D,len(D))
