import os


def rename(file_path, file_name, file_idex):
	if file_name.endswith("csv"):
		new_file_name = str(file_idex + 1) + ".csv"
		os.rename(os.path.join(file_path, file_name), os.path.join(file_path, new_file_name))
	if file_name.endswith("xlsx"):
		new_file_name = str(file_idex + 1) + ".xlsx"
		os.rename(os.path.join(file_path, file_name), os.path.join(file_path, new_file_name))


def main(path):
	for root, dirs, files in os.walk(path):
		for dir in dirs:
			list_dir = os.listdir(os.path.join(root, dir))
			for f_idx in range(len(list_dir)):
				rename(os.path.join(root, dir), list_dir[f_idx], f_idx)


if __name__ == '__main__':
	path = r'/Users/Dijkstraaaaa/Documents/hello'
	main(path)
