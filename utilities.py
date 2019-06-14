import matplotlib.pyplot as plt
import psycopg2 as pg
import random
import utilities

def team_short_names(teams_set):
	team_short=[]
	for i in teams_set:
		letters=[letter[0] for letter in i.split()]
		s=''
		for j in letters:
			s+=j
		team_short.append(s)
	return team_short

def sort_dict(dic):
    output = {}
    for key in sorted(dic):
        output[key] = dic[key]
    return output


def count_of_elements_in_row(x, reader_name):
    output = {}
    for matches in reader_name:
        if matches[x] in output:
            output[matches[x]] = output[matches[x]]+1
        else:
            output[matches[x]] = 1
    y = sort_dict(output)
    return y
def bar_graph_from_dictionary(x,x_label='',y_label=''):
    plt.bar(x.keys(),x.values())
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.show()

def stacked_bar_graph_from_nested_dictionary(x):
    lst_temp=[0]*len(x)
    keys_in_nested_dictionary=list(x[list(x)[0]])
    for team in keys_in_nested_dictionary:
        color_1=random.randint(1,9)*0.1
        color_2=random.randint(1,9)*0.1
        color_3=random.randint(1,9)*0.1
        lst=[]
        for season in x:
            lst.append(x[season][team])
        plt.bar(x.keys(),lst,bottom=lst_temp,color=(color_1,color_2,color_3,1))
        for i in range(len(lst)):
            lst_temp[i]=lst_temp[i]+lst[i]
    
    teams_in_short=utilities.team_short_names(keys_in_nested_dictionary)
    plt.legend(teams_in_short,ncol=5)
    plt.show()

def database_connect():
    con = pg.connect(database="ipl", user="postgres", password="test123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    return con,cur