from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    lat = request.form.get('lat')
    lon = request.form.get('lon')
    api_key = '87b4bd7f089bd1502d7720080ecf8abc'  # Replace with your actual API key
    
    if city:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    elif lat and lon:
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    else:
        return render_template('error.html', error_message='Invalid input, please provide a city or use your location.')

    response = requests.get(url)
    weather_data = response.json()

    if response.status_code == 200:
        return render_template('weather.html', weather_data=weather_data, datetime=datetime)
    else:
        error_message = weather_data.get('message', 'Error fetching data')
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)