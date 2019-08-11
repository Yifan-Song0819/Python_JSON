import json
import matplotlib.pyplot as plt
from Row import Row


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
"""

def get_date(input):
    res = []
    for row in input:
        res.append(row["date"])
    return res

"""
list with only sale
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

def plot_all(rows_ob_list):
    sales_list = []
    for i in range(0, len(rows_ob_list)):
        sales_list.append(rows_ob_list[i].sale)

    dates_list = []
    for i in range(0, len(rows_ob_list)):
        dates_list.append(rows_ob_list[i].date)

    plt.plot(sales_list)
    plt.ylabel('sales')
    plt.xlabel("x1")

    # plt1.plot(dates_list)
    # plt1.ylabel('years')
    # plt1.xlabel("x2")
    plt1.show()


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
    plot_all(res)

main()
