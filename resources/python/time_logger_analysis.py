#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    time_logger_analysis

Version:
	0.0.7

Summary:
    This script produces summary statistical analysis on the CSV files produced for the 10k mastery tracker project.

Author:
    Luke Marren

License: 
    MIT

Requires:
    pandas

Date Last Modified:
	August 08, 2024
"""

import pandas as pd


def load_data():
    pass


def clean_data():
    pass


def explore_data():
    pass


def analyze_data():
    pass


def transform_data():
    pass


def visualize_data():
    pass


def main() -> None:
    """
    Main function to generate analysis variables and their respective summary statistics.
    """
    load_data()
    clean_data()
    explore_data()
    analyze_data()
    transform_data()
    visualize_data()


if __name__ == "__main__":
    main()

# What do I want to know about my csv data?
# we have per session data stored in daily CSVs for start_time,end_time,motivation_level,stress_level,focus_level,minutes_worked

# start_time, end_time, minutes_worked - describe timing and quantity of session

# motivation_level, stress_level, focus_level - describe quality of session

# create session id by adding the session number to the date in the csv name

# Think statistically: measures of center, spread

# create descriptive statistic df

# start with raw data df

