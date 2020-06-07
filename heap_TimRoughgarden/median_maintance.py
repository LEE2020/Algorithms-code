

import time


class  heap:
    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]
        self.data = [] 

    def load_data(self):    
        with open('Median.txt') as f:
            for row in f:
                self.data.append(int(row.strip().split()[0]))
        return self.data

 
    def get_children(self,idx_parent):
        idx_children = int(2*idx_parent +1) ,int(2*idx_parent +2)  # zero-based array 
        return idx_children 
    def get_parent(self, idx_child):
        return int(idx_child/2) if idx_child %2 ==0 else int((idx_child-1) /2 )
    def bubble_up(self,heapdata,inode,t):
        if t == "max" :
            parent = self.get_parent(inode)
            if parent < len(heapdata)  and heapdata[parent]<heapdata[inode]:
            #    print("right")
                heapdata[parent],heapdata[inode] = heapdata[inode],heapdata[parent]
            #    print("nnnnnn"+str(heapdata))
                self.bubble_up(heapdata,parent,t)
                #heapdata[parent] ,heapdata[inode] = heapdata[inode],heapdata[parent]
        elif t == "min":
            parent = self.get_parent(inode)
            if parent < len(heapdata) and heapdata[parent] > heapdata[inode]:
                #self.bubble_up(heapdata,parent,t)
                heapdata[parent],heapdata[inode] = heapdata[inode],heapdata[parent]
                self.bubble_up(heapdata,parent,t)
                
        return heapdata
    def bubble_down(self,heapdata,inode,t):
        if t== "max":
            ichildren = self.get_children(inode)
            for ichild in ichildren:
                if ichild < len(heapdata) and heapdata[inode] < heapdata[ichild]:
                    #self.bubble_down(heapdata,ichild,t)
                    heapdata[inode],heapdata[ichild] = heapdata[ichild],heapdata[inode]
                    self.bubble_down(heapdata,ichild ,t)
        elif t == "min":
            ichildren = self.get_children(inode)
            for ichild in ichildren:
                if ichild < len(heapdata) and heapdata[inode] > heapdata[ichild]:
                    #self.bubble_down(heapdata,ichild,t)
                    heapdata[inode],heapdata[ichild] = heapdata[ichild],heapdata[inode]
                    self.bubble_down(heapdata,ichild,t)
        return heapdata	
    def is_balanced(self,heapdata,idx_parent,idx_child,t):
        if t =="max": is_balance=heapdata[idx_parent] > heapdata[idx_child] 
        if t=="min" : is_balance=heapdata[idx_parent] <  heapdata[idx_child]
        
        return is_balance


    def median(self):
        min_heap = [] ; max_heap = [];rst=[]
        data = self.load_data()
       
        for stream in data:
            if stream == 4289: print ("origin max_heap        " +str(max_heap)+str(max(max_heap)))
            if stream == 4289: print(len(max_heap),len(min_heap))
            if len(min_heap) - len(max_heap) >=1 : 
                max_heap.append(stream)
                inode = len(max_heap) -1 
                idx_parent = self.get_parent(inode)
                #print("orgin" + str(max_heap) )
                if not self.is_balanced(max_heap,idx_parent,inode,"max"):
                    self.bubble_up(max_heap,inode,"max") 
                #    print("new max" + str(max_heap))
            else:
                min_heap.append(stream)
                inode = len(min_heap) -1
                idx_parent = self.get_parent(inode)
                if not self.is_balanced(min_heap,idx_parent,inode,"min"): self.bubble_up(min_heap,inode,"min")
             
            if len(max_heap) >=1 and max_heap[0] > min_heap[0]:
                max_heap[0],min_heap[0] = min_heap[0],max_heap[0]
                self.bubble_down(max_heap,0,"max")
                self.bubble_down(min_heap,0,"min")
        
            if len(max_heap) >= len(min_heap):
                rst.append( max_heap[0])
            else:
                rst.append(min_heap[0])
            #print(rst[-1])
         #   if (len(max_heap)>1 and (max_heap[0] != max(max_heap) )):#or min_heap[0] != min(min_heap))):
         #       print(max_heap)
         #       print(max_heap[0],max(max_heap))
         #       break
            #print(rst[-1])
        return rst,max_heap,min_heap 

if __name__ =="__main__":
    oj = heap()
    #data=oj.load_data()
    #data=[4,9,8,1,3,2,6,7]
    rst,max_heap,min_heap  = oj.median()
    #print(max_heap[0]==max(max_heap))






