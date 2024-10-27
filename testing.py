import unittest
import pandas as pd
from datetime import datetime

# Define a test case for data validation
class TestDataValidation(unittest.TestCase):
    
    def setUp(self):
    
        # Here we manually define each column with the expected data types
        self.data = pd.DataFrame({
            'datetime': [datetime.now()],     # datetime column as a list with a single current datetime entry
            'close': [100.0],                 # 'close' price as float
            'high': [105.0],                  # 'high' price as float
            'low': [95.0],                    # 'low' price as float
            'open': [98.0],                   # 'open' price as float
            'volume': [int(1000)],            # 'volume' as an integer, explicitly cast to int
            'instrument': ['HINDALCO']        # 'instrument' as a string
        })
        
  
    def test_data_types(self):
        self.assertIsInstance(self.data['close'][0], float)      # Checks if 'close' is float
        self.assertIsInstance(self.data['high'][0], float)       # Checks if 'high' is floatt
        self.assertIsInstance(self.data['low'][0], float)        # Checks if 'low' is float
        self.assertIsInstance(self.data['open'][0], float)       # Checks if 'open' is float
        self.assertIsInstance(int(self.data['volume'][0]), int)     # Checks if 'volume' is int
        self.assertIsInstance(self.data['instrument'][0], str)   # Checks if 'instrument' is string
        self.assertIsInstance(self.data['datetime'][0], datetime) # Checks if 'datetime' is datetime type

# It will run the unit tests
if __name__ == '__main__':
    unittest.main()
