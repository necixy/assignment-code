# External imports
from bokeh.plotting import figure, output_file, save
from bokeh.layouts import row, column
from bokeh.models import Title, Range1d
import os

# Defining folder and file names constants.
FOLDER_NAME = 'visualization'
PLOTS_FILE_URL = FOLDER_NAME + '/visualization.html'
PLOT_WIDTH = 450
PLOT_HEIGHT = 450

class DataVisualization():
    '''
    The core class for dealing with all data visualization of the assignment project. It mainly uses Bokeh library to generate HTML charts.

    Public Methods
    ----------
    visualize(train_df, ideal_df, train_ideal_match, test_mapped_df)
        Visualizes the all 3 graphs, combines them and save all html files.

    Private Methods
    ----------
    __plot_train_data(train_df, y_col, line_color)
        Create figure/graph for the Train data plotting using line charts.

    __plot_matched_ideal_data(self, ideal_df, train_ideal_match, y_index, line_color)
        Create figure/graph for the Matched ideal functions data plotting using line charts.

    __plot_mapped_test_data(self, ideal_df, train_ideal_match, test_mapped_df, y_index, line_color)
        Create figure/graph for the mapped Test functions data plotting.

    '''

    def __init__(self):
        '''
        Constructor of class. Mainly creating the folder for visualization.
        '''
        try: 
            # Creating the folder for visualization.
            os.makedirs(FOLDER_NAME, exist_ok=True)
        except OSError:
            print('Error creating reports directory/folder for visualization.')

    def visualize(self, train_df, ideal_df, train_ideal_match, test_mapped_df):
        '''
        Visualizes the all 12 graphs (3 graphs for each y), combines them and save the html file.

        Parameters
        ----------
        train_df : DataFrame
            Pandas DataFrame for Train DataSet.

        ideal_df : DataFrame
            Pandas DataFrame for Ideal DataSet.
        
        test_df : DataFrame
            Pandas DataFrame for Test DataSet.

        train_ideal_match: Dictionary
            This a custom dictionary that has the 4 best matching ideal functions for all 4 train functions.
            Expected format of "train_ideal_match" is exactly what is returned from "find_matching_ideal_functions" function of DataAnalysis class. 
            An example of expected "train_ideal_match" parameter is as below:
            {
                'y1': ('y13', 100.0506255399994, 0.4999699999999976), 
                'y2': ('y31', 95.34986419200027, 0.49812999999999974), 
                'y3': ('y15', 101.28976004399982, 0.4975619999999985), 
                'y4': ('y10', 99.50240088299999, 0.49966569999999955)
            }
        
        test_mapped_df: DataFrame
            Pandas DataFrame for Mapped Test functions data.
        '''

        # Creating 3 plots i.e. train, ideal and test plots for Y1.
        train_plot_y1 = self.__plot_train_data(train_df, 'y1', 'red')
        ideal_plot_y1 = self.__plot_matched_ideal_data(ideal_df, train_ideal_match, 0, 'red')
        test_plot_y1 = self.__plot_mapped_test_data(ideal_df, train_ideal_match, test_mapped_df, 0, 'red')

        # Combine these 3 plots into a row layout.
        row_y1 = row(train_plot_y1, ideal_plot_y1, test_plot_y1)

        # Creating 3 plots i.e. train, ideal and test plots for Y2.
        train_plot_y2 = self.__plot_train_data(train_df, 'y2', 'green')
        ideal_plot_y2 = self.__plot_matched_ideal_data(ideal_df, train_ideal_match, 1, 'green')
        test_plot_y2 = self.__plot_mapped_test_data(ideal_df, train_ideal_match, test_mapped_df, 1, 'green')

        # Combine these 3 plots into a row layout.
        row_y2 = row(train_plot_y2, ideal_plot_y2, test_plot_y2)

        # Creating 3 plots i.e. train, ideal and test plots for Y3.
        train_plot_y3 = self.__plot_train_data(train_df, 'y3', 'blue')
        ideal_plot_y3 = self.__plot_matched_ideal_data(ideal_df, train_ideal_match, 2, 'blue')
        test_plot_y3 = self.__plot_mapped_test_data(ideal_df, train_ideal_match, test_mapped_df, 2, 'blue')

        # Combine these 3 plots into a row layout.
        row_y3 = row(train_plot_y3, ideal_plot_y3, test_plot_y3)

        # Creating 3 plots i.e. train, ideal and test plots for Y4.
        train_plot_y4 = self.__plot_train_data(train_df, 'y4', 'black')
        ideal_plot_y4 = self.__plot_matched_ideal_data(ideal_df, train_ideal_match, 3, 'black')
        test_plot_y4 = self.__plot_mapped_test_data(ideal_df, train_ideal_match, test_mapped_df, 3, 'black')

        # Combine these 3 plots into a row layout.
        row_y4 = row(train_plot_y4, ideal_plot_y4, test_plot_y4)

        # Combine all 4 row layouts into a column layout.
        combined_plots = column(row_y1, row_y2, row_y3, row_y4)
        # Save the combined column plots
        output_file(PLOTS_FILE_URL)
        save(combined_plots)

    def __plot_train_data(self, train_df, y_col, line_color):
        '''
        Create figure/graph for the Train data plotting using line charts.

        Parameters
        ----------
        train_df : DataFrame
            Pandas DataFrame for Train DataSet.
        
        y_col: String
            Y Column name. Values should be y1, y2, y3 or y4. This will define which y col needs to be plotted.
        
        line_color: String
            Color to be used for the plotting line.
        '''

        # Creating the figure / graph and setting up their title, x and y labels.
        graph = figure(title = f'Train data graph with X and Train {y_col.upper()}', plot_width = PLOT_WIDTH, plot_height = PLOT_HEIGHT)
        graph.xaxis.axis_label = 'Train X'
        graph.yaxis.axis_label = f'Train {y_col.upper()}'
        graph.y_range = Range1d(-50, 1000)

        # Plotting the train X and given train functions (either Y1, Y2, Y3 or Y4)
        graph.line(train_df.x, train_df[y_col], line_color=line_color,legend_label=f'Train {y_col.upper()}')

        # Returning the training graph object.
        return graph

    def __plot_matched_ideal_data(self, ideal_df, train_ideal_match, y_index, line_color):
        '''
        Create figure/graph for the Matched ideal functions data plotting using line charts.

        Parameters
        ----------
        ideal_df : DataFrame
            Pandas DataFrame for Ideal DataSet.
        
        train_ideal_match: Dictionary
            This a custom dictionary that has the 4 best matching ideal functions for all 4 train functions.
            Expected format of "train_ideal_match" is exactly what is returned from "find_matching_ideal_functions" function of DataAnalysis class. 
            An example of expected "train_ideal_match" parameter is as below:
            {
                'y1': ('y13', 100.0506255399994, 0.4999699999999976), 
                'y2': ('y31', 95.34986419200027, 0.49812999999999974), 
                'y3': ('y15', 101.28976004399982, 0.4975619999999985), 
                'y4': ('y10', 99.50240088299999, 0.49966569999999955)
            }
        
        y_index: int
            Index for best matched column. Values must be 0, 1, 2 or 3 (respecting to y1, y2, y3 and y4 best match).
        
        line_color: String
            Color to be used for the plotting line.
        '''

        # Using train_ideal_match, extracting the matched ideal y points, with help of List Comprehension.
        matched_y_points = [values[0] for values in train_ideal_match.values()]
        # Getting best match Y ideal functions at given index.
        matched_col = matched_y_points[y_index]

        # Creating the figure / graph and setting up their title, x and y labels.
        graph = figure(title = f'Ideal data graph with X & Ideal{matched_col.upper()} (best match to train Y{y_index+1}).', plot_width = PLOT_WIDTH, plot_height = PLOT_HEIGHT)
        graph.xaxis.axis_label = 'Ideal X'
        graph.yaxis.axis_label = f'Ideal {matched_col.upper()}'
        graph.y_range = Range1d(-50, 1000)

        # Plotting the ideal X and best matched ideal functions at given index.
        graph.line(ideal_df.x, ideal_df[matched_col], line_color=line_color,legend_label=f'Ideal {matched_col} - (Best match to Train y{y_index+1})')
        
        # Returning the ideal graph object.
        return graph

    def __plot_mapped_test_data(self, ideal_df, train_ideal_match, test_mapped_df, y_index, line_color):
        '''
        Create figure/graph for the mapped Test functions data plotting using line charts (for ideal) and scatter points (for test).

        Parameters
        ----------
        ideal_df : DataFrame
            Pandas DataFrame for Ideal DataSet.
        
        train_ideal_match: Dictionary
            This a custom dictionary that has the 4 best matching ideal functions for all 4 train functions.
            Expected format of "train_ideal_match" is exactly what is returned from "find_matching_ideal_functions" function of DataAnalysis class. 
            An example of expected "train_ideal_match" parameter is as below:
            {
                'y1': ('y13', 100.0506255399994, 0.4999699999999976), 
                'y2': ('y31', 95.34986419200027, 0.49812999999999974), 
                'y3': ('y15', 101.28976004399982, 0.4975619999999985), 
                'y4': ('y10', 99.50240088299999, 0.49966569999999955)
            }
        
        test_mapped_df: DataFrame
            Pandas DataFrame for Mapped Test functions data.
        
        y_index: int
            Index for best matched column. Values must be 0, 1, 2 or 3 (respecting to y1, y2, y3 and y4 best match).
        
        line_color: String
            Color to be used for the plotting line.
        '''
        # Using train_ideal_match, extracting the matched ideal y points, with help of List Comprehension.
        matched_y_points = [values[0] for values in train_ideal_match.values()]
        # Getting best match Y ideal functions at given index.
        matched_col = matched_y_points[y_index]

        # Filtering the mapped Test data rows from test_mapped_df DataFrame, based on matched y ideal functions.
        # We are filtering so we can plot them with different colors.
        test_points = test_mapped_df.query(f'ideal_function == "{matched_col}"')
        
        # Creating the figure / graph and setting up their title, x and y labels.
        graph = figure(title = f'Mapped test data to best matched ideal function {matched_col}', plot_width = PLOT_WIDTH, plot_height = PLOT_HEIGHT)
        graph.xaxis.axis_label = 'Ideal X'
        graph.yaxis.axis_label = f'Ideal {matched_col.upper()}'
        graph.y_range = Range1d(-50, 1000)


        # Plotting the given matched ideal function with line.
        graph.line(ideal_df.x, ideal_df[matched_col], line_color=line_color,legend_label=f'Ideal {matched_col} - (Best match to Train y{y_index+1})')
        # Plotting the mapped test data to the given matched ideal function with scatter on same color.
        graph.scatter(test_points.x, test_points.y, fill_color=line_color, line_color=line_color, radius=0.2, legend_label=f'Mapped test points to Ideal {matched_col}')


        # Returning the test graph object.
        return graph
