import requests

API_KEY = "b808f88065a568fa12c83e0840b6044c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Use proper exception handling
try:
    city = input("Enter a city name: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    
    # Make the API request
    response = requests.get(request_url)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Parse the JSON response
    data = response.json()
    
    # Extract and print weather information
    weather_description = data['weather'][0]['description']
    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius

    print(f"Weather: {weather_description}")
    print(f"Temperature: {temperature_celsius:.2f} °C")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
