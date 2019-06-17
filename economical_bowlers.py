import matplotlib.pyplot as plt
import csv
import utilities
import operator
import sqlFunctions as sqlF

def economical_bowlers(matches_file_path, deliveries_file_path):
    with open(matches_file_path) as matches_csv:
        matches_reader = csv.DictReader(matches_csv)
        match_id_2015 =set()
        for match in matches_reader:
            if match['season'] == '2015':
                match_id_2015.add(match['id'])

    with open(deliveries_file_path) as deliveries_csv:
        deliveries_reader = csv.DictReader(deliveries_csv)
        bowlers = []
        runs = []
        balls = []
        for delivery in deliveries_reader:
            if delivery['match_id'] in match_id_2015:
                if delivery['bowler'] not in bowlers:
                    bowlers.append(delivery['bowler'])
                    runs.append(int(delivery['total_runs']))
                    balls.append(1)
                else:
                    k = bowlers.index(delivery['bowler'])
                    runs[k] += int(delivery['total_runs'])
                    if int(delivery['ball']) < 7:
                        balls[k] += 1
    economy = [0]*len(runs)
    economical_bowlers={}
    for i in range(len(runs)):
        economy[i]=(runs[i]/balls[i])*6
        economical_bowlers[bowlers[i]]=economy[i]
    economical_bowlers=sorted(economical_bowlers.items(),key=operator.itemgetter(1))
    i=0
    data={}
    for bowler,economy in economical_bowlers:
        if i<5:
            data[bowler]=economy
            i+=1
        else:
            break
    return data

def plot_economical_bowlers(data):
	utilities.bar_graph_from_dictionary(data)
	plt.show()

def economical_bowlers_from_database(table_name_1='matches',table_name_2='deliveries'):
    return sqlF.economical_bowlers(table_name_1,table_name_2)

# def calculate_and_plot_economical_bowlers(matches_file_path, deliveries_file_path):
#     result = economical_bowlers(matches_file_path, deliveries_file_path)
#     plot_economical_bowlers(result)

if __name__ == '__main__':
    # calculate_and_plot_economical_bowlers('./ipl/matches.csv','./ipl/deliveries.csv')
    plot_economical_bowlers(economical_bowlers_from_database())