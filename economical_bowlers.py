import matplotlib.pyplot as plt
import csv
import utilities

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
    for i in range(len(runs)):
        economy[i]=(runs[i]/balls[i])*6
    
    bowlers_5=['']*5
    economy_sorted = sorted(economy)
    for i in range(5):
        k=economy.index(economy_sorted[i])
        bowlers_5[i]=bowlers[k]

    return bowlers_5,economy_sorted[:5]

def plot_economical_bowlers(data_1,data_2):
    plt.bar(data_1,data_2)
    plt.show()

def calculate_and_plot_economical_bowlers(matches_file_path, deliveries_file_path):
    result_1,result_2 = economical_bowlers(matches_file_path, deliveries_file_path)
    plot_economical_bowlers(result_1,result_2)

if __name__ == '__main__':
    calculate_and_plot_economical_bowlers('./matches.csv','./deliveries.csv')