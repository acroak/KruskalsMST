import math
import pandas as pd

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    # p = node1, q = node2, weight is the weight of the edge between them
    def add_edge(self, p, q, weight):
        self.graph.append([p, q, weight])

    # find the i elements set
    def find(self, parent, i):        
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # apply a union (edge) between 2 node points. This is completed by leveraging the rank of the nodes
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  construct the MST
    def kruskal_algo(self):
        mst = []
        # index counter for the sorted edge list
        i = 0
        # index counter for the mst edges list
        e = 0
        # Sort the graph data based on edge weight, ascending
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        # creation of subsets
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        #  edge number should be |V| - 1
        while e < self.vertices - 1:
            # start with the smallest edge
            p, q, weight = self.graph[i]
            # increment to the next smallest edge
            i = i + 1
            # see if a cycle is created
            x = self.find(parent, p-1)
            y = self.find(parent, q-1)
            if x != y:
                e = e + 1
                mst.append([p, q, weight])
                self.apply_union(parent, rank, x, y)
        # print out the MST
        for p, q, weight in mst:
            print("%d - %d: %f" % (p, q, weight))
            

# def main():

#     # read in data
#     data = pd.read_csv('5800_dataset.csv')
#     # print(data.head())
#     # take only the lat and long columns for graphing 
#     X = data[["lat","long"]]
#     # print(len(X))
    
#     # create graph
#     graph = Graph(len(X))

#     for index1, row_1 in X.iterrows():
#             for index2, row_2 in X.iterrows():   
#                 weight = math.dist(
#                         (row_1["lat"],row_1["long"]),
#                         (row_2["lat"],row_2["long"])
#                         )
#                 graph.add_edge(
#                     index1, index2, weight
#                 )
                
#     graph.kruskal_algo()
    
# if __name__ == "__main__":
#     main()