

import sys


class Tree:
    def __init__(self,data):
        self.weights={}
        self.index={}
        for i in range(len(data)):
            self.weights[data[i]] = str(i)
            #self.index[i] = i 
    def add(self,w,i):
        self.weights[w] = i
    def delete(self,w):
        del self.weights[w]

def code(data):
    tree = Tree(data)
    while len(tree.weights) > 1:
        #print(len(tree.weights))
        sorted_weight = sorted(tree.weights.items(),key=lambda x:x[0])
  
        #print(len(sorted_weight))
        w1,i1 = sorted_weight[0]
        w2,i2 = sorted_weight[1]
        i_all = str(i1)+'*'+str(i2)+'__'
        w_all = int(w1) + int(w2)
        tree.add(w_all,i_all)
        tree.delete(w1)
        tree.delete(w2) 
                
    return tree.weights

if __name__ == "__main__":
    data = []
    flag = True
    with open('huffman.txt') as f:
        for row in f:
            rows = int(row.strip().split()[0])
            if flag : 
                flag = False 
                continue
            data.append(rows) 
    rst = code(data);cnt ={}
    for i in rst.values():
        ii = i.strip().split('_')
        for j in ii:
            if len(j)==0:continue
            if j not in cnt:
                cnt[j]=1 
            else:
                cnt[j]+=1
    cnt_sorted = sorted(cnt.items(),key = lambda x:x[1],reverse =True)
    print(rst.values())
