"""
this file is used to test plot dates

"""
import json
import matplotlib
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as the_dates
from Row import Row

datelist = ['09-03-2016', '31-10-2016', '13-05-2016', '22-10-2016']

converted_dates = list(map(datetime.datetime.strptime, datelist, len(datelist)*['%d-%m-%Y']))
x_axis = converted_dates
formatter = the_dates.DateFormatter('%d-%m-%Y')

y_axis = range(0,4)
plt.plot(x_axis, y_axis, '-' )
ax = plt.gcf().axes[0]
ax.xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate(rotation=25)
plt.show()



# datelist =  ['2014-05-06', '2014-05-07', '2014-05-08', '2014-05-09', '2014-05-10',    '2014-05-11', '2014-05-12', '2014-05-13']
#
# import matplotlib
# from matplotlib import pyplot
# from matplotlib import dates
# import datetime
#
# converted_dates = list(map(datetime.datetime.strptime, datelist, len(datelist)*['%Y-%m-%d']))
# x_axis = converted_dates
# formatter = dates.DateFormatter('%Y-%m-%d')
#
# y_axis = range(0,8)
# pyplot.plot( x_axis, y_axis, '-' )
# ax = pyplot.gcf().axes[0]
# ax.xaxis.set_major_formatter(formatter)
# pyplot.gcf().autofmt_xdate(rotation=25)
# pyplot.show()
