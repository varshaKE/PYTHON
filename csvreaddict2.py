import csv

file=open('birth.csv','r')
read=csv.DictReader(file)
for lines in read:
    if lines:

        print(lines['name'],lines['birthmonth'])
