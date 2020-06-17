import sys
# find median through bst 

class Node:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key 

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right == None:
                root.right = node 
            else:
                insert(root.right,node)
        elif root.value > node.value:
            if root.left == None:
                root.left = node
            else:
                insert(root.left,node)
def countNodes(root):
    global cnt  
    if root == None:
        return 0 
    elif root !=None:
        if root.left != None:
            current = root.left 
            countNodes(current)
        cnt +=1 
        #print(root.value)
        if root.right != None:
            current = root.right
            countNodes(current)
    return cnt  
	 
def findpos(root,pos):
    global rst; global cnt2  
    if root ==None:
        return []
    else:
        if root.left != None:
            current = root.left
            findpos(current,pos)
        cnt2 +=1 
        if cnt2 == pos: 
            rst.append(root.value)
        if root.right != None:
            current = root.right
            findpos(current,pos)
    return rst 
        
if __name__ == "__main__":
    data =[];flag = True
    with open('Median.txt') as f:
        for row in f:
            rows = int(row.strip().split()[0])
            data.append(rows)
    
 
    global cnt ; global rst  ;global rst2 ; global cnt2 
    cnt = 0 ; rst = [];cnt2 = 0 
    flag = True ; result = []
    for idx in range(len(data)):
        if flag == True:
            r = Node(data[idx])
            flag = False 
        else:
            insert(r,Node(data[idx]))
        current_node = int(countNodes(r))
        current_median_pos = int(current_node / 2)  if current_node % 2 == 0 else  int((current_node +1 )/2 )
        #print(current_node,current_median_pos,"current_median_pos")
        current_median  =  findpos(r,current_median_pos)
        result.append(current_median[0])
        print(current_median[0])
        cnt = 0;cnt2 = 0;rst = []
    print(sum(result) % 10000)  
