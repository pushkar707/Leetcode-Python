# Best Position for a Service Centre

customers = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]

def distance_between_cords(cord1 , cord2):
    distance = ((cord2[0] - cord1[0])**2 + (cord2[1] - cord1[1])**2 )**(1/2)
    return distance

def center_of_points(points):

    x = []
    y = []
    sumx = 0
    sumy = 0
    distance = 0
    
    for point in points:        
        x.append(point[0])
        y.append(point[1])

    for x_cord in x:
        sumx += x_cord

    for y_cord in y:
        sumy += y_cord

    centre = (sumx/len(points),sumy/len(points))

    for point in points:
        distance += distance_between_cords(centre , point)
        # print(point)
    
    print(distance)
    print(centre)

center_of_points(customers)

# print(distance_between_cords((1,2) , (3,4)))