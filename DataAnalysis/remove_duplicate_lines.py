import os


def remove_duplicate_lines(_infilename, _outfilename):
	lines_seen = set()  # holds lines already seen
	outfile = open(_outfilename, "w")
	for line in open(_infilename, "r"):
		if line not in lines_seen:  # not a duplicate
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()


inpath = r'/Users/Dijkstraaaaa/Documents/BS Data'
outpath = r'/Users/Dijkstraaaaa/Documents/Base Station'
for root, dirs, files in os.walk(inpath):
	for f in files:
		if f.endswith('.txt'):
			infile_path = os.path.join(inpath, f)
			outfile_path = os.path.join(outpath, f)
			remove_duplicate_lines(infile_path, outfile_path)
