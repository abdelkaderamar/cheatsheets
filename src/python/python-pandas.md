main_title: Python/Pandas Cheatsheet
lang: python

#------------------------------------------------------------------------------
title: Read a json file
with open('capitalisation.json', 'r', encoding='utf-8') as f:
     df = pd.read_json(f)
#------------------------------------------------------------------------------
title: Convert json dataframe to csv
df.to_csv('capitalisation.csv', encoding='utf-8')
#------------------------------------------------------------------------------
title: Convert json dataframe to csv
# The json objects are stored with the key 'info'
df['info'].apply(pd.Series).to_csv('info.csv')
#------------------------------------------------------------------------------
title: Clean a field
# Here we remove the simple quote from the column 
df['symbol'] = df['symbol'].str.replace("'", "")
#------------------------------------------------------------------------------
title: Convert a field to datetime
df['reportDate'] = pd.to_datetime(df['reportDate'])
#------------------------------------------------------------------------------
title: Clean all columns
# Remove single quote and strip the string
df.columns = [c.replace("'", "").strip() for c in df.columns.values.tolist()]
#------------------------------------------------------------------------------
title: 

#------------------------------------------------------------------------------
