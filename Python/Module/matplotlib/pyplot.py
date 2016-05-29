from matplotlib.finance import quotes_historical_yahoo_ochl
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import pandas as pd
import time
today = date.today()
start = (today.year-1,today.month,today.day)
quotes_MSFT = quotes_historical_yahoo_ochl('MSFT',start,today)
quotes_INTC = quotes_historical_yahoo_ochl('INTC',start,today)
fields = ['date','open','close','high','low','volume']
date_list = []
for i in range(0,len(quotes_MSFT)):
    x = date.fromordinal(int(quotes_MSFT[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    date_list.append(y)
data_MSFT = pd.DataFrame(quotes_MSFT,index=date_list,columns = fields)
data_MSFT = data_MSFT.drop(['date'],axis = 1)
data_INTC = pd.DataFrame(quotes_INTC,index=date_list,columns = fields)
data_INTC = data_INTC.drop(['date'],axis = 1)
month = []
for i in range(0,len(quotes_MSFT)):
    month.append(int(data_MSFT.index[i][5:7]))
data_MSFT['month']=month
data_INTC['month']=month
chart_MSFT = data_MSFT.groupby('month').max().close
chart_INTC = data_INTC.groupby('month').max().close
plt.subplot(211)
chart_MSFT.plot(color='r',marker='o',label='Microsoft')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Volume')
plt.subplot(212)
chart_INTC.plot(color='g',marker='o',label='Intel')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Volume')
plt.show()