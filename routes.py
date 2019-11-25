from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask_cors import CORS
from db import accessToDB
import time, datetime
from datetime import date

app = Flask(__name__)
cors = CORS(app, resources = {r"/*": { "origins": "*"}})
sql = accessToDB.accesSql('localhost', 'root', '', 'acdb')
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@app.route('/user', methods=['GET'])
def user():
    data = sql.selectUsers()
    return jsonify(data)

@app.route('/login', methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({'msg' : 'missing JSON in request'}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    print("{}, {}".format(username, password))

    if username == '':
        return jsonify({ 'msg': 'Mising username parameter'})
    if password == '':
        return jsonify({ 'msg': 'Mising password parameter'})
    users = sql.selectUsers()
    for user in users:
        if(username == user[0] and password == user[2]):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200



@app.route('/regforhour', methods = ['GET'])
def regforday():
        data = sql.selectRegforhour('2019-11-13')
        reg = []
        for row in data:
            reg.append({
                'id_ac' : row[0],
                'temp' : row[1],
                'state' : row[3],
                'motion' : row[4]
            })
        return jsonify(reg)