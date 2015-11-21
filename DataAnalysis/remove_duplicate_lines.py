import os
import re
from operator import itemgetter


def remove_duplicate_lines(infilename, outfilename):
	lines_seen = set()  # holds lines already seen
	outfile = open(outfilename, "w")
	infile = open(infilename, 'r')
	# skip the heading line
	infile.next()
	for line in infile:
		a_line = percentage_to_float(line)
		b_line = rewrite_date(a_line)
		if b_line not in lines_seen:  # not a duplicate
			outfile.write(b_line)
			lines_seen.add(b_line)
	outfile.close()


def percentage_to_float(inline):
	inline = inline.strip()
	words = inline.split('\t')
	# transform the percentage number into float
	for word_idx in range(len(words)):
		if words[word_idx].endswith('%'):
			words[word_idx] = str(float(words[word_idx][:-1]) / 100)
	return '\t'.join(words) + '\n'


def rewrite_date(inline):
	inline = inline.strip()
	words = inline.split('\t')
	for word_idx in range(len(words)):
		if '-' in words[word_idx]:
			split_words = re.split(r'-| |:', words[word_idx])
			# for _idx in range(len(split_words)):
			# 	split_words[_idx] = str(int(split_words[_idx]))
			words[word_idx] = '-'.join(split_words[0:4])
		if '/' in words[word_idx]:
			split_words = re.split(r'/| |:', words[word_idx])
			for _idx in range(len(split_words)):
				if len(split_words[_idx]) == 1:
					split_words[_idx] = "0" + split_words[_idx]
			words[word_idx] = '-'.join(split_words[0:4])
	return '\t'.join(words) + '\n'


def sort_by_date(inputfile, outputfile):
	with open(inputfile, 'r') as fin:
		lines = [line.split() for line in fin]
		lines.sort(key=itemgetter(2))
	with open(outputfile, 'w') as fout:
		for el in lines:
			fout.write('{0}\n'.format('\t'.join(el)))

in_path = r'/Users/Dijkstraaaaa/Documents/TYPE2/tmp'
tmp_path = r'/Users/Dijkstraaaaa/Documents/TYPE2/tmp2'
out_path = r'/Users/Dijkstraaaaa/Documents/TYPE2/Data'
for root, dirs, files in os.walk(in_path):
	for f in files:
		if f.endswith('.txt'):
			print f
			infile_path = os.path.join(in_path, f)
			tmpfile_path = os.path.join(tmp_path, f)
			outfile_path = os.path.join(out_path, f)
			remove_duplicate_lines(infile_path, tmpfile_path)
			sort_by_date(tmpfile_path, outfile_path)
