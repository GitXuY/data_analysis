# -*- coding: UTF-8 -*-
import os
import csv


def generate_output_file_name(type_num, info_list):
	# type1 output filename = "SUBNET_ID" + "NET_ELEMENT_ID" + "RACK_ID" + "CHANNEL_ID"
	type1_column = [4, 5, 6, 9]
	# type2 output filename = "SUBNET_ID" + "NET_ELEMENT_ID" + "CELL_ID"
	type2_column = [4, 5, 6]
	# type3 output filename = "SUBNET_ID" + "NET_ELEMENT_ID"
	type3_column = [4, 5]
	type_column = [type1_column, type2_column, type3_column]

	name_list = []
	column_list = type_column[int(float(type_num)) - 1]
	for idx in column_list:
		name_list.append(info_list[idx - 1].split('.')[0])
	output_filename = '_'.join(name_list) + '.csv'

	return output_filename


def extract_csv_file(csv_file_path, output_folder_path, type_num):
	with open(csv_file_path, 'rb') as csv_file:
		file_reader = csv.reader(csv_file)
		for row in file_reader:
			output_file_name = generate_output_file_name(type_num, row)
			# open the corresponding file
			output_file_path = os.path.join(output_folder_path, output_file_name)
			output_file = open(output_file_path, 'a')
			# write row
			wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)
			wr.writerow(row)
			output_file.close()


def main():
	# data_path = r'/Users/Dijkstraaaaa/Documents/LTE/Data/Mon2'
	data_path = r'/Users/Dijkstraaaaa/Documents/LTE/remain'
	TYPE1_output_path = r'/Users/Dijkstraaaaa/Documents/LTE/TYPE1/Mon1'
	TYPE2_output_path = r'/Users/Dijkstraaaaa/Documents/LTE/TYPE2/Mon1'
	TYPE3_output_path = r'/Users/Dijkstraaaaa/Documents/LTE/TYPE3/Mon1'
	output_path_list = [TYPE1_output_path, TYPE2_output_path, TYPE3_output_path]
	# walk the file path
	for root, dirs, files in os.walk(data_path):
		for f in files:
			if f.startswith("TYPE") and f.endswith("csv"):
				type_num = f[4]
				print f
				output_path = output_path_list[int(float(type_num)) - 1]
				file_path = os.path.join(root, f)
				extract_csv_file(file_path, output_path, type_num)


if __name__ == '__main__':
	main()
