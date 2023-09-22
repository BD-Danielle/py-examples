# ch16_3.py
import math

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    area = math.pi * r * r * degree / 360
    print(f'角度 = {degree:3d},\t扇形面積 = {area:6.3f}')



