import requests
import time


def get_content(url):
    for attempt in range(3):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content.decode("utf-8")
        except Exception:
            time.sleep(1)
    raise Exception(f"Failed to get content from {url}")


def get_weather(location):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={location}&appid=<your API key>"
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "location": data["name"],
        "temperature": data["main"]["temp"],
        "weather_description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
    }


def fetch_data():
    response = requests.get('https://example.com/data')
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_average_value(data, field):
    values = [item[field] for item in data if field in item]
    if len(values) > 0:
        return sum(values) / len(values)
    else:
        return None