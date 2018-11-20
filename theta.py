from math import atan, pi

def polar_theta(pointA, pointB):
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
    
from math import acos, sqrt, pi
def theta(pointA, pointB, pointC):
        # inner angle between vector BA et BC
        BA = (pointA[0]-pointB[0], pointA[1]-pointB[1])
        BC = (pointC[0]-pointB[0], pointC[1]-pointB[1])
        dot_prod = (BA[0]*BC[0]) + (BA[1]*BC[1])
        BA_length = sqrt((BA[0]**2 + BA[1]**2))
        BC_length = sqrt((BC[0]**2 + BC[1]**2))
        try:
            return round(acos(dot_prod / (BA_length * BC_length)),10)
        except ZeroDivisionError: # vector dot product with vector of length = 0
            return 0
        except ValueError: # angle = Pi in certain cases of floating point arithmetic ...
            return pi

if __name__ == '__main__':
    assert theta([0,1],[0,0],[0,0]) == 0.0
    assert theta([0,1],[0,0],[0,1]) == 0.0
    assert theta([0,1],[0,0],[1,1]) == 0.7853981633974484
    assert theta([0,1],[0,0],[1,0]) == 1.5707963267948966
    assert theta([0,1],[0,0],[1,-1]) == 2.356194490192345
    assert theta([0,1],[0,0],[0,-1]) == 3.141592653589793
    assert theta([0,1],[0,0],[-1,-1]) == 2.356194490192345
    assert theta([0,1],[0,0],[-1,0]) == 1.5707963267948966
    assert theta([0,1],[0,0],[-1,1]) == 0.7853981633974484
    assert theta((10, 3),[7, 6] ,[4, 9]) == 3.141592653589793
    print('passed all tests')
