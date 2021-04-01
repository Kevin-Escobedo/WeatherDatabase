from weatherDatabase import WeatherDatabase
from getWeather import weatherData

if __name__ == "__main__":
    wd = WeatherDatabase("weather.db")
    city = input("Enter City Name: ")
    data = weatherData(city)
    wd.createTable(city)
    wd.insertData(city, data)
    wd.close()
