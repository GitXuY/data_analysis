import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def plot(prb_data, month, BS_ID, fig_path):
	with PdfPages(fig_path + "Mon" + month + "_" + BS_ID + ".pdf") as pdf:
		t = np.arange(len(prb_data))
		s = prb_data
		fig = plt.figure()
		plt.plot(t, s)
		plt.axis([t[0], t[-1], min(s) * 0.9, max(s) * 1.1])
		plt.xlabel('Hour (h)')
		plt.ylabel('PRB Usage (%)')
		plt.title('PRB Usage in Mon' + month + ' of BS ' + BS_ID)
		plt.grid(True)
		pdf.savefig(fig)
	plt.close('all')



def extract_data(prb_path):
	prb_data = []
	f = open(prb_path, "r")
	lines = f.readlines()  # 读取全部内容
	for line in lines:
		try:
			x = float(line)
			prb_data.append(x)
		except:
			print('cannot convert')
	f.close()
	return prb_data


def main():
	data_path = r'/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/test/result'
	fig_path = r'/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/test/fig/'
	month = "9"
	i = 0
	# walk the file path
	for root, dirs, files in os.walk(data_path):
		for f in files:
			if f.endswith("txt"):
				i += 1
				print(i)
				BS_ID = f[0:13]
				prb_path = os.path.join(data_path, f)
				prb_data = extract_data(prb_path)
				plot(prb_data, month, BS_ID, fig_path)


if __name__ == '__main__':
	main()