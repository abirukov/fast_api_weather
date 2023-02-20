import os
from typing import NamedTuple

from dotenv import load_dotenv

if os.path.exists(os.path.join(os.path.dirname(__file__), '.env')):
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


class WeatherConfig(NamedTuple):
    api_key: str


def get_weather_config() -> WeatherConfig:
    return WeatherConfig(api_key=os.environ.get("WEATHER_API_KEY", ""))
