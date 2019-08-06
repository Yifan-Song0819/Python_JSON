from Row import Row

def get_date(input):
    res = []
    for row in input:
        res.append(row["date"])
    return res

def get_sale(input):
    res = []
    for row in input:
        res.append(row["sale"])
    return res

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

    final_row_list = []
    for i in range(0, len(final_date_list)):
        a_row = Row(final_date_list[i], final_sale_list[i])
        final_row_list.append(a_row)
    return final_row_list

def main():
    input = [{'date':'18/02/2018', 'sale':5.35}, {'date':'18/02/2018', 'sale':15.00}, {'date':'17/02/2017','sale':5.35},
             {'date':'30/07/2017', 'sale':4.79}, {'date': '11/02/2016','sale': 5.31}, {'date':'30/07/2017','sale':10.00}]

    date_list = get_date(input)
    sale_list = get_sale(input)
    # print(len(date_list), len(sale_list))
    res = to_oop(date_list, sale_list)
    for i in range(0, len(res)):
        print(res[i])
        print(res[i].date, res[i].sale)

main()
