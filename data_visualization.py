# External imports
from bokeh.plotting import figure, output_file, save
from bokeh.layouts import row
from bokeh.models import Title
import os

# Defining folder and file names constants.
FOLDER_NAME = 'visualization'
TRAIN_FILE_URL = FOLDER_NAME + '/train_data.html'
IDEAL_FILE_URL = FOLDER_NAME + '/ideal_data_matched.html'
TEST_FILE_URL = FOLDER_NAME + '/test_data_mapped.html'
COMBINED_PLOTS_FILE_URL = FOLDER_NAME + '/combined_visualization.html'

class DataVisualization():
    '''
    The core class for dealing with all data visualization of the assignment project. It mainly uses Bokeh library to generate HTML charts.

    Public Methods
    ----------
    visualize(train_df, ideal_df, train_ideal_match, test_mapped_df)
        Visualizes the all 3 graphs, combines them and save all html files.

    Private Methods
    ----------
    __plot_train_data(train_df)
        Create figure/graph for the Train data plotting using line charts.

    __plot_matched_ideal_data(self, ideal_df, train_ideal_match)
        Create figure/graph for the Matched ideal functions data plotting using line charts.

    __plot_mapped_test_data(self, ideal_df, train_ideal_match, test_mapped_df)
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
        Visualizes the all 3 graphs, combines them and save all html files.

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

        # Creating 3 plots i.e. train, ideal and test plots.
        train_plot = self.__plot_train_data(train_df)
        ideal_plot = self.__plot_matched_ideal_data(ideal_df, train_ideal_match)
        test_plot = self.__plot_mapped_test_data(ideal_df, train_ideal_match, test_mapped_df)

        # Combine these 3 plots into a row layout.
        combined_plots = row(train_plot, ideal_plot, test_plot)

        # Save the combined plots
        output_file(COMBINED_PLOTS_FILE_URL)
        save(combined_plots)

        # Saving the training graph.
        output_file(TRAIN_FILE_URL)
        save(train_plot)

        # Saving the ideal graph.
        output_file(IDEAL_FILE_URL)
        save(ideal_plot)

        # Saving the ideal graph.
        output_file(TEST_FILE_URL)
        save(test_plot)


    def __plot_train_data(self, train_df):
        '''
        Create figure/graph for the Train data plotting using line charts.

        Parameters
        ----------
        train_df : DataFrame
            Pandas DataFrame for Train DataSet.
        '''

        # Creating the figure / graph and setting up their title, x and y labels.
        graph = figure(title = 'Train data graph with X and Y1, Y2, Y3 and Y4')
        graph.xaxis.axis_label = 'Train X'
        graph.yaxis.axis_label = 'Train Y (Y1, Y2, Y3 and Y4)'

        # Plotting the train X and four train functions Y1, Y2, Y3 and Y4
        graph.line(train_df.x, train_df.y1, line_color='red',legend_label='Train Y1')
        graph.line(train_df.x, train_df.y2, line_color='green',legend_label='Train Y2')
        graph.line(train_df.x, train_df.y3, line_color='blue',legend_label='Train Y3')
        graph.line(train_df.x, train_df.y4, line_color='black',legend_label='Train Y4')

        # Returning the training graph object.
        return graph

    def __plot_matched_ideal_data(self, ideal_df, train_ideal_match):
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
        '''

        # Using train_ideal_match, extracting the matched ideal y points, with help of List Comprehension.
        matched_y_points = [values[0] for values in train_ideal_match.values()]
        # Unpacking four matched Y ideal functions in variables.
        match_1, match_2, match_3, match_4 = matched_y_points

        # Creating the figure / graph and setting up their title, x and y labels.
        graph = figure(title = 'Ideal data graph with X and 4 best matched ideal functions.')
        graph.xaxis.axis_label = 'Ideal X'
        graph.yaxis.axis_label = f'Ideal Y ({matched_y_points})'
        # Adding extra title for graph description.
        graph.add_layout(Title(text='Since this graph of matched 4 ideal functions is almost exactly similar \nto the train graph, we can see that we found the best match.', align='center'), 'below')

        # Plotting the ideal X and four best matched ideal functions functions match_1, match_2, match_3, match_4.
        graph.line(ideal_df.x, ideal_df[match_1], line_color='red',legend_label=f'Ideal {match_1} - (Best match to Train y1)')
        graph.line(ideal_df.x, ideal_df[match_2], line_color='green',legend_label=f'Ideal {match_2} - (Best match to Train y2)')
        graph.line(ideal_df.x, ideal_df[match_3], line_color='blue',legend_label=f'Ideal {match_3} - (Best match to Train y3)')
        graph.line(ideal_df.x, ideal_df[match_4], line_color='black',legend_label=f'Ideal {match_4} - (Best match to Train y4)')

        # Returning the ideal graph object.
        return graph

    def __plot_mapped_test_data(self, ideal_df, train_ideal_match, test_mapped_df):
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
        '''
        # Using train_ideal_match, extracting the matched ideal y points, with help of List Comprehension.
        matched_y_points = [values[0] for values in train_ideal_match.values()]
        # Unpacking four matched Y ideal functions in variables.
        match_1, match_2, match_3, match_4 = matched_y_points

        # Filtering the mapped Test data rows from test_mapped_df DataFrame, based on matched y ideal functions.
        # We are filtering so we can plot them with different colors.
        test_points_1 = test_mapped_df.query(f'ideal_function == "{match_1}"')
        test_points_2 = test_mapped_df.query(f'ideal_function == "{match_2}"')
        test_points_3 = test_mapped_df.query(f'ideal_function == "{match_3}"')
        test_points_4 = test_mapped_df.query(f'ideal_function == "{match_4}"')
        
        # Creating the figure / graph and setting up their title, x and y labels.
        graph = figure(title = 'Mapped test data to 4 best matched ideal functions')
        graph.xaxis.axis_label = 'Ideal X'
        graph.yaxis.axis_label = f'Ideal Y ({matched_y_points})'
        # Adding extra title for graph description.
        graph.add_layout(Title(text='Since the scatter points of mapped test points (dots) \nare perfectly matching the 4 matched ideal \nfunctions, we can see that we mapped the test points correctly.', align='center'), 'below')


        # Plotting the first matched ideal function (match_1) with line.
        graph.line(ideal_df.x, ideal_df[match_1], line_color='red',legend_label=f'Ideal {match_1} - (Best match to Train y1)')
        # Plotting the mapped test data to the first matched ideal function (match_1) with scatter on same color.
        graph.scatter(test_points_1.x, test_points_1.y, fill_color='red', line_color='red', radius=0.2, legend_label=f'Mapped test points to Ideal {match_1}')


        # Plotting the second matched ideal function (match_2) with line.
        graph.line(ideal_df.x, ideal_df[match_2], line_color='green',legend_label=f'Ideal {match_2} - (Best match to Train y2)')
        # Plotting the mapped test data to the second matched ideal function (match_2) with scatter on same color.
        graph.scatter(test_points_2.x, test_points_2.y, fill_color='green', line_color='green', radius=0.2, legend_label=f'Mapped test points to Ideal {match_2}')


        # Plotting the third matched ideal function (match_3) with line.
        graph.line(ideal_df.x, ideal_df[match_3], line_color='blue',legend_label=f'Ideal {match_3} - (Best match to Train y3)')
        # Plotting the mapped test data to the third matched ideal function (match_3) with scatter on same color.
        graph.scatter(test_points_3.x, test_points_3.y, fill_color='blue', line_color='blue', radius=0.2, legend_label=f'Mapped test points to Ideal {match_3}')


        # Plotting the fourth matched ideal function (match_4) with line.
        graph.line(ideal_df.x, ideal_df[match_4], line_color='black',legend_label=f'Ideal {match_4} - (Best match to Train y4)')
        # Plotting the mapped test data to the fourth matched ideal function (match_4) with scatter on same color.
        graph.scatter(test_points_4.x, test_points_4.y, fill_color='black', line_color='black', radius=0.2, legend_label=f'Mapped test points to Ideal {match_4}')

        # Returning the test graph object.
        return graph
