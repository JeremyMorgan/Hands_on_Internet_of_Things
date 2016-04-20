#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask.ext.cors import CORS
import reading
import datastore
import logging

logging.basicConfig(filename='api.log', level=logging.ERROR)

# User Configurable settings

# Do not edit past this point

app = Flask(__name__)

CORS(app)

## Function to add URI to each request
def make_public_reading(reading):
    new_reading = {}
    for field in reading:
        if field == 'id':
            new_reading['uri'] = url_for('get_reading', reading_id=reading['id'], _external=True)
        else:
            new_reading[field] = reading[field]
    return new_reading


## 404 handler
@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

## Routes
## /weather/api/v1/readings  GET ALL
@app.route('/weather/api/v1/readings', methods=['GET'])
def get_readings():

    return make_response(str(datastore.getreading(30)), 200)

@app.route('/weather/api/v1/readings/<int:reading_id>', methods=['GET'])
def get_reading(reading_id):

    return make_response(str(datastore.getsinglereading(reading_id)), 200)


@app.route('/weather/api/v1/readings', methods=['POST'])
def create_reading():

    logging.info('Started create_reading()')

    req_json = request.get_json()

    # Adding an ID and Timestamp since we don't have them
    req_json['id'] = None
    req_json['timestamp'] = None

    # Storing the values in our Reading object
    ourReading = reading.Reading(req_json)

    insertresult = datastore.insertreading(ourReading)

    if insertresult:
        return jsonify({'status': 'succeeded'}), 200
    else:
        return jsonify({'status': 'failed'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')