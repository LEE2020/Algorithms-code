import os
# bottom up  by dynamic programming



def floydwarshall(graph,allpoint):
    distance = graph 
    # k is intermedian vertex 
    for k in allpoint:
        for i in allpoint:
            for j in allpoint:
                distance[i][j] =  min(distance[i][j], distance[i][k]+ distance[k][j])



    return distance 



if __name__ =="__main__":
    allpoint =set()
    with open('g3.txt') as f:
        for row in f:
            rows = row.strip().split()
            if len(rows)<3 :continue
            allpoint.add(int(rows[0]))
            allpoint.add(int(rows[1]))

    INF = float('inf')
    allnumber = len(allpoint)
    graph = [[ INF for i in range(allnumber+1)] for j in range (allnumber+1)]
    for i in range(allnumber+1):
        graph[i][i] = 0 

    # construct input matrix: w = n*n matrix, graph[i][j] means vertex i to vertex j 's  length 
    with open('g3.txt') as f:
        for row in f:
            rows = row.strip().split()
            if len(rows)<3 :continue
            tail,head,length = int(rows[0]),int(rows[1]),int(rows[2])
            graph[head][tail] = length
    minvalue = float('inf')       
    distance = floydwarshall(graph,allpoint)
    for i in range(allnumber+1):
        for j in range(allnumber+1):
            if distance[i][j] !=  0 and  distance[i][j] != float('inf'):
                if distance[i][j] < minvalue: minvalue = distance[i][j] 

    print(minvalue)
