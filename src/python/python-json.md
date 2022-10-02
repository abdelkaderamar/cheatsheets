main_title: Python/JSON Cheatsheet
lang: python

#------------------------------------------------------------------------------
title: Read a json file and convert a list of json objects to list of objects
with open(filename, 'r') as f:
        data = json.load(f)
        if 'result_data' in data:
            stocks=[Stock(**d) for d in data['result_data']]
#------------------------------------------------------------------------------
