# 🌦️ Weather Alert Script

## Overview
This Python script fetches weather forecast data from the OpenWeatherMap API and identifies the most frequent weather condition for a specified location. Based on that, it sends a WhatsApp alert with relevant safety tips using Twilio’s API.

---

## Features
- Fetches 48-hour weather forecast (16 x 3-hour intervals)  
- Analyzes the most frequent weather condition ID  
- Sends automated WhatsApp messages with safety advice  
- Easily customizable for any location  

---

## Prerequisites
- Python 3.6 or higher  
- OpenWeatherMap API key  
- Twilio account with WhatsApp messaging enabled  

---

## Installation

1. Clone or download this repository.  
2. Install required Python packages:
   ```bash
   pip install requests twilio
