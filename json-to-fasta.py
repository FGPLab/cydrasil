import json

with open('cydrasil-v3-database.json') as json_file:
    data = json.load(json_file)
    for item in data:
        print('>' + item['cyTaxID'])
        print(item['sequence'])