import os


def main(path):
	count = 0
	for root, dirs, files in os.walk(path):
		for file in files:
			count += 1
	print count


if __name__ == '__main__':
	path = r'/Users/Dijkstraaaaa/Documents/LTE/data'
	main(path)
