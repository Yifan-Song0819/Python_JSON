import json

with open('sales.json') as json_file:
    data = json.load(json_file)
    # print(data)  # here the data is a list and empty data must be "null" otherwise error
    for i in data:
        print(i["id"], i["sales"])
