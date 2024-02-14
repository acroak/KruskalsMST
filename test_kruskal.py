import kruskals as k
import math
def main():
    # Test add edge and mst generation
    print("---------------g1 test------------------")
    node_0 = [1, 2.5]
    node_1 = [2, 5]
    node_2 = [4.5, 2]
    node_3 = [5, 1]
    node_4 = [3, 0]

    g1 = k.Graph(5)

    g1.add_edge(0,1, math.dist(node_0, node_1))
    g1.add_edge(0,2, math.dist(node_0, node_2))
    g1.add_edge(0,3, math.dist(node_0, node_3))
    g1.add_edge(0,4, math.dist(node_0, node_4))
    g1.add_edge(1,2, math.dist(node_1, node_2))
    g1.add_edge(1,3, math.dist(node_1, node_3))
    g1.add_edge(1,4, math.dist(node_1, node_4))
    g1.add_edge(2,3, math.dist(node_2, node_3))
    g1.add_edge(2,4, math.dist(node_2, node_4))
    g1.add_edge(3,4, math.dist(node_3, node_4))

    g1.kruskal_algo()
    
    

    # Rather than manually adding edges, automate it. Should have same output as g1
    print("---------------g2 test------------------")
    g2_point_array = [node_0, node_1, node_2, node_3, node_4]
    g2 = k.Graph(len(g2_point_array))
    for i in range(len(g2_point_array)):     
        for j in  range(i+1,len(g2_point_array)):
            #  print("[" + str(i) + ", " + str(j) + "] " +str(g2_point_array[i]) + ", " + str(g2_point_array[j]))
             g2.add_edge(i, j, math.dist(g2_point_array[i], g2_point_array[j]))
    
    g2.kruskal_algo()

    '''
    g1 and g2 result:
        2 - 3: 1.118034
        3 - 4: 2.236068
        0 - 1: 2.692582
        0 - 4: 3.201562
    '''


    # Try with simplified gps data points
    print("---------------g3 test------------------")
    # 0) 41.698807	-71.156407	Lizzie Borden House
    # 1) 42.6733866	-73.0915873	The Hoosac Tunnel
    # 2) 42.5574852	-71.9807807	S.K. Pierce Mansion
    # 3) 42.3575313	-71.4691568	Longfellow's Wayside Inn

    g3 = k.Graph(4)
    node_0 = [41.69, -71.15]
    node_1 = [42.67,-73.09]
    node_2 = [42.55,-71.98]
    node_3 = [42.35, -71.46]

    g3_point_array = [node_0, node_1, node_2, node_3]
    for i in range(len(g3_point_array)):     
        for j in  range(i+1,len(g3_point_array)):
            # print("[" + str(i) + ", " + str(j) + "] " +str(g3_point_array[i]) + ", " + str(g3_point_array[j]))
            g3.add_edge(i, j, math.dist(g3_point_array[i], g3_point_array[j]))

    g3.kruskal_algo()

    '''
    g3 results
        2 - 3: 0.557136
        0 - 3: 0.729178
        1 - 2: 1.116468
    '''

    


if __name__ == "__main__":
    main()