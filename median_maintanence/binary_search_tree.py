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
            rst.append((pos,root.value))
        if root.right != None:
            current = root.right
            findpos(current,pos)
    return rst 
                 
def findvalue(root,value):
    global rst2;global cnt 
    if root == None:
        return None
    else:
        if root.left !=None:
            current = root.left
            findvalue(current,value)
        cnt += 1
        if root.value == value: 
            rst2.append(cnt)
        if root.right != None:
            current = root.right
            findvalue(current,value)
    return rst2 


# inserts element ,In AVL tree insertion, we used rotation as a tool to do balancing after insertion caused imbalance. 
#In Red-Black tree, we use two tools to do balancing.
# recolor/ rotation 


def avl_rotation(root):
    pass
def red_black_recolor(root):
    pass 


def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.value) 
        inorder(root.right)

if __name__ =="__main__":
    #r = Node(50) 
    #insert(r,Node(30)) 
    #insert(r,Node(20)) 
    #insert(r,Node(40)) 
    #insert(r,Node(70)) 
    #insert(r,Node(60)) 
    #insert(r,Node(80))
#    inorder(r)
    data =[];flag = True
    with open('Median.txt') as f:
        for row in f:
            rows = int(row.strip().split()[0])
            if flag == True:
                r = Node(rows)
                flag = False
            insert(r,Node(rows))
    
    global cnt ; global rst  ;global rst2 ; global cnt2 
    cnt = 0 ; rst = [];rst2= [];cnt2 = 0 
    print("all nodes " +str(countNodes(r)))
    median = int(nums/2) if nums %2 ==0 else int((nums+1)/2)
    print("median " +str(findvalue(r,median)))   
     

