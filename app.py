#Imports Flask Tools
from flask import Flask, render_template, request
#Requests For Call Currency API
import requests

app = Flask(__name__)

#API KEY FOR EXCHANGE-RATE
API_KEY = "5098f5c0287d73ed2b2cfddd"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "NZD"]

#Route For Homepage; Handles Requests
@app.route("/", methods=["GET", "POST"])
def home():
    #Default Values
    result = None
    converted = None
    #If Form Is Submitted
    if request.method == "POST":
        #Gets Data From The Form
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()

        response = requests.get(BASE_URL + from_currency)
        data = response.json()

            #Checks If API Request Was Successful
        if data["result"] != "success":
            result = "Error fetching rates"
            converted = None
        else:
            #Gets The Conversion Rates
            #Calculates Converted Amount
            rates = data["conversion_rates"]
            converted = round(amount * rates[to_currency], 2)
            result = converted

#Renderes HTML Webpage and Sends Values To It
    return render_template(
        "practice.html",
        result=result,
        currencies=CURRENCIES,
        page_title = "Currency Converter - Flask App")

if __name__ == "__main__":
    app.run(debug=True)
