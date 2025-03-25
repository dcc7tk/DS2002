# Weather and Air Quality Analysis

This project collects real-time weather data and air quality measurements for multiple cities using the Weatherstack API. It processes the data and stores it in a structured format for further analysis. Users can query air quality statistics, view weather conditions, and analyze patterns across cities. Users can also work with historical data from a local CSV file in tandem with cities of their choice.

## Usage Instructions

To run the project, execute the script project6.ipynb. You will be prompted to enter the number of cities to search for and the names of those cities. The script will fetch data and display the weather and air quality information for the cities you enter.

## Features

Fetches real-time weather data (temperature, wind, humidity, moon movements, etc.)  
Retrieves air quality measurements (CO, NO2, O3, SO2, EPA Index, etc.)  
Stores collected data in pandas DataFrames for analysis  
Provides basic data aggregation and summary statistics

## Dependencies

json  
pandas  
json  
requests  
sqlite3  
calendar

## API Key Instructions

You need a Weatherstack API key to fetch data. You can sign up for a free API key at Weatherstack. Once you obtain the key, replace “REDACTED” in the code with your actual API key.