from math import sqrt

def dist(x1, y1, x2, y2, x3, y3):
    ab = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    bc = sqrt( (x2 - x3)**2 + (y2 - y3)**2 )

    return ab + bc / 2