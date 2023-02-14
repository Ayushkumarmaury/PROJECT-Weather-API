import requests

API_key = "993a859c72863398d996e1c51377fa1d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name : ")
requests_url = f"{BASE_URL}?appid={API_key}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200 :
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"]- 273.15 , 2)

    print("weather : " , weather)
    print("temperature : ", temperature, "celsius")

else:
    print("an error occured . ")