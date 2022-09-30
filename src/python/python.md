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
#------------------------------------------------------------------------------
