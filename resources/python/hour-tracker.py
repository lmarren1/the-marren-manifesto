import datetime as dt
import os
import csv 

def check_file_exists(file_path):
    '''Check if file path exists, if not then create CSV.'''
    if (not os.path.exists(file_path)):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerow(['Start Time', 'End Time',
                             'Motivation Level', 'Stress Level', 
                             'Focus Level', 'Enjoyment Level',
                             'Minutes Worked', 'Hours Worked',
                             'Number of Sessions',
                             'Cumulative Hours Worked',])

def get_csv_value(file_path, row, col):
    '''Get CSV value based on row and column number.'''
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            # Check if the CSV is empty
            if not rows:
                print('The file is empty.')
                return None
            
            # Handle negative indexing for rows
            if row < 0:
                row = len(rows) + row
            # Handle negative indexing for columns
            if rows:
                if col < 0:
                    col = len(rows[0]) + col
            else:
                print('The file is empty.')
                return None

            # Check if the row and column indices are within range
            if row >= len(rows) or col >= len(rows[row]):
                print('Row or column index out of range.')
                return None

            # Get the value from the CSV
            csv_value = rows[row][col]
            return csv_value

    except Exception as e:
        print(f'Error reading the file: {e}')
        return None

def check_time_format(time):
    '''Reprompt user if time format isn't %H:%M.'''
    try:
        dt.datetime.strptime(time, '%H:%M')
        return time
    except ValueError:
        new_time = input('Incorrect time format. Try again (HH:MM). ')
        return check_time_format(new_time)

    
def check_date_format(date):
    '''Reprompt user if date format isn't %m-%d-%y.'''
    try:
        dt.datetime.strptime(date, '%m-%d-%y')
        return date
    except ValueError:
        new_date = input('Incorrect date format. Try again (MM-DD-YY). ')
        return check_date_format(new_date)

def check_rating_scale(rating):
    '''Reprompt user if rating is outside of 1-5 range.'''
    if rating < 1 or rating > 5:
        new_rating = input('Incorrect rating input. Try again (1-5).')
        return check_rating_scale(new_rating)
    return rating

def calculate_time_difference(time1, time2, time_format='%H:%M'):
    '''Calculate minute difference between two given times.'''
    # Parse the time strings into datetime objects
    t1 = dt.datetime.strptime(time1, time_format)
    t2 = dt.datetime.strptime(time2, time_format)
    
    # Calculate the difference
    difference = t2 - t1
    
    # If the difference is negative, assume that t2 is on the following day
    if difference.total_seconds() < 0:
        difference += dt.timedelta(days=1)
    
    # Convert the difference to minutes
    difference_in_minutes = difference.total_seconds() / 60
    return difference_in_minutes

def count_session_number(file_path):
    '''Count number of sessions had in a given day based on entries in the day's CSV.'''
    count = 0
    with open(file_path, 'r') as file:
        for row in file:
            count += 1
    file.close()
    return count

def get_cumulative_hours_worked(directory, date):
    '''Sort through data directory to get the last cumulative hours worked number logged.'''
    
    # List all CSV files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # Extract dates from filenames and filter based on the provided date
    file_dates = []
    for file in files:
        file_date = dt.datetime.strptime(file.replace('.csv', ''), '%m-%d-%y')
        input_date = dt.datetime.strptime(date, '%m-%d-%y')
        if file_date <= input_date:
            file_dates.append(file_date)
    
    if not file_dates:
        print('Warning: no CSVs found before the provided date.')
        return 0
    
    # Find the latest file based on date
    latest_date = max(file_dates)
    latest_file = latest_date.strftime('%m-%d-%y') + '.csv'
    
    # Construct the full path to the latest CSV file
    latest_file_path = os.path.join(directory, latest_file)
    
    # Return last cumulative hours worked logged
    return float(get_csv_value(latest_file_path, -1, -1))

def get_user_input():
    '''Prompt the user for input and return a list with the data.'''

    # Get user input
    date = check_date_format(input("What is the date you worked? (MM-DD-YY): "))
    start_time = check_time_format(input("When did you START working? (HH-MM) "))
    end_time = check_time_format(input("When did you STOP working? (HH:MM) "))
    motivation_level = check_rating_scale(int(input("How motivated were you during this session? (1-5) ")))
    stress_level = check_rating_scale(int(input("How stressed were you coming into this session? (1-5) ")))
    focus_level = check_rating_scale(int(input("How focused were you during this session? (1-5) ")))
    enjoyment_level = check_rating_scale(int(input("How much did you enjoy this session? (1-5) ")))

    # Calculate other session metrics based on user input
    print('Data collection was successful.')
    minutes_worked = calculate_time_difference(start_time, end_time)
    hours_worked = round(minutes_worked / 60, 2)

    cumulative_hours_worked = get_cumulative_hours_worked('resources/data', date) + hours_worked
    file_path = f'resources/data/{date}.csv'
    check_file_exists(file_path)
    number_of_sessions = count_session_number(file_path)

    # Return session entry
    return {'file path': file_path,
            'entry': [start_time, end_time, motivation_level, stress_level, focus_level, enjoyment_level, 
            minutes_worked, hours_worked, number_of_sessions, cumulative_hours_worked]}

def write_csv(file_path, entry):
    '''Write to existing CSV.'''
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter = ',')
        writer.writerow(entry)
    file.close()

def main():
    '''Main function to prompt user for input and add a work entry.'''   
    input = get_user_input()
    write_csv(input['file path'], input['entry'])

if __name__ == '__main__':
    main()