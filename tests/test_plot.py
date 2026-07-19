import unittest
import pandas as pd
import matplotlib.pyplot as plt
from airspace_monitor import PlotFindings

class TestPlotFindings(unittest.TestCase):
    def setUp(self):
        # Create dummy dataframe matching cleaned columns
        self.df = pd.DataFrame({
            'Carrier': ['LH', 'LH', 'BA'],
            'AC_Type': ['A320', 'A320', 'A321'],
            'Altitude': [30000, 32000, 34000],
            'Date': ['19/07/2026', '19/07/2026', '19/07/2026'],
            'FlightID': ['F1', 'F2', 'F3']
        })

    def tearDown(self):
        plt.close('all')

    def test_plot_dt_v_alt(self):
        plt_obj = PlotFindings.plot_dt_v_alt(self.df, 'LH')
        self.assertIsNotNone(plt_obj)

    def test_plot_dt_v_flight_count(self):
        plt_obj = PlotFindings.plot_dt_v_flight_count(self.df, 'LH')
        self.assertIsNotNone(plt_obj)

    def test_plot_flt_type_v_flight_count(self):
        plt_obj = PlotFindings.plot_flt_type_v_flight_count(self.df, 'LH')
        self.assertIsNotNone(plt_obj)

    def test_plot_flight_count_all(self):
        plt_obj = PlotFindings.plot_flight_count_all(self.df, ['LH', 'BA'])
        self.assertIsNotNone(plt_obj)

if __name__ == '__main__':
    unittest.main()
