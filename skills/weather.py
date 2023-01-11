from pyowm import OWM
from geopy.geocoders import Nominatim
from datetime import datetime
import requests


class Weather():

    def wind_direction_from_deg(self, deg):
        if deg > 337.5:
            return "Nord"
        elif deg > 292.5:
            return "Nord-Ouest"
        elif deg > 247.5:
            return "Ouest"
        elif deg > 202.5:
            return "Sud-Ouest"
        elif deg > 157.5:
            return "Sud"
        elif deg > 122.5:
            return "Sud-Est"
        elif deg > 67.5:
            return "Est"
        elif deg > 22.5:
            return "Nord-Est"
        else:
            return "Nord"

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    # API Key
    api_key = "f700a87822fcd10eb01e8cd839b7c7aa"

    def __init__(self):
        geolocator = Nominatim(user_agent="MoBot")
        location = geolocator.geocode("35 Impasse de la Gare, 40170 Bias")
        self.location = location

    @property
    def get_weather(self):
        url = f'{self.BASE_URL}lat={self.location.latitude}&lon={self.location.longitude}&appid={self.api_key}&units=metric&lang=fr'
        return requests.get(url).json()

    @property
    def forcast(self):
        forcast = self.get_weather
        description = forcast['weather'][0]['description']
        temp = forcast['main']['temp']
        temp_min = forcast['main']['temp_min']
        temp_max = forcast['main']['temp_max']
        humidity = forcast['main']['humidity']
        wind = forcast['wind']['speed']
        wind_direction = self.wind_direction_from_deg(forcast['wind']['deg'])
        sunrise = datetime.fromtimestamp(forcast['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(forcast['sys']['sunset']).strftime('%H:%M:%S')
        return f"Le temps est {description}, la température est de {temp} degrés, avec un minimum de {temp_min} et un maximum de {temp_max}. L'humidité est de {humidity} pourcents. Le vent souffle à {wind} mètres par seconde, en direction du {wind_direction}. Le soleil se lève à {sunrise} et se couche à {sunset}."