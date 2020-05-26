
import json
from flask import Flask, make_response, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "This is the index page, service seems to work!"


@app.route('/basic', methods=[ "POST" ])
def basic():

    parse_intent = request.get_json(force="True")
    intentname = parse_intent[ 'queryResult' ][ "intent" ][ "displayName" ]

    if intentname == 'place_order':
        speech = " What would you like to eat ? Pizza, Souvlaki, Crepa ?" #+ intentname
        response = {"fulfillmentText": speech}
        res = json.dumps(response)
        r = make_response(res)
        r.headers[ 'Content-Type' ] = 'application/json'
        return r

    if intentname == 'place_order - custom':
        user_choice = parse_intent[ 'queryResult' ][ "outputContexts" ][1]['parameters']['food']
        speech = " Your " + user_choice + " is on its way !"
        response = {"fulfillmentText": speech}
        res = json.dumps(response)
        r = make_response(res)
        r.headers[ 'Content-Type' ] = 'application/json'
        return r

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)