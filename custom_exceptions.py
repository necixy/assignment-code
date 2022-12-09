class DataSetNotFoundException(Exception):
    def __init__(self, message):
        self.message = str(message) + ' Please check that there are all 3 files "train.csv", "ideal.csv" and "test.csv" inside the "datasets folder inside the project root directory."'
        super().__init__(self.message)

class InvalidDataFormatException(Exception):
    def __init__(self, message):
        self.message = message + ' Make sure the input files (train.csv, ideal.csv and test.csv) has same structure and columns as defined in the assignment.'
        super().__init__(self.message)
