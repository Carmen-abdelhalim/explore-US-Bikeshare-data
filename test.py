import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
           try:
               city_selection = input('To view the available bikeshare data, type\n (a) for Chicago\n (b) for New York City\n (c) for Washington\n').lower() 
               if city_selection in ('a','b','c'):
                 break 
           except KeyboardInterrupt:
                 print('invalid input')
                                
    city_selections = {"a":"chicago", "b":"new york city", "c":"washington"}
    if city_selection in city_selections.keys():
        city = city_selections[city_selection]

    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['sat','sun','mon','tues','wed','thu','fri']


    while True:
           try:
               time_frame = input('\n\n Would you like to filter {} data by month, day, both, or not at all? type month or day or both or none: \n'.format(city.title())).lower()
               if time_frame in ('month', 'day', 'both', 'none'):
                  break
           except KeyboardInterrupt:
                print('invalid input')
        
    if time_frame == 'none':
       print('\n filtering for {} for the 6 months period \n'.format(city.title()))
    
       month = 'all' 
       day = 'all'
    
    elif time_frame == 'both' :
         month_selection = input('write the month name: january, february, march, april, may, june\n' )
         while month_selection not in months:
               print('invalid choice')
               month_selection = input('write the month name: january,february, march, april, may, june\n')
         if month_selection in months :   
                  month = month_selection
                  day_selection = input ( 'write the day name: sat, sun , mon, tues, wed,thu ,fri\n')
         while day_selection not in days:      
                print('invalid choice')
                day_selection = input ( 'write the day name: sat, sun , mon, tues, wed,thu ,fri\n') 
         if day_selection in days:
                   day = day_selection
                
    elif time_frame == 'month':
         month_selection = input('write the month name:january,february, march, april, may, june\n' )
         while month_selection not in months:
               print('invalid choice')
               month_selection = input('write the month name:january,february, march, april, may,june\n' )
         month = month_selection
         day = "all"
   
    elif time_frame == 'day':
         day_selection = input('write the day name:sat, sun , mon, tues, wed,thu ,fri\n') 
         while day_selection not in days:
               print('invalid choice')
               day_selection = input('write the day name:sat, sun , mon, tues, wed,thu ,fri\n') 
          
         day = day_selection
         month = 'all'
            
    return city, month, day

filtered_values = get_filters()
city, month, day = filtered_values

print("the user input are as follows: \n")
print(city, "\n")
print(month, "\n")
print(day)

df = load_data(city, month, day)
print(df.head())
