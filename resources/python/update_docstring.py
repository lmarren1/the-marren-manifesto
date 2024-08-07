#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: update-version-and-date

Version: v25

Summary:
    This script updates the version portion of the doctring of the Python files whenever commits are made.

Author:
    Luke Marren

License: MIT    

Requires:
    re, sys

Date Last Modified:
    August 07, 2024
    August 07, 2024
"""

import sys
import re
from datetime import datetime
import os


def update_docstring(file_path: str, version: str, date: str) -> None:
    """
    Update the version and 'Date Last Modified' fields in the docstring of a given file.

    Args:
        file_path (str): Path to the Python file to update.
        version (str): New version string to be set in the docstring.
        date (str): New date string to be set in the docstring.

    Returns:
        None: This function does not return any value. It writes the changes directly
              to the specified file.
    """
    if file_path == os.path.abspath(__file__):
        print(f"Skipping update for script itself: {file_path}")
        return

    with open(file_path, "r") as file:
        content = file.read()

    # Define regex patterns for version and date
    version_pattern = r"Version:\s*\n"
    date_pattern = r"Date Last Modified:\s*\n"

    # Update version and date
    content = re.sub(version_pattern, f"Version:\n    {version}\n", content)
    content = re.sub(date_pattern, f"Date Last Modified:\n    {date}\n", content)

    with open(file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: update_docstring.py <file_path> <version> <date>")
        sys.exit(1)

    file_path = sys.argv[1]
    version = sys.argv[2]
    date = sys.argv[3]

    update_docstring(file_path, version, date)
