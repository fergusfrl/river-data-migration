import csv

def readFromCSV(filePath):
    data = []

    with open(filePath) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row)
        
    return data[1:]

def main():
    filePath = 'river-data-csv'
    print(readFromCSV(filePath))

main()
