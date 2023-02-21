import pydantic
from fastapi import FastAPI

from openweathermap.pydantic_models import WeatherByCity
from openweathermap.weather import Weather
from weather_config import get_weather_config

app = FastAPI()
weather_config = get_weather_config()


@app.get("/weather/{city_name}")
def weather_by_name(city_name: str):
    weather = Weather(weather_config.api_key).get_by_city_name(city_name)
    try:
        weather_by_city = WeatherByCity.parse_obj(weather)
    except pydantic.error_wrappers.ValidationError:
        return weather
    return {
        "city": weather_by_city.name,
        "temperature": weather_by_city.main.temp,
    }
