from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return {"greeting":"Hello world"}


@app.route('/create', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        domine_name = json['domain_name']
        password = json['password']
        if (re.fullmatch('[0-9]*', password) and
            re.fullmatch('[A-Za-z]*', domine_name)):
            return json
        else:
            return 'your data is not accepteble'
    else:
        return 'Content-Type not supported!'

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@app.route('/info/<domine_name>', methods=['GET'])
def info(domine_name):
    data = request.json
    domine_name = data['domain_name']
    return 'ok'
