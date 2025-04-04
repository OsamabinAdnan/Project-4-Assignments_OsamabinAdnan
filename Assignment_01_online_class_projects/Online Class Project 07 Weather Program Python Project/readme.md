# Weather Program

A simple Python program that fetches and displays weather data for any city using the OpenWeatherMap API.

## Features

- Fetches real-time weather data using OpenWeatherMap API
- Accepts any city name as input
- Displays comprehensive weather information
- Uses environment variables for secure API key storage

## Prerequisites

- Python 3.x
- `requests` library
- `python-dotenv` library
- OpenWeatherMap API key

## Installation

1. Clone the repository
2. Install required packages:
```bash
pip install requests python-dotenv
```
3. Create a `.env` file in the project root and add your API key:
```
WEATHER_API_KEY=your_api_key_here
```

## Usage

1. Run the program:
```bash
python main.py
```
2. Enter the name of the city when prompted
3. View the weather data output

## Environment Variables

- `WEATHER_API_KEY`: Your OpenWeatherMap API key

## Security

- The `.env` file is included in `.gitignore` to prevent exposing API keys
- Uses `python-dotenv` for secure environment variable management

## API Reference

This program uses the OpenWeatherMap API:
- Base URL: `https://api.openweathermap.org/data/2.5/weather`
- Documentation: [OpenWeatherMap API Docs](https://openweathermap.org/api)