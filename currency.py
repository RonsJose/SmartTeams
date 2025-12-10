from flask import Flask, render_template, request
from dotenv import load_dotenv
<<<<<<< HEAD
import requests
=======
>>>>>>> 1c29c59 (Fixed Flask And HTML/CSS Not Working Correctly)
import os
import requests

app = Flask(__name__)

<<<<<<< HEAD

load_dotenv()
API_KEY=os.getenv("API_KEYC")

def currency_get(amount = 0, from_currency = "EUR", to_currency = "EUR"):
    if amount is None or from_currency is None or to_currency is None:
        return None
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    amount=float(amount)
    result = None
    converted = None
=======
CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "NZD"]

load_dotenv()
API_KEY = os.getenv("API_KEY")

def currency_get(amount=0, from_currency="EUR", to_currency="EUR"):
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}/"
>>>>>>> 1c29c59 (Fixed Flask And HTML/CSS Not Working Correctly)
    response = requests.get(BASE_URL)
    data = response.json()

    if data["result"] != "success":
<<<<<<< HEAD
        result = "Error fetching rates"
        converted = None
    else:
        rates = data["conversion_rates"]
        converted = round(amount * rates[to_currency], 2)

    return converted
=======
        return "Error fetching rates"
    rates = data["conversion_rates"]
    return round(amount * rates[to_currency], 2)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        amount = float(request.form.get("amount", 0))
        from_cur = request.form.get("from_currency", "EUR")
        to_cur = request.form.get("to_currency", "EUR")
        result = currency_get(amount, from_cur, to_cur)
    return render_template("currency.html", currencies=CURRENCIES, result=result, page_title="Currency Converter")

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 1c29c59 (Fixed Flask And HTML/CSS Not Working Correctly)
