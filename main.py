# Internal imports
from csv_helper import CSVHelper
from db_helper import DBHelper
from custom_exceptions import *
from data_analysis import DataAnalysis
from data_visualization import DataVisualization


def main():
    '''
    Main function that uses all other different classes to perform the tasks required in assignment description.
    It can be described with the Steps which are being printed and at the end, it shows the results. 
    '''
    # Load the CSV.
    print('Step 1: Loading the CSV files for train and ideal data.')
    try:
        csv = CSVHelper()
    except DataSetNotFoundException as ex:
        print('Error loading CSVHelper.', ex)
    except InvalidDataFormatException as ex:
        print(ex)
    # Proceed further only if we have successfully load the CSV data. 
    if(csv is None): 
        print('Error loading the CSV, hence stopping the program execution. Please fix the error mentioned above and try to run the program again.')
        return
    
    print('Step 2: Copying the loaded CSV data into SQLite Database. (Will overwrite tables if they exists).')
    try:
        db_helper = DBHelper('sqlite_database')
    except InitDatabaseException as ex:
        # Proceed further only if we have successfully initialized the SQLite database. 
        print(ex.message)
        return

    copy_train_success = db_helper.copy_train_to_db(csv.train)
    copy_ideal_success = db_helper.copy_ideal_to_db(csv.ideal)

    # Proceed further only if we have successfully copied the CSV data into SQLite DB. 
    if(copy_train_success is False or copy_ideal_success is False): 
        print('Error copying the CSV data into SQLite DB, hence stopping the program execution. Please fix the error mentioned above and try to run the program again.')
        return

    print('Step 3: Loading the Pandas DataFrames (train and ideal) from SQLite database for the train and ideal tables.')
    train_df = db_helper.load_train_from_db()
    ideal_df = db_helper.load_ideal_from_db()

    print('Step 4: Finding best ideal functions for each train function.')
    data_analysis = DataAnalysis(train_df, ideal_df)
    train_ideal_match = data_analysis.find_matching_ideal_functions()
    
    print('Step 5: Mapping test data to matched ideal functions.')
    test_map_result = data_analysis.map_test_to_ideal(csv.test, csv.ideal, train_ideal_match)
    test_mapped_df = test_map_result['test_mapped_df']
    test_unmapped_df = test_map_result['test_unmapped_df']

    print('Step 6: Storing the test data mapping result into SQLite database.')
    store_test_mapped_success = db_helper.store_test_mapped_to_db(test_mapped_df)
    store_test_unmapped_success = db_helper.store_test_unmapped_to_db(test_unmapped_df)

    # Proceed further only if we have successfully stored the test mapping data into SQLite DB. 
    if(store_test_mapped_success is False or store_test_unmapped_success is False): 
        print('Error storing the test mapped and unmapped data into SQLite DB, hence stopping the program execution. Please fix the error mentioned above and try to run the program again.')
        return

    print('Step 7: Data visualization (plotting)')
    data_visualization = DataVisualization()
    data_visualization.visualize(train_df, ideal_df, train_ideal_match, test_mapped_df)

    print('\n\n')
    print('All steps are completed successfully. ')

    # Printing outcome results.
    print('\n\n')
    print('Results: \n')
    matched_ideal_y = [match[0] for match in train_ideal_match.values()]
    print('-- Found 4 best matching ideal functions for given train functions: ', matched_ideal_y)
    print(f'-- Out of {csv.test.shape[0]} test functions, {test_mapped_df.shape[0]} test functions (items) were mapped to above found 4 best matched ideal functions. And {test_unmapped_df.shape[0]} items were unmapped.')
    print('-- Visualization: You can now see the visualization (Bokeh HTML) reports inside the "visualization" folder. The file "combined_visualization.html" has all 3 maps plotting done. You can also see individual visualization in remaining 3 files.')
    print('-- Database: You can also browse the SQLite database file "database\sqlite_database.db" for seeing the mapped test functions in "test_mapped" table. Also the unmapped test functions are stored in "test_unmapped" tables. In addition the given CSV datasets train and ideal are also stored in the database tables "train" and "ideal" respectively.')

    print('\n\n')

if __name__ == '__main__':
    main()

