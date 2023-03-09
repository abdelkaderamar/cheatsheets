main_title: Python/JSON Cheatsheet
lang: python

#------------------------------------------------------------------------------
title: Read a json file and convert a list of json objects to list of objects
with open(filename, 'r') as f:
        data = json.load(f)
        if 'result_data' in data:
            stocks=[Stock(**d) for d in data['result_data']]
#------------------------------------------------------------------------------
title: Parse a string as a json object
data = json.loads(script.text)
instrument = data['custom']['instrument']
#------------------------------------------------------------------------------
title: Print a json object
o =   { "name": "AZZ Incorporated", "ticker": "AZZ", "capitalisation": "1037603000" }
print(json.dumps(o, indent=2))
#------------------------------------------------------------------------------
