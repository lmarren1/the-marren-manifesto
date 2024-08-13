#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    visualize

Version:
	0.0.2

Summary:
    This script produces plotly graphs visualizing my progress on the 10k mastery tracker project.

Author:
    Luke Marren

License: 
    MIT

Requires:
    load_data, plotly

Date Last Modified:
	August 12, 2024
"""

from load_data import csvs_to_df
import numpy as np
import plotly.graph_objects as go 


def visualize_data():
    df = csvs_to_df()

    # Accumulate hours
    df["hours_worked"] = np.floor(df["minutes_worked"] / 60)
    df["cumulative_hours"] = df["hours_worked"].cumsum()

    # Create the figure
    fig = go.Figure()

    # Add a trace
    fig.add_trace(go.Scatter(x=df['date'], y=df['cumulative_hours'], mode='lines+markers'))

    # Update layout for x-axis tickformat and hoverformat
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Value',
        xaxis=dict(
            tickformat='%m-%d-%y',  # Format for axis labels
            hoverformat='%m-%d-%y'  # Format for hover tooltips
        )
    )

    # Show the figure
    fig.show()


def main() -> None:
    """
    Main function to generate analysis variables and their respective summary statistics.
    """
    visualize_data()


if __name__ == "__main__":
    main()
