# External imports
import numpy as np

class StatsAnalysis():
    '''
    A basic class having statistics methods. The class is created separately only to include at least one inheritance, else it could be part of "data_analysis.py".

    ...

    Methods
    -------
    sort_list(list)
        Sorts list of tuple based on first index (second value) of tuple.

    max_deviation(col_1, col_2)
        Finds the maximum deviation between two columns data (col_1 and col_2).

    sum_of_deviation_squared(train_col_data, ideal_col_data)
        Finds the sum of squared deviation between train_col_data and 
        ideal ideal_col_data. (As per criteria 1 of assignment.)

    '''

    def sort_list(self, list):
        '''
        Sorts list of tuple based on first index (second value) of tuple.
        ...

        Parameters
        ----------
        list: List
            List to be sorted.
        '''
        # Sorting based on first index of tuple, so that match with least error comes on top.
        return sorted(list, key = lambda x: x[1])

    def max_deviation(self, col_1, col_2):

        '''
        Finds the maximum deviation between two columns data (col_1 and col_2).

        ...

        Parameters
        ----------
        col_1 : NumPy Array
            Column 1 data in NumPy array format.
        
        col_2 : NumPy Array
            Column 2 data in NumPy array format.
        '''
        max_dev = np.max(np.abs(col_1 - col_2))
        return max_dev
    
    def sum_of_deviation_squared(self, train_col_data, ideal_col_data):
        '''
        Finds the sum of squared deviation between train_col_data and 
        ideal ideal_col_data. (As per criteria 1 of assignment.)

        ...

        Parameters
        ----------
        train_col_data: NumPy Array
            Column data of Train data given y column.

        ideal_col_data: NumPy Array
            Column data of Idea data given y column.
        '''
        
        # As per criteria 1 of Assignment. 
        error =  np.sum(np.square(train_col_data-ideal_col_data))

        # Alternative methods to find errors between two columns data:
        
        # 1. Root Mean Square Error (RMSE):
        # error =  np.sqrt(np.sum(np.square(train_col_data-ideal_col_data)) / len(train_col_data))

        # 2. Mean Square Error (MSE):
        # error =  np.sum(np.square(train_col_data-ideal_col_data)) / len(train_col_data)

        return error
