import csv

filePath = 'river-data.csv' 
 
with open(filePath) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader[1:]:
        print(row)
