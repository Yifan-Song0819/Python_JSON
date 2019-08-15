import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as the_dates
from Row import Row
import pandas as pd
import numpy as np


"""
remove_null is used to delete the null value
"""
def remove_null(data):
    # print(len(data))
    for row in data:
        if row["date"] == None or row["sale"] == None:
            data.remove(row)
    return data

"""
list with only date
dealing with data from json not row obs
"""

def get_date(input):
    res = []
    for row in input:
        res.append(row["date"])
    return res

"""
list with only sale
dealing with data from json not row obs
"""

def get_sale(input):
    res = []
    for row in input:
        res.append(row["sale"])
    return res


"""
get no duplicate (keep the larger sale)

then function returns a list with "Row" ob

657 left, which means there are a lot of duplicate data!
"""

def to_oop(date, sale):
    final_date_list = []
    final_sale_list = []
    for i in range(0, len(date)):
        if date[i] not in final_date_list:
            # a_row = Row(date[i], sale[i])
            final_date_list.append(date[i])
            final_sale_list.append(sale[i])
        else:
            if final_sale_list[final_date_list.index(date[i])] < sale[i]:
                final_sale_list[final_date_list.index(date[i])] = sale[i]
    # print("no dull length is: ", len(final_date_list))
    final_row_list = []
    for i in range(0, len(final_date_list)):
        a_row = Row(final_date_list[i], final_sale_list[i])  # initialize rows!
        final_row_list.append(a_row)
    print("final length is: ", len(final_row_list))
    return final_row_list

"""
These two are used to list sale and date from the obs_list
"""

def sales_from_ob(ob_list):
    sales_list = []
    for i in range(0, len(ob_list)):
        sales_list.append(ob_list[i].sale)
    return sales_list

def dates_from_ob(ob_list):
    dates_list = []
    for i in range(0, len(ob_list)):
        dates_list.append(ob_list[i].date)
    return dates_list


"""
just a plot test
"""
def plot_test(rows_ob_list):
    sales_list = sales_from_ob(rows_ob_list)
    dates_list = dates_from_ob(rows_ob_list)

    plt.plot(sales_list)
    plt.suptitle("Every day sales")
    plt.ylabel('Thousands of NZDs')
    plt.xlabel("x1")
    plt.show()
"""
This function is used to get the monthly sales.
It returns a list.
"""

def get_monthly_sale(rows_ob_list, target_year):
    month_list = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0, len(rows_ob_list)):
        if "01-" + target_year in rows_ob_list[i].date:
            month_list[0] += rows_ob_list[i].sale
        elif "02-" + target_year in rows_ob_list[i].date:
            month_list[1] += rows_ob_list[i].sale
        elif "03-" + target_year in rows_ob_list[i].date:
            month_list[2] += rows_ob_list[i].sale
        elif "04-" + target_year in rows_ob_list[i].date:
            month_list[3] += rows_ob_list[i].sale
        elif "05-" + target_year in rows_ob_list[i].date:
            month_list[4] += rows_ob_list[i].sale
        elif "06-" + target_year in rows_ob_list[i].date:
            month_list[5] += rows_ob_list[i].sale
        elif "07-" + target_year in rows_ob_list[i].date:
            month_list[6] += rows_ob_list[i].sale
        elif "08-" + target_year in rows_ob_list[i].date:
            month_list[7] += rows_ob_list[i].sale
        elif "09-" + target_year in rows_ob_list[i].date:
            month_list[8] += rows_ob_list[i].sale
        elif "10-" + target_year in rows_ob_list[i].date:
            month_list[9] += rows_ob_list[i].sale
        elif "11-" + target_year in rows_ob_list[i].date:
            month_list[10] += rows_ob_list[i].sale
        elif "12-" + target_year in rows_ob_list[i].date:
            month_list[11] += rows_ob_list[i].sale

    for i in range(0, len(month_list)):
        month_list[i] = round(month_list[i], 2)

    return month_list

def plot_year(rows_ob_list, target_year):
    month_list = get_monthly_sale(rows_ob_list, target_year)
    year_list = []
    year = ["Jan-", "Feb-", "Mar-", "Apr-", "May-", "Jun-", "Jul-", "Aug-", "Sep-", "Oct-", "Nov-", "Dec-"]
    for i in range(0, 12):
        year_list.append(year[i] + target_year)
    # print(year_list)
    # print(month_list)

    index = np.arange(len(year_list))
    plt.bar(index, month_list)
    # here x and y is coordinates, last 1 is the value shown
    for i in range(0, len(month_list)):
        plt.text(i - 0.4,  month_list[i] + 1, str(month_list[i]), fontsize = 8)

    plt.xlabel('Month', fontsize=10)
    plt.ylabel('Thousands of NZD', fontsize=10)
    plt.xticks(index, year_list, fontsize=5, rotation=30)
    plt.title('Sales data for each month in ' + target_year)
    plt.show()

def plot_min_averge_max(rows_ob_list):
    year = ["2016", "2017", "2018"]

    # df = pd.DataFrame([['g1','c1',10],['g1','c2',12],['g1','c3',13],['g2','c1',8],
    #                ['g2','c2',10],['g2','c3',12]],columns=['group','column','val'])
    # df.pivot("column", "group", "val").plot(kind='bar')
    # average, min, max
    groups = [[50,150,250], [100,200,300], [20,35,60]]
    group_labels = ['2016', '2017', '2018']
    # Convert data to pandas DataFrame.
    df = pd.DataFrame(groups, index=group_labels).T
    # Plot.
    ax = pd.concat([df.min().rename('min'),df.mean().rename('average'),
         df.max().rename('max')], axis=1).plot.bar()
    ax.set_ylabel("Thousands of NZD")
    plt.title('Sales data for each year')

    for i in range(0, len(groups)):
        for j in range(0, len(groups[i])):
            if j == 0:
                # print(str(groups[i][j]))
                plt.text(i-0.22,  groups[i][j] + 3, str(groups[i][j]), fontsize = 10)
            elif j == 1:
                plt.text(i-0.09,  groups[i][j] + 2, str(groups[i][j]), fontsize = 10)
            else:
                plt.text(i+0.09,  groups[i][j], str(groups[i][j]), fontsize = 10)
    plt.show()



def main():
    with open('sales.json') as json_file:
        data = json.load(json_file)
        # print(data)  # here the data is a list and empty data must be "null" otherwise error
    data_no_null = remove_null(data)
    # print("no null", len(data_no_null))
    date_list = get_date(data_no_null)
    sale_list = get_sale(data_no_null)
    # print(len(date_list), len(sale_list))
    res = to_oop(date_list, sale_list) # all rows ob now

    # plot_test(res)
    """
    This is the codes section showing the yearly plots
    """
    # year = ["2016", "2017", "2018"]
    # for i in range(0, len(year)):
    #     plot_year(res, year[i])

    """
    This is the codes showing the min, average and max monthly
    sales for each year
    """
    plot_min_averge_max(res)


main()
