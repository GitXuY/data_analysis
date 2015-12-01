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
	path = r'/Volumes/WIN/LTE/TYPE1'
	# path = r'/Users/Dijkstraaaaa/Documents/LTE/TYPE2'
	for root, dirs, files in os.walk(path):
		for file_idx in range(len(files)):
			if files[file_idx].endswith('csv'):
				type_name = root.split('/')[-2]
				mon_name = root.split('/')[-1]
				print type_name
				print(mon_name)
			# new_file_name = generate_file_name(root, files[file_idx], count)
			# os.rename(os.path.join(root, files[file_idx]), os.path.join(root, new_file_name))
			# files[file_idx] = new_file_name

if __name__ == '__main__':
	main()