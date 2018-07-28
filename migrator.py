import csv
import pymongo
import re

def connectToDB(uri):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    guides = db['riverguides']

    dbObject = readFromCSV()

    guides.insert_many(dbObject)
    print('Completed migration')


def readFromCSV():
    filePath = 'river-data.csv'
    data = []

    with open(filePath) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row)
        
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
    uri = <MongoDB URI>

    connectToDB(uri)

main()
