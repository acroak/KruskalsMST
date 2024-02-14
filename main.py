import CSV_Parser as csv
import kruskals_mst as mst
import elbow_method as elbow
import math
import pandas as pd

def main():
    # read in data
    data = pd.read_csv('5800_dataset.csv')
    # print(data.head())
    # take only the lat and long columns for graphing 
    X = data[["lat","long"]]
    # print(len(X))
    
    # create graph
    graph = mst.Graph(len(X))
    # automate adding edges
    for index1, row_1 in X.iterrows():
            for index2, row_2 in X.iterrows():   
                weight = math.dist(
                        (row_1["lat"],row_1["long"]),
                        (row_2["lat"],row_2["long"])
                        )
                graph.add_edge(
                    index1, index2, weight
                )
    # find MST            # 
    graph.kruskal_algo()
    
    # Use elbow Method to figure out the best k value
    elbow.create_elbow_graph()

if __name__ == "__main__":
    main()