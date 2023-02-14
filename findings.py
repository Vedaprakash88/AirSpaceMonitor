import pandas as pd
from pandas import DataFrame
from pathlib import Path
from plot import PlotFindings

##################################################################################################################
carriers = ['RCH', 'RFR', 'BAF', 'HVK', 'IAM', 'NAT']
df2 = pd.DataFrame()
##################################################################################################################
for carrier in carriers:
    path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Data\\"
    p_path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Pics\\"
    p_nme = p_path + carrier
    file_name = path + carrier + "_Carrier.xlsx"
    path = Path(file_name)
    df: DataFrame = pd.read_excel(path, sheet_name="Sheet1", index_col=None)
    df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
    df = df.rename(columns={'Unnamed: 0': 'FlightID'})

    # Plot by altitude
    alt_obj = PlotFindings()
    plt = alt_obj.plot_dt_v_alt(df, carrier)
    plt.savefig(p_nme + '_Altitude')
    plt.close()

    # Plot by flight count
    num_obj = PlotFindings()
    plt2 = num_obj.plot_dt_v_flight_count(df, carrier)
    plt2.savefig(p_nme + '_No_of_Flights.png', bbox_inches='tight')
    plt2.close()

    # Plot by flight count
    flt_obj = PlotFindings()
    plt3 = flt_obj.plot_flt_type_v_flight_count(df, carrier)
    plt3.savefig(p_nme + '_Type_Flights.png', bbox_inches='tight')
    plt3.close()

    # Gathering data of all flights
    df2: DataFrame = pd.concat([df2, df], ignore_index=False)
    # df2: DataFrame = df2.append(df, ignore_index=False)
plt4 = PlotFindings.plot_flight_count_all(df2, carriers)
p_path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\Pics\\"
plt4.savefig(p_path + '_All_Flights.jpeg', bbox_inches='tight')
