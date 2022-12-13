# External imports
import pandas as pd
import numpy as np

# Internal imports
from custom_exceptions import *


# Defining constants for the paths of CSV files.
TRAIN_CSV_PATH = 'datasets/train.csv'
IDEAL_CSV_PATH = 'datasets/ideal.csv'
TEST_CSV_PATH = 'datasets/test.csv'

class CSVHelper():
    
    def __init__(self):
        try:
            self.train = self.readCSV(TRAIN_CSV_PATH)
            self.ideal = self.readCSV(IDEAL_CSV_PATH)
            self.test = self.readCSV(TEST_CSV_PATH)

        except FileNotFoundError as ex:
            # Raising user-defined exception in case of CSV file not found.
            raise DataSetNotFoundException(ex)

        else:
            # Raising user-defined exception if any of CSV files not having expected columns.
            if(self.train.shape[1] != 5):
                raise InvalidDataFormatException('Invalid format for train.csv. It must have 5 columns.')
            if(self.ideal.shape[1] != 51):
                raise InvalidDataFormatException('Invalid format for ideal.csv. It must have 51 columns.')
            if(self.test.shape[1] != 2):
                raise InvalidDataFormatException('Invalid format for test.csv. It must have 2 columns.')
    
    def readCSV(self, filePath):
        return pd.read_csv(filePath)
    
