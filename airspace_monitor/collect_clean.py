import os
import warnings
import pandas as pd
from pandas import DataFrame
from datetime import datetime
import xlsxwriter
from pathlib import Path

from .fetch import FetchAirspace

class SelectClean:
    def __init__(self, config):
        self.config = config
        self.data_dir = config.get('data_dir', 'Data')
        self.bounds = config.get('bounds', '46.37,10.32/5')
        self.carriers = config.get('collection_carriers', [])
        self.today = datetime.now()

    def flightdata(self) -> DataFrame:
        # Suppress future warnings
        warnings.filterwarnings(action='ignore', category=FutureWarning)

        # Creating an object to fetch the airspace
        df: DataFrame = FetchAirspace.current_space(bounds=self.bounds)

        if df.empty:
            cols = ['ICAO 24-bit Code', 'Latitude', 'Longitude', 'Track', 'Altitude', 'Airspeed(kts)', 'Null', 'DNA',
                    'AC_Type', 'AC_Registration', 'DNA2', 'Origin', 'Destination', 'FlightNo', 'Null2', 'Null3',
                    'CallSign', 'Null4', 'Carrier']
            return pd.DataFrame(columns=cols)

        # DATA TRANSFORMATION:
        df.columns = ['ICAO 24-bit Code', 'Latitude', 'Longitude', 'Track', 'Altitude', 'Airspeed(kts)', 'Null', 'DNA',
                      'AC_Type', 'AC_Registration', 'DNA2', 'Origin', 'Destination', 'FlightNo', 'Null2', 'Null3',
                      'CallSign', 'Null4', 'Carrier']

        # Dropping empty/non-relevant columns
        df.drop(['ICAO 24-bit Code', 'Null', 'Null2', 'Null3', 'Null4', 'DNA', 'DNA2'], axis=1, inplace=True)

        # Adding new columns for additional data
        df["Date"] = self.today
        df["Model"] = "NA"
        df["Airline"] = "NA"
        df["Airport_O"] = "NA"
        df["Airport_D"] = "NA"
        df["Trail"] = "NA"

        # Filling NA in place of empty cells
        df.fillna('NA', inplace=True)

        return df

    def carrierdata(self, df: DataFrame, carrier: str) -> DataFrame:
        carr_frame: DataFrame = df[df['Carrier'] == carrier].copy()

        iter1 = 0
        if carr_frame.shape[0] == 0:
            print(f'No aircraft in the sky of {carrier} carrier in the selected airspace')
        else:
            print(f'{carr_frame.shape[0]} aircraft in the sky of {carrier} carrier in the selected airspace')

            while iter1 < carr_frame.shape[0]:
                flight_id = carr_frame.index[iter1]
                try:
                    df2: DataFrame = FetchAirspace.selected_flights(f_id=flight_id)
                    df2 = df2.astype(object).fillna('NA')

                    if 'aircraft' in df2.index and 'model' in df2.columns and df2.loc["aircraft", "model"] != 'NA':
                        carr_frame.loc[flight_id, ["Model"]] = df2.loc["aircraft", "model"]['text']
                    else:
                        carr_frame.loc[flight_id, ["Model"]] = "N/A"

                    if 'airline' in df2.index and 'name' in df2.columns and df2.loc["airline", "name"] != 'NA':
                        carr_frame.loc[flight_id, ["Airline"]] = df2.loc["airline", "name"]
                    else:
                        carr_frame.loc[flight_id, ["Airline"]] = "N/A"

                    if 'airport' in df2.index and 'origin' in df2.columns and df2.loc["airport", "origin"] != 'NA':
                        carr_frame.loc[flight_id, ["Airport_O"]] = df2.loc["airport", "origin"]['name']
                    else:
                        carr_frame.loc[flight_id, ["Airport_O"]] = "N/A"

                    if 'airport' in df2.index and 'destination' in df2.columns and df2.loc["airport", "destination"] != 'NA':
                        carr_frame.loc[flight_id, ["Airport_D"]] = df2.loc["airport", "destination"]['name']
                    else:
                        carr_frame.loc[flight_id, ["Airport_D"]] = "N/A"

                    if 'trail' in df2.index:
                        carr_frame.loc[flight_id, ["Trail"]] = str(df2.loc["trail"].tolist())
                except Exception as e:
                    print(f"Error fetching details for flight {flight_id}: {e}")
                    carr_frame.loc[flight_id, ["Model"]] = "N/A"
                    carr_frame.loc[flight_id, ["Airline"]] = "N/A"
                    carr_frame.loc[flight_id, ["Airport_O"]] = "N/A"
                    carr_frame.loc[flight_id, ["Airport_D"]] = "N/A"
                    carr_frame.loc[flight_id, ["Trail"]] = "N/A"

                iter1 += 1

        return carr_frame

    def build_database(self, df_fl: DataFrame, carrier: str, file_name: str):
        if not os.path.exists(file_name):
            workbook = xlsxwriter.Workbook(file_name)
            workbook.add_worksheet()
            workbook.close()
            df = pd.DataFrame()
        else:
            try:
                df: DataFrame = pd.read_excel(file_name, sheet_name="Sheet1", index_col=0)
            except Exception:
                df = pd.DataFrame()

        df_car = self.carrierdata(df_fl, carrier)

        if df_car.empty:
            print("Empty carrier data. Nothing to save")
        else:
            if not df.empty:
                df = df.reset_index()
                df_car = df_car.reset_index()
                df_mer: DataFrame = pd.concat([df, df_car])
                df_mer.set_index('index', inplace=True)
            else:
                df_mer = df_car
            df_mer.fillna('NA', inplace=True)
            df_mer.to_excel(file_name, index=True, header=True, index_label=0)
            print(f'Airspace occupancy of {carrier} is saved here: {self.data_dir}')

    def file_checker(self, df_fl: DataFrame, carrier: str):
        os.makedirs(self.data_dir, exist_ok=True)
        file_name = os.path.join(self.data_dir, f"{carrier}_Carrier.xlsx")
        self.build_database(df_fl, carrier, file_name)

    def extract_flight(self) -> DataFrame:
        flights_path = os.path.join(self.data_dir, "Flights.xlsx")
        if not os.path.exists(flights_path):
            return pd.DataFrame()
        try:
            df_ex: DataFrame = pd.read_excel(flights_path, sheet_name="Sheet1", index_col=0)
            return df_ex
        except Exception:
            return pd.DataFrame()

    def save_flights(self, df_ex: DataFrame, df_fl: DataFrame):
        os.makedirs(self.data_dir, exist_ok=True)
        flights_path = os.path.join(self.data_dir, "Flights.xlsx")
        
        if df_ex.empty:
            df_mer = df_fl
        else:
            # Align column types to prevent merge type mismatch
            for col in ['Model', 'Airline', 'Airport_O', 'Airport_D', 'Trail']:
                if col in df_ex.columns:
                    df_ex[col] = df_ex[col].astype(object)
                if col in df_fl.columns:
                    df_fl[col] = df_fl[col].astype(object)

            df_ex = df_ex.reset_index()
            df_fl = df_fl.reset_index()
            df_mer: DataFrame = pd.merge(df_ex, df_fl, how='outer')
            df_mer.set_index('index', inplace=True)
            
        df_mer.fillna('NA', inplace=True)
        df_mer.to_excel(flights_path, index=True, header=True, index_label=0)

    def run_collection(self):
        print(f"Starting flight collection with bounds: {self.bounds}")
        df_fl = self.flightdata()
        
        if df_fl.empty:
            print("No flight data returned from airspace request.")
            return

        df_ex = self.extract_flight()
        self.save_flights(df_ex, df_fl)

        for carrier in self.carriers:
            self.file_checker(df_fl, carrier)
