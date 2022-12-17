import pandas as pd
import numpy as np
from pandas import DataFrame
from pathlib import Path
from plot import PlotFindings

##################################################################################################################
carriers = ['RFR', 'RCH', 'RFR', 'BAF', 'HVK', 'IAM', 'RFR', 'NAT']
df2 = pd.DataFrame()
##################################################################################################################
for carrier in carriers:
    path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Data\\"
    file_name = path + carrier + "_Carrier.xlsx"
    path = Path(file_name)
    df: DataFrame = pd.read_excel(path, sheet_name="Sheet1", index_col=None)
    df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
    df = df.rename(columns={'Unnamed: 0': 'FlightID'})

    alt_obj = PlotFindings()
    plt = alt_obj.plot_dt_v_alt(df)
    plt.savefig('Altitude')
    plt.close()

    num_obj = PlotFindings()
    plt2 = num_obj.plot_dt_v_flight_count(df)
    plt2.savefig('No_of_Flights.png', bbox_inches='tight')
    plt2.close()

    flt_obj = PlotFindings()
    plt3 = flt_obj.plot_flt_type_v_flight_count(df)
    plt3.savefig('Type_Flights.png', bbox_inches='tight')
    plt3.close()

    # Plotting for all flights
    df2: DataFrame = df2.append(df, ignore_index=False)

plt4 = PlotFindings.plot_flight_count_all(df2)
plt4.savefig('All_Flights.png', bbox_inches='tight')
