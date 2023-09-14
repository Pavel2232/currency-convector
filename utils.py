import requests
from datetime import datetime

from environs import Env

env = Env()
env.read_env('.env')
API_KEY = env('TOKEN_FIXER')


def convert_currency_fixerapi_free(src: str, to: str, amount: int | float) -> float:
    """converts `amount` from the `src` currency to `dst` using the free account"""

    url = f"http://data.fixer.io/api/latest?access_key={API_KEY}&symbols={src},{to}&format=1"
    data = requests.get(url)
    data.raise_for_status()
    response = data.json()
    if response["success"]:
        rates = response["rates"]
        exchange_rate = 1 / rates[src] * rates[to]
        return exchange_rate * amount
