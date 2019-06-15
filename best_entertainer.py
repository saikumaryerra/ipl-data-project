import csv
import matplotlib.pyplot as plt
import utilities


def best_entertainer(matches_file_path, deliveries_file_path):
    with open(matches_file_path) as matches_csv:
        matches_reader = csv.DictReader(matches_csv)
        all_teams = set()
        matches_team = {}
        for match in matches_reader:
            all_teams.add(match['team1'])
            all_teams.add(match['team2'])
            if match['team1'] not in matches_team:
                matches_team[match['team1']] = 1
            else:
                matches_team[match['team1']] += 1
            if match['team2'] not in matches_team:
                matches_team[match['team2']] = 1
            else:
                matches_team[match['team2']] += 1
    all_teams = list(all_teams)
    all_teams = sorted(all_teams)
    average_score = {}
    boundaries = {}
    sum_of_scores = {}
    for team in all_teams:
        boundaries[team] = 0
        sum_of_scores[team] = 0
    # print(boundaries)
    with open(deliveries_file_path) as deliveries_csv:
        deliveries_reader = csv.DictReader(deliveries_csv)
        for delivery in deliveries_reader:
            if int(delivery['batsman_runs']) > 3:
                boundaries[delivery['batting_team']] += 1
            sum_of_scores[delivery['batting_team']
                          ] += int(delivery['total_runs'])

    short_team_names = utilities.team_short_names(all_teams)
    boundaries_short_name = {}
    entertainment = [0]*len(short_team_names)
    for i in range(len(short_team_names)):
        average_score[short_team_names[i]] = round(
            sum_of_scores[all_teams[i]]/matches_team[all_teams[i]])
        boundaries_short_name[short_team_names[i]] = boundaries[all_teams[i]]
        entertainment[i] = (boundaries[all_teams[i]]*6) + \
            (average_score[short_team_names[i]]*4)
    top_entertaining_pct = max(entertainment)
    top_entertainer_index = entertainment.index(top_entertaining_pct)
    top_entertainer = all_teams[top_entertainer_index]
    return entertainment, average_score, boundaries_short_name, short_team_names, top_entertainer

def best_entertainer_from_database(table_name='deliveries'):
    con,cur=utilities.database_connect()
    cur.execute('''select batting_team,(sum(total_runs)/count(distinct match_id)),
                sum (case when total_runs>3 then 1 else 0 end),sum(total_runs)/count(distinct match_id)*4+sum (case when total_runs>3 then 1 else 0 end)*6 as entertainment
                from '''+table_name+'''
                group by batting_team
                order by entertainment desc;''')
    rows=cur.fetchall()
    con.commit()
    con.close()
    entertainment_pct=[]
    average_score={}
    boundaries_short_name={}
    short_team_names=[]
    for team,avg_score,boundaries,entertainment in rows:
        entertainment_pct.append(entertainment)
        k=utilities.short_name(team)
        short_team_names.append(k)
        average_score[k]=avg_score
        boundaries_short_name[k]=boundaries
    top_entertainer=rows[0][0]
    plot_best_entertainer(entertainment_pct, average_score, boundaries_short_name, short_team_names, top_entertainer)
    print(entertainment_pct,average_score,boundaries_short_name,short_team_names,top_entertainer)
    return entertainment_pct,average_score,boundaries_short_name,short_team_names,top_entertainer

def plot_best_entertainer(entertainment, average_score, boundaries_short_name, short_team_names, top_entertainer):
    # plotting
    plt.suptitle(top_entertainer+" is best entertaining team",fontweight="bold")
    plt.subplot2grid((2,2),(0,0),rowspan=2)
    plt.pie(entertainment, autopct='%1.1f%%', labels=short_team_names)
    plt.subplot2grid((2,2),(0,1))
    utilities.bar_graph_from_dictionary(average_score, 'team', 'average score')
    plt.subplot2grid((2,2),(1,1))
    utilities.bar_graph_from_dictionary(boundaries_short_name, 'team', 'boundaries')
    plt.show()

def calculate_and_plot_best_entertainer(matches_file_path, deliveries_file_path):
    result_1,result_2,result_3,result_4,result_5= best_entertainer(matches_file_path, deliveries_file_path)
    plot_best_entertainer(result_1,result_2,result_3,result_4,result_5)

if __name__ == '__main__':
    # calculate_and_plot_best_entertainer('./ipl/matches.csv','./ipl/deliveries.csv')
    best_entertainer_from_database('test_deliveries')