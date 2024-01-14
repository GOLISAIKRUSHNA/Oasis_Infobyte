import requests  # only one module we need to install in pc and done
                # One more api is need first we need to sign and search for weather information

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant weather information
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            print(f"\nWeather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {description.capitalize()}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    # Get your free API key from OpenWeatherMap: https://openweathermap.org/api
    api_key = "4cfcddc0c10177f0cf39f8ddd510684c"
    location = input("Enter the city or ZIP code: ")

    get_weather(api_key, location)



#let's start...
#It is present information in worli,now again
    
    #both same 
    #this is all about task2..
    #Thankyou..