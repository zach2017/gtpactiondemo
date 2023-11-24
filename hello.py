from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/privacy', methods=['GET'])
def privacy():
   return "we do not use any of your data"

@app.route('/hello', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        eventsString = "Below is a list of Events at the Lab on Dexter"
        with open('labevents.txt') as f:
          events = f.readlines()

        for line in events:
          eventsString += line
        data = {"data": eventsString}
        return jsonify(data)
