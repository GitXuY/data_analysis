import os
import csv
import re
import datetime

def sort_by_date(inputfile, outputfile):
	with open(inputfile, 'r') as fin:
		data = csv.reader(fin)
		new_data = []
		for row in data:
			try:
				time_list = re.split(r'-| |:|/', row[1])
				new_time_list = []
				for i in time_list:
					if len(i) > 1 and i.startswith('0'):
						i = i[1:]
					new_time_list.append(i)
				new_time = '-'.join(new_time_list[:4])
				row[1] = datetime.datetime.strptime(new_time,'%Y-%m-%d-%H')

				time_list = re.split(r'-| |:|/', row[2])
				new_time_list = []
				for i in time_list:
					if len(i) > 1 and i.startswith('0'):
						i = i[1:]
					new_time_list.append(i)
				new_time = '-'.join(new_time_list[:4])
				row[2] = datetime.datetime.strptime(new_time, '%Y-%m-%d-%H')
				new_data.append(row)
			except Exception, e:
				print Exception, ":", e
		sortedlist = sorted(new_data, key=lambda x: (x[1]))

	with open(outputfile, 'w') as fout:
		fileWriter = csv.writer(fout)
		for row in sortedlist:
			fileWriter.writerow(row)

in_path = r'/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/TYPE2/Mon8'
out_path = r'/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/TYPE2/Mon8_new'
# in_path = r'/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/data_test'
# out_path = r'/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/data_test/out'
for root, dirs, files in os.walk(in_path):
	for f in files:
		if f.endswith('.csv'):
			print f
			infile_path = os.path.join(in_path, f)
			outfile_path = os.path.join(out_path, f)
			sort_by_date(infile_path, outfile_path)

