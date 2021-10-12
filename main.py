import pyowm

from data_file import api

owm = pyowm.OWM(api)
mgr = owm.weather_manager()

city = input("Название города: ")

observation = mgr.weather_at_place(city)
w = observation.weather

temp = w.temperature('celsius')['temp']

print(temp)