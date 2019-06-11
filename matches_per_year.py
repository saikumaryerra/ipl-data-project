import matplotlib.pyplot as plt
import csv
# from fun_used import *
import utilities

with open('matches.csv','r') as matches_csv:
	matches_reader = csv.DictReader(matches_csv)
	# x,y=data_count('season',matches_reader)
	# plt.bar(x,y)
	# plt.bar(data_count('season',matches_reader).keys(),data_count('season',matches_reader).values())

	x=utilities.data_count('season',matches_reader)
	plt.bar(x.keys(),x.values())
	plt.show()



