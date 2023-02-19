from typing import Mapping

from pydantic import BaseModel


class Coords(BaseModel):
    lon: float
    lat: float


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class MainWeatherData(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Sys(BaseModel):
    country: str
    sunrise: int
    sunset: int


class WeatherByCity(BaseModel):
    coord: Coords
    weather: list[Weather]
    base: str
    main: MainWeatherData
    visibility: int
    wind: Wind
    clouds: Mapping[str, int]
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
