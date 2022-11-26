import sys
from fetch import FetchAirspace
from pandas import DataFrame
from datetime import datetime
import warnings
import pandas as pd
from pathlib import Path
import xlsxwriter

root = Path(__file__).parent.parent


class SelectClean:
    @staticmethod
    def carrierdata(carrier: str, bounds: str) -> DataFrame:
        warnings.filterwarnings(action='ignore', category=FutureWarning)
        today = datetime.now()
        fetchobj = FetchAirspace()
        df: DataFrame = fetchobj.current_space(bounds=bounds)

        df.columns = ['ICAO 24-bit Code', 'Latitude', 'Longitude', 'Track', 'Altitude', 'Airspeed(kts)', 'Null', 'DNA',
                      'AC Type', 'AC Registration', 'DNA2', 'Origin', 'Destination', 'FlightNo', 'Null2', 'Null3',
                      'CallSign',
                      'Null4', 'Carrier']

        df.drop(['ICAO 24-bit Code', 'Null', 'Null2', 'Null3', 'Null4', 'DNA', 'DNA2'], axis=1, inplace=True)

        # same function, for single columns
        # df.pop("Null2")
        # del df["Null3"]

        df["Date"] = today
        df["Model"] = 0
        df["Airline"] = 0
        df["Airport_O"] = 0
        df["Airport_D"] = 0
        df.fillna('NA', inplace=True)
        df.to_excel("Flights.xlsx", index=True, header=True, index_label=0)

        carr_frame: DataFrame = df.loc[df['Carrier'] == carrier]
        iter1 = 0
        if carr_frame.shape[0] == 0:
            print(f'No aircraft in the sky of', carrier, 'carrier in the selected airspace')
        else:
            print(carr_frame.shape[0], 'aircraft in the sky of', carrier, 'carrier in the selected airspace')

            while iter1 < carr_frame.shape[0]:
                fetchAcObj = FetchAirspace()
                df2: DataFrame = fetchAcObj.selected_flights(f_id=carr_frame.index[iter1])
                df2.fillna('NA', inplace=True)

                if df2.loc["aircraft", "model"] != 'NA':
                    carr_frame.at[carr_frame.index[iter1], "Model"] = df2.loc["aircraft", "model"]['text']  # ac_model
                else:
                    carr_frame.at[carr_frame.index[iter1], "Model"] = "N/A"
                if df2.loc["airline", "name"] != 'NA':
                    carr_frame.at[carr_frame.index[iter1], "Airline"] = df2.loc["airline", "name"]  # ac_airline
                else:
                    carr_frame.at[carr_frame.index[iter1], "Airline"] = "N/A"
                if df2.loc["airport", "origin"] != 'NA':
                    carr_frame.at[carr_frame.index[iter1], "Airport_O"] = df2.loc["airport", "origin"][
                        'name']  # ac_origin
                else:
                    carr_frame.at[carr_frame.index[iter1], "Airport_O"] = "N/A"
                if df2.loc["airport", "destination"] != 'NA':
                    carr_frame.at[carr_frame.index[iter1], "Airport_D"] = df2.loc["airport", "destination"][
                        'name']  # ac_destination
                else:
                    carr_frame.at[carr_frame.index[iter1], "Airport_D"] = "N/A"
                iter1 += 1

        return carr_frame

    @staticmethod
    def build_database(carrier: str, bounds: str, file_name: str):
        df: DataFrame = pd.read_excel(file_name, sheet_name="Sheet1",
                                      index_col=0)  # creates a DF with column 0 as Row index
        get_data_obj = SelectClean()
        df: DataFrame = df.append(get_data_obj.carrierdata(carrier, bounds), ignore_index=False)
        df.to_excel(file_name, index=True, header=True, index_label=0)
        print('Airspace occupancy of', carrier, 'is saved here: ', root)
        return None


def file_checker(carrier: str, bounds: str):
    file_name = carrier + "_Carrier.xlsx"
    path = Path(file_name)
    if path.is_file():
        SelectClean().build_database(carrier, bounds, file_name)
    else:
        workbook = xlsxwriter.Workbook(file_name)
        workbook.add_worksheet()
        workbook.close()
        SelectClean().build_database(carrier, bounds, file_name)
    return None


# Initiates the data program
file_checker('NAT', '55.675,36.98,-2.057,44.876')  # looking for NATO aircraft in European and Ukrainian Airspace
file_checker('RCH', '55.675,36.98,-2.057,44.876')  # looking for USAF aircraft in European and Ukrainian Airspace
file_checker('IAM', '55.675,36.98,-2.057,44.876')  # looking for Italian AF aircraft in European and Ukrainian Airspace
file_checker('RFR', '55.675,36.98,-2.057,44.876')  # looking for Royal (British) AF aircraft in European and Ukrainian Airspace
file_checker('BAF', '55.675,36.98,-2.057,44.876')  # looking for Belgium AF aircraft in European and Ukrainian Airspace
file_checker('HVK', '55.675,36.98,-2.057,44.876')  # looking for Turkish AF aircraft in European and Ukrainian Airspace

# A/c without carrier
# UC01 - Greece coast guard
