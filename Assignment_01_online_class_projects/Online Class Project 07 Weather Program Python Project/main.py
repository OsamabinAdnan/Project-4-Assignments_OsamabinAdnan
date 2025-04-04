# Import required libraries
import requests  # For making HTTP requests to the weather API
from pprint import pprint  # For pretty-printing JSON data
from dotenv import load_dotenv  # For loading environment variables
import os  # For accessing environment variables

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
my_api_key = os.getenv('WEATHER_API_KEY')

# Get the city name from user input
city = input("Enter city name to check it weather: ")

# Construct the API URL with the API key and city name
base_url = (f"https://api.openweathermap.org/data/2.5/weather?appid={my_api_key}&q={city}")

# Make API request and convert response to JSON
weather_data = requests.get(base_url).json()

# Print the weather data in a readable format
pprint(weather_data)