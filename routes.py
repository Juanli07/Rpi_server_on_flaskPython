from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask_cors import CORS
from db import accessToDB
import time, datetime
from datetime import date

app = Flask(__name__)
cors = CORS(app, resources = {r"/*": { "origins": "*"}})
sql = accessToDB.accesSql('sql10.freemysqlhosting.net', 'sql10314381', '6sqLF2H2Bi', 'sql10314381')
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@app.route('/user', methods=['GET', 'POST'])
def user():
    data = []
    response_object = {'status' : 'success'}
    if(request.method == 'POST'):
        post_data = request.get_json()
        if(sql.insertUsers(post_data.get('email'), '{} {}'.format(post_data.get('firstname'), post_data.get('lastname')), post_data.get('password'))):
            data = "success"
        else:
            data = "duplicate"
    else:
        data = sql.selectUsers()
    return jsonify(data)

@app.route('/login', methods = ['POST'])
def login():
    resp = ""
    if not request.is_json:
        resp = jsonify({'msg' : 'missing JSON in request'}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    print("{}, {}".format(username, password))

    if username == '':
        resp = jsonify({ 'msg': 'Mising username parameter'})
    if password == '':
        resp =  jsonify({ 'msg': 'Mising password parameter'})
    users = sql.selectUsers()
    for user in users:
        if(username == user[0] and password == user[2]):
            access_token = create_access_token(identity=username)
            resp = jsonify(access_token=access_token), 200
    return resp

@app.route('/is_admin/<string:email>', methods = ['GET'])
def is_admin(email):
    print(email)
    rsp = ""
    data = sql.selectUsersad(email)
    for d in data:
        if(d[3] == 1):
            rsp = "true"
    return jsonify(rsp)

@app.route('/regforhour', methods = ['GET', 'POST'])
def regforday():
    reg = []
    if(request.method == 'POST'):
        post_data = request.get_json()
        if(sql.insertRegForHour(str(post_data.get('id_ac')), float(post_data.get('temp')), int(post_data.get('state')), int(post_data.get('motion')))):
            reg.append({"message" : "susccess"})
        else:
            reg.append({"message" : "fail"})
    else:
        data = sql.selectRegforhour()
        for row in data:
            reg.append({
                'id_ac' : row[0],
                'temp' : row[1],
                'time' : row[2],
                'state' : row[3],
                'motion' : row[4]
            })
    return jsonify(reg)
@app.route('/ac', methods = ['GET', 'POST'])
def ac():
    reg = []
    response_object = {'status' : 'success'}
    if(request.method == 'POST'):
        post_data = request.get_json()
        if(post_data.get('state') == "0"):
            sql.insertAC(post_data.get('id_ac'), float(post_data.get('temp')), 0)
        else:
            sql.insertAC(post_data.get('id_ac'), float(post_data.get('temp')), int(post_data.get('state')))

    else:
        data = sql.selecAc()
        for row in data:
            reg.append({
                'id_ac' : row[0],
                'temp' : row[1],
                'state' : row[2]
            })
    return jsonify(reg)

@app.route('/acdel/<id_ac>', methods = ['DELETE'])
def delac(id_ac):
    resp = ""
    if(sql.deleteac(id_ac)):
        resp = 'succesfull'
    else:
        resp = 'failed'

    return jsonify(resp)

@app.route('/acup/<id_ac>', methods=['PUT'])
def acup(id_ac):
    resp = ""
    if(sql.acUpdate(id_ac)):
        resp = 'succesfull'
    else:
        resp = 'failed'

    return jsonify(resp)

@app.route('/regforhour/<dates>', methods = ['GET'])
def regforhour(dates):
    reg = []
    print(dates)
    data = sql.selRegforHour(dates)
    for row in data:
        reg.append({
            'id_ac' : row[0],
            'temp' : row[1],
            'time' : row[2],
            'state' : row[3],
            'motion' : row[4]
        })
    return jsonify(reg)
