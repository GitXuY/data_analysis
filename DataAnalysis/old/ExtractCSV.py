import csv
import os

DATA_PATH = r'/Users/Dijkstraaaaa/Documents/1'
OUTPUT_PATH = r'/Users/Dijkstraaaaa/Documents/BS Data2'

# The wanted column in excel
column_dic = {"SUBNET_ID": 4, "NETELE_ID": 5, "START_TIME": 1, "END_TIME": 2, "CPU_PEAK_USAGE": 8,
              "CPU_AVARATE_USAGE": 9, "CPU_OVERLOAD_RATE": 10}
column_name = ["SUBNET_ID", "NETELE_ID", "START_TIME", "END_TIME", "CPU_PEAK_USAGE", "CPU_AVARATE_USAGE",
               "CPU_OVERLOAD_RATE"]

with open('%s/TYPE3_Day7_Day7_1.csv' % DATA_PATH, 'rb') as csvfile:
    filereader = csv.reader(csvfile)
    for row in filereader:
        subnet_id = row[column_dic['SUBNET_ID']]
        netele_id = row[column_dic['NETELE_ID']]
        file_path = r'%s/%s' % (OUTPUT_PATH, subnet_id) + "_" + '%s.txt' % netele_id
        if not os.path.isfile(file_path):
            output_file = open(file_path, 'a')
            output_file.write("\t".join(column_name) + "\n")
        else:
            output_file = open(file_path, 'a')

        content_list = []
        for item in column_name:
            content_list.append(row[column_dic[item]])

        output_file.write("\t".join(str(v) for v in content_list) + "\n")
        output_file.close()
