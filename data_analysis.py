# External imports
import numpy as np

class DataAnalysis():
    
    def __init__(self, train_df, ideal_df):
        self.train_df = train_df
        self.ideal_df = ideal_df

    def __sort_list(self, list):
        # Sorting based on first index of tuple, so that match with least error comes on top.
        return sorted(list, key = lambda x: x[1])

    def __find_individual_matching_ideal(self, col_name):
        train_col_data = self.train_df[col_name]
        error_list = []
        for ideal_col in self.ideal_df.columns[1:]:
            ideal_col_data = self.ideal_df[ideal_col]
            # Finding error amount by Sum of deviations squared (Least Squared) for each ideal function.
            error = self.__sum_of_deviation_squared(train_col_data, ideal_col_data)

            # Since we're already looping, finding and storing maximum deviation between columns as it'll be required for Criteria 2 when working with Test functions.
            max_dev = self.max_deviation(train_col_data, ideal_col_data)

            # Appending the ideal column, it's error and maximum deviation in error list.
            error_list.append((ideal_col, error, max_dev))

        # Returning the first item of sorted list, this will return the best matching ideal function with minimum (least) error.
        # Returning item will be a Tuple with following 3 elements:
        #       1. Matching ideal function (Y column) name.
        #       2. Error value (based on criteria 1 / sum of squared deviations).
        #       3. Maximum deviation between train and matching ideal function. (This will be used while working with test data.)

        return self.__sort_list(error_list)[0]


    def find_matching_ideal_functions(self):
        '''
        Finding the best matching ideal functions out of all 50 ideal functions, for each training functions. 

        Return format is like below:
        {
            'y1': ('y13', 100.0506255399994, 0.4999699999999976), 
            'y2': ('y31', 95.34986419200027, 0.49812999999999974), 
            'y3': ('y15', 101.28976004399982, 0.4975619999999985), 
            'y4': ('y10', 99.50240088299999, 0.49966569999999955)
        }

        Where each item is a key-value pair. Key being the train function and value has tuple of following 3 elements:
            1. Matching ideal function (Y column) name.
            2. Error value (based on criteria 1 / sum of squared deviations).
            3. Maximum deviation between train and matching ideal function. (This will be used while working with test data.)

        '''

        # Declaring result dictionary
        result = {}

        # Running loop on all ideal_cols of Train DataFrame, except first ideal_col first (which is ideal_col 'x')
        for col_name in self.train_df.columns[1:]:
            # Finding matching ideal function for individual train function and adding that in the result dictionary.
            result[col_name] = self.__find_individual_matching_ideal(col_name)
        
        return result


    def __sum_of_deviation_squared(self, train_col_data, ideal_col_data):
       
        # As per criteria 1 of Assignment. Finding the sum of squared deviation between train and ideal columns.
        error =  np.sum(np.abs(train_col_data-ideal_col_data))

        # Alternative methods to find errors:
        
        # 1. Root Mean Square Error (RMSE):
        # error =  np.sqrt(np.sum(np.square(train_col_data-ideal_col_data)) / len(train_col_data))

        # 2. Mean Square Error (MSE):
        # error =  np.sum(np.square(train_col_data-ideal_col_data)) / len(train_col_data)

        return error

    def max_deviation(self, prediction, label):
        max_dev = np.max(np.abs(prediction - label))
        return max_dev