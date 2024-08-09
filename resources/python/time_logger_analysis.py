#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    time_logger_analysis

Version:
	0.0.8

Summary:
    This script produces summary statistical analysis on the CSV files produced for the 10k mastery tracker project.

Author:
    Luke Marren

License: 
    MIT

Requires:
    os, csv, pandas

Date Last Modified:
	August 08, 2024
"""

import os
import csv
import pandas as pd


def csvs_to_df(directory_path: str = "resources/data") -> pd.DataFrame:
    """
    Read all CSVs in given directory into a combined pandas dataframe.

    Args:
        directory_path (str): the selected directory full of CSVs to be read in.

    Returns:
        pd.DataFrame: a pandas dataframe to be used as the raw data dataframe.
    """
    files = [f for f in os.listdir(directory_path) if f.endswith(".csv")]
    df_list = []

    for file in files:
        file_path = os.path.join(directory_path, file)
        df = pd.read_csv(file_path)  # The file already has unique IDs
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df


# def pretty_print_dict(dict: dict) -> None:
#     """
#     Print a message to the console in ASCII box format.

#     Args: dict (dict): A dict containing strings and lists.
#     """

#     # calc max length of lines
#     # dict will have either single - line strings or lists of strings
#     #
#     separation_line = "\n" + "+" + "-" * (len(message) + 2) + "+" + "\n"
#     print(f"{separation_line}| {message.ljust(len(message))} |{separation_line}")


# dict {message: begin df, }


def print_df_summary(df: pd.DataFrame) -> None:
    """
    Print summary data about the raw_data's structure, data types, and data summary statistics.

    Args: raw_data (pd.DataFrame): a pandas dataframe containing raw, uncleaned, and unfiltered data.
    """
    start_msg = "Begin Data Frame Summary."
    col_names_list = [name for name in df.columns]
    col_names_str = ", ".join(df.columns)
    col_count = len(df.columns)
    col_dtypes = []
    row_count = len(df)
    missing_vals_count = 0
    missing_vals_per_col = []
    duplicate_rows_count = df.duplicated().sum()
    duplicate_cols_count = df.T.duplicated().sum()
    unique_vals_per_col = []
    for col in df[df.columns]:
        unique_vals_per_col.append(f"Unique values in {col}: {len(df[col].unique())}")
        missing_vals_per_col.append(
            f"Missing values in {col}: {(df[col].isnull()).sum()}"
        )
        missing_vals_count += df[col].isnull().sum()
        col_dtypes.append(f"{col}'s data type is: {type(df[col])}")  # Create function for determining homogeneity of type within a column

    print(col_names_str)
    print(f"Row count: {row_count}.")
    print(f"Column count: {col_count}.")
    print(f"Missing values count: {missing_vals_count}.")
    for na in missing_vals_per_col:
        print(na)
    for unique in unique_vals_per_col:
        print(unique)
    for types in col_dtypes:
        print(types)


def load_data():
    raw_data_df = csvs_to_df()
    print_df_summary(raw_data_df)


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
