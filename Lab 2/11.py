def points_are_collinear(x1,y1,x2,y2,x3,y3):
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if(area == 0):
        print("Points are collinear")
    else:
        print("Points are not collinear")

points_are_collinear(1,2,2,3,3,4)