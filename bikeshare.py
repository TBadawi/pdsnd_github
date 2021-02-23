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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ("Please enter the city name: chicago, new york city, or washington:").lower()
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input ("Please enter the city name: chicago, new york city, or washington:")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ("Please enter the month ('January to June') or ('all' if all months required):").lower()
    while month.lower() not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input ("Please enter the month ('January to June') or ('all' if all months required):")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("Please enter the day of week ('Monday to Sunday') or ('all' if all days required):").lower()
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input ("Please enter the day of week ('Monday to Sunday') or ('all' if all days required):")

    print('-'*40)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print (df.columns)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # dups_months = df.pivot_table(index = ['month'], aggfunc ='size')
    # print (dups_months)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month_index = df['month'].value_counts().idxmax()

    print ('\nMost common month: {}'.format(months[common_month_index-1]))

    #months = ['january', 'february', 'march', 'april', 'may', 'june']
   # month_index = df['month'].mode()[0]
   # print ('The most common month: {}'.format(months[month_index]))

    # TO DO: display the most common day of week
    print ('Most common day of week: {}'.format(df['day_of_week'].value_counts().idxmax()))

    # TO DO: display the most common start hour
    print ('Most common hour of the day: {}'.format(df['hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ('\nMost common start station: {}'.format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print ('Most common end station: {}'.format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print ('Most common start and end station combincation: {}'.format(df.groupby('Start Station')['End Station'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ('\nTotal travel time: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print ('Mean travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # TO DO: Display counts of user types
    print ('\nTotal count per User Type: \n{}'.format(df['User Type'].value_counts()))

    if 'Gender' in df:

        # TO DO: Display counts of gender
        print ('\nTotal count per gender: \n{}'.format(df['Gender'].value_counts()))

        # TO DO: Display earliest, most recent, and most common year of birth
        print ('\nUser earliest year of birth: {}'.format(int(df['Birth Year'].min())))
        print ('User latest year of birth: {}'.format(int(df['Birth Year'].max())))
        print ('Most common day of week: {}'.format(int(df['Birth Year'].value_counts().idxmax())))
        # Only access Gender column in this case
    else:
        print('\nGender stats cannot be calculated because Gender does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    """Displays 5 rows of consecutive data on user command."""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while view_data not in ['yes', 'no']:
         view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    view_display = view_data
    while (view_display == 'yes'):
         print(df.iloc[start_loc:start_loc+5])
         start_loc += 5
         view_display = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
