import requests

from typing import Mapping


class Weather:
    METHODS = {
        "weather_by_city": "data/2.5/weather",
    }

    def __init__(self, api_key: str):
        self.url = "api.openweathermap.org"
        self.api_key = api_key

    def __request(self, method: str, params: Mapping[str, str]) -> dict:
        response_data = requests.get(
            f"https://{self.url}/{method}",
            headers={
                "Content-Type": "application/json",
            },
            params=params,
        )
        return response_data.json()

    def get_by_city_name(self, city_name: str) -> dict:
        return self.__request(
            self.METHODS['weather_by_city'],
            {
                "q": city_name,
                "appid": self.api_key,
                "units": "metric",
            },
        )
