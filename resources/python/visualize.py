#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    visualize

Version:
	0.0.4

Summary:
    This script produces plotly graphs visualizing my progress on the 10k mastery tracker project.

Author:
    Luke Marren

License: 
    MIT

Requires:
    pandas, load_data, numpy, plotly

Date Last Modified:
	August 20, 2024
"""

import pandas as pd
from load_data import csvs_to_df
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def visualize_data():
    df = csvs_to_df(directory_path="../../resources/data")

    df["hours_worked"] = np.round(df["minutes_worked"] / 60, 2)
    df["cumulative_hours"] = df["hours_worked"].cumsum()
    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%y")
    cumulative_hours = df.groupby("date")["cumulative_hours"].max().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot cumulative hours
    ax.plot(
        cumulative_hours["date"],
        cumulative_hours["cumulative_hours"],
        label="Cumulative Hours",
        color="#00BFFF",
        linestyle="-",
        marker="o",
    )

    # Plot daily hours
    ax.plot(
        df["date"],
        df["hours_worked"],
        label="Daily Hours",
        color="#333",
        linestyle="-",
        marker="x",
    )

    # Formatting the x-axis to show dates
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d-%y"))
    plt.xticks(rotation=45)

    # Adding titles and labels
    plt.title("Cumulative Hours Worked Over Time", loc="center", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Hours Worked")
    plt.legend()

    # Add watermark
    plt.text(
        0.5, 0.5, "The Marren Manifesto", 
        color="#ff6f61", 
        fontsize=30,  # Adjust the font size to be more suitable
        ha='center', 
        va='center', 
        alpha=0.3,  # Transparency of the watermark
        rotation=30,  # Rotation of the watermark text
        transform=ax.transAxes  # Ensure watermark is in figure coordinates
    )

    # Set grid and show the plot
    plt.grid(True)
    plt.tight_layout()

    # Save the figure
    plt.savefig("../media/cumulative-hours-plot.png", dpi=100)
    plt.show()

def main() -> None:
    """
    Main function to generate analysis variables and their respective summary statistics.
    """
    visualize_data()


if __name__ == "__main__":
    main()
