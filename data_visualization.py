# External imports
from bokeh.plotting import figure, output_file, save

class DataVisualization():

    def __plot_base_graph(self, title, x_axis_lbl, y_axis_lbl):
         # instantiating the figure object
        graph = figure(title = title)
        graph.xaxis.axis_label = x_axis_lbl
        graph.yaxis.axis_label = y_axis_lbl
        
        # graph.scatter(test_mapped_df.x, test_mapped_df.y, fill_color='orange', line_color='orange', fill_alpha=0.9,radius=0.2, legend_label='Mapped test X,Y')
        return graph
    
    def plot_train_data(self, train_df):
        graph_title = "Train data graph with X and Y1, Y2, Y3 and Y4"
        x_axis_lbl = 'Train X'
        y_axis_lbl = 'Train Y (Y1, Y2, Y3 and Y4)'

        graph = self.__plot_base_graph(graph_title, x_axis_lbl, y_axis_lbl)

        # plotting the line graph
        graph.line(train_df.x[::1], train_df.y1[::1], line_color='red',legend_label='Train Y1')
        graph.line(train_df.x[::1], train_df.y2[::1], line_color='green',legend_label='Train Y2')
        graph.line(train_df.x[::1], train_df.y3[::1], line_color='blue',legend_label='Train Y3')
        graph.line(train_df.x[::1], train_df.y4[::1], line_color='black',legend_label='Train Y4')

        # saving the graph
        output_file("train_data.html")
        save(graph)


    def plot_matched_ideal_data(self, ideal_df, train_ideal_match):
        matched_y_points = [values[0] for values in train_ideal_match.values()]
        match_1, match_2, match_3, match_4 = matched_y_points
        # print(matched_y_points)
        graph = figure(title = "Ideal data graph with X and best matched ideal functions")
        graph.xaxis.axis_label = 'Ideal X'
        graph.yaxis.axis_label = f'Ideal Y ({matched_y_points})'

        graph.line(ideal_df.x[::1], ideal_df[match_1][::1], line_color='red',legend_label=f'Ideal {match_1} - (Best match to Train y1)')
        graph.line(ideal_df.x[::1], ideal_df[match_2][::1], line_color='green',legend_label=f'Ideal {match_2} - (Best match to Train y2)')
        graph.line(ideal_df.x[::1], ideal_df[match_3][::1], line_color='blue',legend_label=f'Ideal {match_3} - (Best match to Train y3)')
        graph.line(ideal_df.x[::1], ideal_df[match_4][::1], line_color='black',legend_label=f'Ideal {match_4} - (Best match to Train y4)')

        # saving the graph
        output_file("matched_ideal_data.html")
        save(graph)

    # def plot_mapped_test_data(self, ideal_df, )
