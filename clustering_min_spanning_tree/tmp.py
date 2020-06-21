import sys
#import UnionFind from clustering
from  unionfind  import UnionFind
class UnionFind2:
    def __init__(self,data):
        self.nodes = {i:i for i,x  in enumerate(data)} 
    def find(self,p):
        return self.nodes[p]
    def union(self,list_tmp):
        _i = self.nodes[list_tmp[0]]
        list_tmp.pop(0)
        labels = [self.nodes[i] for i in list_tmp]
        for ind in self.nodes:
            if self.nodes[ind] in labels:
                self.nodes[ind] = _i
            
            
    def union2(self,p,q):
        _i = self.nodes[p]
        _j = self.nodes[q] 
        for ind in self.nodes:
            if self.nodes[ind] ==_j :
                self.nodes[ind] =_i 


def mix_dis(rst2):
    rst3 = []
    for i in rst2:
        for j in rst2:
            if i != j and (i+j) not in rst3: rst3.append(i+j)
    return rst3
def hamming_dis():
   # bin1 = decimal_to_binary(node1)
   # bin2 = decimal_to_binary(node2)
    #rst = node1 ^ node2 
    rst1 = [0]
    rst2 = [1 << i for i in range(24)]
    #rst3 = [3 << i for i in range(24)]
    rst3 = mix_dis(rst2)
    return ( rst1+rst2 +rst3)
#too slowly
def cluster(data):
    global done_points 
    nf = UnionFind(data)
    distance = hamming_dis()
    #print(distance)
    for ii in range(len(data)):
        i = data[ii]
        if ii%100 ==0 : print(ii)
        for j in distance:
            rst = i ^ j
        #    print(i,j,rst)
            if rst in data:
                indexs = [i for i,x in enumerate(data) if x == rst ]
                # self point deleted 
                if ii in indexs: indexs.remove(ii)
                if len(indexs) ==0 :continue
                # done points relation deleted  
                for inx in indexs :
                    if (inx,ii) or (ii,inx) in done_points: continue
                    nf.union(ii,inx)
                    done_points[ii,inx]=1

              # [nf.union(ii,inx)  for inx  in indexs if  len(indexs)>0] 

    return nf.nodes


def cluster_update(data,values_ind_map):
    c = [i for i in range(len(data))] 
    nf = UnionFind(c) 
    distance = hamming_dis() # distance 0 ,1, 2
    print(distance)
    for i in distance:
        for j in values_ind_map:
            #print("i , : j ", i,j )
            k = i^j
            if k in values_ind_map:
                                   
                nodes = values_ind_map[k]
                nodes2 = values_ind_map[j]
                 
                if len(set(nodes+nodes2)) <= 1 : continue
                nf.union(list(set(nodes+nodes2)))
    return nf.parents


def decimal_to_binary(x):
    bins = bin(x).replace("0b","")
    if len(bins)<24:
        "".join(['0']*(24-len(bins)))+(bins)
    return bins

def binary_to_decimal(x):
    return int(x,2)

if __name__ == "__main__":
    #global done_points
    values_ind_map={}
    flag = True
    cnt = 0
    data=[]
    #data =[[] for i in range(200000)]
    with open('test2.txt') as f:
        for row in f:  
            if flag == True:
                flag = False
                continue
            row = "".join(row.strip().split())
            da = binary_to_decimal(row)
            #data[cnt] += [da]
            if da not in values_ind_map:
                values_ind_map[da] = [cnt]
            else:
                if cnt not in values_ind_map[da]:
                    values_ind_map[da] += [cnt]

            cnt +=1
            data.append(da)
			#nodes.append(rows)

    #for row in data:
    #    [i for i,x in enumerate(data) if x == rst ] 
    print(len(data))         
    rst = cluster_update(data,values_ind_map)
    print(set(rst.values()))
 
