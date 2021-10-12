import pyowm

from data_file import api

owm = pyowm.OWM(api)
mgr = owm.weather_manager()

observation = mgr.weather_at_place('London')
w = observation.weather

temp = w.temperature('celsius')['temp']

print(temp)