from flask import Flask, jsonify, request
import requests
from flask_cors import CORS  # <-- Add this import

app = Flask(__name__)
CORS(app)  # <-- Add this line

@app.route('/')
def home():
    return "Weather API is running. Use /weather?city=CityName"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'City not found or API error'}), response.status_code

    data = response.json()
    current = data['current_condition'][0]
    weather_info = {
        'city': city,
        'temperature': current['temp_C'],
        'description': current['weatherDesc'][0]['value'],
        'humidity': current['humidity'],
        'wind_speed': current['windspeedKmph']
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)