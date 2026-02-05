import requests
from flask import Flask, render_template, request

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "19b7870a85666cd7c9d88d1200ffb917"

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    weather_info = None

    if request.method == "POST":
        city = request.form.get("city")

        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get (api_endpoint, params=params)
        data = response.json()

    

        if response.status_code == 200:
            weather_info = {
                "city": city,
                "condition": data["weather"][0]["description"],
                "temperature": data["main"]["temp"]
            }
        else:
            weather_info = {"city": response.status_code}
    return render_template("index.html", weather=weather_info)
if __name__ == "__main__":    app.run(host="0.0.0.0", port=5001)


