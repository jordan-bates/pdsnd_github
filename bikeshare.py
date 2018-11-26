import pandas as pd
import numpy as np
import time

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
    while True:
        try:
            city = input('Please select Chicago, New York City, or Washington to see city data: ')
            city = city.lower()
            if city in ['chicago','new york city','washington']:
                break
            else:
                raise ValueError
        except ValueError:
            print('Please select a valid city to see data for ')
    while True:
        try:
            month = input('Please select a month between January and June or select "all" ')
            month = month.lower()
            if month in ['january','february','march','april','may','june','all']:
                break
            else:
                raise ValueError #asked for help from a friend to figure out to raise ValueError
        except ValueError:
            print('Please select a valid month or select "all" ')
    while True:
        try:
            day = input('Please select a day of the week, or select "all" ')
            day = day.lower()
            if day in ['sunday','monday','wednesday','thursday','friday','tuesday','saturday','all']:
                break
            else:
                raise ValueError
        except ValueError:
            print('Please select a valid day or select "all" ')
    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city]) #load data same as practice question 3
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month']== month]

    if day != 'all':
        df = df[df['day_of_week']== day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    common_month = df['month'].mode()[0]
    print('The most common month is {}'.format(common_month))
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is {}'.format(common_day))
    common_hour = df['hour'].mode()[0]
    print('The most frequent start hour is {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most commonly used start station is {}'.format(df['Start Station'].mode()[0]))
    print('The most commonly used end station is {}'.format(df['End Station'].mode()[0]))

    df['Common Trip'] = df['Start Station'] + df['End Station']

    print('The most common trip is {}'.format(df['Common Trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('\nThe total trip duration is {}\n'.format(df['Trip Duration'].sum()))
    print('\nThe average trip duration is {}\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on the ages and genders of bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types (worked with a programmer friend to help me figure out correct syntax for this TO DO)
    user_count = df['User Type'].value_counts()
    print("There are " + str(user_count[1]) + " customer users, and " +
          str(user_count[0]) + " subscriber users.")
    # Display how many male and female users are present
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("There are  " + str(gender_counts[0]) + " males, and " +
              str(gender_counts[1]) + " females.")
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = str(df['Birth Year'].min())
        recent_birth = str(df['Birth Year'].max())
        common_birth = str(df['Birth Year'].mode()[0])
        print("The earliest birth year is: " + earliest_birth)
        print("The most recent birth year is: " + recent_birth)
        print ("The most common birth year is: " + common_birth)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # Ask the user if they want to see raw data from the .csv files
        get_raw_data = input('Would you like to see raw data? Select "Yes" or "No"')
        if get_raw_data.lower() == 'yes':
            print(df.head())
        restart = input('Would you like to restart? Select "Yes" or "No"')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
