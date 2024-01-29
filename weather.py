import requests


API_KEY = "b808f88065a568fa12c83e0840b6044c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name:  ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather']
    print(weather)
    temperature = data["main"]["temp"]
    print(temperature)
else:
    print("An error occurred")
