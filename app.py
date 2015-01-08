#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

json_data = open('csgo.json').read()
data = json.loads(json_data)

@app.route('/api/v0.1/weapons', methods=['GET'])
def get_weapons():
	return jsonify(data)

@app.route('/api/v0.1/<string:gun_name>', methods=['GET'])
def get_weapon_stat(gun_name):
	for gun_type in data["weapons"]:
		for gun in data["weapons"][gun_type]:
			if gun_name == gun:
				return jsonify(data["weapons"][gun_type][gun])
				


if __name__ == '__main__':
	app.run(debug=True)
