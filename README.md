# Python_JSON

Hi,

Run the program:

1 Clone the whole project and make sure all files are in the same folder.

2 Make sure you have had all the libraries installed.

3 type CMI "python3 main.py"

4 result images have been saved in the folder "images"

===========================================================================

I randomly create sales.json file.

The sales.json describes daily sales from a local pharmacy from 01/01/2016 to 31/12/2018.

There are 1000 pieces of data, but there also exists duplicate dates and null data. Therefore, these data

would be removed. Only 657 data are left when plotting the data. That makes sense in three years. We remove weekends and
public holidays, there are only around 200+ days every year.




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

5. how to show the plots?
    numpy, pandas
