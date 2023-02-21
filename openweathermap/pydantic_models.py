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
    feels_like: float | None
    temp_min: float | None
    temp_max: float | None
    pressure: int | None
    humidity: int | None
    sea_level: int | None
    grnd_level: int | None


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float | None


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
