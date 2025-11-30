import re
from datetime import datetime

def is_valid_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def is_valid_chart_type(chart_type):
    return chart_type in ["1", "2"]

def is_valid_time_series(time_series):
    return time_series in ["1", "2", "3", "4"]

def is_valid_start_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def is_valid_end_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False