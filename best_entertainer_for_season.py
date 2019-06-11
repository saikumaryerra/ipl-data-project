import csv
import matplotlib.pyplot as plt
import utilities

current_season='2017'
with open('matches.csv') as matches_csv:
    matches_reader = csv.DictReader(matches_csv)
    match_id_current_season = set()
    teams_current_season = set()
    matches_team={}
    for match in matches_reader:
        if match['season'] == current_season:
            match_id_current_season.add(match['id'])
            teams_current_season.add(match['team1'])
            teams_current_season.add(match['team2'])
            if match['team1'] not in matches_team:
                matches_team[match['team1']]=1
            else:
                matches_team[match['team1']]+=1
            if match['team2'] not in matches_team:
                matches_team[match['team2']]=1
            else:
                matches_team[match['team2']]+=1
teams_current_season = list(teams_current_season)
teams_current_season = sorted(teams_current_season)
average_score={}
boundaries={}
sum_of_scores={}
for team in teams_current_season:
    boundaries[team]=0
    sum_of_scores[team]=0
# print(boundaries)
with open('deliveries.csv') as deliveries_csv:
    deliveries_reader = csv.DictReader(deliveries_csv)
    for delivery in deliveries_reader:
        if delivery['match_id'] in match_id_current_season:
            if int(delivery['batsman_runs'])>3:
                boundaries[delivery['batting_team']]+=1
            sum_of_scores[delivery['batting_team']]+=int(delivery['total_runs'])

short_team_names=utilities.team_short_names(teams_current_season)
boundaries_short_name={}
entertainment=[0]*len(short_team_names)
for i in range(len(short_team_names)):
    average_score[short_team_names[i]]=round(sum_of_scores[teams_current_season[i]]/matches_team[teams_current_season[i]])
    boundaries_short_name[short_team_names[i]]=boundaries[teams_current_season[i]]
    entertainment[i]=(boundaries[teams_current_season[i]]*7)+(average_score[short_team_names[i]]*3)

# print(entertainment)
# plotting
o=plt.figure(1)
plt.pie(entertainment,autopct='%1.1f%%',labels=short_team_names)
o.show()
m=plt.figure(2)
utilities.bar_graph_from_dictionary(average_score,'team','average score')
m.show()
n=plt.figure(3)
utilities.bar_graph_from_dictionary(boundaries_short_name,'team','boundaries')
n.show()
plt.show()