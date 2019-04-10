#!/usr/bin/python

from flask import Flask, jsonify, request
import string
import threading
import time
import requests


app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
	return jsonify({'Message': "Middleware Executando"})

@app.route('/<name>', methods=['GET', 'POST'])

def main(name):
	print(">>>>", name)
	data = {
		#"  ": name,
		"": (requests.post("http://192.168.43.74:5001/%s"%(name))).json(),
		" ": (requests.post("http://192.168.43.74:5002/%s"%(name))).json()	
			
	}

	return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True, host = '192.168.43.158',port=5000, threaded = True)
	



