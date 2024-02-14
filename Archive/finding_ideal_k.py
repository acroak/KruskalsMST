'''
Keegan Moseley
April 6, 2023
5800
'''
import math
import coordinate as c
import matplotlib.pyplot as plt

'''
The sum of squares is a way of modeling the distance of points in a cluster from the centroid.
A lower sum of squares means the cluster is more "dense" 

This method calculates the sum of squares for a group of GPS coordinates.
'''
@staticmethod
def sum_of_squares(coordinate_set):
    centroid = c.centroid(coordinate_set)

    total = 0

    for coordinate in coordinate_set:
        #find distance of this coordinate to the centroid
        distance = centroid.distance(coordinate)

        #square the distance
        squared_distance = distance * distance

        #add the squared distance to the total
        total += squared_distance

    return total

#NOTE: Need to determine if we should use distortion or inertia

def draw_graph(x_axis_list, y_axis_list):
    plt.plot(x_axis_list, y_axis_list)

    plt.xlabel("K Values")
    plt.ylabel("Inertia or Distorian values, havent decided yet")

    plt.title("Inerita or Distorian per K value")

    plt.show()




