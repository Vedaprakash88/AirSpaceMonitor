import seaborn as sns
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


class PlotFindings:
    # Plot Date vs Altitude
    @staticmethod
    def plot_dt_v_alt(df: DataFrame) -> plt:
        x_values = df.Date
        y_values = df.Altitude
        z_values = df.AC_Type

        plt.scatter(x_values, y_values, color='blue', marker='o')
        plt.title('NATO Aircraft @ Altitude')
        plt.xlabel('Dates')
        plt.ylabel('Altitude')
        plt.grid()
        plt.ylim([1000, 60000])

        for x, y, z in zip(x_values, y_values, z_values):
            label = str(z)
            plt.annotate(label,  # this is the text
                         (x, y),  # these are the coordinates to position the label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='left')  # horizontal alignment can be left, right or center

        # plt.show()
        return plt

    # Plot Date vs No.of Flights
    @staticmethod
    def plot_dt_v_flight_count(df: DataFrame) -> plt:

        lst_dates = df.Date.unique()
        for each_date in lst_dates:
            no_flt: DataFrame = df.loc[df['Date'] == each_date]

            









        # for x in df.Date.unique():
        #     y = (df.AC_Type == lst_ac).sum()
        #     lst_cnt[x] = y
        #
        #
        # y_values = df.AC_Type.unique()
        # print(y_values)
        # print(type(df.AC_Type.value_counts()))
        return plt



