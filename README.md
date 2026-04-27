# DMI Temperature Tracker

A lightweight Python script that fetches historical temperature observations from the Danish Meteorological Institute (DMI) Open Data API and visualizes them using Matplotlib.

## Features

- Real-time Data: Fetches the latest hourly mean temperatures (temp_mean_past1h) for the past 1000 hours (~42 days).

- Automated Plotting: Generates a clean line graph of temperature trends.

- Station Specific: Pre-configured for Århus Lufthavn (Station 06070).

## Prerequisites 
Python is needed along with the following libraries:

    pip install requests numpy matplotlib

## Usage
Simply run the script from your terminal:

    python temperature.py

## How It Works
- **Data Retrieval**
The script queries the DMI MetObs API v2. It targets the observation collection using the following parameters:

    - Parameter: temp_mean_past1h (Mean temperature over the last hour).

    - Station: 06070 (Århus Lufthavn).

- **Visualization**
The data is processed using numpy and matplotlib:

    - Data is reversed to ensure chronological order (left-to-right).
    - The X-axis displays 10 evenly spaced date markers to prevent overlapping text.
    - Temperatures are plotted in Celsius (°C).