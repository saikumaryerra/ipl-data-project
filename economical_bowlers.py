import matplotlib.pyplot as plt
import csv
from fun_used import *
with open('matches.csv') as matches_csv:
    matches_reader = csv.DictReader(matches_csv)
    match_id_2015 = []
    for i in matches_reader:
        if i['season'] == '2015':
            match_id_2015.append(i['id'])

# print(match_id_2015)
with open('deliveries.csv') as deliveries_csv:
    deliveries_reader = csv.DictReader(deliveries_csv)
    bowlers = []
    runs = []
    balls = []
    for i in deliveries_reader:
        if i['match_id'] in match_id_2015:
            if i['bowler'] not in bowlers:
                bowlers.append(i['bowler'])
                runs.append(int(i['total_runs']))
                balls.append(1)
            else:
                k = bowlers.index(i['bowler'])
                runs[k] += int(i['total_runs'])
                if int(i['ball']) < 7:
                    balls[k] += 1
    economy = [0]*len(runs)
    for i in range(len(runs)):
        economy[i]=(runs[i]/balls[i])*6
    
    bowlers_5=['']*5
    # economy_10=[0]*10
    economy_sorted = sorted(economy)
    for i in range(5):
        k=economy.index(economy_sorted[i])
        bowlers_5[i]=bowlers[k]
    plt.bar(bowlers_5,economy_sorted[:5])
    plt.show()