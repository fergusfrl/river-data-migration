import csv
import sys
import pymongo
import re


# Connects to DB specified by uri and adds dbObject to the specified collection
def migrateDataToDB(uri, collection, dbObject):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    guides = db[collection]

    guides.insert_many(dbObject)
    print('Completed migration')


# Asigns CSV values to a dbObject
def readFromCSV(filePath):
    data = []
    with open(filePath) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row)
    
    # modify dbObject to work with particular CSV
    dbObject = map(lambda row: {
        'title': row[3],
        'river': row[2],
        'region': row[1],
        'grade': row[4],
        'description': re.sub('<.*?>', '', row[11]),
        'putInDescription': row[9],
        'takeOutDescription': row[10]
    }, data[1:])

    return dbObject

def main():
    # there is no argument validation so get it right
    uri = sys.argv[0]
    collection = sys.argv[1]
    CSVFilePath = sys.argv[2]
    
    dbObject = readFromCSV(CSVFilePath)
    
    migrateDataToDB(uri, collection, dbObject)

main()
