#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    load_data

Version:
	0.1.2

Summary:
    This script loads in and produces summary analysis on the data produced for the 10k mastery tracker project.

Author:
    Luke Marren

License: 
    MIT

Requires:
    os, pandas

Date Last Modified:
	August 20, 2024
"""

import os
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


def max_str_length_in_dict(dict: dict) -> int:
    """
    Calculate the maximum length of strings or strings contained by lists inside a dictionary.

    Args:
        dict (dict): A dict containing strings and lists of strings.

    Returns:
        int: the maxiumum length of strings contained in the dictionary.
    """
    max_line_length = 0
    for value in dict.values():
        if type(value) is list:
            for list_value in value:
                if len(list_value) > max_line_length:
                    max_line_length = len(list_value)
        if len(value) > max_line_length:
            max_line_length = len(value)

    return max_line_length


def pretty_print_dict(dict: dict) -> None:
    """
    Print a message to the console in ASCII box format.

    Args:
        dict (dict): A dict containing strings and lists of strings.
    """
    max_line_length = max_str_length_in_dict(dict)
    separation_line = "+" + "-" * (max_line_length + 2) + "+"

    last_key = ""
    for key, item in dict.items():
        if key == "start":
            print(f"{separation_line}\n| {item.center(max_line_length)} |")
        elif key == "end":
            print(f"| {item.center(max_line_length)} |\n{separation_line}")
        elif key.endswith("list"):
            if last_key == "list":
                print(separation_line)
            for value in item:
                if value != "":
                    print(f"| {value.ljust(max_line_length)} |")
        else:
            if item != "":
                print(separation_line)
                print(f"| {item.ljust(max_line_length)} |")
                print(separation_line)
        last_key = key


def is_homogenous(series: pd.Series) -> bool:
    """
    Checks whether or not a given pandas series has homogenous data types.

    Args:
        column (pd.Series): a series, potentially of a pandas dataframe.

    Returns:
        bool: True if all the values' data types in the series are the same, False if not.
    """
    types = series.apply(type)
    return types.nunique() == 1


def check_duplicated_cols(df: pd.DataFrame) -> str:
    """
    Check whether or not a pandas data frame has duplicate columns and return a string message if it does.

    Args:
        df (pd.DataFrame): a pandas dataframe containing raw, uncleaned, and unfiltered data.

    Returns:
        str: a string message that is either empty or says how many duplicate columns there are.
    """
    duplicate_cols_count = df.duplicated().sum()
    duplicate_cols = ""
    if duplicate_cols_count != 0:
        duplicate_cols = f"Duplicate columns count: {duplicate_cols_count}"
    return duplicate_cols


def check_missing_col_vals(df: pd.DataFrame) -> list[str]:
    """
    Check whether or not a pandas data frame has missing values and return a string message if it does.

    Args:
        df (pd.DataFrame): a pandas dataframe containing raw, uncleaned, and unfiltered data.

    Returns:
        str: a list of string messages that is either empty or says how many missing values there are and where.
    """
    missing_vals_per_col_list = []
    for col in df[df.columns]:
        col_missing_vals = df[col].isnull().sum()
        if col_missing_vals != 0:
            missing_vals_per_col_list.append(
                f"There are missing values in {col}: {col_missing_vals}"
            )
    return missing_vals_per_col_list


def summarize_df_as_dict(df: pd.DataFrame) -> dict:
    """
    Summarize pandas dataframe into a dict of strings and lists of strings.

    Args:
        df (pd.DataFrame): a pandas dataframe containing raw, uncleaned, and unfiltered data.

    Returns:
        dict: a dictionary providing a summary of the dataframe indicating may need to be cleaned.
    """
    # Contextual messages to be printed to console.
    start = "Dataframe Summary"
    end = "End of Summary"

    # General overview info about df.
    col_count = f"Column count: {len(df.columns)}"
    col_dtypes = []
    dtype_homogeneity_list = []
    for col_name in df.columns:
        # Check for data type homoegeneity.
        if not is_homogenous(df[col_name]):
            dtype_homogeneity_list.append(f"{col_name} has hetergenous data types")
            col_dtypes.append({"heterogenous data type"})
        else:
            col_dtypes.append(df[col_name].dtype)

    # Line break long list of column names at length 50.
    line = "Column names and data types:    "
    line_length = 0
    col_name_and_dtype_list = []
    idx = 0
    for name, dtype in zip(df.columns, col_dtypes):
        line_length += len(f" {name} ({dtype}) ")
        if line_length >= 50:
            col_name_and_dtype_list.append(line)
            line = f"{name} ({dtype}), "
            line_length = 0
        else:
            if idx == len(col_dtypes) - 1:
                line += f"{name} ({dtype})"
                col_name_and_dtype_list.append(line)
            else:
                line += f"{name} ({dtype}), "
        idx += 1
    row_count = f"Observation count: {len(df)}"

    duplicate_cols = check_duplicated_cols(df)
    duplicate_rows = check_duplicated_cols(df.T)
    missing_vals_per_col_list = check_missing_col_vals(df)

    df_summary_dict = {
        "start": start,
        "col_count": col_count,
        "col_name_and_dtype_list": col_name_and_dtype_list,
        "row_count": row_count,
        "dtype_homogeneity_list": dtype_homogeneity_list,
        "duplicate_cols": duplicate_cols,
        "duplicate_rows": duplicate_rows,
        "missing_vals_per_col_list": missing_vals_per_col_list,
        "end": end,
    }
    return df_summary_dict


def print_df_summary(df: pd.DataFrame) -> None:
    """
    Print summary data about the raw_data's structure, data types, and data summary statistics.

    Args:
        df (pd.DataFrame): a pandas dataframe containing raw, uncleaned, and unfiltered data.
    """
    df_summary = summarize_df_as_dict(df)
    pretty_print_dict(df_summary)


def load_data() -> pd.DataFrame:
    """
    Imports CSV all files from a given directory into a pandas dataframe and prints summary information on the dataframe to the console.

    Returns:
        pd.DataFrame: a pandas dataframe containing the previously-mentioned CSVs as raw data.
    """
    raw_data_df = csvs_to_df()
    print_df_summary(raw_data_df)
    return raw_data_df


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
