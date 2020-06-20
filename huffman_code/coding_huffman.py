import sys




class Node(object):
    def __init__(self,weight,index):
        self.left = None
        self.right = None
        self.parent = None 
        self.weight = weight 
        self.index = index
    def isleft(self):
        return self.parent.left == self



def create_nodes(weights):
    nodes = [Node(weight,i) for i, weight in enumerate( weights)]
    return nodes


def huffman_tree(data):
    nodes = create_nodes(data)
    tmp = nodes
    cnt = len(tmp)
    while len(tmp)>1:
        tmp = sorted(tmp,key = lambda x:x.weight,reverse = True  )
        left = tmp.pop()   
        right = tmp.pop()
        node_parent = Node(left.weight + right.weight,cnt) 
        node_parent.left = left 
        node_parent.right = right 
        left.parent = node_parent 
        right.parent = node_parent 
        tmp.append(node_parent)
        cnt +=1 
    tmp[0].parent = None
    root = tmp[0] 
    return  root,nodes
    

def coding(data):
    root,nodes = huffman_tree(data)
    
    for i in nodes:
        note = i
        # all nodes are all leaves in huffman tree
        while note.index != root.index : 
            if note.isleft():
                if i.index not in huffman_code:
                    huffman_code[i.index] =[0]
                else:
                    huffman_code[i.index] +=[0]
            else: 
                if i.index not in huffman_code:
                    huffman_code[i.index] =[1]
                else:
                    huffman_code[i.index] +=[1] 
            note = note.parent  
            #print(huffman_code) 
    return huffman_code 



if __name__=="__main__":
    data = [] ; global huffman_code 
    with open('huffman.txt') as f:
        for row in f:
            rows = int(row.strip().split()[0])
            if rows == 1000:continue
            data.append(rows)
    huffmanTree = huffman_tree(data)
    huffman_code ={}
    huffman_code = coding(data)
    sorted_huffman_code = sorted(huffman_code.items(), key = lambda x: len(x[1]) ,reverse =True)
    print(len(sorted_huffman_code.pop(0)[1]),len(sorted_huffman_code.pop(-1)[1]))
   # print(len(sorted_huffman_code[0]),len(sorted_huffman_code[-1]))
