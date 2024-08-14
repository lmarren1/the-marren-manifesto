#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    visualize

Version:
	0.0.3

Summary:
    This script produces plotly graphs visualizing my progress on the 10k mastery tracker project.

Author:
    Luke Marren

License: 
    MIT

Requires:
    pandas, load_data, numpy, plotly

Date Last Modified:
	August 13, 2024
"""

import pandas as pd
from load_data import csvs_to_df
import numpy as np
import plotly.graph_objects as go


def visualize_data():
    df = csvs_to_df()

    df["hours_worked"] = np.round(df["minutes_worked"] / 60, 2)
    df["cumulative_hours"] = df["hours_worked"].cumsum()
    df["date"] = pd.to_datetime(df["date"], format="%m-%d-%y")
    cumulative_hours = df.groupby("date")["cumulative_hours"].max().reset_index()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=cumulative_hours["date"],
            y=cumulative_hours["cumulative_hours"],
            name="Cumulative Hours",
            marker_color="#00BFFF",
            # hovertext=dict(x=cumulative),
            # hoverinfo="text"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["hours_worked"],
            name="Daily Hours",
            marker_color="#333",
        )
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Value",
        title=dict(
            text="Cumulative Hours Worked Over Time",
            subtitle=dict(
                text="Life expectancy by European country in 1952 and in 2002",
                font=dict(color="gray"),
            ),
            y=0.9,
            x=0.5,
            xanchor="center",
            yanchor="top",
        ),
        font=dict(family="Fire Code", color="#002F4C"),
        xaxis_tickformat="%m-%d-%y",
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
