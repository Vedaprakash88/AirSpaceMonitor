import os
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

class PlotFindings:
    # Plot Date vs Altitude
    @staticmethod
    def plot_dt_v_alt(df: DataFrame, carrier) -> plt:
        if 'AC_Type' not in df.columns or 'Altitude' not in df.columns:
            print(f"Skipped alt plot: Required columns not found in carrier {carrier} data.")
            return plt
        
        # Convert Altitude to numeric, ignore errors
        df['Altitude'] = pd.to_numeric(df['Altitude'], errors='coerce')
        fil_alt = df.groupby('AC_Type')['Altitude'].max()
        x_values = fil_alt.index
        y_values = fil_alt.values
        
        plt.figure()
        plt.bar(x_values, y_values, label="A/c vs Alt")
        plt.title(f'{carrier} Aircraft @ Altitude')
        plt.xlabel('AC_Type')
        plt.ylabel('Altitude')
        plt.ylim([0, 60000])
        plt.legend(loc=0)
        plt.tight_layout()
        plt.xticks(rotation=45, ha='right')
        return plt

    # Plot Date vs No.of Flights
    @staticmethod
    def plot_dt_v_flight_count(df: DataFrame, carrier=None) -> plt:
        if 'Date' not in df.columns or 'FlightID' not in df.columns:
            print("Skipped flight count plot: Required columns not found.")
            return plt

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

        plt.figure()
        plt.plot(x_values, y_values, color='blue', marker='o')
        title_str = 'Flights per day'
        if carrier:
            title_str = f'{carrier} - {title_str}'
        plt.title(title_str)
        plt.xlabel('Dates')
        plt.ylabel('No. of Flights')
        plt.xticks(rotation=45, ha='right')
        plt.grid()
        plt.tight_layout()
        return plt

    # Aircraft Type vs no of flights
    @staticmethod
    def plot_flt_type_v_flight_count(df: DataFrame, carrier) -> plt:
        if 'AC_Type' not in df.columns or 'FlightID' not in df.columns:
            print("Skipped type flight count plot: Required columns not found.")
            return plt

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

        plt.figure()
        plt.bar(x_values, y_values, color='blue')
        plt.title(f'Flights per A/C model ({carrier})')
        plt.xlabel('Type')
        plt.ylabel('No. of Flights')
        plt.xticks(rotation=45, ha='right')
        plt.grid()
        plt.tight_layout()
        return plt

    # Plot all flights per Air-force
    @staticmethod
    def plot_flight_count_all(df: DataFrame, carriers) -> plt:
        if 'Date' not in df.columns or 'Carrier' not in df.columns or 'FlightID' not in df.columns:
            print("Skipped all flights plot: Required columns not found.")
            return plt

        df_copy = df.copy()
        df_copy['Date'] = pd.to_datetime(df_copy['Date'], dayfirst=True, errors='coerce').dt.normalize()

        plt.figure()
        for carrier in carriers:
            df_c: DataFrame = df_copy.loc[df_copy['Carrier'] == carrier]
            if df_c.empty:
                continue
            fl_cnt = df_c.groupby('Date')['FlightID'].nunique()
            plt.plot(fl_cnt.index, fl_cnt.values, label=carrier)
            
        plt.title('All Observed Flights')
        plt.xlabel('Date')
        plt.ylabel('No. of flights')
        plt.xticks(rotation=45, ha='right')
        plt.legend(loc=0)
        plt.tight_layout()
        return plt
