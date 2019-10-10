import requests

def main():

    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

    user_input = int(input('Enter a number of Bitcoin: '))

    rate = data['bpi']['USD']['rate']

    user_USD_value = user_input * rate

    print(f'The rate is: {rate}, The user Bitcoin value in USD is: $ ' + user_USD_value)
    
    # forecast_data = data['list']

    # print('Weather Forecast \n')

    # # Fetch data needed
    # for forecast in forecast_data:
    #     timestamp = forecast['dt']
    #     date = datetime.fromtimestamp(timestamp)
    #     weather_description = forecast['weather'][0]['description']
    #     temp_f = forecast['main']['temp']
    #     wind_speed = forecast['wind']['speed']
    #     print(f'Date: {date}')
    #     print(f'Weather description: {weather_description}')
    #     print(f'Temperature: {temp_f:.2f} F') 
    #     print(f'Wind speed: {wind_speed} \n')

if __name__ == '__main__':
    main()


