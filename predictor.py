import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import constants
key = constants.openAI_key

ipl_matches = pd.read_csv('./archive/matches.csv')
ipl_deliveries = pd.read_csv('./archive/deliveries.csv')
print (ipl_matches.shape)
ipl_deliveries.head()
ipl_matches.head()
const_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
              'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
              'Delhi Daredevils', 'Sunrisers Hyderabad']

ipl_deliveries = ipl_deliveries[(ipl_deliveries['batting_team'].isin(const_teams)) & (ipl_deliveries['bowling_team'].isin(const_teams))]

from seaborn import heatmap
ipl_del_hm = ipl_deliveries.pivot(columns=["over","total_runs","is_wicket"])
ipl_del_hm.info()
#heatmap(data=ipl_del_hm.corr(), annot=True)
#plt.show()