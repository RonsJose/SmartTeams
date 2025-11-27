from dotenv import load_dotenv
from pprint import pprint
from flask import request
import requests
import os

CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "NZD"]


load_dotenv()
API_KEY=os.getenv("API_KEY")

def currency_get(amount = 0, from_currency = "EUR", to_currency = "EUR"):
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}/"
    result = None
    converted = None
    response = requests.get(BASE_URL)
    data = response.json()

    if data["result"] != "success":
        result = "Error fetching rates"
        converted = None
    else:
        rates = data["conversion_rates"]
        converted = round(amount * rates[to_currency], 2)
        result = converted

    result=result,
    currencies=CURRENCIES,
    page_title = "Currency Converter - Flask App"
    return result
