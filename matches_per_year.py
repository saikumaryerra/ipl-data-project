import matplotlib.pyplot as plt
import csv
import utilities

with open('matches.csv','r') as matches_csv:
	matches_reader = csv.DictReader(matches_csv)
	x=utilities.count_of_elements_in_row('season',matches_reader)
	utilities.bar_graph_from_dictionary(x)