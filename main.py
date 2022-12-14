# Internal imports
from csv_helper import CSVHelper
from db_helper import DBHelper
from custom_exceptions import *
from data_analysis import DataAnalysis


def load_csv():
    try:
        csv = CSVHelper()
    except DataSetNotFoundException as ex:
        print('Error loading CSVHelper.', ex)
    except InvalidDataFormatException as ex:
        print(ex)
    else: 
        return csv

def main():

    # Load the CSV.
    print('Step 1: Loading the CSV files for train and ideal data.')
    csv = load_csv()
    # Proceed further only if we have successfully load the CSV data. 
    if(csv is None): 
        print('Error loading the CSV, hence stopping the program execution. Please fix the error mentioned above and try to run the program again.')
        return
    
    print('Step 2: Copying the loaded CSV data into SQLite Database. (Will overwrite tables if they exists).')
    db_helper = DBHelper()
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
    
    print(train_ideal_match)
    
    print('Program executed successfully')

if __name__ == '__main__':
    main()

