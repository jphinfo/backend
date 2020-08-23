from app import app
from flask import Flask, jsonify
import json


with open("quotes.json") as f:
    quotes = json.load(f)

    

@app.route('/')
def index():
    return "Hello world"

@app.route('/quotes', methods=["GET"])
def get_quotes():
    return jsonify({"quotes":quotes})

@app.route("/quotes/<int:id>", methods=["GET"])
def quote_id(id):
    if id <= 0 or id > 5421:
        return "Citação não existente"
    else:
        return quotes[id - 1]


@app.route('/quotes/<string:quoteAuthor>', methods=["GET"])
def get_id(quoteAuthor):
    author = [author for author in quotes if author["quoteAuthor"] == quoteAuthor]
    return jsonify({"quotes": author})


@app.route('/quotes/length', methods=["GET"])
def get_length():
    return f"Há {len(quotes)} citações registradas."

