#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

json_data = open('csgo.json').read()
data = json.loads(json_data)

@app.route('/api/v0.1/weapons', methods=['GET'])
def get_weapons():
	return jsonify(data)

@app.route('/api/v0.1/weapons/<_weapon>', methods=['GET'])
def get_weapon_stat(_weapon):
	weapon = data['pistol']
	return jsonify(weapon)

if __name__ == '__main__':
	app.run(debug=True)
