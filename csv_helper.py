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
    '''
    CSVHelper class deals with loading of CSV files for the project, which are train.csv, ideal.csv and test.csv. 
    ...

    Attributes
    ----------
    train : DataFrame
        a pandas DataFrame loaded from train.csv file.
    ideal : DataFrame
        a pandas DataFrame loaded from ideal.csv file.
    test : DataFrame
        a pandas DataFrame loaded from test.csv file.

    Private Methods
    -------
    __readCSV(filePath)
        Private method for reading given CSV filePath using pandas.

    '''
    
    train = None
    ideal = None
    test = None

    def __init__(self):
        '''
        It loads all 3 files in class constructor using Pandas and assign to the parameters.
        ...

        Parameters
        ----------
        None.

        Raises
        ------
        DataSetNotFoundException
            If any of 3 CSV files not found.

        InvalidDataFormatException
            If any of CSV files not having expected columns.
            
        '''
        try:
            self.train = self.__readCSV(TRAIN_CSV_PATH)
            self.ideal = self.__readCSV(IDEAL_CSV_PATH)
            self.test = self.__readCSV(TEST_CSV_PATH)

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
    
    def __readCSV(self, filePath):
        '''
        Private method for reading given CSV filePath using pandas.
        ...

        Parameters
        ----------
        filePath: str
            File path of CSV file to be loaded/read.

        '''
        return pd.read_csv(filePath)
    
