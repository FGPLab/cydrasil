import json

with open('cydrasil-v2.1-database.json') as json_file:
    data = json.load(json_file)
    for item in data:
        item.update(cyID = '')
        item.update(cyTaxID = '')
        item.update(ncbiFullTax = '')
        item.update(ncbiAbbTax = '')

with open('cydrasil-v2.1-refactored-database.json', 'w') as outfile:
    json.dump(data, outfile, indent=2, sort_keys=True)