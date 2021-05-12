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
     days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']


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
                  day_selection = input( 'write the day name: saturday, sunday, monday , tuesday, wednesday, thursday, friday\n')
          while day_selection not in days:      
                print('invalid choice')
                day_selection = input( 'write the day name: saturday, sunday, monday , tuesday, wednesday, thursday, friday\n')
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
          day_selection = input( 'write the day name: saturday, sunday, monday , tuesday, wednesday, thursday, friday\n')
          while day_selection not in days:
               print('invalid choice')
               day_selection = input( 'write the day name: saturday, sunday, monday , tuesday, wednesday, thursday, friday\n') 
          
          day = day_selection
          month = 'all'
        
     return (city, month, day)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe                      
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

# testing code 
filters = get_filters()
city, month, day = filters

print("the user input are as follows: \n")
print(city, "\n")
print(month, "\n")
print(day)

df = load_data('washington','june', 'saturday')
print(df.head())


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    #display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular day :', popular_day_of_week)

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    #display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['combination start and end']= df['Start Station']+ '-' + df['End Station']
    popular_combination = df['combination start and end'].mode()[0]
    print('popular combination of start station and end station trip:', popular_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
station_stats(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total teravel time :',total_travel_time)
    # TO DO: display mean travel time
    average_travel_time= df['Trip Duration'].mean()
    print('Average teravel time :',average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
trip_duration_stats(df)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of each user type :', user_types)
     
    # Display counts of gender
    try:
       gender_count = df['Gender'].value_counts()
       print('\nBike riders gender split: \n', gender_count)
    
       #Display earliest, most recent, and most common year of birth
       earliest_yob = int(df['Birth Year'].min())
       most_recent_yob = int(df['Birth Year'].max())
       most_common_yob = int(df['Birth Year'].mode()[0])
       print('\n Earliest birth year :  ',earliest_yob)
       print('\n Most recent birth year :  ',most_recent_yob)
       print('\n Most common birth year :  ',most_common_yob)
       # dealing with Washington
    except KeyError:
           print('This data is not available for Washington')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

user_stats(df)

def display_raw_data(city):
    ''' displays raw data of bikeshare in cities'''
    print(' your data is availble to check ...\n')
    display_raw = input(' may you have to look on the raw data ? Type yes or no.\n')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
              print(chunk)  
              display_raw = input(' may you have to look on the raw data ? Type yes or no.\n')
              if display_raw != 'yes':
                 print('Thank You.')
                 break
            break       
        except KeyboardInterrupt:
            print('Thank You.')
display_raw_data(city)           
            

def main():

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)    # the display_raw_data

        while True:
             restart = input('\nWould you like to restart? Enter yes or no.\n')
             if restart.lower() != 'yes':
                  break

if __name__ == "__main__":
    main()