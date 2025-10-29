import requests

API_KEY = "e44dde2076014986841131859252910"
Base = "http://api.weatherapi.com/v1"

def main():
    city = input("Enter city to get current weather: ")
    celsius, fahrenheit = get_weather(city)

    if celsius is not None:
        print(f"Weather in {city.capitalize()} in Celsius: {celsius}°C")
        print(f"Weather in {city.capitalize()} in Fahrenheit: {fahrenheit}°F")
    else:
        print("Can't get data")

def get_weather(city):
    response = requests.get(f"{Base}/current.json?key={API_KEY}&q={city}")
    if response.status_code == 200:
        data = response.json()
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]
        return temp_c, temp_f
    else:
        return None, None

if __name__ == "__main__":
    main()

