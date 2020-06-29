
import os



class Graph(object):
    
    def __init__(self,datafile):
        self.graph=dict()
        with open('g2.txt') as f :
            for row in f:
                rows = row.strip().split()
                if len(rows) <3 :continue
                tail,head,length = int(rows[0]),int(rows[1]),int(rows[2])
                if tail not in self.graph:
                    self.graph[tail]={head:length}
                else:
                    self.graph[tail][head]=length



def bellmanford(graph,source):
    distance = {}
    # initialize, distance[i,s]=0 也要初始化 
    for i in graph:
        distance[0,i]=float('inf')
    
    for i in range(len(graph)+1):
        distance[i,source] = 0 
    
    for i in range(1,len(graph)+1):
        for u in graph:
            tmp = float('inf') 
            for indeg in graph[u]:
                tmp = min( tmp, distance[i-1,indeg] + graph[u][indeg])
            distance[i,u] = min(distance[i-1,u],tmp)
            #print(i,u, distance[i,u])
    # to all vertices , distance[n-1,u] == ditance[n,u] means no negative cycle             
    for u in graph:
        assert  distance[len(graph)-1,u] == distance[len(graph),u] 
        

if __name__ == "__main__":

    datafile = './a.txt'
    job = Graph(datafile)
    #mm = []
    #for node in job.graph:
    source = 1
    distance = bellmanford(job.graph,source)
    #s = sorted(distance.items(), key = lambda x:x[1],reverse=True) 
    #mm.append(s[-1][1])
    #print("node",  s[-1][1])
    #s=sorted(mm)
    #print(s[0])
