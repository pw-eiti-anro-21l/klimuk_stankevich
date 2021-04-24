import yaml

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

	#dummy fix of d parameter
	d_parameter = joint_coordinates_table[3][2]
	joint_coordinates_table[3] = [-d_parameter, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

	return joint_coordinates_table

def write_params_to_yaml(joint_params, path_to_file, node_name):
	joints_dict = [{"joint_fixed": joint_params[0], "joint_shoulder": joint_params[1],
					"joint_elbow": joint_params[2], "joint_wrist": joint_params[3],
					"joint_fixed_end": joint_params[4], "joint_wrist_connector": joint_params[5]}]
	f = open(path_to_file, "w")
	string_to_write = node_name + ":\n"
	f.write(string_to_write)
	f.write("  ros__parameters:\n")
	f.close()
	with open(path_to_file, 'a') as file:
		documents = yaml.dump_all([joints_dict], file, indent=4)
	with open(path_to_file, "r") as file_2:
		data = file_2.readlines()
	string_to_change = data[2]
	new_string = ""
	for i in range(0, len(string_to_change) - 1):
		if i == 0:
			new_string += " "
		else:
			new_string += string_to_change[i]
	data[2] = new_string + "\n"
	with open(path_to_file, "w") as file_2:
		file_2.writelines(data)

