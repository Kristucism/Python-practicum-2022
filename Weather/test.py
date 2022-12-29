import requests
import json

city="Riga"
country="Latvia"

api_key = "60aa068482d6ddc251ae5f53570ac5fb"

weather_url = requests.get(f'http://api.openweather.org/data/2.5/weather?appid={api_key}&q={Riga},{country}&units=imperial')

weather_data = weather_url.json()

temp = round(weather_data['main']['temp'])
humidity = weather_data['main']['humidity']
wind_speed =nweather_data ['wind'][_'speed'_]