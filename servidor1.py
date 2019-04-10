#!/usr/bin/python
from flask import Flask, jsonify, request
import string

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return jsonify({'Message': "Servidor 1 executando"})

@app.route('/<name>', methods=['GET', 'POST'])
def main(name):
	print(">>>>", name)

	data = {
		"": name,
		"Uppercase": name.upper()
	}

	return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True, host='192.168.43.74', port=5001)
