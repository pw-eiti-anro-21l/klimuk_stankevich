import math
from math import *

class Quaternion:
    def __init__(self):
        self.x = 0.0;
        self.y = 0.0;
        self.z = 0.0;
        self.w = 0.0;
    def calculate(self,roll,pitch,yaw):
        cy = cos(yaw * 0.5);
        sy = sin(yaw * 0.5);
        cp = cos(pitch * 0.5);
        sp = sin(pitch * 0.5);
        cr = cos(roll * 0.5);
        sr = sin(roll * 0.5);
        self.w = cr * cp * cy + sr * sp * sy;
        self.x = sr * cp * cy - cr * sp * sy;
        self.y = cr * sp * cy + sr * cp * sy;
        self.z = cr * cp * sy - sr * sp * cy;
    def __str__(self):
        return f"x: {self.x}\ny: {self.y}\nz: {self.z}\nw: {self.w}"

