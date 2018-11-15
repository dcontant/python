from math import atan, pi

def theta(pointA, pointB):
    # angular distance from x axis when using polar coordinates
    xA, yA = pointA
    xB, yB = pointB
    delta_y = (yB - yA)
    delta_x = (xB - xA)
    if delta_x > 0 and delta_y >= 0:
        return atan(delta_y / delta_x )
    if delta_x > 0 and delta_y < 0:
        return atan(delta_y / delta_x) + 2 * pi 
    if delta_x < 0:
        return atan(delta_y / delta_x) +  pi
    if delta_x == 0 and delta_y > 0:
        return pi / 2
    if delta_x == 0 and delta_y < 0:
        return 3 * pi / 2

    
theta((1,1), (1,-1))
    
    
    
