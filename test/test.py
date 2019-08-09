"""
this files is used to test matplotlib
"""
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# sale_list = [20, 10, 30]
# dates = ['01/02/1991','01/03/1991','01/04/1991']


dates = ['01/02/1991','01/03/1991','01/04/1991']
x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
y = range(len(x))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()
