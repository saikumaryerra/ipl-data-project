import matplotlib.pyplot as plt
import csv
import random
from fun_used import *

with open('matches.csv', 'r') as matches_csv:
    matches_reader = csv.DictReader(matches_csv)
    # teams_set = set()
    # seasons_set = set()
    # for i in matches_reader:
    #     teams_set.add(i['team1'])
    #     teams_set.add(i['team2'])
    #     seasons_set.add(i['season'])
    # print(teams_set)
    matches_won_per_season = {}
    # for i in matches_reader:
    #     if i['winner'] == '':
    #         continue
    #     elif i['winner'] in matches_won_per_season:
    #         if i['season'] in matches_won_per_season[i['winner']]:
    #             matches_won_per_season[i['winner']][i['season']] = matches_won_per_season[i['winner']][i['season']]+1
    #         else:
    #             matches_won_per_season[i['winner']][i['season']] = 1
    #     else:
    #         matches_won_per_season[i['winner']] = {i['season']: 1}
    teams_set = set()
    for i in matches_reader:
        teams_set.add(i['team1'])
        if i['season'] in matches_won_per_season:
            k=matches_won_per_season[i['season']]
            if i['winner'] in matches_won_per_season[i['season']]:
                k[i['winner']]=k[i['winner']]+1
            else:
                k[i['winner']]=1
        else:
            matches_won_per_season[i['season']]={i['winner']:1}
    
    #sorting the dictionary
    matches_won_per_season=sort_dict(matches_won_per_season)
    teams_set=list(teams_set)
    teams_set=sorted(teams_set)
    # print(teams_set)

    for i in matches_won_per_season:
        for j in teams_set:
            if j not in matches_won_per_season[i]:
                matches_won_per_season[i][j]=0
    for i in matches_won_per_season:
        matches_won_per_season[i]=sort_dict(matches_won_per_season[i])
    
    #for ploy
    lst_temp=[0]*len(matches_won_per_season)
    for i in teams_set:
        q=random.randint(1,9)*0.1
        w=random.randint(1,9)*0.1
        e=random.randint(1,9)*0.1
        lst=[]
        for j in matches_won_per_season.keys():
            lst.append(matches_won_per_season[j][i])
        plt.bar(matches_won_per_season.keys(),lst,bottom=lst_temp,color=(q,w,e,1))
        for i in range(len(lst)):
            lst_temp[i]=lst_temp[i]+lst[i]
    
    teams_short_names=[]
    for i in teams_set:
        letters=[letter[0] for letter in i.split()]
        s=''
        for i in letters:
            s+=i
        teams_short_names.append(s)


    plt.legend(teams_short_names,ncol=5)
    plt.show()