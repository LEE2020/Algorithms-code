import os
import sys
import threading 
#sys.setrecursionlimit(2**20)



def DFS(G,i):
    global t ; global is_explored;global leader ;global f 
    is_explored[i] = True
    leader[i]=s
    if len(G[i]) == 0 : 
        t = t+1 
        f[i] =t

    else: 
        for j in G[i]:
            if is_explored[j]==False:
                DFS(G,j)
        t =t +1
        f[i]=t

def DFS_loop( G):
    #n = sorted( G.keys(), reverse = True)
    n = len(G) 
    global s 
    leader={}
    for i in range(n-1,-1,-1):
        if is_explored[i] == False:
            s = i 
            DFS(G,i)  

def main():
    global is_explored;global t; global f;global s;global leader 
    t = 0  ; f =dict() ; s = None ; leader = dict();
    num_nodes= 875714
    G = [[] for row in range(num_nodes)]
    G_new = [[] for row in range(num_nodes)]
    is_explored = [False] * num_nodes
    with open('SCC.txt') as ff:
        for row in ff:
            if len(row.strip().split() )<2 :continue
            ver1,ver2 = row.strip().split(' ' ,1)
            ver1,ver2 = int(ver1)-1,int(ver2)-1
            G_new[ver2]+=[ver1]
    DFS_loop(G_new)
    print("finish reverse: and magical ordering length:      "+ str(len(f)))
    t= 0 ; s=None; is_explored = [False]*num_nodes; leader = dict()
    G_new =[]
    with open('SCC.txt') as ff:
        for row in ff:
            if len(row.strip().split())<2 :continue
            ver1,ver2 = row.strip().split(' ' ,1)
            ver1= int(ver1)-1;ver2=int(ver2)-1
            ver1,ver2 = f[ver1],f[ver2]
            G[ver1-1]+= [ver2-1]
    DFS_loop(G)
    rst ={};rst2=[]
    for key,value in leader.items():
        if value not in rst:
            rst[value]=[];rst[value].append(key)
        else:
            rst[value].append(key)
    for key in rst.keys():
        rst2.append(len(rst[key]))
    rst2 = sorted(rst2,reverse = True);tmp=0
    print(rst2[:5])
if __name__ =="__main__":
    threading.stack_size(67108864)        
    sys.setrecursionlimit(2 ** 20)        
    thread = threading.Thread(target=main)       
    thread.start()
        
   
