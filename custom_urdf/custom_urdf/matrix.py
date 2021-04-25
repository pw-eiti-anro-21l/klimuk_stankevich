import math
from math import *

class Translation:
	def __init__(self):
		self.matrix = []
		self.matrix_roll = []
		self.matrix_pitch = []
		self.matrix_yawl = []
		self.matrix_x = []
		self.matrix_y = []
		self.matrix_z = []
		self.roll = 0
		self.pitch = 0
		self.yawl = 0
	def set_matrix_roll(self,roll):
		self.matrix.append([1,0,0,0])
		self.matrix.append([0,cos(roll),-sin(roll),0])
		self.matrix.append([0,sin(roll),cos(roll),0])
		self.matrix.append([0,0,0,1])
	def set_matrix_pitch(self,pitch):
		self.matrix.append([cos(pitch),0,sin(pitch),0])
		self.matrix.append([0,1,0,0])
		self.matrix.append([-sin(pitch),0,cos(pitch),0])
		self.matrix.append([0,0,0,1])
	def set_matrix_yawl(self,yawl):
		self.matrix.append([cos(yawl),-sin(yawl),0,0])
		self.matrix.append([sin(yawl),cos(yawl),0,0])
		self.matrix.append([0,0,1,0])
		self.matrix.append([0,0,0,1])
	def set_matrix_x(self,x):
		self.matrix.append([1,0,0,x])
		self.matrix.append([0,1,0,0])
		self.matrix.append([0,0,1,0])
		self.matrix.append([0,0,0,1])
	def set_matrix_y(self,y):
		self.matrix.append([1,0,0,0])
		self.matrix.append([0,1,0,y])
		self.matrix.append([0,0,1,0])
		self.matrix.append([0,0,0,1])
	def set_matrix_z(self,z):
		self.matrix.append([1,0,0,0])
		self.matrix.append([0,1,0,0])
		self.matrix.append([0,0,1,z])
		self.matrix.append([0,0,0,1])
	def calculate_roll(self):
		self.roll = atan2(-self.matrix[1][2], self.matrix[2][2])
		return atan2(-self.matrix[1][2], self.matrix[2][2])
	def calculate_pitch(self):
		cosY = sqrt(1-self.matrix[0][2])
		self.pitch = atan2(self.matrix[0][2], cosY)
		return atan2(self.matrix[0][2], cosY)
	def calculate_yawl(self):
		self.calculate_roll()
		sinZ = cos(self.roll) * self.matrix[1][0] + sin(self.roll) * self.matrix[2][0]
		cosZ = cos(self.roll) * self.matrix[1][1] + sin(self.roll) * self.matrix[2][1] 
		self.yawl = atan2(sinZ,cosZ)
		return atan2(sinZ,cosZ)
	def __mul__(self, other):
		result = Translation()
		result.matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		for i in range(0,4):
			for j in range(0,4):
				result.matrix[i][j] = self.matrix[i][0] * other.matrix[0][j] + self.matrix[i][1] * other.matrix[1][j] + self.matrix[i][2] * other.matrix[2][j] + self.matrix[i][3] * other.matrix[3][j]
		return result
	def __str__(self):
		return f"{self.matrix[0]}\n{self.matrix[1]}\n{self.matrix[2]}\n{self.matrix[3]}"
