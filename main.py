from datetime import *
from twilio.rest import Client
import requests
from weather_safety import weather_safety_tips

# API Endpoints and Credentials (Replace with your actual keys)
Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # OpenWeatherMap API key
account_sid = "YOUR_TWILIO_ACCOUNT_SID"  # Twilio account SID
auth_token = "YOUR_TWILIO_AUTH_TOKEN"  # Twilio authentication token

# Define location parameters for weather forecast (Latitude & Longitude hidden)
weather_params = {
    'lat': YOUR_LATITUDE,  # Replace with your latitude
    'lon': YOUR_LONGITUDE,  # Replace with your longitude
    'appid': api_key,  # API key for authentication
    'cnt': 16  # Number of forecast entries to fetch (each entry is 3 hours apart)
}

# Fetching weather data from OpenWeather API
response = requests.get(url=Endpoint, params=weather_params)
response.raise_for_status()  # Raise an error for unsuccessful requests
print(f"Response Status Code: {response.status_code}")  # Check if the request was successful

weather_data = response.json()  # Convert API response to JSON format
print(weather_data)  # Print the entire weather data (for debugging)

# Extract weather condition IDs from the forecast data
weather_data_list = []
for i in range(0, 16):
    weather_data_list.append(weather_data["list"][i]["weather"][0]["id"])
print(f"Extracted Weather Condition IDs: {weather_data_list}")

# Count occurrences of each weather condition
counter_dict = {}
for weather_id in weather_data_list:
    counter_dict[weather_id] = counter_dict.get(weather_id, 0) + 1

# Determine the most frequently occurring weather condition ID
max_weather_id = None
max_weather_id_count = 0

for weather_id, count in counter_dict.items():
    if count > max_weather_id_count:
        max_weather_id_count = count
        max_weather_id = weather_id

print(f"Most Frequent Weather Condition ID: {max_weather_id}")

# If the most frequent weather condition exists in our predefined safety tips dictionary, send an alert
if max_weather_id in weather_safety_tips:
    client = Client(account_sid, auth_token)  # Initialize Twilio client

    # Sending WhatsApp message with the weather forecast and safety tips
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio's WhatsApp sender number
        body=f"📅 Weather Forecast for Tomorrow 📅\n"
             f"OVERALL CONDITION: {weather_safety_tips[max_weather_id]}",  # Weather condition & safety tips
        to='whatsapp:+YOUR_PHONE_NUMBER'  # Replace with the recipient's WhatsApp number
    )

    print(f"Message Status: {message.status}")  # Print the status of the message
