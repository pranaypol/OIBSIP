import requests

api_key = "ace34a013792707bdff2bb6443f5dd81"

user_input = input ("Enter city name: ")

weather_data = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")

if weather_data.json()['cod'] == '404':
    print("City not found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = weather_data.json()['main']['temp']
    humidity = weather_data.json()['main']['humidity']
    
   
    print (f"Weather in {user_input} is: {weather}")
    print (f"Temperature in {user_input} is: {temperature}")
    print (f"Humidity in {user_input} is: {humidity}")
    print (f"Temperature in {user_input} is: {temperature}°C")
    