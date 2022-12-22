
# Assignment-code

Source code for MSCS Programming with Python assignment.

## Author

[Pratik Purohit](https://www.github.com/necixy) 

Matriculation Number: 9224625

## Cloning GitHub repository

To clone the GitHub repository, please use the following command.

```bash
  git clone https://github.com/necixy/assignment-code.git
```


## Installation

Install all packages required with

```bash
  cd assignment-code
  pip install -r packages.txt  
```
    
## Running / execution

To run the assignment code, you can use following command.

```bash
  python main.py  
```

On running main.py file you will see output like below:

```bash
  Step 1: Loading the CSV files for train and ideal data.
  Step 2: Copying the loaded CSV data into SQLite Database. (Will overwrite tables if they exists).
  Step 3: Loading the Pandas DataFrames (train and ideal) from SQLite database for the train and ideal tables.
  Step 4: Finding best ideal functions for each train function.
  Step 5: Mapping test data to matched ideal functions.
  Step 6: Storing the test data mapping result into SQLite database.
  Step 7: Data visualization (plotting)



  All steps are completed successfully. 



  Results: 

  -- Found 4 best matching ideal functions for given train functions:  ['y35', 'y40', 'y18', 'y48']
  -- Out of 100 test functions, 40 test functions (items) were mapped to above found 4 best matched ideal functions. And 60 items were unmapped.
  -- Visualization: You can now see the visualization (Bokeh HTML) reports inside the "visualization" folder. The file "combined_visualization.html" has all 3 maps plotting done. You can also see individual visualization in remaining 3 files.
  -- Database: You can also browse the SQLite database file "database\sqlite_database.db" for seeing the mapped test functions in "test_mapped" table. Also the unmapped test functions are stored in "test_unmapped" tables. In addition the given CSV datasets train and ideal are also stored in the database tables "train" and "ideal" respectively.

```

## Unit testing

To unit test the project, you can use following command.

```bash
  python unit_test.py  
```

You should be seeing following output:

```bash
  ----------------------------------------------------------------------
  Ran 3 tests in 0.178s

  OK
```
## FAQ

#### Q. Why am I seeing two datasets?

Answer: The main dataset files being used in program are in the "datasets" folder. 
The other datasets inside "unittest_datasets" is purely being used for the Unit Testing. Make sure you do not change the contents inside "unittest_datasets" folder.
If you want to run the program with different datasets, 
you can replace train.csv, ideal.csv and test.csv only inside the "datasets" folder.

#### Q. Why are there two SQLite database files inside "database" folder?

Answer: The one file with the name of "sqlite_database.db" is populated by real datasets inside "datasets" folder. The database file "unit_test_sqlite.db" is purely being used for Unit Testing and it's using unit testing datasets.

#### Q. How do I see visualization reports?
Answer: You can go inside "visualization" folder and you'll find four files. Which are:
- train_data.html
- ideal_data_matched.html
- test_data_mapped.html
- combined_visualization.html

It is recommended to see the combined_visualization.html to see all 3 graph plots in one web page.
But those 3 graphs are also saved in their stand alone files as well.


## Support

If you have any problem while running this program or would like to understand some of the program's aspect, please email pratik.purohit@iu-study.org.

