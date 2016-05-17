from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('MSFT', start, today)
attributes = ['date', 'open', 'close', 'high', 'low', 'volume']
quotesdf = pd.DataFrame(quotes, columns=attributes)
list1 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list1.append(y)
quotesdf.index = list1
quotesdf = quotesdf.drop(['date'], axis=1)
print(quotesdf.ix['15/01/30':'15/02/10', ['open', 'close']])
print(quotesdf['14/01/01':'15/01/01'].sort_values(by='close', ascending=False)[:5])
list1 = []
tmpdf = quotesdf['15/01/01':'15/12/31']
for i in range(0, len(tmpdf)):
    list1.append(int(tmpdf.index[i][3:5]))
tmpdf.loc[:, ('month')] = list1
# tmpdf.__setitem__('test', list1)
# tmpdf['test'] = list1
# tmpdf.loc.__setitem__((slice(None), ('test')), list1)
print(tmpdf[tmpdf.close > tmpdf.open]['month'].value_counts())
tmpdf.groupby('month')['volume'].sum()
sorted = quotesdf.sort_values(by='close')
pd.concat([sorted[:5], sorted[-5:]])
