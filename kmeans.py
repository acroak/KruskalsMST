#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
1. specify number of clusters you want (k)
2. randomly init centroid for each cluster
3. discover which data points belong to which cluster by finding closest centroid to each data point
4. update centroids based on geometric mean of all data points in cluster. update datapoints to what cluster they belong to
5. iterate through/run 3 and 4 until centroids stop changing position.
'''

def KMeans(dataset, k, Centroids):
    
    diff = 1
    counter = 0
    # Step 5, repeat commands until the diff is 0
    while(diff!=0):
        # Step 3 which data points belong to which cluster
        i=1
        # compare the lat and long of each row against all other rows to calculate distance between points
        for index1, row_1 in Centroids.iterrows():
            distances=[]
            for index2, row_2 in dataset.iterrows():
                # Euclidian Distance formula sqrt((x1-x2)^2 + (y1-y2)^2)
                # np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)   
                d1=(row_1["lat"]-row_2["lat"])**2
                d2=(row_1["long"]-row_2["long"])**2
                d=np.sqrt(d1+d2)
                distances.append(d)
            dataset[i] = distances
            # print(distances)
            i=i+1
        
            
        # Step 4 update centroids based on geometric mean of all data points in cluster
        # cluster_num = list for holding what cluster our data belongs to
        cluster_num=[]
        # iterate through each row and determine what cluster the values belong to
        for index, row in dataset.iterrows():
            min_dist=row[1]
            pos=1
            # for each cluster generated (k), if row i+1 is less than our current minimum distance we update the minimum distance value
            for i in range(k):
                if row[i+1] < min_dist:
                    min_dist = row[i+1]
                    pos=i+1
            cluster_num.append(pos)
        # add cluster column to our dataframe and set equal to cluster numbers
        dataset["Cluster"] = cluster_num
        Centroids_new = dataset.groupby(["Cluster"]).mean()[["long","lat"]]
        # print(Centroids_new)
        # print(dataset) #the dataframe is updating with a column named clustetrs which contains the cluster number, we just need to use pandas to add this data to our csv or a new csv so we can then apply the mst to the clusters
        
        # conditional stop control statement
        if counter == 0:
            diff = 1
            counter = counter + 1
        else:
            # once this diff calc == 0, the while loop will complete
            diff = (Centroids_new['long'] - Centroids['long']).sum() + (Centroids_new['lat'] - Centroids['lat']).sum()
            # print(diff.sum())
        # create a dataframe of centroids generated
        Centroids = dataset.groupby(["Cluster"]).mean()[["long","lat"]]
    
    # print out the final scatter plot  
    color=['green','blue','cyan','indigo','violet']
    for k in range(k):
        data=dataset[dataset["Cluster"]==k+1]
        plt.scatter(data["lat"],data["long"],c=color[k])
    plt.scatter(Centroids["lat"],Centroids["long"],c='red')
    plt.xlabel('Latitude')
    plt.ylabel('Long')
    plt.show()

def show_init_plot(dataset):
    #this scatter plot will show us how all the datapoints look on a graph
    plt.scatter(dataset["lat"],dataset["long"],c='black')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.show()
    
def show_init_plot_and_rnd_centroids(dataset, Centroids):
    # this scatter plot will show all our points and random centroid prior to clustering
    plt.scatter(dataset["lat"],dataset["long"],c='black')
    plt.scatter(Centroids["lat"],Centroids["long"],c='red')
    plt.xlabel('lat')
    plt.ylabel('long')
    plt.show()

def main():
    # read in data
    data = pd.read_csv('5800_dataset.csv')
    # print(data.head())
    # take only the lat and long columns for graphing 
    X = data[["lat","long"]]
    # show_init_plot(X)
       
    # Step 1 number of clusters
    # we get this number from our elbow graph
    K=5

    # Step 2 Select random observation as centroids
    Centroids = (X.sample(n=K))
    # show_init_plot_and_rnd_centroids(X, Centroids)
    
    KMeans(X, K, Centroids)
    
if __name__ == "__main__":
    main()
    
