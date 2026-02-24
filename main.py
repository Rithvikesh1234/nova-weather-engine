"""Nova Weather Engine - Fetches real-time weather data."""
import urllib.request, json

API_KEY = "your_api_key_here"

def get_weather(city: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())

def display(data: dict):
    print(f"City   : {data['name']}")
    print(f"Temp   : {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")

if __name__ == "__main__":
    city = input("Enter city: ")
    try:
        display(get_weather(city))
    except Exception as e:
        print(f"Error: {e}")
