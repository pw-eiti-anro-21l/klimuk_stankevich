class DH_row:
	def __init__(self, row):
		self.a = row[0]
		self.d = row[1]
		self.alpha = row[2]
		self.theta = row[3]

class Joint:
	def __init__(self,DH_row):
		self.origin_xyz = [DH_row.a, 0.0, DH_row.d]
		self.origin_rpy = [0.0, 0.0, 0.0]
		self.axis = [0.0, 0.0, 0.0]
		if type(DH_row.alpha) == float or type(DH_row.alpha) == int:
			self.origin_rpy[0] = DH_row.alpha
		else:
			self.axis[0] = 1.0
		if type(DH_row.theta) == float or type(DH_row.theta) == int:
			self.origin_rpy[2] = DH_row.theta
		else:
			self.axis[2] = 1.0
	
	# def __str__(self):
	# 	return f'<origin xyz="{self.origin_xyz[0]} {self.origin_xyz[1]} {self.origin_xyz[2]}" rpy="{self.origin_rpy[0]} {self.origin_rpy[1]} {self.origin_rpy[2]}" /> \n \
	# 	 <axis xyz="{self.axis[0]} {self.axis[1]} {self.axis[2]}" />'

def check_if_a_and_d(row):
	return (row[0] != 0.0) and (row[1] != 0.0)


def process_data(list_of_rows_strings):
	new_table = []
	for row in list_of_rows_strings:
		new_inner_table = []
		for element in row:
			try:
				element = float(element)
			except:
				element = element
			new_inner_table.append(element)
		new_table.append(new_inner_table)
	
	return new_table



def calculate_joints_coordinates(list_of_string_rows):
	raw_DH_table = process_data(list_of_string_rows)
	DH_table = []
	for raw_row in raw_DH_table:
		if check_if_a_and_d(raw_row):
			raw_row1 = [raw_row[0], 0.0, raw_row[2], raw_row[3]]
			raw_row2 = [0.0, raw_row[1], 0.0, 0.0]
			DH_table.append(DH_row(raw_row1))
			DH_table.append(DH_row(raw_row2))
		else:
			DH_table.append(DH_row(raw_row))
	Joints = []
	for row in DH_table:
		Joints.append(Joint(row))
	# for joint in Joints:
	# 	print(joint)
	joint_coordinates_table = []
	for  joint in Joints:
		inner_coordinates_table = []
		for a in joint.origin_xyz:
			inner_coordinates_table.append(a)
		for b in joint.origin_rpy:
			inner_coordinates_table.append(b)
		for c in joint.axis:
			inner_coordinates_table.append(c)
		joint_coordinates_table.append(inner_coordinates_table)

	return joint_coordinates_table

def print_hello():
	print("Hello")
	return 0
