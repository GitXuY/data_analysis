import os


bad_words = ['[FDD]']

old_path = r'/Users/Dijkstraaaaa/Documents/TYPE2/reformat2'
new_path = r'/Users/Dijkstraaaaa/Documents/TYPE2/tmp'
for root, dirs, files in os.walk(old_path):
	for f in files:
		if f.endswith('.txt') and not f.startswith('_'):
			print f
			with open(os.path.join(old_path, f)) as old_file, open(
				os.path.join(new_path, f)) as new_file:
				for line in old_file:
					if not any(bad_word in line for bad_word in bad_words):
						new_file.write(line)
