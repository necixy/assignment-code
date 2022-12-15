# External imports
import numpy as np
from math import sqrt

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

        Where each item is a key-value pair. Key being the train function and value is a tuple of following 3 elements:
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

    def map_test_to_ideal(self, test_df, ideal_df, ideal_match):
        # We use the test data provided to determine for each and every x-y- pair of 
        # values whether or not they can be assigned to the four chosen ideal functions

        mapped_tests = {}
        unmapped_tests = {}

        matching_count = 0
        unmatching_count = 0

        # Looping through all Test DataFrame rows using iterrows function.
        # Since Test dataset isn't expected to be too large in size, hence iterrows is being used to simplify, for large dataset vectorization is recommended.

        for index, test_row in test_df.iterrows():
            # Unpacking x and y value from current loop Test row.
            test_x, test_y = test_row

            match_found = False


            matching_ideal_function = None
            matching_ideal_function_difference = 0

            

            # Looping through all 4 ideal match that we found earlier and passed to this function.
            for train_col, matching in ideal_match.items():

                # Getting the ideal column name.
                ideal_col = matching[0]

                # Getting the ideal column value for given Test X value. "ideal_col" is the name of matching ideal column.
                ideal_value = float(ideal_df.loc[ideal_df['x']==test_x][ideal_col])

                # Finding the difference between test and ideal values.
                test_ideal_difference = np.abs(test_y-ideal_value)

                # Since we already calculated maximum deviation between train and ideal function, we are using it here in order to 
                # calculate the maximum deviation allowed (Criteria 2 of assignment) by multiplying it with sqrt(2).
                max_deviation_allowed = matching[2] * sqrt(2)

                # Based on Criteria 2 of mapping test data to ideal, we are checking if the difference between
                # test and ideal is less than or equal to maximum deviation allowed.

                # A test point can be mapped to an ideal function if the deviation between test point and ideal function 
                # is smaller than the maximum deviation between that ideal function and its training function times sqrt(2).
                if (test_ideal_difference<=max_deviation_allowed):
                    
                    if(matching_ideal_function == None or test_ideal_difference < matching_ideal_function_difference):
                        matching_ideal_function = ideal_col
                        matching_ideal_function_difference = test_ideal_difference

                    # if ((test_x not in mapped_tests) or (mapped_tests[test_x][2]>test_ideal_difference)):
                    #         mapped_tests[test_x]    = (test_x, test_y, test_ideal_difference, ideal_col)        
                    #         match_found = True         

            # if(not match_found):
            #     unmapped_tests[test_x]    = (test_x, test_y, None, None)

            if(matching_ideal_function is None):
                unmatching_count += 1
                unmapped_tests[test_x]    = (test_x, test_y, None, None)
            else:
                matching_count += 1
                if(test_x in mapped_tests):
                    print('dup test_x', test_x)
                mapped_tests[test_x]    = (test_x, test_y, test_ideal_difference, ideal_col)        
        
        
        print(f'ARR {len(mapped_tests)} items mapped out of {test_df.shape[0]} test items')
        print(f'ARR {len(unmapped_tests)} items COULDN\'T out of {test_df.shape[0]} test items')
        # mapped_x = [i[0] for i in mapped_tests.values()]
        # mapped_points = [i[1] for i in mapped_tests.values()]

        print(f'{matching_count} items mapped out of {test_df.shape[0]} test items')
        print(f'{unmatching_count} items COULDN\'T out of {test_df.shape[0]} test items')

    def __sum_of_deviation_squared(self, train_col_data, ideal_col_data):
       
        # As per criteria 1 of Assignment. Finding the sum of squared deviation between train and ideal columns.
        error =  np.sum(np.abs(train_col_data-ideal_col_data))

        # Alternative methods to find errors:
        
        # 1. Root Mean Square Error (RMSE):
        # error =  np.sqrt(np.sum(np.square(train_col_data-ideal_col_data)) / len(train_col_data))

        # 2. Mean Square Error (MSE):
        # error =  np.sum(np.square(train_col_data-ideal_col_data)) / len(train_col_data)

        return error

    def max_deviation(self, col_1, col_2):
        '''
        Finds the maximum deviation between two columns data.
        '''
        max_dev = np.max(np.abs(col_1 - col_2))
        return max_dev