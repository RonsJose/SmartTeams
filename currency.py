from dotenv import load_dotenv
import requests
import os


load_dotenv()
API_KEY=os.getenv("API_KEYC")

def currency_get(amount = 0, from_currency = "EUR", to_currency = "EUR"):
    if amount is None or from_currency is None or to_currency is None:
        return None
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    amount=float(amount)
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

    return converted
