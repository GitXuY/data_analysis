# -*- coding: UTF-8 -*-
import os


column_dic = {"SUBNET_ID": 5, "NET_ELEMENT_ID": 6, "CELL_ID": 7, "START_TIME": 2, "END_TIME": 3, "DOWN_RATE1": 140,
              "UP_RATE1": 141, "DOWN_RATE2": 142, "UP_RATE2": 143}
column_name = ["SUBNET_ID", "NET_ELEMENT_ID", "CELL_ID", "START_TIME", "END_TIME", "DOWN_RATE1", "UP_RATE1",
               "DOWN_RATE2", "UP_RATE2"]


def extract_txt_file(text_file_path, output_folder_path):
	global column_dic
	global column_name
	with open(text_file_path, 'rb') as text_file:
		for line in text_file.read():

		for row in file_reader:
			subnet_id = row[column_dic['SUBNET_ID'] - 1]
			net_element_id = row[column_dic['NET_ELEMENT_ID'] - 1]
			cell_id = row[column_dic['CELL_ID'] - 1]
			output_file_name = '_'.join([str(subnet_id), str(net_element_id), str(cell_id)]) + '.txt'
			output_file_path = os.path.join(output_folder_path, output_file_name)
			if not os.path.isfile(output_file_path):
				output_file = open(output_file_path, 'a')
				output_file.write("\t".join(column_name) + "\n")
			else:
				output_file = open(output_file_path, 'a')
			content_list = []
			for item in column_name:
				content_list.append(row[column_dic[item] - 1])
			output_file.write("\t".join(str(v) for v in content_list) + "\n")
			output_file.close()


def main():
	data_path = r'/Users/Dijkstraaaaa/Documents/remain'
	output_path = r'/Users/Dijkstraaaaa/Documents/TYPE2/tmp'

	file_matrix = generate_file_list(31, data_path)
	for i in range(len(file_matrix)):
		for j in range(len(file_matrix[i])):
			file_name = 'TYPE2_Mon1_Day%s' % (i + 1) + '_%s' % file_matrix[i][j]
			print file_name
			# date = 'Day' + str(i + 1)
			file_path = os.path.join(data_path, file_name)
			# file_path = os.path.join(data_path, date, 'TYPE2', file_name)
			if file_path.endswith("xlsx"):
				extract_excel_file(file_path, output_path)
			if file_path.endswith("csv"):
				extract_csv_file(file_path, output_path)


if __name__ == '__main__':
	main()
