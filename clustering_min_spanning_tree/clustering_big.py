import sys

import UnionFind from clustering

def hamming_dis(node1,node2):
    dis = 0
    for i in range(24):
        if node1[i] != node2[i]: dis += 1 

    return dis 


def cluster(nodes):
    distance = []
    for i in nodes:
        


if __name__ == "__main__":
    nodes = []
    with open('clustering_big.txt') as f:
        for row in f:
            rows = row.strip().split()
            if len(rows) <24:continue
            nodes.append(rows)
    
        
