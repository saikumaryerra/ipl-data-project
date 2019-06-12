import matplotlib.pyplot as plt
import csv
import utilities

def matches_per_year(matches_file_path):
	with open(matches_file_path,'r') as matches_csv:
		matches_reader = csv.DictReader(matches_csv)
		x=utilities.count_of_elements_in_row('season',matches_reader)
	return x

def plot_matches_per_year(data):
	utilities.bar_graph_from_dictionary(data,'season','no\'of matches')
	plt.show()

def calculate_and_plot_matches_per_year(matches_file_path):
    result = matches_per_year(matches_file_path)
    plot_matches_per_year(result)

if __name__ == '__main__':
    calculate_and_plot_matches_per_year('./matches.csv')
