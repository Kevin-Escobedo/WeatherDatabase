import secret #secret.py contains the OpenWeathermap API key
import requests
import json

def weatherData(city: str) -> tuple:
    '''
    Calls the OpenWeathermap API
    Returns the temperature in Kelvin,
    the pressure in hPa,
    the humidity percentage,
    and the weather conditions of the
    specified city.
    '''
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    completeURL = "{}appid={}&q={}".format(baseURL, secret.APIKEY, city)
    response = requests.get(completeURL)
    x = response.json()
    
    if x["cod"] != "404":
        y = x["main"]
        currentTemperature = y["temp"]
        currentPressure = y["pressure"]
        currentHumidity = y["humidity"]
        z = x["weather"]
        weatherConditions = z[0]["description"]
        return (currentTemperature, currentPressure, currentHumidity, weatherConditions)
        
    else:
        return None
