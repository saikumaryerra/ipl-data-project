import matplotlib.pyplot as plt
import csv
import random
import utilities

def matches_won_per_year(matches_file_path):
    with open(matches_file_path, 'r') as matches_csv:
        matches_reader = csv.DictReader(matches_csv)
        matches_won_per_season = {}
        teams_set = set()
        for match in matches_reader:
            teams_set.add(match['team1'])
            if match['season'] in matches_won_per_season:
                k=matches_won_per_season[match['season']]
                if match['winner'] in matches_won_per_season[match['season']]:
                    k[match['winner']]=k[match['winner']]+1
                else:
                    k[match['winner']]=1
            else:
                matches_won_per_season[match['season']]={match['winner']:1}
    #adding the teams who havent played in that season
    for season in matches_won_per_season:
        for team in teams_set:
            if team not in matches_won_per_season[season]:
                matches_won_per_season[season][team]=0
    #sorting the dictionary
    matches_won_per_season=utilities.sort_dict(matches_won_per_season)
    teams_set=list(teams_set)
    teams_set=sorted(teams_set)
    for season in matches_won_per_season:
        matches_won_per_season[season]=utilities.sort_dict(matches_won_per_season[season])
    return matches_won_per_season

def matches_won_per_year_from_database(table_name='matches'):
    con,cur=utilities.database_connect()
    cur.execute('select season,winner,count(winner) from '+table_name+' where winner is not null group by season,winner')
    rows1=cur.fetchall()
    cur.execute('select distinct(team1) from '+table_name+' order by team1')
    rows2=cur.fetchall()
    con.commit()
    con.close()
    data={}
    for season,team,wins in rows1:
        if season not in data:
            data[season]={}
            data[season][team]=wins
        else:
            data[season][team]=wins
    teams=[]
    for row in rows2:
        teams.append(row[0])
    #adding the teams who havent played in that season
    for season in data:
        for team in teams:
            if team not in data[season]:
                data[season][team]=0
    #sorting the dictionary
    data=utilities.sort_dict(data)
    for season in data:
        data[season]=utilities.sort_dict(data[season])
    plot_matches_won_per_year(data)
    return data
#for plot
def plot_matches_won_per_year(data):
    utilities.stacked_bar_graph_from_nested_dictionary(data)
    plt.show()

def calculate_and_plot_matches_won_per_year(matches_file_path):
    result = matches_won_per_year(matches_file_path)
    plot_matches_won_per_year(result)

if __name__ == '__main__':
    # calculate_and_plot_matches_won_per_year('./ipl/matches.csv')
    matches_won_per_year_from_database()