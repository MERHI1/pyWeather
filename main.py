import pyowm
from pyowm.utils import config

from data_file import api

config = config.get_default_config()
config['language'] = 'ru'

owm = pyowm.OWM(api, config)
mgr = owm.weather_manager()

city = input("Название города: ")

observation = mgr.weather_at_place(city)
w = observation.weather

temp = w.temperature('celsius')['temp']
status = w.detailed_status
print(str(temp) + ', ' + str(status))