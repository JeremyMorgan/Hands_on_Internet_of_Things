#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
import time
import sys
import reading
import datastore
import logging

logging.basicConfig(filename='api.log', level=logging.DEBUG)

from flask.ext.httpauth import HTTPBasicAuth

# User Configurable settings

# Do not edit past this point

auth = HTTPBasicAuth()
app = Flask(__name__)

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
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

## Routes
## /weather/api/v1/readings  GET ALL
@app.route('/weather/api/v1/readings', methods=['GET'])
def get_readings():

    #return jsonify({'readings': [make_public_reading(reading) for reading in readings]})

    #print jsonify(datastore.getreading(60))
    #return make_response(jsonify(datastore.getreading(60)), 200)

    return make_response(str(datastore.getreading(3)), 200)

@app.route('/weather/api/v1/readings/<int:reading_id>', methods=['GET'])
def get_reading(reading_id):

    #print "sent ID: " + str(reading_id)

    #reading = [reading for reading in readings if reading['id'] == reading_id]

    #ourReading = datastore.getreading(60)

    #if len(ourReading) == 0:
        #abort(404)
    #return jsonify({'reading': ourReading})
    return make_response("SUCCESS", 200)

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