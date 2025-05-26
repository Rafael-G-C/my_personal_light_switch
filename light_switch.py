from flask import Flask, render_template, request, send_file, redirect, Response
import requests
import random as rnd

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("main.html")

@app.route("/on", methods=['POST'])
def turn_on():
    data = """{"on":true,"bri":98,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":150,"grp":1,"spc":0,"of":0,"on":true,"frz":false,"bri":255,"cct":127,"set":0,"n":"","col":[[255,213,0],[0,2,33],[255,0,204]],"fx":104,"sx":60,"ix":128,"pal":2,"c1":128,"c2":128,"c3":16,"sel":true,"rev":false,"mi":false,"o1":false,"o2":false,"o3":false,"si":0,"m12":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}"""

    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://192.168.100.18/json/state", data=data, headers=headers)

    return "ON ☀️"

@app.route("/off", methods=['POST'])
def turn_off():
    data = """{"on":"t"}"""

    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://192.168.100.18/json/state", data=data, headers=headers)

    return "OFF 🌙"


@app.route("/sleepy", methods=['POST'])
def turn_sleepy():
    data = """{"on":true,"bri":98,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":150,"grp":1,"spc":0,"of":0,"on":true,"frz":false,"bri":255,"cct":127,"set":0,"n":"","col":[[0,97,93],[0,2,33],[255,0,204]],"fx":75,"sx":128,"ix":128,"pal":2,"c1":128,"c2":128,"c3":16,"sel":true,"rev":false,"mi":false,"o1":false,"o2":false,"o3":false,"si":0,"m12":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}"""
    
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://192.168.100.18/json/state", data=data, headers=headers)

    return "Sleepy 💤"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True)
