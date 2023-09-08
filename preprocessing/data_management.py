
import config.config as config
import pandas as pd

def load_dataset(filename): 
    _data = pd.read_csv(config.DATA_PATH + filename)
    return _data
