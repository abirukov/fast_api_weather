from typing import Mapping, Optional

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
    feels_like: Optional[float]
    temp_min: Optional[float]
    temp_max: Optional[float]
    pressure: Optional[int]
    humidity: Optional[int]
    sea_level: Optional[int]
    grnd_level: Optional[int]


class Wind(BaseModel):
    speed: float
    deg: int
    gust: Optional[float]


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
