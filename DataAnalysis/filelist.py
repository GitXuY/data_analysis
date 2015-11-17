# -*- coding: UTF-8 -*-
import os
import numpy

path = r'/Users/Dijkstraaaaa/Documents/Data/Mon1'
file_matrix = []
DAY_NUM = 31
while DAY_NUM != 0:
	file_matrix.append([])
	DAY_NUM -= 1

for root, dirs, files in os.walk(path):
	for f in files:
		if f.startswith("TYPE3"):

			if f.endswith("xlsx"):
				f = f[:-5]
			if f.endswith("csv"):
				f = f[:-4]
			f_words = f.split("_")
			day_info = f_words[-2]
			day_num = int(day_info[3:])
			serial_info = f_words[-1]
			serial_num = int(serial_info)
			file_matrix[day_num - 1].append(serial_num)

print file_matrix
