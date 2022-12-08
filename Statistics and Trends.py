#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:02:22 2022

@author: danieloyeduntan
"""


#As we begin our analysis, we need to import the necessary libraries (Pandas, Numpy, Scipy, Seaborn and Matplotlib)
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#For the purpose of this analysis, we would define a function (i.e. a group of related statements that performs a specific task). As we proceed in the analysis, we would call the function and make use of it.

def data_read(filename,indicators,countries,cols):
    '''This is a function that reads csv file and returns an output of two data frames, it takes 4 arguments - the filename, indicators, columns to drop and countries to be presented in the dataframe'''
    data = pd.read_csv(filename,skiprows=4)
    data = data[data['Indicator Name'] == col_filter]
    data = data[cols]
    data.set_index('Country Name',inplace=True)
    data = data.loc[countries]
    return data,data.transpose()


#We would now proceed to create a few dataframes using our predefined function.

filename = 'API_19_DS2_en_csv_v2_4700503.csv'
cols = ['Country Name','1990','1995','2000','2005','2010','2005','2010','2015','2020']
col_filters = ['Population, total',
               'Access to electricity (% of population)',
               'Electric power consumption (kWh per capita)',
               'Mortality rate, under-5 (per 1,000 live births)',
               'CO2 emissions (kt)']
               
drop_cols = ['Country Code','Indicator Name','Indicator Code']
countries = ['United Kingdom',
             'United States',
             'China',
             'Nigeria',
             'Russian Federation']

countries22 = ['United Kingdom',
             'United States',
             'Spain',
             'China',
             'France',
             'Germany',
             'Japan',
             'India',
             'Nigeria',
             'Russian Federation']


df_name_population,df_year_population = data_read(filename,col_filters[0],drop_cols,countries,cols)
df_name_acc2elec,df_year_acc2elec = data_read(filename,col_filters[1],drop_cols,countries,cols)
df_name_eleccons,df_year_eleccons = data_read(filename,col_filters[2],drop_cols,countries,cols)
df_name_mortality,df_year_mortality = data_read(filename,col_filters[3],drop_cols,countries,cols)
df_name_co2,df_year_co2 = data_read(filename,col_filters[4],drop_cols,countries,cols)


#Now that we have created out dataframes of interest, we would now plot a few graphs to help us understand our data and selected indicators better.

#This is a line graph that visualizes the population of selected countries for selected years
plt.figure(figsize=(8,5),dpi=1000)
for i in range(len(countries)):
    plt.plot(df_year_population.index,df_year_population[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor = (1,1))
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()

#This is a bar chart that visualizes the electricity consumption of some countries across selected years
df_name_eleccons.plot(kind='bar',figsize=(8,5))
plt.xlabel('Countries')
plt.ylabel('Electricity Consumption KM / Capita')
plt.legend(loc='upper right',fontsize=8)
plt.xticks(rotation=0,fontsize=7)
plt.rcParams["figure.dpi"] = 1000
plt.show()

#This is a bar chart that visualizes the CO2 emission of some countries across selected years
df_name_co2.plot(kind='bar',figsize=(8,5))
plt.xlabel('Countries')
plt.ylabel('CO2 emission')
plt.legend(loc='upper right',fontsize=8)
plt.xticks(rotation=0,fontsize=7)
plt.rcParams["figure.dpi"] = 1000
plt.show()

#This is a bar chart that visualizes the mortality rate of some countries across selected years
df_name_mortality.plot(kind='bar',figsize=(8,5))
plt.xlabel('Countries')
plt.ylabel('Mortality rate under 5 /1000')
plt.legend(loc='upper right',fontsize=8)
plt.xticks(rotation=0,fontsize=7)
plt.rcParams["figure.dpi"] = 1000
plt.show()