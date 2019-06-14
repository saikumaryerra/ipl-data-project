import matplotlib.pyplot as plt
import csv
import utilities

def extra_runs_2016(matches_file_path, deliveries_file_path):
    with open(matches_file_path) as matches_csv:
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
    with open(deliveries_file_path) as deliveries_csv:
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
    return extra_runs_with_short_name

def extra_runs_2016_from_database(table_name_1='matches',table_name_2='deliveries'):
    con,cur=utilities.database_connect()
    cur.execute('''select bowling_team,sum(extra_runs) 
                    from '''+table_name_2+'''
                    inner join '''+table_name_1+''' on '''+table_name_1+'''.id='''+table_name_2+'''.match_id 
                    where '''+table_name_1+'''.season='2016'
                    group by bowling_team''')
    rows=cur.fetchall()
    con.commit()
    con.close()
    data={}
    for team,extra_runs in rows:
        data[utilities.short_name(team)]=extra_runs
    plot_extra_runs_2016(data)
    return data

#plot
def plot_extra_runs_2016(data):
    utilities.bar_graph_from_dictionary(data,'teams','extra runs')
    plt.show()

def calculate_and_plot_extra_runs_2016(matches_file_path, deliveries_file_path):
    result = extra_runs_2016(matches_file_path, deliveries_file_path)
    plot_extra_runs_2016(result)

if __name__ == '__main__':
    # calculate_and_plot_extra_runs_2016('./ipl/matches.csv','./ipl/deliveries.csv')
    extra_runs_2016_from_database()