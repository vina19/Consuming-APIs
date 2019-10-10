import requests
import os
from datetime import datetime

def main():
    # API key
    key = os.environ.get('WEATHER_KEY')

    # User input of the place where they want to know its weather forecast.
    user_choose = input('Enter the place for weather 5-day forecast: ')
    
    query= {'q': user_choose, 'units': 'imperal', 'appid': key }
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()

    forecast_data = data['list']

    print('Weather Forecast \n')

    # Fetch data needed
    for forecast in forecast_data:
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp)
        weather_description = forecast['weather'][0]['description']
        temp_f = forecast['main']['temp']
        wind_speed = forecast['wind']['speed']
        print(f'Date: {date}')
        print(f'Weather description: {weather_description}')
        print(f'Temperature: {temp_f:.2f} F') 
        print(f'Wind speed: {wind_speed} \n')

if __name__ == '__main__':
    main()
    
# It will show UTC time because beside it's in the 5 day/3 hour API document,
# UTC is the time standard used in internet and World Wide Web.