import requests

API_KEY = 'fe8afe3391c9ea2f05ede058c41e112e'  # Замените на ваш API-ключ
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
