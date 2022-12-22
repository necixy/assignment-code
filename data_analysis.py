# External imports
import numpy as np
import pandas as pd
from math import sqrt
from stats_analysis import StatsAnalysis

class DataAnalysis(StatsAnalysis):
    '''
    The core class for dealing with all data analysis of the assignment project. It does include all the analysis 
    logic and implements all the criteria given in the assignment task description. It also inherits the class StatsAnalysis
    which provides methods like sort_list, max_deviation, sum_of_deviation_squared.

    ...

    Attributes
    ----------
    train_df : DataFrame
        A pandas DataFrame for train dataset given to the constructor.
    ideal_df : DataFrame
        A pandas DataFrame for ideal dataset given to the constructor.

    Public Methods
    ----------
    find_matching_ideal_functions()
        Finds the matching ideal function for all 4 training functions.
    
    map_test_to_ideal(test_df, ideal_df, ideal_match)
        Maps the test data to chosen best 4 ideal function based on criteria 2, given in assignment task.

    Private Methods
    -------

    __find_individual_matching_ideal(col_name)
        Finds the matching ideal function for a given train function.

    '''

    def __init__(self, train_df, ideal_df):
        '''
        DataAnalysis class constructor to initialize attributes train_df and ideal_df.
        ...

        Parameters
        ----------
        train_df: DataFrame
            a pandas DataFrame for train dataset.

        ideal_df : DataFrame
            a pandas DataFrame for ideal dataset.

        '''
        super().__init__()
        self.train_df = train_df
        self.ideal_df = ideal_df

    def find_matching_ideal_functions(self):
        '''
        Finds the best matching ideal functions out of all 50 ideal functions, for each training functions. 

        Return
        ----------
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
        '''
        Maps the test data provided to the four chosen best ideal functions based on criteria 2, in given assignment task.
        It checks for each x-y pair of values (test functions), whether or not they can be mapped.
        
        ...

        Return
        ----------
        Returns a dictionary with two keys "test_mapped_df" and 
        "test_unmapped_df" with both mapped and unmapped test data.
        
        Parameters
        ----------
        test_df : DataFrame
            Pandas DataFrame for Test DataSet.

        ideal_df : DataFrame
            Pandas DataFrame for Ideal DataSet.

        ideal_match: Dictionary
            This a custom dictionary that has the 4 best matching ideal functions for all 4 train functions.
            Expected format of "ideal_match" is exactly what is returned from "find_matching_ideal_functions" function. 
            An example of expected "ideal_match" parameter is as below:
            {
                'y1': ('y13', 100.0506255399994, 0.4999699999999976), 
                'y2': ('y31', 95.34986419200027, 0.49812999999999974), 
                'y3': ('y15', 101.28976004399982, 0.4975619999999985), 
                'y4': ('y10', 99.50240088299999, 0.49966569999999955)
            }
        '''


        # Creating blank pandas data frames with column definitions. These will be used to store mapped and unmapped test points.
        test_mapped_df = pd.DataFrame(columns = ['x', 'y', 'ideal_function', 'related_deviation'])
        test_unmapped_df = pd.DataFrame(columns = ['x', 'y'])

        # Looping through all Test DataFrame rows using iterrows function.
        # Since Test dataset isn't expected to be too large in size, hence iterrows is being used to simplify, for large dataset vectorization is recommended.

        for index, test_row in test_df.iterrows():
            # Unpacking x and y value from current loop Test row.
            test_x, test_y = test_row

            # These two vars will store the mapped ideal function and it's difference (related deviation) with test function.
            # In case there are multiple mapping ideal function with one test function, we will 
            # over-write this with the best ideal function mapped having least difference with test function.
            mapping_ideal_function = None
            mapping_ideal_function_difference = 0

            # Looping through all 4 ideal match that we found earlier and passed to this function.
            for train_col, matching in ideal_match.items():

                # Getting the ideal column name from 0th index of matching tuple.
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
                    
                    if(mapping_ideal_function == None or test_ideal_difference < mapping_ideal_function_difference):
                        # In case there are multiple mapping ideal function with one test function, we will 
                        # over-write this with the best ideal function having least difference.
                        mapping_ideal_function = ideal_col
                        mapping_ideal_function_difference = test_ideal_difference
            
            # Once loop of ideal functions is finished, we check if there was a mapping_ideal_function.
            if(mapping_ideal_function is None):
                # If not (None) we add the data in 'test_unmapped_df' DataFrame.
                test_unmapped_df.loc[len(test_unmapped_df), test_unmapped_df.columns] = test_x, test_y
            else:
                # Else (if found a map) we add the data in 'test_mapped_df' DataFrame along with 'mapping_ideal_function' as well as 'mapping_ideal_function_difference'.
                test_mapped_df.loc[len(test_mapped_df), test_mapped_df.columns] = test_x, test_y, mapping_ideal_function, mapping_ideal_function_difference
        
        return {'test_mapped_df': test_mapped_df, 'test_unmapped_df': test_unmapped_df}


    def __find_individual_matching_ideal(self, col_name):
        '''
        Finds the matching ideal function for a given train function by finding the error (using sum_of_deviation_squared) 
        and returns the best matched ideal function that has the least error (sum_of_deviation_squared).

        ...

        Parameters
        ----------
        col_name: NumPy Array
            Name of column for finding the best ideal function. Should be y1, y2, y3 or y4.
        '''
        train_col_data = self.train_df[col_name]
        error_list = []
        for ideal_col in self.ideal_df.columns[1:]:
            ideal_col_data = self.ideal_df[ideal_col]
            # Finding error amount by Sum of deviations squared (Least Squared) for each ideal function.
            error = self.sum_of_deviation_squared(train_col_data, ideal_col_data)

            # Since we're already looping, finding and storing maximum deviation between columns as it'll be required for Criteria 2 when working with Test functions.
            max_dev = self.max_deviation(train_col_data, ideal_col_data)

            # Appending the ideal column, it's error and maximum deviation in error list.
            error_list.append((ideal_col, error, max_dev))

        # Returning the first item of sorted list, this will return the best matching ideal function with minimum (least) error.
        # Returning item will be a Tuple with following 3 elements:
        #       1. Matching ideal function (Y column) name.
        #       2. Error value (based on criteria 1 / sum of squared deviations).
        #       3. Maximum deviation between train and matching ideal function. (This will be used while working with test data.)

        return self.sort_list(error_list)[0]
    