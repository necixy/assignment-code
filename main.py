from datasets import DataSets
from db_helper import DBHelper
from custom_exceptions import *


def main():
    try:
        dbHelper = DBHelper()
        ds = DataSets()
    except DataSetNotFoundException as ex:
        print('Error loading datasets.', ex)
    except InvalidDataFormatException as ex:
        print(ex)
    else: 
        print(ds.train.shape)
        print(ds.ideal.shape)
        print(ds.test.shape)


if __name__ == '__main__':
    main()

