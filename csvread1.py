import csv



file=open('abc.csv','r')
fileread=csv.reader(file)
for lines in fileread:
     if lines:
            print('\t',lines[0], '\t',lines[1], '\t', lines[2])
