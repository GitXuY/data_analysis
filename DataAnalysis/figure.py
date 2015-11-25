import matplotlib.pyplot as plt
import numpy as np
import csv

type1_column_dic = {}
type2_column_dic = {"PRB up peak": 167, "PRB down peak": 168, "PRB up average": 169, "PRB down average": 170,
                    "gather down rate": 139, 'gather up rate': 140, 'equivalent down rate': 141,
                    'equivalent up rate': 142, 'down mac user average rate': 83, 'erab': 53, 'rrc': 52, 'pdcp': 61,
                    'qci9 down pdcp average': 138, 'qci1 down e-utran average': 74, 'qci2 down e-utran average': 75,
                    'qci3 down e-utran average': 76, 'qci4 down e-utran average': 77, 'qci5 down e-utran average': 78,
                    'qci6 down e-utran average': 79, 'qci7 down e-utran average': 80, 'qci8 down e-utran average': 81,
                    'qci9 down e-utran average': 82, 'qci9 down prb average': 184}
type3_column_dic = {'cpu peak': 8, 'cpu average': 9, 'memory peak': 11, 'memory average': 12}
column_dic_list = [type1_column_dic, type2_column_dic, type3_column_dic]


def extract_data(file_path, data_type, column_name):
	"""
	read file and extract the given column
	:param data_type:
	:param file_path:
	:param column_name:
	:return: list
	"""
	column_dic = column_dic_list[data_type - 1]
	column_idx = column_dic[column_name] - 1
	csv_file = open(file_path, 'rb')
	content = csv.reader(csv_file)
	return_list = []
	# read lines
	for row in content:
		return_list.append(float(row[column_idx].replace(",","")))
	return return_list


def plot_figure(data_list, start_date, end_date, y_label):
	start_index = (start_date - 1) * 24
	end_index = (end_date - start_date) * 24 + 23
	data = data_list[start_index:end_index]
	plt.plot(data)
	plt.axis([start_index, end_index, min(data) * 0.9, max(data) * 1.1])
	plt.xticks(np.arange(start_index, end_index + 2, 24))
	plt.xlabel('Hours')
	plt.ylabel(y_label)
	plt.title('Day Figure')
	plt.grid(True)
	plt.show()


def main():
	path = r'/Users/Dijkstraaaaa/Documents/LTE/TYPE2/Mon1/320505_269582_49_reformat.csv'
	data_type = 2
	column_name = "PRB down average"
	data_list = extract_data(path, data_type, column_name)
	start_date = 1
	end_date = 14
	plot_figure(data_list, start_date, end_date, column_name)


if __name__ == '__main__':
	main()
