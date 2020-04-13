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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs no
    while True:
        try:
            city = input("Enter city name to analyze: ").lower()
            valid = CITY_DATA[city]
            break
        except KeyError:
            print('This is not a city name we have on file')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Enter name of month to analyze or \"all\" if you do not want to filter by month: ').lower()
            if month != 'all':
               months = ['january', 'february', 'march', 'april', 'may', 'june']
               test = months.index(month)
            break
        except ValueError:
            print('Not a valid month name please try again.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Input fullname of day of the week i.e. monday, tuesday, wednesday...etc for analysis or \"all\": ').lower()
            if day != 'all':
                weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
                test = weekDays.index(day.title())
            break
        except ValueError:
            print('not a valid day of the week please try again')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month user can't do any other month or else faggot in ass
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print(months[df['month'].mode()[0]-1].title())

    # TO DO: display the most common day of week any day works
    print(df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Itinerary'] = df['Start Station'] + " " + df['End Station']
    print(df['Itinerary'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time: ' , df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travel Time: ' , df['Trip Duration'].mean())

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
    print('Earliest Year of Birth', df['Birth Year'].min())
    print('Most Recent Year of Birth', df['Birth Year'].max())
    print('Most Common Year of Birth', df['Birth Year'].mode())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n\n').lower()
        counter = 0;
        while rawdata == 'yes':
            print(df.iloc[counter:(counter+5)])
            rawdata = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n\n').lower()
            counter += 5
            if counter > df.shape[0]:
                print('You have reached the end of the data')
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
