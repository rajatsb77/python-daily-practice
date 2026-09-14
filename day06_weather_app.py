# Day 6 — Weather CLI
import requests


def get_weather(city):
    # Step 1: Convert city name into latitude and longitude
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(geocoding_url, params=params, timeout=10)

    if response.status_code != 200:
        print("Could not connect to the weather service.")
        return

    location_data = response.json()

    if "results" not in location_data:
        print("City not found.")
        return

    location = location_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]
    city_name = location["name"]
    country = location.get("country", "")

    # Step 2: Get weather using coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10
    )

    if weather_response.status_code != 200:
        print("Could not retrieve weather data.")
        return

    weather_data = weather_response.json()
    current = weather_data["current"]

    print("\n===== CURRENT WEATHER =====")
    print(f"Location    : {city_name}, {country}")
    print(f"Temperature : {current['temperature_2m']} °C")
    print(f"Humidity    : {current['relative_humidity_2m']}%")
    print(f"Wind Speed  : {current['wind_speed_10m']} km/h")


def main():
    print("===== WEATHER APP =====")

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city.")
        return

    try:
        get_weather(city)

    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")

    except KeyError:
        print("Unexpected data received from the weather service.")


if __name__ == "__main__":
    main()
