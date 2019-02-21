# -*- coding: utf-8 -*-
"""
@author: CHARU

"""


import csv
import pandas as pd
from datetime import datetime

#loading scraped csv and preprocessing it to
#remove blank rows from it
with open('yelp.csv') as input, open('yelp_upd.csv.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):  #removing blank rows
             writer.writerow(row)
             
#read the processed CSV into Pandas
shak_df = pd.read_csv('/yelp_upd.csv.csv')
shak_df.sort_index(axis = 1, ascending = True)
#extract year and month from date to use later
shak_df['Date Published'] = pd.to_datetime(shak_df['Date Published'])
shak_df['Year'] = pd.DatetimeIndex(shak_df['Date Published']).year  
shak_df['Month'] = pd.DatetimeIndex(shak_df['Date Published']).month
#display final dataframe
display(shak_df)
#display columns
#shak_df.columns

#Printing General Restaurant information
rest_name = "SHAKE SHACK"
rest_addr = "Madison Square Park"
tot_ratings = shak_df['User Name'].count() #total number of ratings on YELP
mean_rating = round(shak_df['User Rating'].mean(),2) #overall mean rating from 2005-2018
store_head = str("The restaurant " + str(rest_name) + " located in " + str(rest_addr) +
      " has a total of " + str(tot_ratings) + " ratings by YELP users and an aggregate average rating of "
      + str(mean_rating))
print(store_head) #Print Store Header summary

#============================================================================================

#Data Analysis and Data Visualization

#Display rating stats over the years 2005-2018 YTD.
shak_df_da = shak_df.drop('User Name',axis = 1)           #drop unnecessary columns
shak_df_da = shak_df_da.drop('Date Published',axis = 1)
shak_df_da = shak_df_da.drop('Month',axis = 1)  
shak_stats = shak_df_da.groupby(['Year']).describe()      #to group by year for stat summary
display(shak_stats) #output

#write output to csv
shak_stats.to_csv('C:/Users/CHARU/tutorial/yelp_result.csv', sep=',')

#Graphics
#PLOT count of ratings by year
shak_df_by_year1 = shak_df.groupby(['Year']).size()
shak_df_by_year2 = shak_df_by_year1.to_frame(name = 'Count').reset_index()
plot1 = shak_df_by_year2.plot(kind = 'line',x='Year',y='Count',legend= False) #lineplot
plot1.set_xlabel("Year")                                        #renaming labels
plot1.set_ylabel("Count of user ratings")
plot1.set_title('Yearly Count of Ratings/Users',fontsize = 10)  #title

#PLOT count of ratings through the months
shak_df_by_month1 = shak_df.groupby(['Year','Month']).size().reset_index()
shak_df_by_month2 = shak_df_by_month1.assign(Date=pd.to_datetime(shak_df_by_month1[['Year', 'Month']].assign(day=1))).reset_index()
plot2 = shak_df_by_month2.plot(kind = 'line',x='Date',y=0,legend= False)
plot2.set_xlabel("Time")
plot2.set_ylabel("Count of user ratings")
plot2.set_title('Monthly Count of Ratings/Users',fontsize = 10)

#PLOT avg ratings by month
shak_df_by_month3 = shak_df.groupby(['Year','Month']).mean().reset_index()
shak_df_by_month4 = shak_df_by_month3.assign(Date=pd.to_datetime(shak_df_by_month1[['Year', 'Month']].assign(day=1))).reset_index()
plot3 = shak_df_by_month4.plot.line(x='Date',y='User Rating',legend= False)
plot3.set_xlabel("Time")
plot3.set_ylabel("Avg User Rating")
plot3.set_title('Monthly Average Ratings',fontsize = 10)

#PLOT Distribution of ratings of restaurant in YELP.
shak_df_by_ratings1 = shak_df.groupby(['User Rating']).size().reset_index()
plot4 = shak_df_by_ratings1.plot.bar(x = 'User Rating',y = 0,legend= False)
plot4.set_xlabel("Rating")
plot4.set_ylabel("Count of Users")
plot4.set_title('Distribution of ratings',fontsize = 10)

#Save all plots 
fig1 = plot1.get_figure()
fig1.savefig('yelp_plot1.pdf')

fig2 = plot2.get_figure()
fig2.savefig('yelp_plot2.pdf')

fig3 = plot3.get_figure()
fig3.savefig('yelp_plot3.pdf')

fig4 = plot4.get_figure()
fig4.savefig('yelp_plot4.pdf')
