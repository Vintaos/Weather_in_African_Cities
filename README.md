# Weather_in_African_Cities
@ -1 +1,44 @@
World Capitals Weather Data Automation
This project fetches the current weather and temperature for all world capitals, saves the results to a CSV file, pushes the file to your GitHub repository, and sends a WhatsApp notification to a group.

Features
Downloads a public dataset of world capitals and countries
Fetches weather and temperature for each capital using the OpenWeatherMap API
Saves results to a CSV file in your GitHub repository
Automatically adds, commits, and pushes the CSV to GitHub
Instantly sends a WhatsApp message to a specified group
Requirements
Python 3.7+
Packages: requests, csv, pywhatkit
A valid OpenWeatherMap API key (get one here)
A local clone of your GitHub repository
WhatsApp Web logged in on your default browser
Setup
Install dependencies:
Clone your GitHub repository locally (if not already):
Edit the script:
Set your api_key (OpenWeatherMap)
Set repo_path to your local repo folder
Set your WhatsApp group ID and message
Usage
Run the script:

The script will download the capitals dataset if not present.
It will fetch weather data for each capital and save to world_capitals_weather.csv in your repo.
The CSV will be committed and pushed to GitHub.
A WhatsApp message will be sent instantly to your group.
Output
world_capitals_weather.csv with columns:
Capital City
Country
Weather
Temperature (°C)
Notes
The script runs silently (no console output).
Make sure your Python environment has all dependencies installed.
WhatsApp Web must be open and logged in for the message to send.
For more details or customization, edit the script as needed.
License
MIT License

# Weather_in_African_Cities
