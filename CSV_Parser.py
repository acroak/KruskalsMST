import pandas

# array for storing Node Objects
GPS_Points = []

class Node:
    def __init__(self, id, xcoord, ycoord):
        self.id = id
        self.xcoord = xcoord
        self.ycoord = ycoord

# Methods to fetch data from CSV based on column name
def getID(dataset):
    return dataset.ID
    
def getPlace(dataset):
    return dataset.Place

def getState(dataset):
    return dataset.State
       
def getCity(dataset):
      return dataset.City

def getX(dataset):
       return dataset.lat #returns lat

def getY(dataset):
       return dataset.long #returns long

# Fetch Datapoints from CSV and create a Node object, add the object to a globablly available array, GPS_Points. These objects indices and ID number correlate. ie object ID 24 will be located at index 24. The count starts from 0
def createNodes(filepath):
    dataset = pandas.read_csv(filepath) 
    IDList = getID(dataset) 
    #    PlaceList = getPlace(dataset)
    #    StateList = getState(dataset)
    #    CityList = getCity(dataset)
    XCoordList = getX(dataset)
    YCoordList = getY(dataset)
    # print(len(XCoordList))

    # For every row in the provided CSV, grab the information based on the column name and create a node object to contain it.
    for i in range(len(IDList)):
        # print(i)
        GPS_Points.append(Node(IDList[i], XCoordList[i], YCoordList[i]))
    
    return GPS_Points

    
        
# createNodes("5800_dataset.csv")
# print(GPS_Points[4].xcoord)
# print(GPS_Points[0].id)
# print(GPS_Points[0].xcoord)
# print(GPS_Points[0].ycoord)

# For K-Means we will want to create another csv sheet to store the new cluster information