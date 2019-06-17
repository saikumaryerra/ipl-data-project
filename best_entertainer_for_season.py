import csv
import matplotlib.pyplot as plt
import utilities
import sqlFunctions as sqlF

def best_entertainer_for_season(matches_file_path, deliveries_file_path,current_season_name):
    current_season=current_season_name
    with open(matches_file_path) as matches_csv:
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
    with open(deliveries_file_path) as deliveries_csv:
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

    top_entertaining_pct=max(entertainment)
    top_entertainer_index=entertainment.index(top_entertaining_pct)
    top_entertainer=teams_current_season[top_entertainer_index]
    return entertainment, average_score, boundaries_short_name, short_team_names, top_entertainer,current_season

def best_entertainer_for_season_from_database(table_name_1='matches',table_name_2='deliveries',season='2015'):
    return sqlF.best_entertainer_for_season(table_name_1,table_name_2,season)

# plotting
def plot_best_entertainer_for_season(entertainment, average_score, boundaries_short_name, short_team_names, top_entertainer,season):
    plt.suptitle(top_entertainer+" is best entertaining team for "+season,fontweight="bold")
    plt.subplot2grid((2,2),(0,0),rowspan=2)
    plt.pie(entertainment, autopct='%1.1f%%', labels=short_team_names)
    plt.subplot2grid((2,2),(0,1))
    utilities.bar_graph_from_dictionary(average_score, 'team', 'average score')
    plt.subplot2grid((2,2),(1,1))
    utilities.bar_graph_from_dictionary(boundaries_short_name, 'team', 'boundaries')
    plt.show()

# def calculate_and_plot_best_entertainer_for_season(matches_file_path, deliveries_file_path,match_id_current_season):
#     result_1,result_2,result_3,result_4,result_5= best_entertainer_for_season(matches_file_path, deliveries_file_path,current_season)
#     plot_best_entertainer_for_season(result_1,result_2,result_3,result_4,result_5)

if __name__ == '__main__':
    # current_season=input("enter season \n")
    # calculate_and_plot_best_entertainer_for_season('./ipl/matches.csv','./ipl/deliveries.csv',current_season)
   result=best_entertainer_for_season_from_database('test_matches','test_deliveries','2016')
   plot_best_entertainer_for_season(*result)