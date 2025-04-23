class Weather:
    def __init__(self, temperature, humidity, windspeed, pressure):
        self.weather_params = [temperature, humidity, windspeed, pressure]

    def __contains__(self, item):
        return item in self.weather_params

    def display(self):
        print("Weather Parameters:")
        print(f"Temperature: {self.weather_params[0]} °C")
        print(f"Humidity: {self.weather_params[1]} %")
        print(f"Wind Speed: {self.weather_params[2]} km/h")
        print(f"Pressure: {self.weather_params[3]} hPa")

weather = Weather(25, 80, 15, 1013)

weather.display()

print("\nIs Temperature in weather parameters?", 25 in weather)  
print("Is 'Rain' in weather parameters?", 'Rain' in weather)  
print("Is Wind Speed in weather parameters?", 15 in weather)