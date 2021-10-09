import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # this is my bikshare project
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            "Enter name of the city:chicago, new york, washington").lower()
        if city not in CITY_DATA:
            print("Please type a valid answer")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        time = input("Choose your filter: month, day, all or none?").lower()
        if time == 'month':
            month = input(
                "choose month: January, Feburary, March, April, May or June?").lower()
            day = 'all'
            break

        elif time == 'day':
            month = 'all'
            day = input(
                "choose day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break

        elif time == 'all':
            month = input(
                "choose month: January, Feburary, March, April, May or June?").lower()
            day = input(
                "choose day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break
        elif time == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("Invalid Input Please type a correct one. month, day, all or none?")
            break

    print(city)
    print(month)
    print(day)
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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(common_day)
    # TO DO: display the most common start hour
    common_start_hour = df['Start Time'].mode()[0]
    print(common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_frequent_combination = df['combination'].mode()[0]
    print(common_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print(user_types_counts)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print("Sorry, there is no Gender Information")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_year = df['Birth_Year'].min()
        print(earliest_year)
        recent_year = df['Birth_Year'].max()
        print(recent_year)
        common_year_of_birth = df['Birth Year'].mode()[0]
        print(common_year_of_birth)
    else:
        print("Sorry, there is no Birth Year Information")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see raw data? Y or N").lower()
        if answer not in ['y', 'n']:
            answer = input("Invalid...please enter Y or N.").lower()
        elif answer == 'y':
            raw_data += 5
            print(df.iloc[raw_data: raw_data + 5])
            again = input("Do you want to see more? Y or N").lower()
            if again == 'n':
                break
        elif answer == 'n':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
