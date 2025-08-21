import requests
import csv
import os
import time
import pywhatkit

# --- CONFIGURATION ---
api_key = "a12c68e26d08a83f6c186d7c38c6ee56"  # Replace with your OpenWeatherMap API key
repo_path = r"C:\Users\Finance Trainee\Documents\GitHub\Weather_in_African_Cities" # Replace with your local repo path
csv_filename = "world_capitals_weather.csv"
csv_path = os.path.join(repo_path, csv_filename)
group_id = "FATKNmEsC5iGhjbSlpisA0"
message = """Thank you for running my code. I look forward to know how you used it in your works. Write to me through: vaaketch@gmail.com"""

# --- READ COUNTRY DATA FROM CSV ---
capitals_url = "https://raw.githubusercontent.com/icyrockcom/country-capitals/master/data/country-list.csv"
local_capitals_csv = "country-list.csv"

# Download the CSV if not present
if not os.path.exists(local_capitals_csv):
    import urllib.request
    urllib.request.urlretrieve(capitals_url, local_capitals_csv)

country_data = []
with open(local_capitals_csv, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        country = row['country']
        capital = row['capital']
        country_data.append((capital, country))

results = []

for capital, country in country_data:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={capital},{country}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            results.append([capital, country, weather, temp])
        else:
            results.append([capital, country, "Failed", ""])
    except Exception as e:
        results.append([capital, country, "Error", ""])
    time.sleep(1)

# Save to CSV in GitHub repo folder
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Capital City", "Country", "Weather", "Temperature (°C)"])
    writer.writerows(results)

# Git add, commit, push
os.chdir(repo_path)
os.system(f'git add {csv_filename}')
os.system('git commit -m "Add world capitals weather data CSV"')
os.system('git push')

# Send WhatsApp message instantly
pywhatkit.sendwhatmsg_to_group_instantly(group_id, message)