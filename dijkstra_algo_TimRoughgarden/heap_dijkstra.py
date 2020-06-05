# author: frona_li@126.com#
import os
import sys


class Dijkstra:
    t = 0
    def __init__(self,s):
        self.X = set()
        self.V = set()
        self.A = {s:0}
        self.X.add(s)
        self.B ={s:[]}
        self.Graph = dict()
 
    def load_data(self,filepath):
        with open(filepath) as f:
            for line in f:
                row = line.strip().split('\t',1)             
                self.Graph[int(row[0])] = row[1]  
        self.V = set(self.Graph)
    def work(self):
        #print("original point" + str(last))        
        while self.X != self.V :
            tmp = [] 
            for vertex in self.X: 
                edges = self.Graph[vertex]
                for row in edges.strip().split('\t'):
                    tail,weight = int(row.strip().split(',',1)[0]),int(row.strip().split(',',1)[1])
                    if tail in self.X : continue
                    score = int(weight) + self.A[vertex]
                    tmp.append((vertex,tail,score))
                    if len(tmp) ==1: continue 
                    parent = int(len(tmp)/2 if len(tmp)%2 ==0 else (len(tmp)-1)/2) 
                    current = int(len(tmp))
                    #print(tmp)
                    while  tmp[current-1][2] < tmp[parent-1][2] :  # score 比较
                        tmp[current-1],tmp[parent-1] = tmp[parent-1],tmp[current-1]
                        current = parent
                        parent = int(((current+1)/2 if (current +1 ) %2 ==0 else (current)/2))
                        #print(current,parent)
           # tmp = sorted(tmp,key= lambda x :x[2]) 
            self.A[int(tmp[0][1])] = int(tmp[0][2])
            self.B[int(tmp[0][1])] = str(self.B[int(tmp[0][0])])+ '->'+ str(tmp[0][1])+"->"
            self.X.add(tmp[0][1])

            print("now vertex  added " + str(tmp[0][1]) + " with path length  " + str(tmp[0][2])+ " head point " + str(tmp[0][0]))
            
        return self.A 




if __name__ == "__main__":
    dijkstra = Dijkstra(1)
    result=''    
    dijkstra.load_data('./dijkstraData.txt')
    #print(dijkstra.V)
    outlist = [7,37,59,82,99,115,133,165,188,197]  
    rst = dijkstra.work()
    print([rst[i] for i in outlist if rst[i]])
    #print(dijkstra.B)
	#for i in outlist:
    #    result+= str(rst.get(i,1000000))+','
    #print(result)
