# snek
This python code easily allows one to add NBER recession bars to matplotlib graphs within its familiar API. At the minimum (after an appropriate import) one must simply include `snek.add_rec_bars(ax)`, where "ax" is the axis on which one wants to add recession bars, in order to achieve the desired result.

## Installation
If using miniconda3, install to "~/miniconda3/lib/python3.6/site-packages". 

## Example

```python
# Imports
import datetime
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import snek.rec_bars as snek

# Set Dates
start = datetime.datetime(1947,1,1)
end   = datetime.datetime.today()

# Pull in some data from FRED
rGDP = pdr.DataReader('GDPC1','fred',start,end)

# Plot
fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(rGDP)
ax.yaxis.grid()
ax.set_xlabel('Year')
ax.set_ylabel('Billions of Chained 2009 Dollars')
snek.add_rec_bars(ax,start,end)
plt.xlim([start,end])
plt.title('Real Gross Domestic Product (GDPC1)')
plt.show()
```

![Alt text](/images/rGDP.png?raw=true "Original Title")
