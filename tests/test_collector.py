import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import tempfile
import shutil
import os
from airspace_monitor import SelectClean

class TestSelectClean(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.config = {
            'data_dir': self.temp_dir,
            'bounds': '12,34/5',
            'collection_carriers': ['LH', 'BA']
        }
        self.collector = SelectClean(self.config)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    @patch('airspace_monitor.FetchAirspace.current_space')
    def test_flightdata_clean(self, mock_current_space):
        # Mock returned flight Dataframe before cleaning
        mock_df = pd.DataFrame.from_dict({
            'flight1': ["ICAO", 12.3, 45.6, 90, 30000, 450, "N", "D", "A320", "REG", "D2", "LHR", "JFK", "LH123", "N2", "N3", "CS123", "N4", "LH"],
            'flight2': ["ICAO2", 12.4, 45.7, 95, 32000, 460, "N", "D", "A321", "REG2", "D2", "LHR", "CDG", "BA456", "N2", "N3", "CS456", "N4", "BA"]
        }, orient='index')
        mock_current_space.return_value = mock_df

        df_cleaned = self.collector.flightdata()
        
        # Verify columns after dropping Null / DNA columns
        self.assertIn("AC_Type", df_cleaned.columns)
        self.assertIn("Carrier", df_cleaned.columns)
        self.assertIn("Model", df_cleaned.columns)
        self.assertEqual(df_cleaned.loc['flight1', 'Carrier'], 'LH')

    @patch('airspace_monitor.FetchAirspace.selected_flights')
    def test_carrierdata(self, mock_selected_flights):
        # Create input df_fl
        df_fl = pd.DataFrame({
            'Carrier': ['LH', 'BA'],
            'AC_Type': ['A320', 'A321'],
            'Model': ['NA', 'NA'],
            'Airline': ['NA', 'NA'],
            'Airport_O': ['NA', 'NA'],
            'Airport_D': ['NA', 'NA'],
            'Trail': ['NA', 'NA']
        }, index=['flight1', 'flight2'])

        mock_selected_df = pd.DataFrame.from_dict({
            'aircraft': pd.Series({'model': {'text': 'A320neo'}}),
            'airline': pd.Series({'name': 'Lufthansa'}),
            'airport': pd.Series({'origin': {'name': 'Munich'}, 'destination': {'name': 'Berlin'}}),
            'trail': pd.Series([1, 2])
        }, orient='index')
        mock_selected_flights.return_value = mock_selected_df

        carrier_df = self.collector.carrierdata(df_fl, 'LH')
        
        # flight1 is LH
        self.assertEqual(carrier_df.loc['flight1', 'Model'], 'A320neo')
        self.assertEqual(carrier_df.loc['flight1', 'Airline'], 'Lufthansa')

if __name__ == '__main__':
    unittest.main()
