import os
import re
import csv
from operator import itemgetter


def reformat(raw_file_path, reformat_file_path):
	# read the raw data
	raw_file = open(raw_file_path, 'r')
	raw_file_content = csv.reader(raw_file)
	reformat_row_list = []
	# create the reformat file
	reformat_file = open(reformat_file_path, "w")
	csv_writer = csv.writer(reformat_file)

	# reformat the percentage form and date info
	for row in raw_file_content:
		reformat_row = reformat_date(reformat_percentage(row))
		reformat_row_list.append(reformat_row)
	# sort the list by date info
	reformat_row_list.sort(key=itemgetter(1))

	# remove duplicate lines
	rows_seen = list()  # holds rows already seen
	for item in reformat_row_list:
		if item not in rows_seen:
			csv_writer.writerow(item)
			rows_seen.append(item)
	reformat_file.close()


def reformat_percentage(row):
	for item_idx in range(len(row)):
		if row[item_idx].endswith('%'):
			row[item_idx] = str(float(row[item_idx][:-1]) / 100)
	return row


def reformat_date(row):
	for item_idx in range(len(row)):
		split_words = re.split(r'-|/| |:', row[item_idx])
		if len(split_words) > 1:
			for idx in range(len(split_words)):
				if len(split_words[idx]) == 1:
					split_words[idx] = "0" + split_words[idx]
			row[item_idx] = '-'.join(split_words[0:4])
	return row


def main():
	folder_path = r'/Users/Dijkstraaaaa/Documents/LTE/TYPE2'
	for root, dirs, files in os.walk(folder_path):
		for f in files:
			if f.endswith('.csv') and not f.endswith('reformat.csv'):
				print f
				raw_file_path = os.path.join(root, f)
				dot_index = f.find('.')
				reformat_filename = f[:dot_index] + '_reformat' + f[dot_index:]
				reformat_file_path = os.path.join(root, reformat_filename)
				reformat(raw_file_path, reformat_file_path)
				os.remove(raw_file_path)

if __name__ == '__main__':
	main()
