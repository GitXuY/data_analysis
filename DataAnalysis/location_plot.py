import xlrd
import numpy as np
import matplotlib.pyplot as plt

# make up data points

bk = xlrd.open_workbook("/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/location.xlsx")
#shxrange = range(bk.nsheets)
sh = bk.sheets()[0]

nrows = sh.nrows

output = dict()
output['lon'] = []
output['lat'] = []
output['ID1'] = []
output['ID2'] = []


def MaxMinNormalization(x, Max, Min):
	x = (x - Min) / (Max - Min);
	return x;


points = [[0 for x in range(2)] for y in range(nrows - 1)]

for i in range(0, nrows - 1):
	output['lon'].append(sh.cell(i, 0).value)
	output['lat'].append(sh.cell(i, 1).value)
	output['ID1'].append(sh.cell(i, 2).value)
	output['ID2'].append(sh.cell(i, 3).value)

for k in range(0, nrows - 1):
	points[k][0] = output['lat'][k]
	points[k][1] = output['lon'][k]

y = output['lat']
z = output['lon']
norm_y = []
norm_z = []
Max_y = max(y)
Min_y = min(y)
Max_z = max(z)
Min_z = min(z)
for i in y:
	norm_y.append(MaxMinNormalization(i, Max_y, Min_y))
for i in z:
	norm_z.append(MaxMinNormalization(i, Max_z, Min_z))
norm = zip(norm_y, norm_z, output['ID1'], output['ID2'])
# data_path = r'/Users/Dijkstraaaaa/Documents/BSDataAnalysis/Data/location.txt'
# with open(data_path,'a') as f:
# 	for i in norm:
# 		line = str(round(i[0], 3)) + '\t' + str(round(i[1], 3)) + '\t' + str(round(i[2])) + '\t' + str(round(i[3]))
# 		print(line)
# 		f.write(line + '\n')
# f.close()


n = []
for i in range(1, len(output['lat'])):
	n.append(i)
fig, ax = plt.subplots()
ax.scatter(z, y)

for i, txt in enumerate(n):
	ax.annotate(txt, (z[i], y[i]))
plt.show()