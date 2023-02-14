##!./venv/Scripts/python.exe

# Code created by Veda Chintha, Computer Science Master's student of SRH Berlin University of Applied Sciences.
#######################################################################################################################

# importing the required libraries

import os.path  # for picking the paths of Excel workbooks for extracting the data
from pathlib import Path
from fetch import FetchAirspace  # Library created by me to fetch data from the website
from datetime import datetime
import warnings  # To supress future warnings
import pandas as pd  # to work with data received from website
from pandas import DataFrame  # for use as type hints
import xlsxwriter  # for saving the data in Excel format

#######################################################################################################################

# gets the path of the Project folder

r = Path(__file__).parent
root = os.path.join(r, "Data")
root = Path(root)

#######################################################################################################################

# user Inputs

carriers = ['RFR', 'RCH', 'BAF', 'HVK', 'IAM', 'NAT']  # carrier list
bounds = '61.62,23.185,-18.04,54.645'  # Geo-space ==> latitude and longitudes (from Flightradar24)
today = datetime.now()


#######################################################################################################################

# Class to work with data from thw website

class SelectClean:

    # Get and save all the flights in the selected geo-space

    @staticmethod
    def flightdata() -> DataFrame:

        #  Suppressing future warnings
        warnings.filterwarnings(action='ignore', category=FutureWarning)

        #  Creating an object to fetch the airspace
        df: DataFrame = FetchAirspace().current_space(bounds=bounds)

        #  DATA TRANSFORMATION:

        #  Assigning column names
        df.columns = ['ICAO 24-bit Code', 'Latitude', 'Longitude', 'Track', 'Altitude', 'Airspeed(kts)', 'Null', 'DNA',
                      'AC_Type', 'AC_Registration', 'DNA2', 'Origin', 'Destination', 'FlightNo', 'Null2', 'Null3',
                      'CallSign',
                      'Null4', 'Carrier']

        #  Dropping empty/non-relevant columns
        df.drop(['ICAO 24-bit Code', 'Null', 'Null2', 'Null3', 'Null4', 'DNA', 'DNA2'], axis=1, inplace=True)

        # df.pop("Null2") # same function, for single columns
        # del df["Null3"] # same function, for single columns

        #  Adding new columns for additional data

        df["Date"] = today
        df["Model"] = 0
        df["Airline"] = 0
        df["Airport_O"] = 0
        df["Airport_D"] = 0
        df["Trail"] = 0

        # Filling NA in place of empty cells

        df.fillna('NA', inplace=True)

        # saving the airspace in Excel format in project folder - to keep date-wise record
        # path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Data\\Flights.xlsx"
        # df.to_excel(path, index=True, header=True, index_label=0)

        #  Returns the airspace in the form of DataFrame object
        return df

    #######################################################################################################################

    #  Gets Carrier based data from the airspace received from  "def flightdata() -> DataFrame" function
    @staticmethod
    def carrierdata(df: DataFrame, carrier: str):

        #  Slicing the airspace as per selected carrier and storing it in carrier dataframe

        carr_frame: DataFrame = df[df['Carrier'] == carrier]
        print(carr_frame)

        iter1 = 0  # variable to store number of iterations (see below)

        #  Checking if there are any flights of the selected carrier
        if carr_frame.shape[0] == 0:
            print(f'No aircraft in the sky of', carrier, 'carrier in the selected airspace')
        else:
            print(carr_frame.shape[0], 'aircraft in the sky of', carrier, 'carrier in the selected airspace')

            # Looping through each flight and getting the additional flight data from the website

            while iter1 <= carr_frame.shape[0]:

                #  Creating an object and fetching a specific flight's data

                df2: DataFrame = FetchAirspace().selected_flights(f_id=carr_frame.index[iter1])

                #  Filling NA in place of empty cells

                df2.fillna('NA', inplace=True)

                # Temp lines - to save carrier data to Excel
                # path_c = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Data\\carrier.xlsx"
                # df2.to_excel(path_c, index=True, header=True, index_label=0)

                #  Finding and filling additional flight data to carrier dataframe

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

                carr_frame.at[carr_frame.index[iter1], "Trail"] = df2.loc["trail"]  # ac_destination

                iter1 += 1
        # Returning the transformed Carrier DataFrame

        return carr_frame

    #######################################################################################################################

    #  Building the Carrier Database - fetching already saved carrier database and the adding newly fetched data
    #  to it and the saving it back

    @staticmethod
    def build_database(carrier: str, file_name: str):
        df: DataFrame = pd.read_excel(file_name, sheet_name="Sheet1",
                                      index_col=0)  # creates a DF with column 0 as Row index
        df: DataFrame = df.append(SelectClean().carrierdata(df_fl, carrier), ignore_index=False)
        df.fillna('NA', inplace=True)
        df.to_excel(file_name, index=True, header=True, index_label=0)
        print('Airspace occupancy of', carrier, 'is saved here: ', root)
        return None


#######################################################################################################################

#  Independent function to check if a carrier's file exists. If not, it will create one
def file_checker(carrier: str):
    path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Data\\"
    file_name = path + carrier + "_Carrier.xlsx"
    path = Path(file_name)
    if path.is_file():
        SelectClean().build_database(carrier, file_name)
    else:
        workbook = xlsxwriter.Workbook(file_name)
        workbook.add_worksheet()
        workbook.close()
        SelectClean().build_database(carrier, file_name)
    return None


#######################################################################################################################

#  Independent function to extract flights data
def extract_flight():
    path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Data\\Flights.xlsx"
    df_ex: DataFrame = pd.read_excel(path, sheet_name="Sheet1",
                                     index_col=0)
    return df_ex


#######################################################################################################################

#  Independent function to save flights data
def save_flights(df_ex: DataFrame, df_fl: DataFrame):
    df_ex: DataFrame = df_ex.append(df_fl, ignore_index=False)
    df_ex.fillna('NA', inplace=True)
    path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Data\\Flights.xlsx"
    df_ex.to_excel(path, index=True, header=True, index_label=0)


#######################################################################################################################
#######################################################################################################################


# Initiating the Program

de_ex = extract_flight()
df_fl = SelectClean().flightdata()
save_flights(de_ex, df_fl)

for af in carriers:
    file_checker(af)  # looking for NATO aircraft in European and Ukrainian Airspace

###################################################*End of Package*####################################################
#######################################################################################################################
