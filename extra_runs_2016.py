import matplotlib.pyplot as plt
import csv
from fun_used import *
with open('matches.csv') as matches_csv:
    matches_reader = csv.DictReader(matches_csv)
    match_id_2016 = []
    teams_2016 = set()
    for i in matches_reader:
        if i['season'] == '2016':
            match_id_2016.append(i['id'])
            teams_2016.add(i['team1'])
            teams_2016.add(i['team2'])

teams_2016 = list(teams_2016)
teams_2016 = sorted(teams_2016)
# print(match_id_2016)
# print(teams_2016)
extra_runs=[0]*len(teams_2016)
with open('deliveries.csv') as deliveries_csv:
    deliveries_reader = csv.DictReader(deliveries_csv)
    for i in deliveries_reader:
        bowling_team=i['bowling_team']
        if i['match_id'] in match_id_2016:
            k=teams_2016.index(bowling_team)
            extra_runs[k]=extra_runs[k]+int(i['extra_runs'])
# print(extra_runs)
teams_2016=team_short_names(teams_2016)
plt.bar(teams_2016,extra_runs)
plt.show()