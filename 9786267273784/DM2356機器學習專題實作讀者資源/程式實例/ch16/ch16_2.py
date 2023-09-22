# ch16_2.py
import math

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    curve = 2 * math.pi * r * degree / 360
    print(f'角度 = {degree:3d},\t弧長 = {curve:6.3f}')



