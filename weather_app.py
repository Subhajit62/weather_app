# -*- coding: utf-8 -*-
"""weather_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VcaC71HRCTVzbYlo6Q2MDtLBTVzEpba8
"""

!pip install requests

import requests

def get_weather(city):
  api_key = "280010c5884d7c1824bacef2c3735e6f"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = base_url + "appid=" + api_key + "&q=" + city
  response = requests.get(complete_url)
  data = response.json()
  if response.status_code == 200:
    weather = data["weather"][0]["main"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    description = data["weather"][0]["description"]
    return f"Weather in {city}: {weather}, {temperature}°C, {description}"
  else:
    return f"Error fetching weather data. Status code: {data.get('cod', response.status_code)}, Message: {data.get('message', 'Unknown')}"

city_name = input("Enter city name: ")
weather_info = get_weather(city_name)
print(weather_info)