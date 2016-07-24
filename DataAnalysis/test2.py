# -*- coding: UTF-8 -*-
# rename the files in current direction
import os
import re


def generate_file_name(root_path, file_name, count):
	if file_name.endswith("csv") or file_name.endswith("xlsx"):
		# print parent_dir
		dir_words = root_path.split('/')
		type_name = dir_words[-1]
		day_name = dir_words[-2]
		mon_name = dir_words[-3]
		file_type = '.' + file_name.split('.')[-1]
		serial_number = str(count)
		sep = "_"
		sequence = (type_name, mon_name, day_name, serial_number)
		new_file_name = sep.join(sequence) + file_type
	else:
		new_file_name = file_name
	return new_file_name


def main():
	path = r'/Users/Dijkstraaaaa/Documents/LTE/TYPE1/Mon1/error'
	for root, dirs, files in os.walk(path):
		for file_idx in range(len(files)):
			# if files[file_idx].endswith('csv') and not files[file_idx].endswith('TYPE'):
			# 	type_name = root.split('/')[-2]
			# 	mon_name = root.split('/')[-1]
			# 	new_file_name_list = [type_name, mon_name, files[file_idx]]
			# 	new_file_name = "_".join(new_file_name_list)
			# 	os.rename(os.path.join(root, files[file_idx]), os.path.join(root, new_file_name))
			# 	files[file_idx] = new_file_name
			if files[file_idx].endswith('csv'):
				name_list = files[file_idx].split('_')
				new_file_name = "_".join(name_list[-7:])
				os.rename(os.path.join(root, files[file_idx]), os.path.join(root, new_file_name))
				files[file_idx] = new_file_name

if __name__ == '__main__':
	main()