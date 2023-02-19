from fastapi import FastAPI
from openweathermap.pydantic_models import WeatherByCity
from openweathermap.weather import Weather

app = FastAPI()


@app.get("/weather/{city_name}")
def weather_by_name(city_name: str):
    weather = Weather().get_by_city_name(city_name)
    weather_by_city = WeatherByCity.parse_raw(weather)
    return {
        "city": weather_by_city.name,
        "temperature": weather_by_city.main.temp,
    }
