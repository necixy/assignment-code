# External imports
import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String
import pandas as pd
import os

# Internal imports
from custom_exceptions import InitDatabaseException

# Defining tables name and database URL constants.
TRAIN_TBL_NAME = 'train'
IDEAL_TBL_NAME = 'ideal'
TEST_MAPPED_TBL_NAME = 'test_mapped'
TEST_UNMAPPED_TBL_NAME = 'test_unmapped'

DB_FOLDER = "database"

class DBHelper():
    '''
    The core class for dealing with all database operations of the assignment project. 
    It mainly uses SQLAlchemy library to work with SQLite database.

    Public Methods
    ----------
    copy_train_to_db(train_df)
        Copies (stores) Train DataFrame provided, to the train table.

    copy_ideal_to_db(ideal_df)
        Copies (stores) Ideal DataFrame provided, to the train table.
    
    load_train_from_db()
        Loads and returns the train dataset by reading the SQLite database train table.

    load_ideal_from_db()
        Loads and returns the ideal dataset by reading the SQLite database ideal table.
    
    store_test_mapped_to_db(test_mapped_df)
        Copies (stores) Test (Mapped) DataFrame provided, to the test_mapped table.

    store_test_unmapped_to_db(test_unmapped_df)
        Copies (stores) Test (Un Mapped) DataFrame provided, to the test_unmapped table.        

    Private Methods
    ----------
    __copy_data_frame_to_db(self, table_name, table_data_frame)
        Stores the given data frame into the SQLite table with given table_name.
    '''

    def __init__(self, db_name):
        '''
        Constructor of DBHelper Class. Main tasks are:
        - Creates the database folder.
        - Connects to the database.
        - Defines all table schemas.

        Raises
        ----------
        InitDatabaseException
            If there is problem while initializing or connecting to the database.

        Parameter
        ----------
        db_name: str
            Name of SQLite database file.
        '''
        try:
            # Creating the folder for database.
            os.makedirs(DB_FOLDER, exist_ok=True)
        except OSError:
            print('Error creating reports directory/folder for database.')

        try:
            # Creating the folder for database.
            # os.makedirs(DB_FOLDER)

            # Setting up connection.
            self.engine = create_engine('sqlite:///' + DB_FOLDER + '/' + db_name + '.db')
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
            
            # Defining test_mapped table schema
            self.tbl_test_mapped = Table(
                    TEST_MAPPED_TBL_NAME, self.meta, 
                    Column('id',Integer, primary_key = True), 
                    Column('x', Float), 
                    Column('y', Float), 
                    Column('ideal_function', String), 
                    Column('related_deviation', Float)
                    )

            # Defining test_unmapped table schema
            self.tbl_test_mapped = Table(
                    TEST_UNMAPPED_TBL_NAME, self.meta, 
                    Column('id',Integer, primary_key = True), 
                    Column('x', Float), 
                    Column('y', Float)
                    )

        except Exception as ex:
            # Raising user-defined exception in case of SQLite database could not be initialized.
            raise InitDatabaseException('Could not initialize the database.')

    def copy_train_to_db(self, train_df):
        '''
        Copies (stores) Train DataFrame provided, to the train table.

        Parameters
        ----------
        train_df : DataFrame
            Pandas DataFrame for Train DataSet.
        '''
        return self.__copy_data_frame_to_db(TRAIN_TBL_NAME, train_df)
    
    def copy_ideal_to_db(self, ideal_df):
        '''
        Copies (stores) Ideal DataFrame provided, to the train table.

        Parameters
        ----------
        ideal_df : DataFrame
            Pandas DataFrame for Ideal DataSet.
        '''
        return self.__copy_data_frame_to_db(IDEAL_TBL_NAME, ideal_df)
    
    def __copy_data_frame_to_db(self, table_name, table_data_frame):
        '''
        Stores the given data frame into the SQLite table with given table_name.

        Parameters
        ----------
        table_name: str
            Name of the table to be stored in the database.
        
        table_data_frame: DataFrame
            Pandas DataFrame to be stored.

        Returns:
        ----------
        copy_success: Boolean
            Wether the copy operation was success.
        '''
        copy_success = False
        try:
            # Using if_exists='replace' to avoid failure while overwriting.
            table_data_frame.to_sql(table_name, self.connection, if_exists='replace')
            copy_success = True
        except Exception as ex:
            print('Error copying dataset to table. Error: ', ex)
        return copy_success

    def load_train_from_db(self):
        '''
        Loads and returns the train dataset by reading the SQLite database train table.
        '''
        return pd.read_sql(TRAIN_TBL_NAME, self.connection, index_col='index')
    
    def load_ideal_from_db(self):
        '''
        Loads and returns the ideal dataset by reading the SQLite database ideal table.
        '''
        return pd.read_sql(IDEAL_TBL_NAME, self.connection, index_col='index')
    
    def store_test_mapped_to_db(self, test_mapped_df):
        '''
        Copies (stores) Test (Mapped) DataFrame provided, to the test_mapped table.

        Parameters
        ----------
        test_mapped_df : DataFrame
            Pandas DataFrame for mapped Test DataSet.
        '''
        return self.__copy_data_frame_to_db(TEST_MAPPED_TBL_NAME, test_mapped_df)
    
    def store_test_unmapped_to_db(self, test_unmapped_df):
        '''
        Copies (stores) Test (Un Mapped) DataFrame provided, to the test_unmapped table.

        Parameters
        ----------
        test_unmapped_df : DataFrame
            Pandas DataFrame for unmapped Test DataSet.
        '''
        return self.__copy_data_frame_to_db(TEST_UNMAPPED_TBL_NAME, test_unmapped_df)

    # Destructor
    def __del__(self):
        '''
        Destructor of DBHelper Class. Main tasks are:
        - Closing the database connection.
        - Dispose the database engine.
        '''
        # Closing connection and disposing engine in case of destructor called.
        self.connection.close()
        self.engine.dispose()

