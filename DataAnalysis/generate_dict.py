# from itertools import zip

column = 1
column_name = []
while column !=199:
	column_name.append(column)
	column += 1

column_name2 = column_name
# print column2
zipped = zip(column_name, column_name2)
print(dict(zipped))