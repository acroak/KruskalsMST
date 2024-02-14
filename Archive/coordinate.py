'''
Keegan Moseley
CS 5800
April 5, 2023
'''
import math
import point

'''
Method to return a centroid (gravitational center) Coodinate from a set of Coordinate objects
'''
@staticmethod
def centroid(input_set):
    #create set of cartestian points of all cities
    point_set = set()
    for coordinate in input_set:
        point_set.add(coordinate.point)

    #get average cartesian point of all cities
    middle_point = point.average_of(point_set)
    #convert the cartestian point into a coordinate
    middle_coordinate = point_to_coordinate(middle_point)

    return middle_coordinate

'''
Method to create a Coordinate point from a cartesian (x,y,z) point
'''
@staticmethod
def point_to_coordinate(point):
    radian_longitude = math.atan2(point.y, point.x)
    hypotenouse = math.sqrt(point.x * point.x + point.y * point.y)
    radian_latitude = math.atan2(point.z, hypotenouse)

    degree_latitude = radian_latitude * 180/math.pi
    degree_longitude = radian_longitude * 180/math.pi

    new_coord = Coordinate(degree_latitude, degree_longitude)

    return new_coord

'''
Class representing a DD Coordinate (Latitude, Longitude)
Only works for locations in both the North and Western hemispheres

The radian versions of the latidude and longitude are stored, as well 
as a representation of the coordinate as a cartesian point (x,y,z)
'''
class Coordinate:
    def __init__(self, latitude_deg, longitude_deg):
        #degrees of lattitude
        self.latitude = latitude_deg
        #degrees of longitude
        self.longitude = longitude_deg

        #latitude in radians
        self.radian_latitude = latitude_deg * math.pi/180
        #longitude in radians   Fliped negative since all points are in W hemisphere
        self.radian_longitude = longitude_deg * -1 * math.pi/180

        #cartesian point of this coordinate. 
        # x and y plane is at the equator, with origin at center of the earth. 
        #   Positive x line passes through 0 degrees E 
        #   Positive y line passes through 90 degrees E
        # Positive z line is from the center of the earch to the north pole
        x = math.cos(self.radian_latitude) * math.cos(self.radian_longitude)
        y = math.cos(self.radian_latitude) * math.sin(self.radian_longitude)
        z = math.sin(self.radian_latitude)
        self.point = point.Point(x,y,z)

    '''
    Method to get the distance between two coordinates (in Nautical Miles)
    '''
    def distance(self, otherCoordinate):
        
        #cental angle between two coordinates. See this article for math explaination: https://en.wikipedia.org/wiki/Great-circle_distance
        angle = math.acos(math.sin(self.radian_latitude) * math.sin(otherCoordinate.radian_latitude) + 
                          math.cos(self.radian_latitude) * math.cos(otherCoordinate.radian_latitude) *
                          math.cos(self.radian_longitude - otherCoordinate.radian_longitude) )
        
        #in nautical miles  
        #NM are nice b/c 1 NM == 1 minute, but this can easily be changed to a different unit
        distance = angle * 3443.92

        return distance

    def __str__(self):
        string = "Latitude : " + str(self.latitude) + " Longitude : " + str(self.longitude)
        return string

def main():
    boston = Coordinate(42.3601, 71.0589)
    portland = Coordinate(43.6591, 70.2568)
    burlington = Coordinate(44.4759, 73.2121) #Vermont, not mass

    #test over most of NE
    set_1 = set()
    set_1.add(boston)
    set_1.add(portland)
    set_1.add(burlington)
    print(centroid(set_1))

    #test over a short distance, the boston area
    arlington = Coordinate(42.4154, 71.1565)
    brookline =  Coordinate(42.3318, 71.1212)

    set_2 = set()
    set_2.add(boston)
    set_2.add(arlington)
    set_2.add(brookline)

    print(centroid(set_2))
    
main()
