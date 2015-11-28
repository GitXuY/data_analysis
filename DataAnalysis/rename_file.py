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
	path = r'/Volumes/WIN/LTE/Mon9'
	for root, dirs, files in os.walk(path):
		for folder_idx in range(len(dirs)):
			new_folder_name = generate_folder_name(dirs[folder_idx])
			os.rename(os.path.join(root, dirs[folder_idx]), os.path.join(root, new_folder_name))
			dirs[folder_idx] = new_folder_name
		count = 0
		for file_idx in range(len(files)):
			count += 1
			new_file_name = generate_file_name(root, files[file_idx], count)
			os.rename(os.path.join(root, files[file_idx]), os.path.join(root, new_file_name))
			files[file_idx] = new_file_name

if __name__ == '__main__':
	main()
