# External imports
import unittest
import pandas as pd

# Internal imports
from csv_helper import CSVHelper
from db_helper import DBHelper
from custom_exceptions import *
from data_analysis import DataAnalysis
from data_visualization import DataVisualization


class UnitTestCSVHelper(unittest.TestCase):
    def test_csv_loading(self):
        load_success = False
        try:
            csv = CSVHelper()
        except DataSetNotFoundException as ex:
            print('Error loading CSVHelper.', ex)
        except InvalidDataFormatException as ex:
            print(ex)
        else:
            load_success = True

        self.assertTrue(load_success, 'CSV Loading Unit Testing Failed.')

class UnitTestDBHelper(unittest.TestCase):
    def test_db_operations(self):
        csv_loaded = False
        try:
            train_df = pd.read_csv('unittest_datasets/train_ut.csv')
            ideal_df = pd.read_csv('unittest_datasets/ideal_ut.csv')
            test_mapped_df = pd.read_csv('unittest_datasets/test_mapped_ut.csv')
            test_unmapped_df = pd.read_csv('unittest_datasets/test_unmapped_ut.csv')
        except FileNotFoundError as ex:
            print('Error loading unit test CSV files in Unit Test case.')
        else:
            csv_loaded = True
            
        self.assertTrue(csv_loaded, "CSV couldn't be loaded. Make sure you have datasets file (train_ut.csv, ideal_ut.csv, test_mapped_ut.csv, test_unmapped_df.csv) in unittest_datasets folder.")

        db_helper = None
        try:
            db_helper = DBHelper('unit_test_sqlite')
        except InitDatabaseException as ex:
            # Proceed further only if we have successfully initialized the SQLite database. 
            print(ex.message)
        self.assertIsNotNone(db_helper, "Database could not be connected.")
        
        copy_train_success = db_helper.copy_train_to_db(train_df)
        self.assertTrue(copy_train_success, "Train dataset couldn't be copied in unit_test_sqlite database.")

        copy_ideal_success = db_helper.copy_ideal_to_db(ideal_df)
        self.assertTrue(copy_ideal_success, "Ideal dataset couldn't be copied in unit_test_sqlite database.")

        store_test_mapped_success = db_helper.store_test_mapped_to_db(test_mapped_df)
        self.assertTrue(store_test_mapped_success, "Storing Test_Mapped failed in unit_test_sqlite database.")

        store_test_unmapped_success = db_helper.store_test_unmapped_to_db(test_unmapped_df)
        self.assertTrue(store_test_unmapped_success, "Storing Test_UnMapped failed in unit_test_sqlite database.")

class UnitTestDataAnalysis(unittest.TestCase):
    def test_data_analysis(self):
        csv_loaded = False
        try:
            train_df = pd.read_csv('unittest_datasets/train_ut.csv')
            ideal_df = pd.read_csv('unittest_datasets/ideal_ut.csv')
            test_df = pd.read_csv('unittest_datasets/test_ut.csv')
        except FileNotFoundError as ex:
            print('Error loading unit test CSV files in Unit Test case.')
        else:
            csv_loaded = True
            
        self.assertTrue(csv_loaded, "CSV couldn't be loaded. Make sure you have datasets file (train_ut.csv, ideal_ut.csv, test_ut.csv) in unittest_datasets folder.")

        data_analysis = DataAnalysis(train_df, ideal_df)
        train_ideal_match = data_analysis.find_matching_ideal_functions()
        test_map_result = data_analysis.map_test_to_ideal(test_df, ideal_df, train_ideal_match)
        test_mapped_df = test_map_result['test_mapped_df']
        test_unmapped_df = test_map_result['test_unmapped_df']

        expected_train_ideal_match = {'y1': ('y13', 33.15543517310224, 0.4999699999999976), 'y2': ('y31', 30.83450463458651, 0.49812999999999974), 'y3': ('y15', 34.679790780916896, 0.4975619999999985), 'y4': ('y10', 33.01178951893059, 0.49966569999999955)}
        self.assertDictEqual(train_ideal_match, expected_train_ideal_match, "Not finding expected train_ideal match.")

        expected_test_mapped_df_shape = (42, 4)
        self.assertEqual(test_mapped_df.shape, expected_test_mapped_df_shape, 'Not found test_mapped_df shape as expected.')

        expected_test_unmapped_df_shape = (58, 2)
        self.assertEqual(test_unmapped_df.shape, expected_test_unmapped_df_shape, 'Not found test_unmapped_df shape as expected.')

if __name__ == "__main__":
   unittest.main()