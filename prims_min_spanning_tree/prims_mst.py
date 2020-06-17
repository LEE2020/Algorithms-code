import random


class Prim(object):
    def __init__(self):
        self.data = []
        self.V = set()
        self.X = set()
        self.T = []
    def  loaddata(self):
        with open('edges.txt') as ff:
            for row in ff:
                if len(row.strip().split()) < 3 :continue 
                vext1,vext2,weight = int(row.strip().split()[0]),int(row.strip().split()[1]),int(row.strip().split()[2])
                self.data.append((vext1,vext2,weight))                
				
        return self.data            
    def get_vextices(self,data):
        
        v1 = set([i for i,j,v in data])
        self.V= v1.union(set([j for i,j,v in data]))

    def mst(self):
        data = self.loaddata()
        print(" load data finished...")
        self.get_vextices(data)
        self.X.add(random.sample(self.V,1)[0])
        cnt =1 
        while self.X != self.V :
            all_X_edges = [e for e in self.data if (e[0] in self.X and e[1] not in self.X) or (e[0] not in self.X and e[1] in self.X)] 
            if all_X_edges:
                cheapest_edge = sorted(all_X_edges, key = lambda x: x[2])[0]
                self.X = self.X.union({cheapest_edge[0],cheapest_edge[1]})
                self.T.append(cheapest_edge)
                print("the " + str(cnt) + " cheapest edge " + str(cheapest_edge)) 
                cnt +=1 
        cost = sum([T[2] for T in self.T])
        return cost 
            
            

if __name__ == "__main__":
    prim = Prim()
    print(prim.mst())
 
