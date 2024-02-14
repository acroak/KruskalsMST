'''
Keegan Moseley
CS 5800
April 5, 2023
'''

from math import *

'''
Method to return a new Centoid (average/center) point for an input set of points. 
Paremeters:
    - points set populated by only Point objects, and with a size > 0 
Returns:
    new Point object
'''
@staticmethod
def average_of(points):

    num_points = len(points)

    if (num_points == 0):
        #ensure the input set is not empty
        raise ValueError("Must input a set of Point objects with at least 1 object")
    elif (not(isinstance(list(points)[0],Point))):
        #ensure the input set contains Point objects
        raise ValueError("The objecst in the set must be Point objects")

    #get average x coord
    average_x = 0
    for pt in points:
        average_x += pt.x
    average_x = average_x/num_points

    #get average y coord
    average_y = 0
    for pt in points:
        average_y += pt.y
    average_y = average_y/num_points

    #get average z coord
    average_z = 0
    for pt in points:
        average_z += pt.z
    average_z = average_z/num_points

    return Point(average_x,average_y, average_z)


'''
Class representing a cartesian point

Attributes:
    - x coordinate
    - y coordinate
    - z coordinate
'''
class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[ x = " + str(self.x) + ", y = " + str(self.y) + ", z = " + str(self.z) + ']'
    

        
