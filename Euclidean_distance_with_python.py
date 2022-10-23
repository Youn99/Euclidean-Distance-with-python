from math import sqrt
import heapq
def euclidean_distance(a, b, c, e, alpha, my_output):
    
    distance_a = sqrt((a[0]-alpha[0])**2 + (a[1]-alpha[1])**2 + (a[2]-alpha[2])**2 )
    distance_b = sqrt((b[0]-alpha[0])**2 + (b[1]-alpha[1])**2 + (b[2]-alpha[2])**2 )
    distance_c = sqrt((c[0]-alpha[0])**2 + (c[1]-alpha[1])**2 + (c[2]-alpha[2])**2 )
    distance_e = sqrt((e[0]-alpha[0])**2 + (e[1]-alpha[1])**2 + (e[2]-alpha[2])**2 )
    k=3
    tuple_distances = ((distance_a), my_output[0]), ((distance_b), my_output[1]), ((distance_c), my_output[2]), ((distance_e), my_output[3])
    closed = tuple(heapq.nsmallest(k,tuple_distances))
    list_closed = [closed[0][1] , closed[1][1] , closed[2][1]]
    most_common = max(list_closed, key = list_closed.count)
    print(f'the euclidean distance is {tuple_distances}.\nthe most closed are {closed}.\n the 3NN(xnew) is: {most_common}')

euclidean_distance([1, 2, 3],[0 , 2, -1],[-1, 2, 3],[3, 1, 3],[-1,-1,-1], [0, 1, 0, 1])