import datetime
import copy


def read_big_file(path):
    f = open(path, mode='r')
    data = f.readlines()
    f.close()

    lines = []

    for line in data[1:]:
        line = [int(n) for n in line.split()]
        lines.append(line)

    return lines


# UnionFind data structure
class HammingUnionFind:
    def __init__(self, codes):
        self.codes = {binary_list_to_decimal(c): c for c in codes}
        self.clusters = {key: key for key in self.codes.keys()}
        self.neighbors = {key: self.find_neighbors(key) for key in self.codes.keys()}

    def find(self, p):
        return self.clusters[p]

    def distance(self, i, j):
        dist = 0

        line_i = self.codes[i]
        line_j = self.codes[j]

        for k in range(len(line_i)):
            if line_i[k] != line_j[k]:
                dist += 1

        return dist

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)

        neighbors_of_p = self.neighbors[p]
        # neighbors_of_p = self.clusters

        for np in neighbors_of_p:
            try:
                z = self.clusters[np]
            except KeyError:
                continue

            if self.find(z) == qid:
                self.clusters[z] = pid

    def find_neighbors(self, p):
        code_p = self.codes[p]

        neighbors_one = []
        neighbors_two = []

        N = len(code_p)

        # Find all neighbors of distance one
        for i in range(N):
            swap_one = copy.copy(code_p)

            if code_p[i] == 1:
                swap_one[i] = 0
            else:
                swap_one[i] = 1

            neighbors_one.append(binary_list_to_decimal(swap_one))

        # Find all neighbors of distance two
        for i in range(N):
            for j in range(i+1, N):
                if j != i:
                    swap_two = copy.copy(code_p)

                    if code_p[i] == 1:
                        swap_two[i] = 0
                    else:
                        swap_two[i] = 1

                    if code_p[j] == 1:
                        swap_two[j] = 0
                    else:
                        swap_two[j] = 1

                    neighbors_two.append(binary_list_to_decimal(swap_two))

        neighbors = neighbors_one + neighbors_two

        return neighbors

    def n_clusters(self):
        # Counts up number of unique parents
        # return len(set(self.clusters.values()))

        # Need to count up number of unique roots
        num = 0

        for key in self.clusters:
            if key == self.clusters[key]:
                num += 1

        return num


def binary_list_to_decimal(x):
    n = len(x)

    b = 0

    for i in range(n):
        b += x[n - i - 1]*2**i

    return b


################
#  TEST CASES  #
################

# TEST #1: Use file test_big3.txt
#lines = read_big_file('week-9/test_big3.txt')

#decimals = list(map(binary_list_to_decimal, lines))

#hammingUF = HammingUnionFind(codes=lines)

#for i, p in enumerate(decimals):
#    neighbors_of_p = hammingUF.neighbors[p]

#    for q in neighbors_of_p:
#        try:
#            d_pq = hammingUF.distance(p, q)
#        except KeyError:
#            continue
#
#        if 1 <= d_pq <= 2:
#            hammingUF.union(p, q)

# The minimum k required is 1
#   CHECK: CORRECT!
#print(hammingUF.n_clusters())


# TEST #2: Use the file test_big22.txt
######################
#  HOMEWORK PROBLEM  #
######################

# Run on homework problem #2 file clustering_big.txt
lines = read_big_file('./clustering_big.txt')

decimals = list(map(binary_list_to_decimal, lines))

hammingUF = HammingUnionFind(codes=lines)

for i, p in enumerate(decimals):
    neighbors_of_p = hammingUF.neighbors(p)

    for q in neighbors_of_p:
        try:
            d_pq = hammingUF.distance(p, q)
        except KeyError:
            continue

        if 1 <= d_pq <= 2:
            hammingUF.union(p, q)

    if i % 100 == 0:
        print(i, datetime.datetime.now())

print(hammingUF.n_clusters())
