def position_of_point(cent_x,cent_y,radius,point_x,point_y):
    dist = (((point_x)**2) -((cent_x)**2)) + (((point_y)**2) -((cent_y)**2)) 
    
    if dist > radius:
        print("Point is outside the circle")
    elif dist < radius :
        print("Point is inside the circle")
    else:
        print("Point is on the circle")

position_of_point(0,0,5,3,4)