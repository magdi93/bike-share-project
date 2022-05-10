import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city to analyze its data.
    Ask user if he wants to filter by month, day or both.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n')
    print('Hello! Let\'s explore some US bikeshare data! ^_^')
    print('\n')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities = ['chicago', 'new york city', 'washington']
    print(cities, '\n')
    city = input('\nPlease, enter one of the above cities to start analyzings its data: ').lower()
    
    while city not in cities:
        city = input('The city you entered is not available.\n{}\n\nPlease, enter one of the available cities: '.format(cities)).lower()
    
    ''' Getting city input from the user and handling errors of input'''
    
    
    print('\nThat\'s cool! It seems that you\'ve choosen {}. Interesting choice. Let\'s explore {}\'s BikeShare data together ^_^\n'.format(city.title(), city.title()) )
    
    
    """
    Now, it\'s time to ask user about if he wants to apply a time filter
    and this part of code asks the user and apply month filter or day filter or both filters or no filter at all
    taking errors of input in consideration
    """    
    
    time_filters = ['month', 'day', 'both', 'none']
    time_filter = input('Do you want to filter data by month, day, both or no filte(choose none for no filter)?').lower()
    while time_filter not in time_filters:
        time_filter = input('{}\nPlease, choose one of the available options:'.format(time_filters)).lower()
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['friday', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday']
    
    if time_filter == 'none':
        month = 'all'
        day = 'all'
        
    elif time_filter == 'month':
        day = 'all'
        month = input('{}\nPlease, enter the month you want to filter with: '.format(months)).lower()
        while month not in months:
            month = input('Unfortunately, {} is not a valid month,\n{}\nPlease, enter one of the available months: '.format(month, months)).lower()
    
    elif time_filter == 'day':
        month = 'all'
        day = input('{}\n\nPlease, enter the day you want to filter with: '.format(days)).lower()
        while day not in days:
            day = input('Unfortunately {} is not a valid day,\n{}\n\nPlease, enter one of the available days: '.format(day, days)).lower()
    
    elif time_filter == 'both':
        month = input('{}\nPlease, enter the month you want to filter with: '.format(months)).lower()
        while month not in months:
            month = input('Unfortunately, {} is not a valid month,\n{}\nPlease, enter one of the available months: '.format(month, months)).lower()
        
        day = input('{}\n\nPlease, enter the day you want to filter with: '.format(days)).lower()
        while day not in days:
            day = input('Unfortunately {} is not a valid day,\n{}\n\nPlease, enter one of the available days: '.format(day, days)).lower()
        
        

    print('-'*50)
    return city, month, day


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
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    
        
    df['day of week'] = df['Start Time'].dt.day_name()
    
    if day != 'all':
        df = df[df['day of week'] == day.title()]
        
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    print('\nThese are the most frequent time of travel:\n')

    # display the most common month
    
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    
    if len(df['month'].unique()) == 1:
        month = df['month'].mode()[0]
        month = months[month-1]
        print('    Since month filter was applied to the data, this is the data of the month you\'ve already choosen: ', month)
    else:
        pop_month = df['month'].mode()[0]
        pop_month = months[pop_month-1]
        print('    The most frequent month of travel is: ', pop_month)
    

    # display the most common day of week
    
    if len(df['day of week'].unique()) == 1:
        day_of_week = df['day of week'].mode()[0]
        print('    Since day filter was applied to the data, this is the data of the day you\'ve already choosen: ', day_of_week)
    else:
        pop_day = df['day of week'].mode()[0]
        print('    The most frequent day of travel is: ', pop_day)
    

    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('    The most frequent start hour is: {}:00'.format(pop_hour))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    most_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}\n'.format(most_start))


    # display most commonly used end station
    
    most_end = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}\n'.format(most_end))
    
    
    # create a trip start and end column
    
    df['Total Trip Destination'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']


    # display most frequent combination of start station and end station trip
    
    most_comb = df['Total Trip Destination'].mode()[0]
    print('The most frequent combination of start and end station trip is: {}\n'.format(most_comb))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def time_units(sec):
    """"
    converting seconds of any time stats into hours, minutes and seconds
    
    This function takes one arguments which is seconds
    
    and it returns: 
        (int)hours = number of hours
        (int)minutes = number of minutes
        (int)seconds = noumber of secods
    """
    
    hours = sec/3600
    hours = int(hours)
    
    # Handling the error of ZeroDivision
    
    if hours == 0:
        minutes = sec / 60
    elif hours > 0:
        minutes = (sec - (hours*3600)) / 60
        
    
    minutes = int(minutes)
    seconds = sec - ((hours*3600) + (minutes*60))
    seconds = round(seconds, 2)
    
    return(hours, minutes, seconds)
    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    tot_travel = df['Trip Duration'].sum()
    hours, minutes, seconds = time_units(tot_travel)
    print('The total travel time is: {} Seconds which are: {} Hours, {} Minutes, and {} Seconds\n'.format(round(tot_travel, 2), hours, minutes, seconds))


    # display mean travel time
    
    mean_travel = df['Trip Duration'].mean()
    hours, minutes, seconds = time_units(mean_travel)
    print('The mean of travel time is: {} Seconds which are: {} Hours, {} Minutes, and {} Seconds\n'.format(round(mean_travel, 2), hours, minutes, seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_type = df['User Type'].value_counts()
    print('Counts of user types\n{}\n'.format(user_type))


    # Display counts of gender (with handling of not available data of Washington)
    
    if 'Gender' not in df.columns:
        print('Unfortnately, gender counts data is not available for Washington\n')
    else:
        gender_count = df['Gender'].value_counts()
        print('The gender counts are:\n{}\n'.format(gender_count))


    # Display earliest, most recent, and most common year of birth (with handling of not available data of Washington)
    
    if 'Birth Year' not in df.columns:
        print('Unfortunately, users\' birth years are not available for Washington\n')
    else:
        most_early = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        
        print('The earliest year of birth among the users is: {}. That means that our oldest user is {} years old. WOW!\n'.format(most_early, 2021-most_early))
        print('The most recent year of birth among the users is: {}. That means that our youngest user is {} years old. OH, SO CUTE! ^_^\n'.format(most_recent, 2021-most_recent))
        print('The most common year of birth among the users is: {}. It\'s amazing to know that most of users are {} years old.\n'.format(most_common_year, 2021-most_common_year))
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        sample = input('\nDo you want to print a sample of data befor calculating some statistics?\nEnter yes or no.\n').lower()
        while sample == 'yes':
            print(df.sample(5))
            sample = input('\nDo you want to print another sample before calculating statistics?\n')
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
