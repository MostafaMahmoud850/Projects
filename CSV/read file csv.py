# # read file with header

# import csv 

# with open('fav.csv', 'r') as file:
#    reader = csv.reader(file)      # reader return rows as a list
#    for row in reader:
#       print(row)

# # read file without header

# import csv 

# with open('fav.csv', 'r') as file:
#    reader = csv.reader(file)      # reader return rows as a list
#    next(reader)
#    for row in reader:
#       print(row)  # print(row[index]) to view column selected by index

# # read file with header
# import csv 

# with open('fav.csv', 'r') as file:
#    reader = csv.reader(file)      # reader return rows as a list
#    for row in reader:
#       print(row)

# write data into a new CSV File (without headers and indexes (Dictionary)) - append mode 
import csv 

with open('fav.csv', 'r') as file:
   reader = csv.DictReader(file)  # DictReader return rows as a Dictionary
   for row in reader:             # print(row["column name"]) to view column contant selected 
      print(row["language"])