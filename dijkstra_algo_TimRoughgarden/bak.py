import math 
def read_weighted_adjacency_list(path):
    # Read the adjacency list from a specified file
    f = open(path, mode='r')
    data = f.readlines()

    adjacency_list = {}

    for row in data:
        row_data = row.split()
        vertex = int(row_data[0])

        pairs = [t.split(',') for t in row_data[1:]]
        weighted_edges = {int(t[0]): int(t[1]) for t in pairs}

        adjacency_list[vertex] = weighted_edges

    return adjacency_list
class DirectedGraph:
    def __init__(self, adjacency_list):
        self.adj_list = adjacency_list
        self.explored = {key: False for key in self.adj_list.keys()}
        self.vertices = set([v for v in self.adj_list])

    def __getitem__(self, item):
        return self.adj_list[item]

    def __repr__(self):
        return str(self.adj_list)

    def exploreVertex(self, vertex):
        # Mark vertex as explored
        self.explored[vertex] = True

    def isExplored(self, vertex):
        # Check if vertex has been explored
        return self.explored[vertex]
def slowDijkstra(G, s):
    # Implementation of Dijkstra's algorithm without using a heap
    V = G.vertices
    X = {s}
    A = {s: 0}
    B = {s: []}
    while X != V:
        dijkstra_scores = {}

        for v in X:
            edges = G[v]

            for w in edges:
                if w not in X:
                    dijkstra_scores[(v, w)] = A[v] + edges[w]

        e, score = sorted(dijkstra_scores.items(), key=lambda x: x[1])[0]
        v_star, w_star = e
        print("add vertex       " + str(w_star) + "      weights     " + str(score) + "      origin  " +str(v_star)) 
        A[w_star] = score
        B[w_star] = B[v_star] + [(v_star, w_star)]
        X.add(w_star)
    return A, B
adj_list = read_weighted_adjacency_list(path='./dijkstraData.txt')
G = DirectedGraph(adjacency_list=adj_list)

A, B = slowDijkstra(G=G, s=1)
#print(B)
print([A[x] for x in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]])
