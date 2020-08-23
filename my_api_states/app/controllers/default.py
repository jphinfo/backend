from app import app
from flask import Flask, jsonify
import json


with open("date.json", encoding = "UTF8") as f:
    date = json.load(f)

@app.route("/")
def index():
    return "Brasil acima de tudo e Deus acima de todos."

@app.route("/states/", methods=["GET"])
def get_states():
    return jsonify(date)

@app.route("/states/length/", methods=["GET"])
def get_length():
    return f"No Brasil exitem {len(date['estados'])} estados"


@app.route("/states/<string:uf>", methods=["GET"])
def get_uf(uf):
    city = range(len(date["estados"]))
    city = [city for city in (date["estados"])]
    for k, v in enumerate(city):
        if v['sigla'] == uf.upper():
            return f'{v["cidades"]}'







