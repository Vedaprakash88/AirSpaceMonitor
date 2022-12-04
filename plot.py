import seaborn as sns
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df: DataFrame = pd.read_excel("NAT_Carrier.xlsx", sheet_name="Sheet1",
                              index_col=0)

df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

# Plot Date vs Altitude
def plot_dt_v_alt():
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

    plt.show()

# Plot Date vs No.of Flights




















plot_dt_v_alt()