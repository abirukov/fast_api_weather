import os
from typing import NamedTuple

from dotenv import load_dotenv

if os.path.exists(os.path.join(os.path.dirname(__file__), '.env')):
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


class WeatherConfig(NamedTuple):
    url: str
    api_key: str


def get_weather_config() -> WeatherConfig:
    return WeatherConfig(
        url=os.environ.get("WEATHER_URL", "api.openweathermap.org"),
        api_key=os.environ.get("WEATHER_API_KEY", ""),
    )
