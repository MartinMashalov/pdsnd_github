import time
import pandas as pd
import numpy as np
import statistics as sc

CITY_DATA = { 'chicago': 'chicago_test.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#dictionaries
days_dataframe = {}
months_dataframe = {}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    months = pd.Series(data = ['01', '02', '03', '04', '05', '06', '-07', '08', '09', '10', '11', '12'],
    index = ['January', 'Febuary', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'])

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input = input('What city: ')

    if city_input == 'chicago' or city_input == 'Chicago':
        chicago = open('chicago_test.csv', 'r')
        filter_object = input('Day or Month: ')

        if filter_object == 'month' or filter_object == 'Month':
            specific_month = input('What month: ')
            #return test
            specific_month = 0
            firstline = True
            for line in chicago:
                if firstline:
                    firstline = False
                else:
                    full_date = line.split(',')[1]
                    compressed_date = full_date.split(' ')[0]
                    print('compressed_date ', compressed_date)
                    print(len(compressed_date))
                    c_month = compressed_date.split('-')[1]
                    if c_month == specific_month:
                        days_dataframe[specific_month] = line.split(',')[1]

        elif filter_object == 'day' or filter_object == 'Day':
            specific_day = input('What day: ')
            #return test
            specific_day = 0
            firstline = True
            for line in chicago:
                if firstline:
                    firstline = False
                else:
                    full_date = line.split(',')[1]
                    compressed_date = full_date.split(' ')[0]
                    c_day = compressed_date.split('-')[2]
                    if c_day == specific_day:
                        days_dataframe[specific_day] = line.split(',')[2]
        chicago.close()


    elif city_input == 'new york' or city_input == 'New York':
        new_york = open('new_york_city.csv', 'r')
        filter_object = input('Day or Month')
        if filter_object == 'month' or filter_object == 'Month':
            specific_month = input('What month: ')
            #return test
            specific_month = 0
            firstline = True
            for line in new_york:
                if firstline:
                    firstline = False
                else:
                    full_date = line.split(',')[1]
                    compressed_date = full_date.split(' ')[0]
                    print('compressed_date ', compressed_date)
                    print(len(compressed_date))
                    c_month = compressed_date.split('-')[1]
                    if c_month == specific_month:
                        days_dataframe[specific_month] = line.split(',')[1]

        elif filter_object == 'day' or filter_object == 'Day':
            specific_day = input('What day: ')
            #return test
            specific_day = 0
            firstline = True
            for line in new_york:
                if firstline:
                    firstline = False
                else:
                    full_date = line.split(',')[1]
                    compressed_date = full_date.split(' ')[0]
                    c_day = compressed_date.split('-')[2]
                    if c_day == specific_day:
                        days_dataframe[specific_day] = line.split(',')[2]
        new_york.close()


    elif city_input == 'washington' or city_input == 'Washington':
        washington = open('washington.csv', 'r')
        filter_object = input('Day or Month')

        if filter_object == 'month' or filter_object == 'Month':
            specific_month = input('What month: ')
            #return test
            specific_month = 0
            firstline = True
            for line in washington:
                if firstline:
                    firstline = False
                else:
                    full_date = line.split(',')[1]
                    compressed_date = full_date.split(' ')[0]
                    print('compressed_date ', compressed_date)
                    print(len(compressed_date))
                    c_month = compressed_date.split('-')[1]
                    if c_month == specific_month:
                        days_dataframe[specific_month] = line.split(',')[1]

        elif filter_object == 'day' or filter_object == 'Day':
            specific_day = input('What day: ')
            #return test
            specific_day = 0
            firstline = True
            for line in washington:
                if firstline:
                    firstline = False
                else:
                    full_date = line.split(',')[1]
                    compressed_date = full_date.split(' ')[0]
                    c_day = compressed_date.split('-')[2]
                    if c_day == specific_day:
                        days_dataframe[specific_day] = line.split(',')[2]
        washington.close()

    else:
        print('There was an error')


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city_input, specific_month, specific_day


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
    combined_date_days = {'Days': days_dataframe}
    combined_date_month = {'Months': months_dataframe}

    month_date = input('Month or date:')
    if month_date == 'date' or month_date == 'Date':
        df = pd.DataFrame(combined_date_days)
    elif month_date == 'month' or month_date == 'Month':
        df = pd.DataFrame(combined_date_month)
    else:
        print('error')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    chicago = open('chicago_test.csv', 'r')
    new_york = open('new_york_city.csv', 'r')
    washington = open('washington.csv', 'r')

    month_dict = {}
    day_dict = {}

    firstline = True
    for line in chicago:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[0]
            line_list = list(compressed_date)
            print(count)
            month = line_list[6]
            for month in line_list:
                if month not in month_dict:
                    month_dict[month] = 1
                else:
                    month_dict[month] += 1


    max_value = max(month_dict.values())  # maximum value
    max_keys = [k for k, v in month_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)
#-------------------------------------------------------------
    firstline = True
    for line in new_york:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[0]
            line_list = list(compressed_date)
            print(count)
            month = line_list[6]
            for month in line_list:
                if month not in month_dict:
                    month_dict[month] = 1
                else:
                    month_dict[month] += 1


    max_value = max(month_dict.values())  # maximum value
    max_keys = [k for k, v in month_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)
#------------------------------------------------------------
    firstline = True
    for line in washington:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[0]
            line_list = list(compressed_date)
            print(count)
            month = line_list[6]
            for month in line_list:
                if month not in month_dict:
                    month_dict[month] = 1
                else:
                    month_dict[month] += 1


    max_value = max(month_dict.values())  # maximum value
    max_keys = [k for k, v in month_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)

    # display the most common day of week
    firstline = True
    for line in chicago:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[0]
            day = compressed_date.split('-')[2]
            for day in line_list:
                if day not in day_dict:
                    day_dict[day] = 1
                else:
                    day_dict[day] += 1


    max_value = max(day_dict.values())  # maximum value
    max_keys = [k for k, v in day_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)


    firstline = True
    for line in new_york:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[0]
            day = compressed_date.split('-')[2]
            for day in line_list:
                if day not in day_dict:
                    day_dict[day] = 1
                else:
                    day_dict[day] += 1


    max_value = max(day_dict.values())  # maximum value
    max_keys = [k for k, v in day_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)

    firstline = True
    for line in washington:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[0]
            day = compressed_date.split('-')[2]
            for day in line_list:
                if day not in day_dict:
                    day_dict[day] = 1
                else:
                    day_dict[day] += 1


    max_value = max(day_dict.values())  # maximum value
    max_keys = [k for k, v in day_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)
    hours_dict = {}
    # display the most common start hour
    firstline = True
    for line in chicago:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[1]
            hours = compressed_date.split(':')[0]
            for hour in hours:
                if hour not in hours_dict:
                    hours_dict[hour] = 1
                else:
                    hours_dict[hour] += 1


    max_value = max(hours_dict.values())  # maximum value
    max_keys = [k for k, v in hours_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)


    firstline = True
    for line in new_york:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[1]
            hours = compressed_date.split(':')[0]
            for hour in hours:
                if hour not in hours_dict:
                    hours_dict[hour] = 1
                else:
                    hours_dict[hour] += 1


    max_value = max(hours_dict.values())  # maximum value
    max_keys = [k for k, v in hours_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)


    firstline = True
    for line in washinton:
        if firstline:
            firstline = False
        else:
            full_date = line.split(',')[1]
            compressed_date = full_date.split(' ')[1]
            hours = compressed_date.split(':')[0]
            for hour in hours:
                if hour not in hours_dict:
                    hours_dict[hour] = 1
                else:
                    hours_dict[hour] += 1


    max_value = max(hours_dict.values())  # maximum value
    max_keys = [k for k, v in hours_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    stations_dict = {}
    # display most commonly used start station
    firstline = True
    for line in chicago:
        if firstline:
            firstline = False
        else:
            first_station = line.split(',')[4]
            for station in stations:
                if station not in stations_dict:
                    stations_dict[station] = 1
                else:
                    stations_dict[station] += 1

    #most efficient way to find max value of dictionaries
    #k is the key and v is the value
    max_value = max(stations_dict.values())  # maximum value
    max_keys = [k for k, v in stations_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)


    # display most commonly used end station
    firstline = True
    for line in chicago:
        if firstline:
            firstline = False
        else:
            first_station = line.split(',')[5]
            for station in stations:
                if station not in stations_dict:
                    stations_dict[station] = 1
                else:
                    stations_dict[station] += 1


    max_value = max(stations_dict.values())  # maximum value
    max_keys = [k for k, v in stations_dict.items() if v == max_value] # getting all keys containing the `maximum`
    print(max_value, max_keys)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    distance_list = [0]
    firstline = True
    for line in chicago:
        if firstline:
            firstline = False
        else:
            each_distance = line.split(',')[5]
            distance_list.extend(each_distance)
    return sum(distance_list)  #total distance
    # display mean travel time
    return sc.mean(distance_list)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type = input('What type of user:')
    # Display counts of user types
    for line in chicago:
        type_of_user = line.split(',')[4]
        if user_type == type_of_user or type_of_user == capitalize(user_type):
            return line

    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
