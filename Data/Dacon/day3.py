print('hello world')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=pd.Series(1,1)
a=pd.Series([1,2,3])
a
from datetime import datetime
dates = [datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]
dates = [datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]
ts = pd.Series(np.random.randn(6), index=dates)
ts.index
ts + ts[::2]
ts.index.dtype
stamp = ts.index
ts
ts['12/01/2011']
ts['1/12/2011']
ts['20110112']
ts['12-1-2011']
longer_ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000',periods=1000))
longer_ts
longer_ts['2001']
longer_ts['2001-05']
ts[datetime(2011,1,7):]
ts
ts['1/6/2011':'1/11/2011']
ts.truncate(after='1/9/2011')
dates = pd.date_range('1/1/2000', periods = 100, freq = 'W-WED')
long_df = pd.DataFrame(np.random.randn(100,4),index=dates,columns=['Colorado','Texas','New York','Ohio'])
long_df.loc['5-2001']
dates = pd.DatetimeIndex([''])
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000','1/2/2000','1/2/2000','1/3/2000'])
dup_ts=pd.Series(np.arange(5), index=dates)
dup_ts
dup_ts.index.is_unique
dup_ts['1/3/2000']
dup_ts['1/2/2000']
grouped = dup_ts.groupby(level=0)
grouped.mean()
grouped.count()
ts.resample('D')
resampler = ts.resample('D')
resampler
index = pd.date_range('2012-04-04','2012-06-01')
index
index
dup_ts
index = pd.date_range('2012-04-01', '2012-06-01')
index
pd.date_range(start='2012-04-01',periods=20)
pd.date_range(end='2012-06-01', periods = 20)
pd.date_range('2001-01-01','2000-12-01', freq='BM')
pd.date_range('2012-05-02 12:56:31', periods=5)

pd.date_range('2012-05-02 12:56:31', periods=5, normalize = True)
from pandas.tseries.offsets import Hour, Minute
hour = Hour()
hour
four_hour = Hour(4)
four_hour
pd.date_range('2000-01-01','2000-01-03 23:59',freq='4h')
Hour(2) + Minute(30)
pd.date_range('2000-01-01', periods = 10, freq = '1h30min')
rng = pd.date_range('2012-01-01','2012-09-01', freq = 'WOM-3FRI')
list(rng)
ts = pd.Series(np.random.randn(4), index = pd.date_range('1/1/2000', periods=4, freq='M'))
ts
ts.shift(2)
ts.shift(-2)
ts/ts.shift(1)-1
ts.shift(2, freq = 'M')
ts.shift(3,freq='D')
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011,11,17)
now + 3*Day()
ts= pd.Series(np.random.randn(20), index = pd.date_range('1/15/2000',periods=20, freq ='4d'))
ts
import pytz
pytz.common_timezones[-5:]
tz = pytz.timezone('America/New_York')
tz
