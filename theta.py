from math import atan, pi

def theta(pointA, pointB):
    # angular distance of vector AB from x axis when using polar coordinates
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
    
def theta(pointA, pointB, pointC):
    #interior angle between two vector BA and BC , that share the same vertice
    BA = (pointA[0]-pointB[0], pointA[1]-pointB[1])
    BC = (pointC[0]-pointB[0], pointC[1]-pointB[1])
    dot_prod = (BA[0]*BC[0]) + (BA[1]*BC[1])
    BA_length = sqrt((BA[0]**2 + BA[1]**2))
    BC_length = sqrt((BC[0]**2 + BC[1]**2))
    return acos(dot_prod / (BA_length * BC_length))


