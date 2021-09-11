import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

from datetime import date
import csv


try:
    # Try to fetch a list of Matplotlib releases and their dates
    # from https://api.github.com/repos/matplotlib/matplotlib/releases
    import urllib.request
    import json

    url = 'https://api.github.com/repos/matplotlib/matplotlib/releases'
    url += '?per_page=100'
    data = json.loads(urllib.request.urlopen(url, timeout=.4).read().decode())

    dates = []
    names = []
    for item in data:
        if 'rc' not in item['tag_name'] and 'b' not in item['tag_name']:
            dates.append(item['published_at'].split("T")[0])
            names.append(item['tag_name'])
    # Convert date strings (e.g. 2014-10-18) to datetime
    dates = [datetime.strptime(d, "%d.%m.%Y") for d in dates]

except Exception:
    header = []
    data = []
    
    
    filename = "Oversikt.csv"
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
    
        header = next(csvreader)
    
        for datapoint in csvreader:
    
            values = [str(value) for value in datapoint]
            data.append(values)
    
    names = [p[0] for p in data]# ['Aria', 'thomas']
    dates = [p[1] for p in data] # ['15.11.2000', '12.11.2000']
    
    print(dates)
    
    
    dates = [datetime.strptime(d, "%d.%m.%Y") for d in dates]
    
    dates.append(date.today())
    names.append('Today')    
    
    
    
    
#-----------------------------------------------------------------





    

#------------------------------------------------------------------

# Choose some nice levels
levels = np.tile([-4, 4, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Kommende jobber")

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")

# format xaxis with 1 month intervals
ax.xaxis.set_major_locator(mdates.DayLocator(interval=10))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b %Y"))
#ax.xaxis.set_major_locator(dates)
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y axis and spines
ax.yaxis.set_visible(False)
#ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
