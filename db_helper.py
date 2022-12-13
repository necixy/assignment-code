# External imports
import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float

# Internal imports
from datasets import DataSets
from custom_exceptions import *

TRAIN_TBL_NAME = 'train'
IDEAL_TBL_NAME = 'ideal'

class DBHelper():

    
    # Initializing
    def __init__(self):
        
        # Setting up connection.
        self.engine = create_engine("sqlite:///sqlite_database.db")
        self.connection = self.engine.connect()
        self.meta = MetaData()

        # Defining train table schema
        self.tbl_train = Table(
                TRAIN_TBL_NAME, self.meta, 
                Column('id',Integer, primary_key = True), 
                Column('x', Float), 
                Column('y1', Float), 
                Column('y2', Float), 
                Column('y3', Float), 
                Column('y4', Float)
                )
        
        # Defining ideal table schema
        self.tbl_ideal = Table(
                IDEAL_TBL_NAME, self.meta, 
                Column('id',Integer, primary_key = True), 
                Column('x', Float), 
                Column('y1', Float), Column('y2', Float), Column('y3', Float), Column('y4', Float), 
                Column('y5', Float), Column('y6', Float), Column('y7', Float), Column('y8', Float), 
                Column('y9', Float), Column('y10', Float), Column('y11', Float), Column('y12', Float), 
                Column('y13', Float), Column('y14', Float), Column('y15', Float), Column('y16', Float), 
                Column('y17', Float), Column('y18', Float), Column('y19', Float), Column('y20', Float), 
                Column('y21', Float), Column('y22', Float), Column('y23', Float), Column('y24', Float), 
                Column('y25', Float), Column('y26', Float), Column('y27', Float), Column('y28', Float), 
                Column('y29', Float), Column('y30', Float), Column('y31', Float), Column('y32', Float), 
                Column('y33', Float), Column('y34', Float), Column('y35', Float), Column('y36', Float), 
                Column('y37', Float), Column('y38', Float), Column('y39', Float), Column('y40', Float), 
                Column('y41', Float), Column('y42', Float), Column('y43', Float), Column('y44', Float), 
                Column('y45', Float), Column('y46', Float), Column('y47', Float), Column('y48', Float), 
                Column('y49', Float), Column('y50', Float),
                )
        self.__copy_dataset_to_db()

    def __load_dataset_from_csv(self):
        try:
            ds = DataSets()
        except DataSetNotFoundException as ex:
            print('Error loading datasets.', ex)
        except InvalidDataFormatException as ex:
            print(ex)
        else: 
            return ds

    def __copy_dataset_to_db(self):
        ''' Reads the training and ideal datasets from CSV files and copy into SQLite database file. '''

        copy_success = False
        try:
            ds = self.__load_dataset_from_csv()
            if(ds is not None):
                # Once the datasets are loaded, storing them into SQLite database.
                # Using if_exists="replace" to avoid failure while overwriting.
                ds.train.to_sql(TRAIN_TBL_NAME, self.connection, if_exists="replace")
                ds.ideal.to_sql(IDEAL_TBL_NAME, self.connection, if_exists="replace")

                copy_success = True
        except Exception as ex:
            print('Error copying dataset to table.', ex)
        
        return copy_success
    
    # Destructor
    def __del__(self):
        # Closing connection and disposing engine in case of destructor called.
        self.connection.close()
        self.engine.dispose()

