import os
import pandas as pd
from pandas import DataFrame
from .collect_clean import SelectClean
from .plot import PlotFindings

class AirspaceMonitorOrchestrator:
    def __init__(self, config):
        self.config = config
        self.data_dir = config.get('data_dir', 'Data')
        self.output_dir = config.get('output_dir', 'Pics')
        self.collection_carriers = config.get('collection_carriers', [])
        self.plotting_carriers = config.get('plotting_carriers', [])

    def run_pipeline(self, run_collection=True, run_plotting=True):
        print("\n" + "="*80)
        print("🚀 AIRSPACE MONITOR PIPELINE ORCHESTRATOR STARTED")
        print("="*80 + "\n")

        if run_collection:
            print("--- STEP 1: AIRSPACE DATA COLLECTION ---")
            collector = SelectClean(self.config)
            collector.run_collection()
            print("Completed airspace data collection.\n")

        if run_plotting:
            print("--- STEP 2: GENERATING FINDINGS PLOTS ---")
            os.makedirs(self.output_dir, exist_ok=True)
            df_all_carriers = pd.DataFrame()

            for carrier in self.plotting_carriers:
                file_name = os.path.join(self.data_dir, f"{carrier}_Carrier.xlsx")
                if not os.path.exists(file_name):
                    print(f"⚠️ Carrier database not found for plotting: {file_name}")
                    continue

                try:
                    df = pd.read_excel(file_name, sheet_name="Sheet1", index_col=None)
                    if df.empty:
                        print(f"⚠️ Carrier database is empty: {file_name}")
                        continue
                    
                    # Align columns and types
                    if 'Date' in df.columns:
                        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                    
                    # Rename first unnamed column to FlightID if it exists
                    if 'Unnamed: 0' in df.columns:
                        df = df.rename(columns={'Unnamed: 0': 'FlightID'})
                    elif 'FlightID' not in df.columns:
                        df['FlightID'] = df.index

                    # Convert Date to formatted string for carrier-level aggregation
                    df_carrier_plot = df.copy()
                    if 'Date' in df_carrier_plot.columns:
                        df_carrier_plot['Date'] = df_carrier_plot['Date'].dt.strftime('%d/%m/%Y')

                    p_nme = os.path.join(self.output_dir, carrier)

                    # Plot 1: Altitude
                    plt = PlotFindings.plot_dt_v_alt(df_carrier_plot, carrier)
                    plt.savefig(f"{p_nme}_Altitude.png", bbox_inches='tight')
                    plt.close()

                    # Plot 2: Flight Count
                    plt2 = PlotFindings.plot_dt_v_flight_count(df_carrier_plot, carrier)
                    plt2.savefig(f"{p_nme}_No_of_Flights.png", bbox_inches='tight')
                    plt2.close()

                    # Plot 3: Type Flights
                    plt3 = PlotFindings.plot_flt_type_v_flight_count(df_carrier_plot, carrier)
                    plt3.savefig(f"{p_nme}_Type_Flights.png", bbox_inches='tight')
                    plt3.close()

                    # Collect data for all carriers combined plot
                    df_all_carriers = pd.concat([df_all_carriers, df], ignore_index=True)
                    print(f"Generated plots for carrier: {carrier}")
                except Exception as e:
                    print(f"❌ Error generating plots for carrier {carrier}: {e}")

            if not df_all_carriers.empty:
                try:
                    # Rename Unnamed: 0 if present in aggregated frame
                    if 'Unnamed: 0' in df_all_carriers.columns:
                        df_all_carriers = df_all_carriers.rename(columns={'Unnamed: 0': 'FlightID'})
                    elif 'FlightID' not in df_all_carriers.columns:
                        df_all_carriers['FlightID'] = df_all_carriers.index
                        
                    plt4 = PlotFindings.plot_flight_count_all(df_all_carriers, self.plotting_carriers)
                    plt4.savefig(os.path.join(self.output_dir, '_All_Flights.jpeg'), bbox_inches='tight')
                    plt4.close()
                    print("Generated combined carrier plot: _All_Flights.jpeg")
                except Exception as e:
                    print(f"❌ Error generating combined carrier plot: {e}")

            print("Completed plotting findings.\n")

        print("="*80)
        print("🎉 ALL REQUESTED PIPELINE STEPS COMPLETED!")
        print("="*80 + "\n")
