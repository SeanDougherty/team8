import csv
import json

csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("DateTime", "Aggregate Feed Rates: Proprietary Equities and Commodities")
reader = csv.DictReader( csvfile, fieldnames)

#Iterates over the CSV and dumps into a new JSON file
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
