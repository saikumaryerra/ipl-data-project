import utilities
# import matches_per_year
# import matches_won_per_year
# import extra_runs_2016
# import economical_bowlers
# import best_entertainer

def matches_per_year(table_name):
	con,cur=utilities.database_connect()
	cur.execute('select season,count(*) from '+table_name+' group by season')
	rows=cur.fetchall()
	data={}
	for season,matches in rows:
		data[season]=matches
	con.commit()  
	con.close()
	return data

def matches_won_per_year(table_name):
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
    return data

def extra_runs_2016(table_name_1,table_name_2):
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
    return data

def economical_bowlers(table_name_1,table_name_2):
    con,cur=utilities.database_connect()
    cur.execute('''select bowler,
                    cast(sum(total_runs)as float)*6/sum(case when ball <7 then 1 else 0 end) as economy
                    from '''+table_name_2+'''
                	inner join '''+table_name_1+''' on '''+table_name_1+'''.id='''+table_name_2+'''.match_id where season='2015'
                    group by bowler
                    order by economy
                    limit 5''')
    rows=cur.fetchall()
    con.commit()
    con.close()
    data={}
    for bowler,economy in rows:
        data[bowler]=economy
    return data

def best_entertainer(table_name):
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
    print(entertainment_pct,average_score,boundaries_short_name,short_team_names,top_entertainer)
    return entertainment_pct,average_score,boundaries_short_name,short_team_names,top_entertainer

def best_entertainer_for_season(table_name_1,table_name_2,season):
    con,cur=utilities.database_connect()
    cur.execute('''select batting_team,(sum(total_runs)/count(distinct match_id)),
                sum (case when total_runs>3 then 1 else 0 end),sum(total_runs)/count(distinct match_id)*4+sum (case when total_runs>3 then 1 else 0 end)*6 as entertainment
                from '''+table_name_2+''' inner join '''+table_name_1+''' on '''+table_name_1+'''.id='''+table_name_2+'''.match_id
                where season= \''''+season+'''\' group by batting_team
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
    print(entertainment_pct,average_score,boundaries_short_name,short_team_names,top_entertainer,season)
    return entertainment_pct,average_score,boundaries_short_name,short_team_names,top_entertainer,season