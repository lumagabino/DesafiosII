import math

ax, ay, bx, by, cx, cy = [int(x) for x in input().split()]

def distance(x1,y1,x2,y2):
    return (pow(x1-x2, 2)+pow(y1-y2, 2))

distAB = distance(ax,ay,bx,by)
distBC = distance(bx,by,cx,cy)

delta1 = (by-ay)*(cx-ax)
delta2 = (cy-ay)*(bx-ax)
isColinear = False
if delta1==delta2:
    isColinear = True

if distAB==distBC and not isColinear:
    print("Yes")
else:
    print("No")
