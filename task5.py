import requests

def get_weather(location):
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

    except requests.RequestException:
        print("Error fetching weather data. Please check your internet connection.")

if __name__ == "__main__":
    user_location = input("Enter a city name or ZIP code: ")
    get_weather(user_location)