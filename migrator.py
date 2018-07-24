import csv

filePath = 'river-data.csv'
data = []

# Read from CSV
with open(filePath) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        data.append(row)
    
# Remove title line
data = data[1:]

# Output data
print(data)
