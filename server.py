from flask import Flask, render_template,request
from weather import get_current_weather
from waitress import serve
import subprocess
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY=os.getenv("API_KEY")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "NZD"]

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/applications')
def applications():
    return render_template('index2.html')

@app.route('/weather1')
def weather1():
    return render_template('weather_index.html')

@app.route('/weather')
def get_weather():
    city=request.args.get('city')
    weather_data=get_current_weather(city)
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        humidity=f"{weather_data['main']['humidity']:.1f}"
    )

@app.route('/run-tetris')
def run_tetris():
    subprocess.Popen(["python", "SmartTeams/tetris.py"], shell = True)
    return "Tetris Started!"

@app.route('/currency',methods=["GET", "POST"])
def currency():
    result = None
    converted = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()

        response = requests.get(BASE_URL + from_currency)
        data = response.json()

        if data["result"] != "success":
            result = "Error fetching rates"
            converted = None
        else:
            rates = data["conversion_rates"]
            converted = round(amount * rates[to_currency], 2)
            result = converted

    return render_template(
        "currency.html",
        result=result,
        currencies=CURRENCIES,
        page_title = "Currency Converter - Flask App")

if __name__  == "__main__":
    serve(app, host="0.0.0.0", port=8000)