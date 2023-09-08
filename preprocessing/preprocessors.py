import pandas as pd
import config.config as config
from datetime import datetime


def convert_to_datetime(data: pd.DataFrame = None, column: str = None):
    
  dummy = data.copy()
  dummy[column] = pd.to_datetime(dummy[column], format='%Y-%m-%d %H:%M:%S')
  return dummy

def convert_timestamp_to_hourly(data: pd.DataFrame = None, column: str = None):
    dummy = data.copy()
    new_ts = dummy[column].tolist()
    new_ts = [i.strftime('%Y-%m-%d %H:00:00') for i in new_ts]
    new_ts = [datetime.strptime(i, '%Y-%m-%d %H:00:00') for i in new_ts]
    dummy[column] = new_ts
    return dummy

def convert_to_time(data: pd.DataFrame = None):
    data[config.MERGE_COLS[0]] = data[config.TIME_COL].dt.day
    data[config.MERGE_COLS[1]] = data[config.TIME_COL].dt.dayofweek
    data[config.MERGE_COLS[2]] = data[config.TIME_COL].dt.hour
    data.drop(columns=[config.TIME_COL], inplace=True)
    return data


