import os
import sys
from airspace_monitor import load_config, AirspaceMonitorOrchestrator

# Reconfigure stdout to use UTF-8 to prevent UnicodeEncodeError on Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("="*80)
    print("✈️ AIRSPACE MONITOR PIPELINE ENTRYPOINT")
    print("="*80)

    # 1. Load config
    try:
        config = load_config()
    except Exception as e:
        print(f"Warning loading config.ini: {e}. Fallback to defaults.")
        config = {
            'data_dir': os.path.abspath('Data'),
            'output_dir': os.path.abspath('Pics'),
            'collection_carriers': ['RFR', 'RCH', 'BAF', 'HVK', 'IAM', 'NAT', 'IAF', 'IRIAF'],
            'plotting_carriers': ['RCH', 'RFR', 'BAF', 'HVK', 'IAM', 'NAT'],
            'bounds': '46.37,10.32/5'
        }

    print(f"Data Directory: {config['data_dir']}")
    print(f"Plots Directory: {config['output_dir']}")
    print(f"Collection Carriers: {config['collection_carriers']}")
    print(f"Plotting Carriers: {config['plotting_carriers']}")
    print(f"Geographic Bounds: {config['bounds']}")

    # 2. Run orchestrator
    orchestrator = AirspaceMonitorOrchestrator(config)
    orchestrator.run_pipeline(
        run_collection=True,
        run_plotting=True
    )

if __name__ == "__main__":
    main()
