#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    update_docstring

Version: 
    0.0.1

Summary:
    This script updates the version portion of the doctring of the Python files whenever commits are made.

Author:
    Luke Marren

License: 
    MIT    

Requires:
    re, sys, datetime

Date Last Modified:
    August 07, 2024
"""

import sys
import re
from datetime import datetime


def update_version(content: str) -> str:
    """
    Update the version number in the docstring.

    Args:
        content (str): The content of the file as a string.

    Returns:
        str: The updated content with the new version.
    """
    # Pattern to match "Version:" followed by a newline and a tab
    version_pattern = re.compile(r"(Version:\s*\n\s*)\d+\.\d+\.\d+")
    version_match = version_pattern.search(content)

    if version_match:
        # Extract current version and increment it
        current_version = version_match.group().strip().split("\n\t")[-1]
        major, minor, patch = map(int, current_version.split("."))
        patch += 1
        if patch > 9:
            patch = 0
            minor += 1
        if minor > 9:
            minor = 0
            major += 1
        new_version = f"{major}.{minor}.{patch}"
        content = version_pattern.sub(f"Version:\n\t{new_version}", content)

    return content


def update_date(content: str) -> str:
    """
    Update the date in the docstring.

    Args:
        content (str): The content of the file as a string.

    Returns:
        str: The updated content with the new date.
    """
    date_pattern = re.compile(r"(Date Last Modified:\s*\n\s*)\w+ \d{2}, \d{4}")
    current_date = datetime.now().strftime("%B %d, %Y")
    content = date_pattern.sub(f"Date Last Modified:\n\t{current_date}", content)

    return content


def update_version_and_date(file_path: str) -> None:
    """
    Updates the version and date in the docstring of the given Python file.

    Args:
        file_path (str): The path to the Python file to update.
    """
    # Read the file content
    with open(file_path, "r") as file:
        content = file.read()

    # Update version and date
    content = update_version(content)
    content = update_date(content)

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_docstring.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    update_version_and_date(file_path)
