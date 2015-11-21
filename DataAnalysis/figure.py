import matplotlib.pyplot as plt
import numpy as np


# read file and extract the given column
def extract_data(file_path, given_column):
	open_file = open(file_path, 'r')
	# skip the heading line
	open_file.next()
	return_list = []
	# read lines
	for line in open_file:
		words = line.split('\t')
		# transform the percentage number into float
		if words[given_column - 1].endswith('%'):
			return_list.append(float(words[given_column - 1][:-1]) / 100)
		else:
			return_list.append(float(words[given_column - 1]))
	return return_list


def plot_day_figure(_data_list, _date_index, _data_meaning):
	start_index = (_date_index - 1) * 24
	end_index = start_index + 23
	data = _data_list[start_index:end_index]
	plt.plot(data)
	plt.axis([0, 23, min(data) * 0.9, max(data) * 1.1])
	plt.xlabel('Hours')
	plt.ylabel(_data_meaning)
	plt.title('Day Figure')
	plt.grid(True)
	plt.show()


def main():
	path = r'/Users/Dijkstraaaaa/Documents/TYPE2/reformat2/320505_272298_49.txt'
	cpu_peak_list = extract_data(path, 10)
	# x = np.arange(0, len(cpu_peak_list), 1)
	x = np.arange(0, 200, 1)
	plot_day_figure(cpu_peak_list, 3, 'Memory PEAK USAGE')
	plt.plot(x, cpu_peak_list[:200])
	plt.axis([0, 200, min(cpu_peak_list[:200]) * 0.9, max(cpu_peak_list[:200]) * 1.1])
	# plt.plot(x, cpu_peak_list)
	# plt.axis([0, 200, min(cpu_peak_list) * 0.9, max(cpu_peak_list) * 1.1])
	plt.xlabel('Hours')
	plt.ylabel('Memory PEAK USAGE')
	plt.title('Day Figure')
	plt.grid(True)
	plt.show()

if __name__ == '__main__':
	main()
