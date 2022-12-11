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
    city = input('Enter city:').lower()
    while city not in CITY_DATA:
        print('Invalid input! Please enter city name again:')
        city = input('Enter city:').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter month:').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                        'october', 'november', 'december']:
        print('Invalid input! Please enter month again:')
        month = input('Enter month:').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter week_of_the_day:').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print('Invalid input! Please enter day again:')
        day = input('Enter week_of_the_day:').lower()



    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(df)

    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day=days.index(day)+1
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].value_counts().idxmax()

    print('Most Common Start Month:', popular_month)


    # TO DO: display the most common day of week
    df['day_of_the_week'] = df['Start Time'].dt.weekday
    popular_day = df['day_of_the_week'].value_counts().idxmax()
    popular_day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][popular_day]
    print('Most Common Day of Week:', popular_day_name)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Common Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MStart_Station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', MStart_Station )

    # TO DO: display most commonly used end station
    MEnd_S = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station:',MEnd_S )

    # TO DO: display most frequent combination of start station and end station trip
    c = df[['Start Station', 'End Station']].value_counts().idxmax()
    print('The most frequent combination is when the start station being {} and the end station being {}.'.format(c[0],
                                                                                                                  c[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    Earliest = df['Birth Year'].min()
    print('Earliest:', Earliest )
    Most_Recent = df['Birth Year'].max()
    print('Most Recent:', Most_Recent)
    Common =df['Birth Year'].mode()
    print('Most Common:', Common[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    decision = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    while decision != 'yes' and decision != 'no':
        print('Invalid input! Please enter yes or no again:')
        decision = input('Would you like to view 5 rows of individual trip data?: yes/no').lower()
    start_loc = 0
    while decision == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        decision = input("Do you wish to continue?: yes/no ").lower()
        while decision != 'yes' and decision != 'no':
            print('Invalid input! Please enter yes or no again:')
            decision = input('continue?: yes/no').lower()
        




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