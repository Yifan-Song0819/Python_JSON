# Python_JSON
Please link to a python git repo that performs filtering on time-series data and outputs a plot of the filtered and unfiltered data, the minimum, mean and average of the data. Include a JSON schema for the data model in the source code. Show images of the above plots.


1. what is performs filtering on time-series data?

    remove outliers, noise data

2. create JSON file and JSON schema
    A pharmacy daily sales from 01-01-1998 to 01-01-2018. The sales unit is kNZD which means thousands NZD per day.

    {
        "date" : "01-01-1998",
        "sale" : 0-6.6
    }

3. reads JSON by python

    import json then open and load

3'. filtering the data (pre-process the data)

    (1) there are some rows which have the same date. we keep the large sale's one

    (2) there are some rows with both values are null, we need to delete the data

4. handle the json format data to get mean, average, minimum, maximum, standard deviation.....

    (1) if some days are missing, we assume the pharmacy was closed for some reason (like holidays)

        so we need to handle this part when doing calculation

    (2)

5. how to show the plots?

6. do i need tkinter?
