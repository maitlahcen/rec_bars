# snek
Some Python Code that may be useful to some.

## Installation
If using miniconda3, install to "~/miniconda3/lib/python3.6/site-packages". 

## Example

```python
# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import statsmodels.api as sm
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
