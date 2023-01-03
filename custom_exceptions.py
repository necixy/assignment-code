class DataSetNotFoundException(Exception):
    '''
    Should be raised if any of DataSet not found.
    '''
    def __init__(self, message):
        '''
        User defined exception DataSetNotFoundException constructor.

        Parameters
        ----------
        message : str
            Error message given at time of raising the exception.

        '''
        self.message = str(message) + ' Please check that there are all 3 files "train.csv", "ideal.csv" and "test.csv" inside the "datasets" folder inside the project root directory."'
        super().__init__(self.message)

class InvalidDataFormatException(Exception):
    '''
    Should be raised if any DataSet not having expected columns.
    '''
    def __init__(self, message):
        '''
        User defined exception InvalidDataFormatException constructor.

        Parameters
        ----------
        message : str
            Error message given at time of raising the exception.
            
        '''
        self.message = message + ' Make sure the input files (train.csv, ideal.csv and test.csv) has same structure and columns as defined in the assignment.'
        super().__init__(self.message)

class InitDatabaseException(Exception):
    '''
    Should be raised if there is problem while initializing or connecting to the database. 
    '''
    def __init__(self, message):
        '''
        User defined exception InitDatabaseException constructor.

        Parameters
        ----------
        message : str
            Error message given at time of raising the exception.
            
        '''
        self.message = message + ' Make sure you have required permissions to create SQLite database in project\'s directory.'
        super().__init__(self.message)