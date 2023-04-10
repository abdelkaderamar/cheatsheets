main_title: Python cheatsheet
lang: python

#------------------------------------------------------------------------------
title: Sort a list of objects
class stock:
    def __init__(self, name, ticker, isin):
self.name = name
self.ticker = ticker
self.isin = isin

sorted_stocks=sorted(stocks, key=lambda s: s.ticker, reverse=True)
stocks.sort(key=lambda s : s.ticker, reverse=True)
#------------------------------------------------------------------------------
title: Sort a dictionary by key
sorted_stocks_dict = {key: val for key, val     
    in sorted(stocks_dict.items(), key=lambda kvp : kvp[0])}
#------------------------------------------------------------------------------
title: Sort a dictionary by value (define \_\_lt\_\_ or \_\_gt\_\_)
class stock:
    def __init__(self, name, ticker, isin):
self.name = name
self.ticker = ticker
self.isin = isin

    def __lt__(self, other):
return self.name < other.name

sorted_stocks_dict = {key: val for key, val     
    in sorted(stocks_dict.items(), key=lambda kvp : kvp[1])}

#------------------------------------------------------------------------------
title: Remove a list elements from another list
watchlist=['SGO.PA', 'GLE.PA', 'LVMH.PA', 'MT.PA', 'ACA.PA']
banks=['GLE.PA', 'ACA.PA', 'BNP.PA']
watchlist=[ticker for ticker in watchlist if ticker not in banks]
#------------------------------------------------------------------------------
title: Check if a dictionary is included in another dictionary and get the difference
included=set(stocks_dict2.items()).issubset(set(stocks_dict1.items()))
diff={key: value for (key, value) in stocks_dict1.items() 
    if (key, value) not in stocks_dict2.items()}
#------------------------------------------------------------------------------
title: Find the matched object(s) in a list
# if the list contains a single match
match = next((s for s in stocks if s.ticker == equity.reuters_ticker), None)
# if the list contains one or more matches
matches = [s for s in stocks if s.ticker == equity.reuters_ticker]
#------------------------------------------------------------------------------
title: File basename           
import os
s.path.basename(temp_tex_file.name)
#------------------------------------------------------------------------------
title: Capitalize the first letter of each word (for only the first letter of the string use capitalize())
s.title()
#------------------------------------------------------------------------------
title: Date in french
start_date.strftime("%B %Y").title() 
start_date.strftime('%d %B %Y').title()
#------------------------------------------------------------------------------
title: Iterate through 2 lists
for a,b in zip(l1, l2):
        print(a, b)
#------------------------------------------------------------------------------
title: Convert a list (of non string objects) to a string
', '.join(str(v) for v in start_date_range)
', '.join(map(str, list_of_ints))
#------------------------------------------------------------------------------
title: Range of date (frequency one month\, using pandas library)
pandas.period_range(start_date, end_date, freq='M')
#------------------------------------------------------------------------------
title: Add a delta to datetime
from datetime import datetime, timedelta
d = datetime.now() + timedelta(days=7)
#------------------------------------------------------------------------------
title: Run an external command
subprocess.run(["pdflatex", '-interaction=nonstopmode', temp_tex_file.name],
                       cwd='media/generated')
#------------------------------------------------------------------------------
title: Create a temporary file
temp_tex_file = tempfile.NamedTemporaryFile(mode="w", suffix=".tex", delete=False)
#------------------------------------------------------------------------------
title: Convert a number to word (using num2words library)
amount_words = num2words(amount, lang='fr')
#------------------------------------------------------------------------------
title: Access environment variable
mail_secret = os.environ['MAIL_SECRET']
#------------------------------------------------------------------------------
title: Log to a file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("company_info.log"),
        logging.StreamHandler()
    ]
)
#------------------------------------------------------------------------------
title: Read file by (n) lines each iteration
  with open(filename, 'r') as infile:
    while True:
      next_n_lines = list(islice(infile, 5))
      if not next_n_lines:
          break
#------------------------------------------------------------------------------
title: Escape special characters
import re
re.espace(str)
#------------------------------------------------------------------------------
