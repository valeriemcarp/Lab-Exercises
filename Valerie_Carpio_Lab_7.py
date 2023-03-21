import requests
import json
import pandas as pd
import csv
import numpy as np

lat = "42.098701"
lon = "-75.912537"
genius = requests.get(f"https://api.weather.gov/{lat},{lon}")

json_f = genius.json()

forecast = json_f["properties"]["forecast"]
request = requests.get(forecast)

json = request.json()

new = json["properties"]["periods"]

csv = open("weather.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(csv)
csv_writer.writerow(["Name", "Temperature", "Detailed Forecast"])

for i in range(len(new)):
    name = (new[i]["name"])
    temp = (new[i]["temp"])
    dforecast = (new[i]["dforecast"])

    csv_writer.writerow([name, temp, dforecast])

csv.close()