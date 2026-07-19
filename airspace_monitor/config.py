import os
import configparser

def load_config(config_path=None):
    """
    Loads configurations from a .ini file and formats them as a dictionary.
    """
    if config_path is None:
        # Resolve config.ini relative to this package installation or workspace root
        possible_paths = [
            "config.local.ini",
            os.path.join(os.getcwd(), "config.local.ini"),
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.local.ini"),
            "config.ini",
            os.path.join(os.getcwd(), "config.ini"),
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.ini")
        ]
        for path in possible_paths:
            if os.path.exists(path):
                config_path = path
                break
        if not config_path:
            raise FileNotFoundError("Could not locate config.ini in standard paths. Please supply a direct path.")

    print(f"Reading configuration from: {config_path}")
    parser = configparser.ConfigParser()
    parser.read(config_path)

    # Resolve paths (fallback to 'Data' and 'Pics' relative to current working directory)
    data_dir = parser.get('paths', 'data_dir', fallback='Data')
    output_dir = parser.get('paths', 'output_dir', fallback='Pics')

    # Convert to normalized absolute paths
    data_dir = os.path.abspath(data_dir)
    output_dir = os.path.abspath(output_dir)

    # Parse collection carriers and plotting carriers as lists
    collection_carriers_str = parser.get('collection', 'carriers', fallback='RFR, RCH, BAF, HVK, IAM, NAT, IAF, IRIAF')
    collection_carriers = [c.strip() for c in collection_carriers_str.split(',') if c.strip()]

    plotting_carriers_str = parser.get('plotting', 'carriers', fallback='RCH, RFR, BAF, HVK, IAM, NAT')
    plotting_carriers = [c.strip() for c in plotting_carriers_str.split(',') if c.strip()]

    bounds = parser.get('collection', 'bounds', fallback='46.37,10.32/5')

    config = {
        'data_dir': data_dir,
        'output_dir': output_dir,
        'collection_carriers': collection_carriers,
        'plotting_carriers': plotting_carriers,
        'bounds': bounds
    }

    return config
