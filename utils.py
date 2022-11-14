import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f"невозможно перевести одинаковые валюты {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"не удалось обработать количество {amount}")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base
