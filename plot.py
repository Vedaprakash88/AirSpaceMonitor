import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


class PlotFindings:
    # Plot Date vs Altitude
    @staticmethod
    def plot_dt_v_alt(df: DataFrame, carrier) -> plt:
        fil_alt = df.groupby('AC_Type')['Altitude'].max()
        x_values = fil_alt.index
        y_values = fil_alt.values
        plt.bar(x_values, y_values, label="A/c vs Alt")
        plt.title(carrier + ' Aircraft @ Altitude')
        plt.xlabel('AC_Type')
        plt.ylabel('Altitude')
        plt.ylim([0, 60000])
        plt.legend(loc=0)
        plt.tight_layout()
        plt.xticks(rotation=45, ha='right')

        # for x, y in zip(x_values, y_values):
        #     label = str(y)
        #     plt.annotate(label,  # this is the text
        #                  (x, y),  # these are the coordinates to position the label
        #                  textcoords="offset points",  # how to position the text
        #                  xytext=(0, 10),  # distance from text to points (x,y)
        #                  ha='left')  # horizontal alignment can be left, right or center
        return plt

    # Plot Date vs No.of Flights
    @staticmethod
    def plot_dt_v_flight_count(df: DataFrame) -> plt:
        flt_dict = {}
        lst_dates = df.Date.unique()
        for each_date in lst_dates:
            no_flt: DataFrame = df.loc[df['Date'] == each_date]
            no_of_flights = len((no_flt.FlightID.unique()))
            flt_dict[each_date] = int(no_of_flights)
        df_to_plot: DataFrame = pd.DataFrame.from_dict(data=flt_dict, orient='index')
        df_to_plot.columns = ['No_of_Flts']

        x_values = df_to_plot.index
        y_values = df_to_plot.No_of_Flts.values

        plt.plot(x_values, y_values, color='blue', marker='o')
        plt.title('Flights per day')
        plt.xlabel('Dates')
        plt.ylabel('No. of Flights')
        plt.xticks(rotation=45, ha='right')
        plt.grid()
        # plt.ylim([1000, 60000])

        # for x, y in zip(x_values, y_values):
        #     label = str(y)
        #     plt.annotate(label,  # this is the text
        #                  (x, y),  # these are the coordinates to position the label
        #                  textcoords="offset points",  # how to position the text
        #                  xytext=(0, 10),  # distance from text to points (x,y)
        #                  ha='left')  # horizontal alignment can be left, right or center
        return plt

    # Aircraft Type vs no of flights
    @staticmethod
    def plot_flt_type_v_flight_count(df: DataFrame, carrier) -> plt:
        typ_dict = {}
        lst_flight_types = df.AC_Type.unique()
        for each_flt_type in lst_flight_types:
            type_flt: DataFrame = df.loc[df['AC_Type'] == each_flt_type]
            no_of_flights = len((type_flt.FlightID.unique()))
            typ_dict[each_flt_type] = int(no_of_flights)
        df_to_plot: DataFrame = pd.DataFrame.from_dict(data=typ_dict, orient='index')
        df_to_plot.columns = ['No_of_Flts']
        x_values = df_to_plot.index
        y_values = df_to_plot.No_of_Flts.values

        plt.bar(x_values, y_values, color='blue')
        plt.title('Flights per A/C model')
        plt.xlabel('Type')
        plt.ylabel('No. of Flights')
        plt.xticks(rotation=45, ha='right')
        plt.grid()
        # plt.ylim([1000, 60000])

        # for x, y in zip(x_values, y_values):
        #     label = str(y)
        #     plt.annotate(label,  # this is the text
        #                  (x, y),  # these are the coordinates to position the label
        #                  textcoords="offset points",  # how to position the text
        #                  xytext=(0, 10),  # distance from text to points (x,y)
        #                  ha='left')  # horizontal alignment can be left, right or center
        return plt

    # Plot all flights per Air-force

    @staticmethod
    def plot_flight_count_all(df: DataFrame, carriers) -> plt:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True).dt.normalize()

        for carrier in carriers:
            df_c: DataFrame = df.loc[df['Carrier'] == carrier]
            fl_cnt = df_c.groupby('Date')['FlightID'].nunique()
            plt.plot(fl_cnt.index, fl_cnt.values, label=carrier)
            plt.title('All Observed Flights')
            plt.xlabel('Date')
            plt.ylabel('No. of flights')
            plt.xticks(rotation=45, ha='right')
            plt.legend(loc=0)
            plt.tight_layout()
        return plt

    # @staticmethod
    # def plot_flight_type_at_date(df: DataFrame, carriers) -> plt:
    #     # under development
    #         plt.plot(x, y)
    #         plt.title('All Observed Flights')
    #         plt.xlabel('Date')
    #         plt.ylabel('No. of flights')
    #         plt.xticks(rotation=45, ha='right')
    #         plt.legend(loc=0)
    #         plt.tight_layout()
    #     return plt
    #
