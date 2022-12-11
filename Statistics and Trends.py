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
    data = data[data['Indicator Name'] == indicators]
    data = data[cols]
    data.set_index('Country Name',inplace=True)
    data = data.loc[countries]
    return data,data.transpose()


def country_dataframe(country):
    '''This is a fucntion that creates a new dataframe specific countries, passing the selected years as indexes and the selected indicators as columns'''
    df = pd.DataFrame(
    {'Population': df_year_population[country],
    'CO2 Emission': df_year_co2[country],
    'Electricity Cons.': df_year_eleccons[country],
    'Mortality rate': df_year_mortality[country]},
    ['1990','1995','2000','2005','2010','2005','2010','2015','2020'])
    return df

def stat_properties(dataframe):
    '''This is a function that return some statistical properties of all the columns of the dataframe passed into it'''
    cols = dataframe.columns
    from pandas.api.types import is_numeric_dtype
    for i in cols:
        if is_numeric_dtype(dataframe[i]):
            print('This is a brief statistical description of {}'.format(i))
            print(dataframe[i].describe())
            print('The Peak-to-Peak of {} is {}'.format(i,np.ptp(dataframe[i])))
            print('The skewness of {} is {}'.format(i,sp.stats.skew(dataframe[i])))
            print()

#We would now proceed to create a few dataframes using our predefined function.

filename = 'API_19_DS2_en_csv_v2_4700503.csv'
cols = ['Country Name','1990','1995','2000','2005','2010','2005','2010','2015','2020']
indicators = ['Population, total',
               'Electric power consumption (kWh per capita)',
               'Mortality rate, under-5 (per 1,000 live births)',
               'CO2 emissions (kt)']
               
countries = ['United Kingdom',
             'United States',
             'China',
             'Nigeria',
             'Russian Federation']

df_name_population,df_year_population = data_read(filename,indicators[0],countries,cols)
df_name_eleccons,df_year_eleccons = data_read(filename,indicators[1],countries,cols)
df_name_mortality,df_year_mortality = data_read(filename,indicators[2],countries,cols)
df_name_co2,df_year_co2 = data_read(filename,indicators[3],countries,cols)

name_list = [df_name_population,df_name_eleccons,df_name_mortality,df_name_co2]
year_list = [df_year_population,df_year_eleccons,df_year_mortality,df_year_co2]

#Now that we have created our dataframes of interest, we would do a brief descriptive analysis of our table and then plot a few graphs to help us understand our data and selected indicators better.
for i in range(len(year_list)):
    print('Indicator: {}'.format(indicators[i]))
    stat_properties(year_list[i])
    print()
    
#This is a line graph that visualizes the population of selected countries for selected years
plt.figure(figsize=(8,5),dpi=1000)
for i in range(len(countries)):
    plt.plot(df_year_population.index,df_year_population[countries[i]],label=countries[i])
plt.legend()
plt.title('A line graph that shows the Population of selected countries over selected years',fontsize=8)
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()

#This is a bar chart that visualizes the electricity consumption of some countries across selected years
df_name_eleccons.plot(kind='bar',figsize=(8,5))
plt.title('A bar chart that shows the Electricity Consumption of selected countries over selected years',fontsize=8)
plt.xlabel('Countries')
plt.ylabel('Electricity Consumption KM / Capita')
plt.legend(loc='upper right',fontsize=8)
plt.xticks(rotation=0,fontsize=7)
plt.rcParams["figure.dpi"] = 1000
plt.show()

#This is a bar chart that visualizes the CO2 emission of some countries across selected years
df_name_co2.plot(kind='bar',figsize=(8,5))
plt.title('A bar chart that shows the CO2 emission of Children under 5 of selected countries over selected years',fontsize=8)
plt.xlabel('Countries')
plt.ylabel('CO2 emission')
plt.legend(loc='upper right',fontsize=8)
plt.xticks(rotation=0,fontsize=7)
plt.rcParams["figure.dpi"] = 1000
plt.show()

#This is a bar chart that visualizes the mortality rate of some countries across selected years
df_name_mortality.plot(kind='bar',figsize=(8,5))
plt.title('A bar chart that shows the Mortality rate of Children under 5 of selected countries over selected years',fontsize=8)
plt.xlabel('Countries')
plt.ylabel('Mortality rate under 5 /1000')
plt.legend(loc='upper right',fontsize=8)
plt.xticks(rotation=0,fontsize=7)
plt.rcParams["figure.dpi"] = 1000
plt.show()


#Now we have to create a dataframes for each country with the indicators as features and years as indexes using our predefined function
uk = country_dataframe('United Kingdom')
usa = country_dataframe('United States')
china = country_dataframe('China')
nigeria = country_dataframe('Nigeria')
russia = country_dataframe('Russian Federation')

#Next we plot a correlation heatmap for all countries using seaborn to show the relation between all the indicators
countries = [uk, usa, china, nigeria, russia]
labels = ['United Kingdom', 'USA', 'China', 'Nigeria', 'Russia']

for i in range(len(countries)):
    plt.figure()
    label = 'Correlation heatmap for all selected indicators for {}' .format(labels[i])
    plt.title(label,fontsize=8)
    sns.heatmap(countries[i].corr(),cmap='Blues', annot=True)
plt.show()