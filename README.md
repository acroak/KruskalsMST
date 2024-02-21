# Kruskals, Clusters, and Creeps
An exploration of Kruskals Minimum spanning tree algorithm and data mining techniques. Completed as the final project for for CS 5800.

[Presentation Slides](https://docs.google.com/presentation/d/11EplUqDGT-1qiBw_tUAmfMQNFtDv574Lv6r2bq4sTQQ/edit?usp=sharing)

[Final Report](https://github.com/acroak/KruskalsMST/blob/main/Archive/5800_Final_Report.pdf)

Team: Andrea Croak, Wil Moore, Keegan Moseley

<hr />   
<h3>Goal</h3>
The goal of the "KruskalsMST" project is to utilize advanced data mining and machine learning techniques, specifically K-means clustering and Kruskal's algorithm, to analyze and optimize the exploration of historical and paranormal sites across New England. By clustering the geographic coordinates of the sites, calculating the minimum spanning tree between clusters, and visualizing the data points on maps, the project aims to identify spatial patterns. Thus optimizing the travel route to visit all clusters efficiently, and provide a visually appealing representation of the clustered data points. The overarching objective was to leverage these techniques to enhance the exploration and understanding of the historical and paranormal sites in New England through a data-driven and geospatial analysis approach.

<hr />   
<h3>Topics of Exploration</h3>

* Kruskal's Algorithm:

  * Definition: Kruskal's algorithm is a method used to find the minimum spanning tree in a graph by selecting edges in ascending order of their weights.
  * Application in the Project: In the "KruskalsMST" project, Kruskal's algorithm was applied to determine the minimum spanning tree between all clusters generated through k-means clustering. This approach helped in identifying the most efficient path to visit all clusters, optimizing the travel route for exploration.

* Clustering:

  * Definition: Clustering is a data mining technique that groups similar data points together based on certain characteristics or features.
  * Application in the Project: The project utilized k-means clustering to categorize data points into clusters based on their similarities, in this case geographic proximity to one another. By clustering the data, the project was able to identify patterns and relationships within the dataset, facilitating further analysis and visualization of the clustered data points.

* Elbow Graphs:

  * Definition: Elbow graphs are used to determine the optimal number of clusters in a dataset by analyzing the distortion or inertia values at different k values.
  * Application in the Project: The project employed elbow graphs to select the appropriate number of clusters for the dataset. By running k-means clustering multiple times for each k value and plotting the average distortion, the project identified the optimal number of clusters, enhancing the accuracy of the clustering results and subsequent analysis.

* Accounting for the Curvature of the Earth:

  * Definition: Accounting for the curvature of the Earth involves considering the spherical shape of the Earth when calculating distances between geographic coordinates.
  * Application in the Project: To accurately calculate distances between data points on the Earth's surface, the project accounted for the curvature of the Earth. By incorporating the Earth's curvature into distance calculations, the project ensured that the path between clusters and centroids was calculated along the curved surface, providing more precise and realistic distance measurements for route optimization.

<hr />   
<h3>Process</h3>

* Clustering Analysis:

The latitude and longitude data points were utilized in the k-means clustering algorithm to group locations into clusters based on their proximity. By clustering the data points, the project identified spatial patterns and relationships among the sites, enabling efficient organization and analysis of the locations.

* Minimum Spanning Tree (MST) Calculation:

The geographic coordinates of the data points were essential for calculating the minimum spanning tree using Kruskal's algorithm. By considering the distances between the clustered centroids, the project determined the optimal path to visit all clusters, leveraging the geographical information to plan the most efficient route for exploration.

* Distance Calculations:

The latitude and longitude data were crucial for accounting for the curvature of the Earth when calculating distances between data points. By accurately considering the spherical shape of the Earth in distance calculations, the project ensured precise measurements for determining the optimal path between clusters and centroids, improving the overall accuracy of the exploration route planning.

  
* Visualization:

The geographic coordinates were also used for visualizing the clustered data points on maps. By plotting the locations based on their latitude and longitude, the project created visual representations of the clusters and the minimum spanning tree, enhancing the understanding and interpretation of the spatial relationships among the sites.

<hr />   
<h3>Languages and Libraries used</h3>

* Languages:
  * Python: Python programming language was used for implementing the data mining, machine learning, and visualization algorithms in the project.
* Libraries:
  * NumPy: NumPy library was used for numerical computations and array operations, essential for data manipulation and calculations in the project.
  * Pandas: Pandas library was utilized for data manipulation and analysis, particularly for handling the dataset containing geographic coordinates and site information.
  * Scikit-learn: Scikit-learn library was employed for implementing the K-means clustering algorithm, a key component in grouping the data points into clusters based on similarities.
  * Plotly: Plotly library was used for data visualization, enabling the creation of interactive and visually appealing plots and maps to represent the clustered data points and minimum spanning tree.
  * Matplotlib: Matplotlib library may have been used for additional data visualization tasks, such as creating static plots and graphs to showcase the results of the clustering and analysis processes.
 
<hr />   
<h3>Results</h3>

* Map of all locations provided from CSV data
![All Locals](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/all_locals.png)

* Centroids from each designated cluster
![Centroids](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/cluster_centroids.png)

* Cluster 1 - Northern Maine Based Locals
![Northern Maine](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/CLUSTER1.png)

* Cluster 2 - Southern Maine and Northern New Hampshire based Locals
![Southern Maine](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/CLUSTER3.png)

* Cluster 3 - Massachusetts and Southern New Hampshire Locals
![Massachusetts and Southern New Hampshire](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/CLUSTER2.png)

* Cluster 4 - Western Massachusetts and Vermont Locals
![Western Massachusetts and Vermont](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/CLUSTER5.png)

* Cluster 5 - Rhode Island and Eastern Connecticut Locals
![Rhode Island and Eastern Connecticut](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/CLUSTER0.png)

* Cluster 6 - Western Connecticut Locals
![Western Connecticut](https://github.com/acroak/KruskalsMST/blob/main/Archive/IMGS/CLUSTER4.png)
