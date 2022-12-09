import pandas as pd
import numpy as np
from custom_exceptions import *

class DataSets():
    
    def __init__(self):
        try:
            self.train = self.readCSV('datasets/train.csv')
            self.ideal = self.readCSV('datasets/ideal.csv')
            self.test = self.readCSV('datasets/test.csv')
        except FileNotFoundError as ex:
            raise DataSetNotFoundException(ex)
        else:
            if(self.train.shape[1] != 5):
                raise InvalidDataFormatException('Invalid format for train.csv.')
            if(self.ideal.shape[1] != 51):
                raise InvalidDataFormatException('Invalid format for ideal.csv.')
            if(self.test.shape[1] != 2):
                raise InvalidDataFormatException('Invalid format for test.csv.')
    
    def readCSV(self, filePath):
        return pd.read_csv(filePath)
    
