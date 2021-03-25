import json

with open('cydrasil-v2.1-refactored-database.json') as json_file:
    data = json.load(json_file)
    for item in data:
        item.update(isolationSource = '')

with open('cydrasil-v2.1-refactored-w-iso-database.json', 'w') as outfile:
    json.dump(data, outfile, indent=2, sort_keys=True)