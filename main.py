# Internal imports
from datasets import DataSets
from db_helper import DBHelper
# from custom_exceptions import *


# def load_datasets():
#     try:
#         ds = DataSets()
#     except DataSetNotFoundException as ex:
#         print('Error loading datasets.', ex)
#     except InvalidDataFormatException as ex:
#         print(ex)
#     else: 
#         return ds

def main():

    # Load the datasets.
    # ds = load_datasets()

    # Proceed further only if we have successfully load the data. 
    # if(ds is None): return

    db_helper = DBHelper()
    
    print('Program proceeding further.')

if __name__ == '__main__':
    main()

