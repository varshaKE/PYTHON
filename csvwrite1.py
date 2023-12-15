import csv

try:

    fields=['slno','name','age']
    rows=[
        [1,'vinu',21],
        [2,'anu',22],
        [3,'manu',20]
        ]
    file=open('abc.csv','w')
    writer=csv.writer(file)
    writer.writerow(fields)
    writer.writerows(rows)
    print("success")

except Exception as e:

    print(e)

finally:

    file.close()
