#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: time_logger

Version: 0.0.4

Summary:
    This script tracks progress made towards my 10,000-hour mastery goal.
    It generates a CSV file to log such progress for a specific day if none already exists.
    Otherwise, it will add a work session entry to the day's CSV.

Author:
    Luke Marren

License: MIT    

Requires:
    datetime, os, csv, typing

Date Last Modified: August 07, 2024
"""

import datetime as dt
import os
import csv
from typing import Optional, Any


def check_file_exists(file_path: str) -> None:
    """
    Create a new CSV if the given file path doesn't exist.

    Args:
        file_path (string): file path to CSV.
    """
    if not os.path.exists(file_path):
        # Always add newline='' to ensure no line skipping on appending to file
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(
                [
                    "start_time",
                    "end_time",
                    "motivation_level",
                    "stress_level",
                    "focus_level",
                    "minutes_worked",
                ]
            )


def get_csv_value(file_path: str, row: int, col: int) -> Optional[Any]:
    """
    Get a CSV value based on given row and column indices.

    Args: 
        file_path (string): file path to CSV.
        row (int): index of desired row.
        col (int): index of desired column.

    Returns: 
        Optional[Any]: a single CSV value or None if the CSV is empty or indices are out of range.
    """
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            # Check if CSV is empty
            if not rows:
                print("The file is empty.")
                return None

            # Check if row index is within range
            if not (-len(rows) <= row < len(rows)):
                print("Row index out of range.")
                return None

            # Check if col index is within range
            if not (-len(rows[row]) <= col < len(rows[row])):
                print("Column index out of range.")
                return None

            # Get value from CSV
            return rows[row][col]

    except Exception as e:
        print(f"Error reading the file: {e}")
        return None


def check_time_format(time: str) -> str:
    """
    Reprompt user if time format isn't %H:%M.

    Args: 
        time (str): a potentially variable-length string that may or may not adhere to %H:%M format.

    Returns: 
        str: a 5-character string in %H:%M format.
    """
    try:
        dt.datetime.strptime(time, "%H:%M")
        return time
    except ValueError:
        new_time = input("Incorrect time format. Try again (HH:MM). ")
        return check_time_format(new_time)


def check_date_format(date: str) -> str:
    """
    Reprompt user if date format isn't %m-%d-%y.

    Args: 
        date (str): a potentially variable-length string that may or may not adhere to %m-%d-%y format.

    Returns: 
        str: an 8-character string in %m-%d-%y format.
    """
    try:
        dt.datetime.strptime(date, "%m-%d-%y")
        return date
    except ValueError:
        new_date = input("Incorrect date format. Try again (MM-DD-YY). ")
        return check_date_format(new_date)


def check_rating_scale(rating: int) -> int:
    """
    Reprompt user if rating is outside of 1-5 range.

    Args: 
        rating (int): an integer used to rate levels of motivation, stress, and focus.

    Returns: 
        int: a 1-character integer value between 1 and 5, inclusive.
    """
    try:
        rating = int(rating)
        if 1 <= rating <= 5:
            return rating
        else:
            raise ValueError
    except ValueError:
        new_rating = input("Incorrect rating input. Try again (1-5): ")
        return check_rating_scale(new_rating)


def calculate_time_difference(
    time1: str, time2: str, time_format: str = "%H:%M"
) -> int:
    """
    Calculate the minute difference between two pre-formated times.

    Args: 
        time1 (str): a pre-formated 5-character string representing the first of the 2 time stamps in "%H:%M" format.
        time2 (str): a pre-formated 5-character string representing the second of 2 time stamps in "%H:%M" format.
        time_format (str): the datetime format to be applied to both timestamps; has default value of %H:%M.

    Returns: 
        int: the minute difference between the two timestamps.
    """
    # Parse the time strings into datetime objects
    t1 = dt.datetime.strptime(time1, time_format)
    t2 = dt.datetime.strptime(time2, time_format)

    # Calculate the difference
    difference = t2 - t1

    # If the difference is negative, assume that t2 is on the following day
    if difference.total_seconds() < 0:
        difference += dt.timedelta(days=1)

    # Convert the difference to minutes.
    difference_in_minutes = difference.total_seconds() / 60
    return difference_in_minutes


# def count_session_number(file_path):
#     '''Count number of sessions had in a given day based on entries in the day's CSV.'''
#     count = 0
#     with open(file_path, 'r') as file:
#         for row in file:
#             count += 1
#     return count

# def get_cumulative_hours_worked(directory, date):
#     '''Sort through data directory to get the last cumulative hours worked number logged.'''

#     # List all CSV files in the directory
#     files = [f for f in os.listdir(directory) if f.endswith('.csv')]

#     # Extract dates from filenames and filter based on the provided date
#     file_dates = []
#     for file in files:
#         file_date = dt.datetime.strptime(file.replace('.csv', ''), '%m-%d-%y')
#         input_date = dt.datetime.strptime(date, '%m-%d-%y')
#         if file_date <= input_date:
#             file_dates.append(file_date)

#     if not file_dates:
#         print('Warning: no CSVs found before the provided date.')
#         return 0

#     # Find the latest file based on date
#     latest_date = max(file_dates)
#     latest_file = latest_date.strftime('%m-%d-%y') + '.csv'

#     # Construct the full path to the latest CSV file
#     latest_file_path = os.path.join(directory, latest_file)

#     # Return last cumulative hours worked logged
#     return float(get_csv_value(latest_file_path, -1, -1))


def get_user_input() -> dict[str, Any]:
    """
    Prompt the user for input and return a dictionary with said input.

    Return: 
        dict[str, Any]: a dictionary of the user's prompt responses, which are strings and integers.
    """

    # Get user input.
    date = check_date_format(input("What is the date you worked? (MM-DD-YY): "))
    start_time = check_time_format(input("When did you START working? (HH-MM) "))
    end_time = check_time_format(input("When did you STOP working? (HH:MM) "))
    motivation_level = check_rating_scale(
        int(input("How motivated were you during this session? (1-5) "))
    )
    stress_level = check_rating_scale(
        int(input("How stressed were you coming into this session? (1-5) "))
    )
    focus_level = check_rating_scale(
        int(input("How focused were you during this session? (1-5) "))
    )

    # Calculate minutes worked - keep calculations low in raw data!
    print("Data collection was successful.")
    minutes_worked = calculate_time_difference(start_time, end_time)

    file_path = f"resources/data/{date}.csv"
    check_file_exists(file_path)

    # Return the session entry.
    return {
        "file path": file_path,
        "entry": [
            start_time,
            end_time,
            motivation_level,
            stress_level,
            focus_level,
            minutes_worked,
        ],
    }


def write_csv(file_path: str, entry: list[Any]) -> None:
    """
    Write to existing CSV.

    Args: 
        file_path (str): a string representing the CSV's file path.
    """
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(entry)


def main() -> None:
    """
    Main function to prompt user for input and add a work entry.
    """
    user_input = get_user_input()
    write_csv(user_input["file path"], user_input["entry"])


if __name__ == "__main__":
    main()