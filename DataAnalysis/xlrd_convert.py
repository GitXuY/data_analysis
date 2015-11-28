import xlrd
import os
import csv
import numbers
global_error_column = {"TYPE1": [3, 5, 7, 9, 11, 13, 15], "TYPE2": [3, 5, 7, 9, 11], "TYPE3": [3, 5, 7]}


def csv_from_excel(filename, input_folder_path, output_folder_path):
	# error column
	error_column = global_error_column[filename[:5]]
	# open excel_file
	excel_path = os.path.join(input_folder_path, filename)
	work_book = xlrd.open_workbook(filename=excel_path)
	work_sheet = work_book.sheet_by_index(0)  # ws is now an IterableWorksheet

	# open output file
	output_file_name = filename[:-5] + '_reformat.csv'
	output_file = open(os.path.join(output_folder_path, output_file_name), 'wb')
	wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)
	for row in xrange(work_sheet.nrows):
		# delete the heading info lines
		if not isinstance(work_sheet.cell(row, 0).value, numbers.Number):
			continue
		content_list = []
		for column in xrange(work_sheet.ncols):
			if column in error_column:
				continue
			# print column
			content_list.append(work_sheet.cell(row, column).value)
		wr.writerow(content_list)
	output_file.close()
	return True


def csv_from_csv(filename, input_folder_path, output_folder_path):
	# error column
	error_column = global_error_column[filename[:5]]
	# open csv_file
	csv_path = os.path.join(input_folder_path, filename)
	# open output file
	output_file_name = filename[:-4] + '_reformat.csv'
	output_file = open(os.path.join(output_folder_path, output_file_name), 'wb')
	wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)
	with open(csv_path, 'rb') as csv_file:
		file_reader = csv.reader(csv_file)
		for row in file_reader:
			if not row[0].isdigit():
				continue
			content_list = []
			for column in range(len(row)):
				if column not in error_column:
					content_list.append(row[column])
			wr.writerow(content_list)
		output_file.close()
	return True


def main():
	data_path = r'/Volumes/WIN/LTE/Mon9'
	# walk the file path
	for root, dirs, files in os.walk(data_path):
		for f in files:
			if f.startswith('TYPE'):
				is_done = False
				print f
				if f.endswith('csv'):
					is_done = csv_from_csv(f, root, root)
				if f.endswith('xlsx'):
					is_done = csv_from_excel(f, root, root)
				if is_done:
					os.remove(os.path.join(root, f))


if __name__ == '__main__':
	main()
