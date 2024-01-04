import requests
from flask import Flask, render_template, request

app = Flask(__name__)

cities=['mumbai','pune']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        
        if new_city:
            cities.append(new_city)
        new_city=''

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)


    return render_template('weather.html', weather_data=weather_data)

if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)