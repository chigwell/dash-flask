"""Routes for parent Flask app."""
import json
import pandas as pd
from flask import current_app as app
from flask import render_template, jsonify, make_response, redirect, request


@app.route("/")
def home():
    """Landing page."""
    return render_template(
        "index.jinja2",
        title="Elections",
        description="Elections.",
        template="home-template",
        body="This is a homepage served with Flask.",
    )


@app.route("/api/uploader", methods=['POST'])
def uploader():
    # TODO: check the uploaded file by the security
    f = request.files['file']
    f.save('data/input.csv')
    return redirect("/dashapp/", code=200)

# to get the winner

@app.route("/api/winner", methods=['GET'])
def get_winner():
    winner = pd.read_csv("data/winner.csv", sep=';')
    data = {
        'message': 'The winner is...',
        'status': 200,
        'data': json.loads(winner.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))

# to get the constituencies

@app.route("/api/constituencies", methods=['GET'])
def get_constituencies():
    constituencies = pd.read_csv('data/constituency_uk_2019.csv', sep=";")
    data = {
        'message': 'The list of constituencies',
        'status': 200,
        'data': json.loads(constituencies.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))