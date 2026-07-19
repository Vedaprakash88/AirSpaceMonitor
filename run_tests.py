import unittest
import sys

def run_all_tests():
    print("=" * 80)
    print("RUNNING AIRSPACE MONITOR TEST SUITE")
    print("=" * 80)
    
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == '__main__':
    run_all_tests()
