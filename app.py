from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods =['GET', '_POST_'])
def index():

    if request.method == '_POST_':
        city = request.form['city']
        country = request.form['country']
        api_key = "_60aa068482d6ddc251ae5f53570ac5fb_"

        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

    return render_template ("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)
    
    return render_template ("index.html")