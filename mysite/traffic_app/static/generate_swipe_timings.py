import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime



#plt.plot(s)
#plt.show()


def generate_data():

    # create an empty dataframe
    columns_names = ["Date","Swipe_In_Mean","Swipe_In_Std","Swipe_Out_Mean","Swipe_Out_Std"]
    df = pd.DataFrame(columns=columns_names)
    df.set_index("Date", inplace=True)
    df.fillna(value=0, inplace=True)

    # generate a date list
    a = datetime.datetime.today()
    numdays = 190
    dateList = []
    for x in range (0, numdays):
        dateList.append(a - datetime.timedelta(days = x))

    dateList.sort()
    print dateList

    # for each day in date list generate swipe in swipe out timings
    count=0
    for date_obj in dateList:
        date = date_obj.strftime("%d-%m-%Y")
        month= date.split("-")[1]
        print month
        if month in ["12","01","02","03"]:
            sigma = 0.25
        if month in ["04","05"]:
            sigma = min(0.05 + sigma,1)
        if month in ["07"]:
            sigma = 1


        mu_in = 9+np.random.normal(0, 0.5, 1000)
        mu_out = 6


        print sigma
        swipe_times = np.random.normal(mu_in, sigma, 1000)
        swipe_in_time_mean = 9+np.random.normal(0, 0.25)
        swipe_in_time_std = min(abs(np.random.normal(0, sigma)),3)

        swipe_out_time_mean = 17 + np.random.normal(0, 0.25)
        swipe_out_time_std = min(abs(np.random.normal(0, sigma)),3)


        df.ix[date]=[swipe_in_time_mean, swipe_in_time_std,swipe_out_time_mean, swipe_out_time_std]
        print date,swipe_in_time_mean, swipe_in_time_std

    df.to_csv("simulated_swipe_times.csv")
    print df










if __name__ == "__main__":
    generate_data()
