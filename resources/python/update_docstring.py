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
    August 07, 2024
"""

import sys
import re
from datetime import datetime
import os


def get_next_version(version: str) -> str:
    """
    Increment the version number in '0.0.0' format.

    Args:
        version (str): Current version string.

    Returns:
        str: Next version string.
    """
    major, minor, patch = map(int, version.split("."))
    if patch < 9:
        patch += 1
    elif minor < 9:
        patch = 0
        minor += 1
    else:
        patch = 0
        minor = 0
        major += 1
    return f"{major}.{minor}.{patch}"


def update_docstring(file_path: str) -> None:
    """
    Update the version and date in the docstring of the specified file.

    Args:
        file_path (str): Path to the Python file to update.
    """
    with open(file_path, "r") as file:
        content = file.read()

    # Update the version number
    version_pattern = r"Version:\s*(\d+\.\d+\.\d+)"
    date_pattern = r"Date Last Modified:\s*(.*)"

    current_version = re.search(version_pattern, content)
    current_date = re.search(date_pattern, content)

    if not current_version or not current_date:
        print(f"Version or Date Last Modified not found in {file_path}")
        return

    new_version = get_next_version(current_version.group(1))
    new_date = datetime.datetime.now().strftime("%B %d, %Y")

    new_content = re.sub(version_pattern, f"Version: {new_version}", content)
    new_content = re.sub(date_pattern, f"Date Last Modified: {new_date}", new_content)

    with open(file_path, "w") as file:
        file.write(new_content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: update_docstring.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    update_docstring(file_path)
