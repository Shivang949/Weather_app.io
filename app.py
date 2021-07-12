from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api = "d56c8f69033661adb7ab6298b3df2444"

        source = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}").read()

        json_data = json.loads(source)



        data = {
            "city": city,
            "weather": str(json_data["weather"][0]["description"]),
            "temperature": str(json_data["main"]["temp"]),
            "humidity": str(json_data["main"]["humidity"]),
            "wind_speed": str(json_data["wind"]["speed"]),
        }




        return render_template('index.html', data=data)
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)