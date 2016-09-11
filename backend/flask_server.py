import os
import json

from flask import Flask, jsonify, render_template, request
from flask.ext.cors import CORS, cross_origin

import data_manager

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def show_data():
	return render_template('index.html')

@app.route("/data", methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def data():
	if request.method == 'GET': # Retrieve JSON data
		return jsonify(data=data_manager.read_data())
	elif request.method == 'POST': # Post new data
		data = request.data.decode('utf-8')
		data_manager.write_data(json.loads(data))
		return ('', 201)
	elif request.method == 'DELETE': # Clear all data
		data_manager.clear_data()
		return ('', 200)

if __name__ == '__main__':
	port = int(os.environ.get("PORT"))
	app.run(host='0.0.0.0', port=port)

	# app.run(debug=True)