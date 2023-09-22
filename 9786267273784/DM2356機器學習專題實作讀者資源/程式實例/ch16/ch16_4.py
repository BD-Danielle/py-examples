# ch16_4.py
import math

degrees = [x*30 for x in range(0,13)]
for d in degrees:
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    print(f'角度={d:3d}\t弧度={rad:.2f}\tsin{d:3d}={sin:.2f},\
\tcos{d:3d}={cos:5.2f}')



