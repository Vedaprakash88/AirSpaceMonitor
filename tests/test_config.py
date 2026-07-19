import os
import unittest
import tempfile
import shutil
from airspace_monitor import load_config

class TestConfigLoader(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.ini_path = os.path.join(self.temp_dir, "test_config.ini")
        
        ini_content = """[paths]
data_dir = /dummy/data/dir
output_dir = /dummy/output/dir

[collection]
carriers = RFR, RCH, BAF
bounds = 12.34,56.78/9
"""
        with open(self.ini_path, 'w') as f:
            f.write(ini_content)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_load_config(self):
        config = load_config(self.ini_path)
        self.assertEqual(config['data_dir'], os.path.abspath("/dummy/data/dir"))
        self.assertEqual(config['output_dir'], os.path.abspath("/dummy/output/dir"))
        self.assertEqual(config['collection_carriers'], ["RFR", "RCH", "BAF"])
        self.assertEqual(config['bounds'], "12.34,56.78/9")

if __name__ == '__main__':
    unittest.main()
