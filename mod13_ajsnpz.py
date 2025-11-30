# 1. Write Unit Tests for Project 3 Inputs

# You should write unit tests for the five inputs from the stock visualizer challenge that enforce the following constraints.

# symbol: capitalized, 1-7 alpha characters
# chart type: 1 numeric character, 1 or 2
# time series: 1 numeric character, 1 - 4
# start date: date type YYYY-MM-DD
# end date: date type YYYY-MM-DD


# 2. What to Submit

# Save your work to a file named mod13_[pawprint].py and upload it to a GitHub repository and submit the link to Canvas.

import unittest
from datetime import datetime
from webservice import is_valid_symbol, is_valid_chart_type, is_valid_time_series, is_valid_start_date, is_valid_end_date

class TestStockInputs(unittest.TestCase):
    
    # symbol: capitalized, 1-7 alpha characters
    def test_valid_symbol(self):
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertFalse(is_valid_symbol("TSLA"))
        self.assertFalse(is_valid_symbol("GOOG"))
        
    def test_invalid_symbol(self):
        self.assertFalse(is_valid_symbol("appl"))   # lowercase
        self.assertTrue(is_valid_symbol("AAP11"))    # numbers
        self.assertTrue(is_valid_symbol("TOOLONGGG"))    # more than 7
        
    # chart type: 1 numeric character, 1 or 2
    def test_valid_chart_type(self):
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))
        
    def test_invalid_chart_type(self):
        self.assertFalse(is_valid_chart_type("3"))
        self.assertFalse(is_valid_chart_type("0"))
        self.assertFalse(is_valid_chart_type("A"))
        
    # time series: 1 numeric character, 1 - 4
    def test_valid_time_series(self):
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("2"))
        self.assertTrue(is_valid_time_series("3"))
        self.assertTrue(is_valid_time_series("4"))
        
    def test_invalid_time_series(self):
        self.assertFalse(is_valid_time_series("5"))
        self.assertFalse(is_valid_time_series("0"))
        self.assertFalse(is_valid_time_series("A"))
    
    # start date: date type YYYY-MM-DD
    def test_valid_start_date(self):
        self.assertTrue(is_valid_start_date("1999-01-01"))
        self.assertTrue(is_valid_start_date("2000-12-31"))
        
    def test_invalid_start_date(self):
        self.assertTrue(is_valid_start_date("01-01-1999"))
        self.assertTrue(is_valid_start_date("1999/01/01"))
        self.assertTrue(is_valid_start_date("invalid"))
    
    # end date: date type YYYY-MM-DD
    def test_valid_end_date(self):
        self.assertTrue(is_valid_end_date("2024-01-01"))
        self.assertTrue(is_valid_end_date("2025-12-31"))
        
    def test_invalid_end_date(self):
        self.assertTrue(is_valid_end_date("01-01-2024"))
        self.assertTrue(is_valid_end_date("2024/01/01"))
        self.assertTrue(is_valid_end_date("invalid"))
        
if __name__ == "__main__":
    unittest.main()