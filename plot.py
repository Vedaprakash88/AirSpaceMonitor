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
        return plt

    # Plot Date vs No.of Flights
    @staticmethod
    def plot_dt_v_flight_count(df: DataFrame) -> plt:
        flt_dict = {}
        lst_dates = df.Date.unique()
        for each_date in lst_dates:
            no_flt: DataFrame = df.loc[df['Date'] == each_date]
            l = len((no_flt.FlightID.unique()))
            flt_dict[each_date] = int(l)
        df_to_plot: DataFrame = pd.DataFrame.from_dict(data=flt_dict, orient='index')
        df_to_plot.columns = ['No_of_Flts']

        x_values = df_to_plot.index
        y_values = df_to_plot.No_of_Flts

        plt.scatter(x_values, y_values, color='blue', marker='o')
        plt.title('NATO Aircraft per day')
        plt.xlabel('Dates')
        plt.ylabel('No. of Flights')
        plt.grid()
        # plt.ylim([1000, 60000])

        for x, y in zip(x_values, y_values):
            label = str(y)
            plt.annotate(label,  # this is the text
                         (x, y),  # these are the coordinates to position the label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='left')  # horizontal alignment can be left, right or center
        return plt

    # Aircraft Type vs no of flights


    # Aircraft type vs geo location


