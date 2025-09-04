import requests
from flask import Flask, render_template, request, jsonify
import threading
import time
import json
import os

app = Flask(__name__)

API_KEY = os.environ.get('WEATHER_API_KEY', 'fe8afe3391c9ea2f05ede058c41e112e')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Хранилище для истории погоды
weather_history = []
favorites = []

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Добавляем в историю
            weather_history.append(weather_info)
            if len(weather_history) > 50:  # Ограничиваем историю
                weather_history.pop(0)
            
            return weather_info
        else:
            return {'error': 'City not found or API error'}
    except Exception as e:
        return {'error': f'Connection error: {str(e)}'}

# Фоновый сервис для обновления погоды для избранных городов
def background_weather_service():
    while True:
        try:
            for city in favorites[:]:  # Копия списка для безопасной итерации
                weather_data = get_weather(city)
                if 'error' in weather_data:
                    print(f"Error updating weather for {city}: {weather_data['error']}")
            time.sleep(300)  # Обновляем каждые 5 минут
        except Exception as e:
            print(f"Background service error: {e}")
            time.sleep(60)

# Запуск фонового сервиса
def start_background_service():
    thread = threading.Thread(target=background_weather_service, daemon=True)
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if city:
        weather_data = get_weather(city)
        return jsonify(weather_data)
    return jsonify({'error': 'City parameter is required'})

@app.route('/history')
def history():
    return jsonify(weather_history[-10:])  # Возвращаем последние 10 записей

@app.route('/favorites')
def get_favorites():
    return jsonify(favorites)

@app.route('/favorites/add', methods=['POST'])
def add_favorite():
    data = request.get_json()
    city = data.get('city')
    if city and city not in favorites:
        favorites.append(city)
    return jsonify({'favorites': favorites})

@app.route('/favorites/remove', methods=['POST'])
def remove_favorite():
    data = request.get_json()
    city = data.get('city')
    if city in favorites:
        favorites.remove(city)
    return jsonify({'favorites': favorites})

if __name__ == '__main__':
    start_background_service()
    app.run(host='0.0.0.0', port=8099, debug=False)
