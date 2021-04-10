class DH_row:
	def __init__(self, row):
		self.a = row[0]
		self.d = row[1]
		self.alpha = row[2]
		self.theta = row[3]

class Joint:
	def __init__(self,DH_row):
		self.origin_xyz = [DH_row.a,0,DH_row.d]
		self.origin_rpy = [0,0,0]
		self.axis = [0,0,0]
		if type(DH_row.alpha) == float or type(DH_row.alpha) == int:
			self.origin_rpy[0] = DH_row.alpha
		else:
			self.axis[0] = 1
		if type(DH_row.theta) == float or type(DH_row.theta) == int:
			self.origin_rpy[2] = DH_row.theta
		else:
			self.axis[2] = 1
	def __str__(self):
		return f'<origin xyz="{self.origin_xyz[0]} {self.origin_xyz[1]} {self.origin_xyz[2]}" rpy="{self.origin_rpy[0]} {self.origin_rpy[1]} {self.origin_rpy[2]}" /> \n \
		 <axis xyz="{self.axis[0]} {self.axis[1]} {self.axis[2]}" />'

def check_if_a_and_d(row):
	return (row[0] != 0) and (row[1] != 0)






def my_main():
	raw_DH_table = [[0, 1.3, 0, "theta_1"], [0.5, 0, 0, "theta_2"], [0.5, 0.5, -3.14, 0]]
	DH_table = []
	for raw_row in raw_DH_table:
		if check_if_a_and_d(raw_row):
			raw_row1 = [raw_row[0], 0, raw_row[2], raw_row[3]]
			raw_row2 = [0,raw_row[1],0,0]
			DH_table.append(DH_row(raw_row1))
			DH_table.append(DH_row(raw_row2))
		else:
			DH_table.append(DH_row(raw_row))
	Joints = []
	for row in DH_table:
		Joints.append(Joint(row))
	for joint in Joints:
		print(joint)

my_main()