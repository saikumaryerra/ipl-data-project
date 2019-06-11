import matplotlib.pyplot as plt
import csv
import utilities
with open('matches.csv') as matches_csv:
    matches_reader = csv.DictReader(matches_csv)
    match_id_2016 = set()
    teams_2016 = set()
    for match in matches_reader:
        if match['season'] == '2016':
            match_id_2016.add(match['id'])
            teams_2016.add(match['team1'])
            teams_2016.add(match['team2'])

teams_2016 = list(teams_2016)
teams_2016 = sorted(teams_2016)
extra_runs={}
with open('deliveries.csv') as deliveries_csv:
    deliveries_reader = csv.DictReader(deliveries_csv)
    for delivery in deliveries_reader:
        bowling_team = delivery['bowling_team']
        if delivery['match_id'] in match_id_2016:
            if bowling_team not in extra_runs:
                extra_runs[bowling_team]=int(delivery['extra_runs'])
            else:
                extra_runs[bowling_team]=extra_runs[bowling_team]+int(delivery['extra_runs'])
extra_runs_with_short_name={}
short_name=utilities.team_short_names(extra_runs)
i=0
for team in extra_runs:
    extra_runs_with_short_name[short_name[i]]=extra_runs[team]
    i+=1
#plot
utilities.bar_graph_from_dictionary(extra_runs_with_short_name)
plt.show()