import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle * math.pi / 180)
    ny = y - step * math.sin(angle * math.pi / 180)
    return nx, ny
nx,ny = move(0,0,math.sqrt(2),45)
print nx, ny
print move(0,0,math.sqrt(2),45)    #return is tuple
