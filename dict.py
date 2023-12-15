import csv

fields=['name','birthmonth']
rows=[

      {'name':'vinu','birthmonth':'march'},
      {'name':'anu','birthmonth':'may'},
      {'name':'sonu','birthmonth':'april'}

      ]

with open('birth.csv','w') as file:

    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    file.close()
    
      
