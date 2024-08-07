#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: update-version-and-date

Version: 0.0.0

Summary:
    This script updates the version portion of the doctring of the Python files whenever commits are made.

Author:
    Luke Marren

License: MIT    

Requires:
    re, sys

Date Last Modified:
    August 7, 2024
"""

import re
import sys
from datetime import datetime


def update_docstring(file_path: str, new_version: str) -> None:
    """
    Update the version and date last modified in the docstring of the specified Python file.

    Args:
        file_path (str): The path to the Python file whose docstring is to be updated.
        new_version (str): The new version number to be set in the file's docstring.

    Returns:
        None: The function performs an in-place update of the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an issue reading or writing the file.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Define the regex patterns to match the version and date last modified
        version_pattern = re.compile(r"(Version:\s*)(\S+)")
        date_pattern = re.compile(r"(Date Last Modified:\s*)([\w\s\d,-]+)")

        # Get the current date
        current_date = datetime.now().strftime("%B %d, %Y")

        # Update version and date last modified
        updated_content = version_pattern.sub(r"\1" + new_version, content)
        updated_content = date_pattern.sub(r"\1" + current_date, updated_content)

        # Write the updated content back to the file
        with open(file_path, "w") as file:
            file.write(updated_content)

        print(
            f"Updated {file_path}: Version set to {new_version} and Date Last Modified set to {current_date}."
        )

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except IOError as e:
        print(f"Error: Unable to read/write file. {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python update_version_and_date.py <file_path> <new_version>")
        sys.exit(1)

    file_path = sys.argv[1]
    new_version = sys.argv[2]

    update_docstring(file_path, new_version)
