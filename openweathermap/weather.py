import requests

from config import get_weather_config
from openweathermap.methods import Method
from typing import Mapping


class Weather:
    def __init__(self):
        config = get_weather_config()
        self.url = config.url
        self.api_key = config.api_key

    def __request(self, method: str, params: Mapping[str, str]) -> str:
        response_data = requests.get(
            f"https://{self.url}/{method}",
            headers={
                "Content-Type": "application/json",
            },
            params=params,
        )
        return response_data.text

    def get_by_city_name(self, city_name: str) -> str:
        return self.__request(
            Method.WEATHER_BY_CITY.value,
            {
                "q": city_name,
                "appid": self.api_key,
                "units": "metric",
            },
        )
