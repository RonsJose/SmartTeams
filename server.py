from flask import Flask, render_template,request
from weather import get_current_weather
from waitress import serve
import subprocess
from currency import currency_get

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
    amount = request.args.get('amount')
    from_currency = request.args.get('from_currency')
    to_currency = request.args.get('to_currency')
    
    result = currency_get(amount, from_currency, to_currency)

    return render_template(
    "currency.html",
    result=result,
    currencies=CURRENCIES,
    )

if __name__  == "__main__":
    serve(app, host="0.0.0.0", port=8000)