# -*- coding: UTF-8 -*-
# rename the files in current direction
import os
import re


def generate_folder_name(folder_name):
	mon_number = re.findall(r"\d+", folder_name)
	# folder contains "月"
	if '\xe6\x9c\x88' in folder_name:
		new_folder_name = "Mon{0}".format(mon_number[0])
	# folder contains "号"
	elif '\xe5\x8f\xb7' in folder_name:
		new_folder_name = "Day{0}".format(mon_number[0])
	# file name contains "天线端口"
	elif '\xe5\xa4\xa9\xe7\xba\xbf\xe7\xab\xaf\xe5\x8f\xa3' in folder_name:
		new_folder_name = "TYPE1"
	# folder name contains "网元"
	elif '\xe5\xb0\x8f\xe5\x8c\xba' in folder_name:
		new_folder_name = "TYPE2"
	# folder name contains "小区"
	elif '\xe7\xbd\x91\xe5\x85\x83' in folder_name:
		new_folder_name = "TYPE3"
	else:
		new_folder_name = folder_name

	return new_folder_name


def generate_file_name(parent_dir, file_name):
	if (file_name.endswith("csv") or file_name.endswith("xlsx")) and (not file_name.startswith("TYPE")):
		dir_words = parent_dir.split('/')
		type_name = dir_words[-1]
		day_name = dir_words[-2]
		mon_name = dir_words[-3]
		sep = "_"
		sequence = (type_name, mon_name, day_name, file_name)
		new_file_name = sep.join(sequence)
	else:
		new_file_name = file_name
	return new_file_name


def main(path):
	for root, dirs, files in os.walk(path):
		for folder_idx in range(len(dirs)):
			print dirs[folder_idx]
		# new_folder_name = generate_folder_name(dirs[folder_idx])
		# os.rename(os.path.join(root, dirs[folder_idx]), os.path.join(root, new_folder_name))
		# dirs[folder_idx] = new_folder_name
		# for file_idx in range(len(files)):
		# 	new_file_name = generate_file_name(root, files[file_idx])
		# 	print new_file_name
		# 	os.rename(os.path.join(root, files[file_idx]), os.path.join(root, new_file_name))
		# 	files[file_idx] = new_file_name


if __name__ == '__main__':
	path = r'/Volumes/XUY/data'
	main(path)

