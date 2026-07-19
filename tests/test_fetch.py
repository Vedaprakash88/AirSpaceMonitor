import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from airspace_monitor import FetchAirspace

class TestFetchAirspace(unittest.TestCase):
    @patch('requests.get')
    def test_current_space(self, mock_get):
        # Mock requests.get response
        mock_response = MagicMock()
        mock_response.text = '{"full_count": 100, "version": 4, "stats": {}, "flight_123": ["ICAO", 12.3, 45.6, 90, 30000, 450, "N", "D", "A320", "REG", "D2", "LHR", "JFK", "LH123", "N2", "N3", "CS123", "N4", "LH"]}'
        mock_get.return_value = mock_response

        df = FetchAirspace.current_space("12.34,56.78/9")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("flight_123", df.index)
        self.assertEqual(df.loc["flight_123", 8], "A320")

    @patch('requests.get')
    def test_selected_flights(self, mock_get):
        # Mock requests.get response
        mock_response = MagicMock()
        mock_response.text = '{"aircraft": {"model": {"text": "Boeing 777"}}, "airline": {"name": "Lufthansa"}, "airport": {"origin": {"name": "Frankfurt"}, "destination": {"name": "Tokyo"}}, "trail": [1, 2, 3]}'
        mock_get.return_value = mock_response

        df = FetchAirspace.selected_flights("flight_123")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("aircraft", df.index)

if __name__ == '__main__':
    unittest.main()
