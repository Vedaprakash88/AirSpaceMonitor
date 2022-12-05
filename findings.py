import pandas as pd
import numpy as np
from pandas import DataFrame
from pathlib import Path
from plot import PlotFindings

##################################################################################################################
carrier = 'NAT'  # 'RCH', 'RFR', 'BAF', 'HVK', 'IAM', 'RFR'
path = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\6. Open Source Intelligence\\AirSpaceMonitor\\"
##################################################################################################################

file_name = path + carrier + "_Carrier.xlsx"
path = Path(file_name)
df: DataFrame = pd.read_excel(path, sheet_name="Sheet1", index_col=None)
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
df = df.rename(columns={'Unnamed: 0': 'FlightID'})

alt_obj = PlotFindings()
plt = alt_obj.plot_dt_v_alt(df)
plt.show()
num_obj = PlotFindings()
plt2 = num_obj.plot_dt_v_flight_count(df)
plt2.show()
