import os
import sys
import threading 
#sys.setrecursionlimit(2**20)



def DFS_first(G,i):
    global t ; global is_explored;#global leader ;global f 
    is_explored[i] = True
    #leader[i]=s 
    for j in G[i]:
        try:  # sink point 没有G[i]值
            if is_explored[j]==False:
                DFS_first(G,j)
        except:
            continue
    t =t +1
    stack_finish.append(i)
    #f.append(j)
def DFS_sec(G,i):
    global is_explored; global leader 
    is_explored[i] = True
    leader[i] = s 
    for j in G[i]:
        try: 
            if is_explored[j] == False:
                DFS_sec(G,j)
        except:
            continue   

def main():
    global is_explored;global stack_finish ;global s;global leader ;global t 
    stack_finish =[] ; s = None ; leader = dict();f=[];t=0
    num_nodes= 875714
    G = [[] for row in range(num_nodes)]
    G_new = [[] for row in range(num_nodes)]
    is_explored = [False] * num_nodes
    with open('SCC.txt') as ff:
        for row in ff:
            if len(row.strip().split() )<2 :continue
            ver1,ver2 = row.strip().split(' ' ,1) 
            try:
                G[int(ver1)-1] += [int(ver2)-1] 
                G_new[int(ver2)-1] += [int(ver1)-1]
            except:
                print(ver1,ver2)

    
    for i in range(num_nodes):
        
        if is_explored[i] == False:
            DFS_first(G_new,i)

    print("finish reverse: and magical ordering length:      "+ str(len(stack_finish)))
    t= 0 ; s=None; is_explored = [False]*num_nodes; leader = dict()
    G_new =[]
    while stack_finish:
        i = stack_finish.pop()
        if is_explored[i] == False:
            s = i 
            DFS_sec(G,i)


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
        
 
