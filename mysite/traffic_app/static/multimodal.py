import numpy as np
import pandas as pd

def generate_histogram():

    # create an empty dataframe
    columns_names = ["Time","Swipe_In_1", "Swipe_In_2", "Swipe_In_3", "Swipe_In_4",
                     "swipe_In_All",
                     "Swipe_Out_1", "Swipe_Out_2", "Swipe_Out_3", "Swipe_Out_4",
                     "Swipe_Out_All"]
    df = pd.DataFrame(columns=columns_names)




    mu1,sigma1 = 8, 0.5
    num_of_members_1 = 50
    swipe_team1 = np.random.normal(mu1, sigma1, num_of_members_1*30)
    Swipe_In_1, bins = np.histogram(swipe_team1, bins= np.linspace(5.875,23.125,70))
    print "swipe_len" ,len(Swipe_In_1),'bins',len(bins)
    print [Swipe_In_1,bins]
    time =[]
    for count in range(0,len(bins)-1):
        print count
        time.append((bins[count]+ bins[count+1])/2)
    print time

    df["Time"]=time


    df["Swipe_In_1"] = Swipe_In_1

    mu2, sigma2 = 9, 0.5
    num_of_members_2 = 50
    swipe_team2 = np.random.normal(mu2, sigma2, num_of_members_2 * 30)
    Swipe_In_2, bins = np.histogram(swipe_team2, bins= np.linspace(5.875,23.125,70))
    df["Swipe_In_2"] = Swipe_In_2

    mu3, sigma3 = 10, 0.5
    num_of_members_3 = 70
    swipe_team3 = np.random.normal(mu3, sigma3, num_of_members_3 * 30)
    Swipe_In_3, bins = np.histogram(swipe_team3, bins= np.linspace(5.875,23.125,70))
    df["Swipe_In_3"] = Swipe_In_3

    mu1, sigma1 = 11, 0.5
    num_of_members_4 = 120
    swipe_team4 = np.random.normal(mu1, sigma2, num_of_members_1 * 30)
    Swipe_In_4, bins = np.histogram(swipe_team3, bins= np.linspace(5.875,23.125,70))
    df["Swipe_In_4"] = Swipe_In_4

    swipe_in_all = Swipe_In_1+Swipe_In_2+Swipe_In_3+Swipe_In_4
    df["swipe_In_All"]=swipe_in_all
    print swipe_in_all



    df.set_index("Time", inplace=True)
    df.fillna(value=0, inplace=True)

    #print df
    df.to_csv("swipe_histograms.csv")

if __name__ == "__main__":
    generate_histogram()
