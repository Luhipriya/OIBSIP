import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\n===========================")
        print("    WEATHER INFORMATION")
        print("===========================\n")
        print(f"Location: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print("\nHave a great day!\n")
    else:
        print("\nError: City not found! Please enter a valid city name.\n")

if __name__ == "__main__":
    print("=== Welcome to Weather App ===")
    city_name = input("Enter city name: ")
    api_key = "855b9e0cda88895b70441f0b3d1cc9ee"  # Replace with your actual API key
    get_weather(city_name, api_key)
