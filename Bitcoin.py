import requests

def main():

    user_input = get_value_bitcoin()
    rate_value = get_API_rate_data()
    convert_value = convert_value_to_USD(user_input, rate_value)
    display_result = display_value_in_USD(user_input, rate_value)

# Get the user input
def get_value_bitcoin():

    user_input = int(input('Enter your Bitcoin number: '))
    
    return user_input

# Fetch the data
def get_API_rate_data():

    # Using requests to get the bitcoin API in json format
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    
    rate = data['bpi']['USD']['rate']

    return rate

# Conversion to USD value
def convert_value_to_USD(user_input, rate):

    user_USD_value = user_input * rate

    return user_USD_value

# Displaying the result
def display_value_in_USD(user_input, rate):

    user_USD_value = convert_value_to_USD(user_input, rate)

    print(f'The user Bitcoin value in USD is: $ ' + user_USD_value)

    
if __name__ == '__main__':
    main()